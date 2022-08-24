import os.path
import re
import settings
import main
from apps import const
from starlette.requests import Request
from apps.blogs import payload
from apps.blogs.models import Blogs, Emojis, BlogImages, BlogLikes, Comments, Collections
from apps.users.models import Users, Follows
from settings import EMOJI_PREFIX
from utils.db_session import objects
from utils.tools import parse_time


async def get_emojis():
    emojis = await objects.execute(Emojis.select())
    res = []
    for item in emojis:
        tmp = {'id': item.id, 'url': EMOJI_PREFIX + item.origin_uri, 'display_name': item.display_name}
        res.append(tmp)
    return {'code': 200, 'msg': 'success', 'data': res}


async def publish_blog(request: Request, form: payload.Blogs):
    content = form.content
    es = re.findall("\[.*?\]", content)
    rps = []
    for i in es:
        r = re.sub('.*\[', '[', i)
        if r not in rps:
            try:
                emoji = await objects.get(Emojis, display_name=i)
                img = f' <img style="width:18px; height:18px;vertical-align:-3px;"  src=' \
                      f'"{settings.EMOJI_PREFIX + emoji.origin_uri}">'
            except:
                img = i
            content = content.replace(i, img)
            rps.append(r)
    blog = await objects.create(Blogs, content=content, user_id=request.user)
    images_res = []
    for i in form.images:
        direction = i.get('direction', 'h')
        small = settings.SMALL_URI_PREFIX + i['name'] if i['copper'] else None

        tmp_dict = {
            'small': small,
            'middle': settings.MIDDLE_URI_PREFIX + i['name'],
            'large': settings.LARGE_URI_PREFIX + i['name'],
            'direction': direction
        }
        images_res.append(tmp_dict)
        await objects.create(BlogImages, avatarName=i['name'], blog_id=blog.id, direction=direction, copper=i['copper'])
    user = await objects.get(Users, id=request.user)
    userInfo = user.to_dict()
    pub_time = '3s前'

    tmp = {'id': blog.id, 'content': blog.content, 'userInfo': userInfo, 'pub_time': pub_time, 'images': images_res,
           'is_self': True, 'likes': 0, 'comments': 0}
    return {'code': 200, 'msg': '发布成功！', 'data': tmp}


async def comment(request: Request, form: payload.Blogs):
    content = form.content
    es = re.findall("\[.*?\]", content)
    rps = []
    for i in es:
        r = re.sub('.*\[', '[', i)
        if r not in rps:
            try:
                emoji = await objects.get(Emojis, display_name=i)
                img = f' <img style="width:18px; height:18px;vertical-align:-3px;"  src=' \
                      f'"{settings.EMOJI_PREFIX + emoji.origin_uri}">'
            except:
                img = i
            content = content.replace(i, img)
            rps.append(r)
    comment = await objects.create(Comments, content=content, user_id=request.user, blog_id=form.blog_id,
                                   parent_id=form.parent_id)
    user = await objects.get(Users, id=request.user)
    userInfo = user.to_dict()
    pub_time = '3s前'
    tmp = {'id': comment.id, 'content': comment.content, 'userInfo': userInfo, 'pub_time': pub_time, 'is_self': True}
    username = comment.blog_id.user_id.username
    await main.sm.send('prompt', username=username)
    return {'code': 200, 'msg': '评论成功！', 'data': tmp}


async def get_comments(request: Request, blog_id: int):
    result = await objects.execute(Comments.select().where(Comments.blog_id == blog_id, Comments.is_active))
    res = {'code': 200,
           'data': [],
           'position': '北京',
           'islike': False,
           'likes': 800,
           'comments': 800,
           }
    for item in result:
        user = await objects.get(Users, id=item.user_id)
        userInfo = user.to_dict()
        pub_time = parse_time(item.create_time)
        likes = BlogLikes.select().where(BlogLikes.blog_id == item, BlogLikes.is_active).count()
        is_active = BlogLikes.select().where(BlogLikes.blog_id == item, BlogLikes.user_id == request.user,
                                             BlogLikes.is_active).exists()
        tmp = {'id': item.id,
               'content': item.content,
               'userInfo': userInfo,
               'pub_time': pub_time,
               'likes': likes,
               'is_self': request.user == item.user_id,
               'commentShow': False,
               'comments': 800,
               'is_active': is_active,
               }
        res['data'].insert(0, tmp)
    return res


