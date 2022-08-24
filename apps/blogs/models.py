import peewee as pw

import settings
from apps.users.models import Users
from utils.baseModel import BaseModel


class Blogs(BaseModel):
    """
    2: 广场可见
    3: 粉丝可见
    4: 仅自己可见
    """
    user_id = pw.ForeignKeyField(Users, on_delete='CASCADE', related_name='user_blogs')
    comments = pw.IntegerField(default=0)
    content = pw.TextField()
    is_top = pw.BooleanField(null=True, default=True)
    permission = pw.SmallIntegerField(null=True, default=2)

    class Meta:
        table_name = 'tb_blogs'


class BlogLikes(BaseModel):
    user_id = pw.ForeignKeyField(Users, on_delete='CASCADE', related_name='likes_user')
    blog_id = pw.ForeignKeyField(Blogs, on_delete='CASCADE', related_name='likes_blog')
    clicked = pw.BooleanField(null=True, default=False)

    class Meta:
        table_name = 'tb_blog_likes'


class BlogImages(BaseModel):
    avatarName = pw.CharField(max_length=255)
    blog_id = pw.ForeignKeyField(Blogs, on_delete='CASCADE', related_name='blog_image')
    direction = pw.CharField(max_length=10)
    copper = pw.BooleanField(null=True, default=False)

    class Meta:
        table_name = 'tb_blogImages'

    def to_dict(self):
        small = settings.SMALL_URI_PREFIX + self.avatarName if self.copper else None
        return {
            'small': small,
            'middle': settings.MIDDLE_URI_PREFIX + self.avatarName,
            'large': settings.LARGE_URI_PREFIX + self.avatarName,
            'blog_id': self.blog_id,
            'direction': self.direction,
        }


class Comments(BaseModel):
    blog_id = pw.ForeignKeyField(Blogs, on_delete='CASCADE', related_name='blog_comments')
    user_id = pw.ForeignKeyField(Users, on_delete='CASCADE', related_name='comment_users')
    content = pw.TextField()
    like = pw.IntegerField(default=0)
    parent_id = pw.ForeignKeyField('self', on_delete='SET NULL', related_name='subs', null=True,
                                   verbose_name='父级评论')
    clicked = pw.BooleanField(null=True, default=False)

    class Meta:
        table_name = 'tb_comments'


class Collections(BaseModel):
    user_id = pw.ForeignKeyField(Users, on_delete='CASCADE', related_name='collection_users')
    blog_id = pw.ForeignKeyField(Blogs, on_delete='CASCADE', related_name='collection_blogs')

    class Meta:
        table_name = 'tb_collections'


class Emojis(BaseModel):
    origin_uri = pw.CharField(max_length=30)
    display_name = pw.CharField(max_length=20)

    class Meta:
        table_name = 'tb_emojis'


if __name__ == '__main__':
    b = Blogs.get(id=7)
    print(b.collection_blogs.select().where(Collections.user_id == 1).exists())