async def del_comment(comment_id: int):
    await objects.execute(Comments.update(is_active=0).where(Comments.id == comment_id))
    return {'code': 200}


async def _get_blogs(request, flag, u_id, index, pageNum, pageSize):
    if flag == 'all':
        query = Blogs.select().where(Blogs.is_active).order_by(Blogs.id.desc()).paginate(pageNum, pageSize)

    else:
        if index == 0:
            query = Blogs.select().where(Blogs.is_active, Blogs.user_id == u_id).order_by(Blogs.id.desc()).paginate(
                pageNum, pageSize)
        else:
            query = Blogs.select().join(Collections).where(
                Collections.user_id == u_id, Collections.is_active, Blogs.is_active).order_by(
                Collections.id.desc()).paginate(pageNum, pageSize)
    result = await objects.execute(query)
    res = {'code': 200, 'data': []}
    permission_map = {
        2: '广场可见',
        3: '粉丝可见',
        4: '仅自己可见',
    }
    for item in result:
        userInfo = item.user_id.to_dict()
        pub_time = parse_time(item.create_time)

        query = item.blog_image.select().where(BlogImages.is_active == 1)
        image = await objects.execute(query)
        likes = item.likes_blog.count()
        comments = item.blog_comments.count()
        is_active = item.likes_blog.select().where(BlogLikes.user_id == request.user, BlogLikes.is_active).exists()
        images_res = [i.to_dict() for i in image]
        is_self = request.user == item.user_id
        if flag == 'user':
            if index == 0:
                dropdown_menus = const.user_dropdown_menus[:4]
                top = const.user_dropdown_menus[7] if item.is_top else const.user_dropdown_menus[6]
                dropdown_menus = [i for i in dropdown_menus if i['id'] != item.permission]
                dropdown_menus.insert(0, top)
            else:
                dropdown_menus = [const.user_dropdown_menus[5]]
        else:
            dropdown_menus = [const.user_dropdown_menus[-1]]
            if is_self:
                dropdown_menus.append(const.user_dropdown_menus[3])
            else:
                c = item.collection_blogs.select().where(Collections.user_id == request.user).exists()
                if c:
                    dropdown_menus.append(const.user_dropdown_menus[5])
                else:
                    dropdown_menus.append(const.user_dropdown_menus[4])

        tmp = {'id': item.id,
               'content': item.content,
               'userInfo': userInfo,
               'pub_time': pub_time,
               'create_time': str(item.create_time),
               'images': images_res,
               'likes': likes,
               'is_self': is_self,
               'comment': False,
               'comments': comments,
               'dropdown_menus': dropdown_menus,
               'is_active': is_active,
               'is_top': item.is_top,
               'permission_text': permission_map[item.permission]
               }
        res['data'].append(tmp)
    return res


async def get_blogs(request: Request, flag: str = 'all', u_id: int = None, index: int = 0, pageNum: int = 1,
                    pageSize: int = 10):
    res = await _get_blogs(request, flag, u_id, index, pageNum, pageSize)
    return res


async def get_blog(request: Request, blog_id: int):
    item = await objects.get(Blogs, id=blog_id)

    userInfo = item.user_id.to_dict()
    pub_time = parse_time(item.create_time)

    query = item.blog_image.select().where(BlogImages.is_active == 1)
    image = await objects.execute(query)
    likes = item.likes_blog.count()
    comments = item.blog_comments.count()
    is_active = item.likes_blog.select().where(BlogLikes.user_id == request.user, BlogLikes.is_active).exists()
    images_res = [i.to_dict() for i in image]
    is_self = request.user == item.user_id
    dropdown_menus = const.user_dropdown_menus[:4]

    res = {'id': item.id,
           'content': item.content,
           'userInfo': userInfo,
           'pub_time': pub_time,
           'create_time': str(item.create_time),
           'images': images_res,
           'likes': likes,
           'is_self': is_self,
           'comment': False,
           'comments': comments,
           'dropdown_menus': dropdown_menus,
           'is_active': is_active,
           }
    return {'code': 200, 'data': res}


async def del_blog(blog_id: str):
    await objects.execute(Blogs.update(is_active=0).where(Blogs.id == blog_id))
    return {'code': 200}


async def like(request: Request, blog_id: str):
    blogLikes, status = await objects.get_or_create(BlogLikes, user_id=request.user, blog_id=blog_id)
    if not status:
        blogLikes.is_active = True
        await objects.update(blogLikes, only=['is_active'])
    else:
        username = blogLikes.blog_id.user_id.username
        await main.sm.send('prompt', username=username)

    return {'code': 200}


async def dislike(request: Request, blog_id: str):
    try:
        blogLikes = await objects.get(BlogLikes, user_id=request.user, blog_id=blog_id)
        blogLikes.is_active = False
        await objects.update(blogLikes, only=['is_active'])
    except:
        pass
    return {}


async def get_taste(request: Request):
    users = await objects.execute(Users.select().where(Users.username == 'gs4weet'))
    res = []
    for i in users:
        follow = request.user.follow_user.select().where(Follows.be_user_id == i.id, Follows.is_active).exists()
        tmp = i.to_dict()
        tmp['follow'] = follow
        res.append(tmp)
    return {'code': 200, 'data': res}


async def get_box_msg(request: Request):
    query1 = BlogLikes.select().join(Blogs).where(Blogs.user_id == request.user, Blogs.is_active, BlogLikes.user_id != request.user)
    query2 = Comments.select().join(Blogs).where(Blogs.user_id == request.user, Comments.is_active, Comments.user_id != request.user)
    like_msg = await objects.execute(query1)
    comment_msg = await objects.execute(query2)

    def serialize(iterable, flag='comment'):
        tmp_res = []
        for item in iterable:
            userInfo = item.user_id.to_dict()
            content = item.blog_id.content
            middle = item.blog_id.blog_image.first()
            direction = 'h'
            if middle is not None:
                direction = middle.direction
                middle = settings.MIDDLE_URI_PREFIX + middle.avatarName
            tmp_dict = {
                'id': item.id,
                'flag': flag,
                'clicked': item.clicked,
                'blog_id': item.blog_id.id,
                'userInfo': userInfo,
                'middle': middle,
                'blog_content': content,
                'direction': direction
            }
            if flag == 'comment':
                tmp_dict['comment_content'] = item.content
                tmp_dict['sort'] = item.create_time
            else:
                tmp_dict['sort'] = item.update_time
            pub_time = parse_time(tmp_dict['sort'])
            tmp_dict['pub_time'] = pub_time
            tmp_res.append(tmp_dict)
        return tmp_res

    res1 = serialize(like_msg, flag='like')
    res2 = serialize(comment_msg)
    res = res1 + res2
    res = sorted(res, key=lambda x: (-x['clicked'], x['sort']), reverse=True)
    return {'code': 200, 'data': res}


async def click_msg(request: Request, msg_id: int, flag: str, all_read: bool = False):
    if all_read:
        await objects.execute(Comments.update(clicked=1).where(Comments.user_id == request.user))
        await objects.execute(BlogLikes.update(clicked=1).where(BlogLikes.user_id == request.user))
    else:
        if flag == 'comment':
            await objects.execute(Comments.update(clicked=1).where(Comments.id == msg_id))
        else:
            await objects.execute(BlogLikes.update(clicked=1).where(BlogLikes.id == msg_id))
    return {'code': 200}


def get_msg_count(request: Request):
    like_count = BlogLikes.select().join(Blogs).where(
        BlogLikes.user_id != request.user, Blogs.user_id == request.user, Blogs.is_active, ~BlogLikes.clicked).count()
    comment_count = Comments.select().join(Blogs).where(Comments.user_id != request.user, Blogs.user_id == request.user, Blogs.is_active, Comments.is_active,
        ~Comments.clicked).count()
    count = like_count + comment_count
    return {'code': 200, 'data': count}
