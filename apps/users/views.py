import base64
import random
import os
import re
import time
import cv2
import settings
import numpy as np
import pandas as pd
from starlette.requests import Request
from fastapi import UploadFile, File
from datetime import datetime
from utils.db_session import objects, redis
from utils.email.auth_user import sendmail
from . import payload
from .models import Users, OurImages, Follows
from utils.jwt_auth import create_password, create_token, verify_password
from ..blogs.models import BlogImages, Blogs


async def login(form: payload.Login):
    if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', form.username):
        try:
            user = await objects.get(Users, email=form.username)
        except Exception as e:
            return {'msg': '用户不存在！', 'code': 400}
    else:
        try:
            user = await objects.get(Users, username=form.username)
        except Exception as e:
            return {'msg': '用户不存在！', 'code': 400}
    flag = verify_password(form.password, user.password)
    if not flag:
        return {'msg': '用户名或密码错误！', 'code': 400}

    payload = user.to_dict()
    payload['code'] = 200
    res = create_token(payload=payload)
    payload.update(res)
    return payload


async def get_email_code(email: str):
    ran = random.randint(100000, 999999)
    print(ran)
    html_message = f'<p>Thanks for joining the fantastic cats community.<br/>' \
                   f'We started Candy Cats in 2022 and we are committed to providing a wonderful ' \
                   f'cats world.<br/> You will enjoy being one of our members and rock with the cats!</p>' \
                   f'<p>Verify code：<strong style="margin-right:5px">{ran}</strong> Valid within 5 minutes</p>' \
                   f'<img src="http://8.141.150.118/static/email_bg.png" style="margin-top:20px"> '
    try:
        await redis.set(1, 1)
    except:
        return {'code': 400, 'msg': 'redis服务未开启！'}
    result = sendmail(email, html_message)

    if result == {}:
        await redis.set(email, ran)
        return {'code': 200, 'msg': '验证码已发送 请查收！'}
    else:
        return {'code': 400, 'msg': '邮箱地址不存在，请检查！'}


async def signUp(form: payload.SignUp):
    try:
        code = await redis.get(form.email)
    except:
        return {'msg': 'redis服务未开启！', 'code': 400}
    if code != form.code:
        return {'msg': '验证码不正确', 'code': 400}

    password = create_password(form.password)
    user, status = await objects.create_or_get(Users, username=form.username, email=form.email, password=password)
    if not status:
        return {'msg': '用户名已存在', 'code': 400}

    payload = {'id': user.id, 'username': user.username, 'code': 200}
    res = create_token(payload=payload)
    payload.update(res)
    return payload


async def check_user(email: str = None, username: str = None):
    if email is not None:
        try:
            await objects.get(Users, email=email)
            return {'code': 400, 'msg': '邮箱已经有人使用啦！'}
        except:
            return {'code': 200}

    if username is not None:
        try:
            await objects.get(Users, username=username)
            return {'code': 400, 'msg': '用户名已经被人使用啦！'}
        except:
            return {'code': 200}
    return {'code': 400, 'msg': '参数错误'}


async def password_reset(form: payload.PasswordReset):
    try:
        code = await redis.get(form.email)
    except:
        return {'msg': 'redis服务未开启！', 'code': 400}
    if code != form.code:
        return {'msg': '验证码不正确', 'code': 400}
    password = create_password(form.password1)
    users = await objects.get(Users, email=form.email)
    users.password = password
    await objects.update(users, only=['password'])

    return {'code': 200, 'msg': '密码更新成功！'}


async def upload_b64(form: payload.UpdateAvatar):
    res = form.imgB64.split(',')[1]
    b64decode = base64.b64decode(res)

    if form.flag == 'blog':
        name = form.name
        img_path = os.path.join(settings.SMALL_PATH, name)

    else:
        name = str(form.u_id) + '_' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'
        img_path = os.path.join(settings.AVATAR_PATH, name)
        query = Users.update(avatarUrl=name).where(Users.id == form.u_id)
        await objects.execute(query)

    with open(img_path, 'wb') as f:
        f.write(b64decode)

    avatarUrl = settings.AVATAR_URI_PREFIX + name
    return {
        'avatarUrl': avatarUrl,
        'code': 200
    }


async def upload_binary(request: Request, file: UploadFile = File(...)):
    large_img = await file.read()
    imgB64 = 'data:image/jpeg;base64,' + base64.b64encode(large_img).decode()
    img_arr = cv2.imdecode(np.frombuffer(large_img, np.uint8), cv2.IMREAD_COLOR)
    if img_arr.shape[0] <= img_arr.shape[1]:
        w = 440
        h = int(img_arr.shape[0] / img_arr.shape[1] * w)
        direction = 'v'
    else:
        h = 440
        w = int(img_arr.shape[1] / img_arr.shape[0] * h)
        direction = 'h'
    middle_img = cv2.resize(img_arr, (w, h))
    name = str(request.user.id) + '_' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'
    large_path = os.path.join(settings.LARGE_PATH, name)
    middle_path = os.path.join(settings.MIDDLE_PATH, name)

    with open(large_path, 'wb') as f:
        f.write(large_img)
    cv2.imwrite(middle_path, middle_img)
    cv2.waitKey()

    middle = settings.MIDDLE_URI_PREFIX + name
    return {'name': name,
            'imgB64': imgB64,
            'direction': direction,
            'origin_b64': middle,
            'copper': False,
            'code': 200
            }


async def get_images():
    res = await objects.execute(OurImages.select())
    images = [{'middle': settings.OUR_PREFIX + i.imgName} for i in res]

    return {'count': len(images), 'images': images, 'code': 200, 'msg': '密码更新成功！'}


async def get_userinfo(request: Request, u_id: int = None):
    key = 'u_id'
    if u_id is None:
        u_id = await redis.get(key)
    else:
        await redis.set(key, u_id)
    user = await objects.get(Users, id=u_id)
    follow = request.user.follow_user.select().where(Follows.be_user_id == u_id, Follows.is_active).exists()
    fans = Follows.select().where(Follows.be_user_id == u_id, Follows.user_id != u_id,
                                  Follows.is_active).count()
    be_fans = Follows.select().where(Follows.user_id == u_id, Follows.be_user_id != u_id,
                                     Follows.is_active).count()

    res = user.to_dict()
    res['follow'] = follow
    res['fans'] = fans
    res['be_fans'] = be_fans
    return {'code': 200, 'data': res}


async def get_album(u_id: int):
    query = BlogImages.select(BlogImages.create_time, BlogImages.avatarName, BlogImages.direction).join(Blogs).where(
        Blogs.user_id == u_id, Blogs.is_active)
    result = await objects.execute(query)
    result = [i.__data__ for i in result]
    if not result:
        return {'data': []}
    df = pd.DataFrame(result)
    df['month'] = df['create_time'].apply(lambda x: str(x.month) + '月')
    df['middle'] = df['avatarName'].apply(lambda x: settings.MIDDLE_URI_PREFIX + x)
    res = df.groupby(by=['month'], sort=False).apply(
        lambda x: list(x[['middle', 'direction']].T.to_dict().values())).to_dict()
    return {'data': res}


async def follow_in(request: Request, be_user_id: int):
    follows, status = await objects.get_or_create(Follows, user_id=request.user, be_user_id=be_user_id)
    if not status:
        follows.is_active = True
        await objects.update(follows, only=['is_active'])
    else:
        username = follows.be_user_id.user_id.username


async def follow_out(request: Request, be_user_id: int):
    try:
        follows = await objects.get(Follows, user_id=request.user, be_user_id=be_user_id)
        follows.is_active = False
        await objects.update(follows, only=['is_active'])
    except:
        pass
    return {'code': 200}


async def get_fans(request: Request, u_id: int, index: int, is_self: bool):
    time.sleep(1)
    res = []
    if index == 0:
        query = Follows.select().where(Follows.be_user_id == u_id, Follows.user_id != u_id, Follows.is_active)
        result = await objects.execute(query)
        for i in result:
            follow = Follows.select().where(Follows.user_id == request.user, Follows.be_user_id == i.user_id,
                                            Follows.is_active).exists()
            tmp = i.user_id.to_dict()
            flag = True if follow else False
            tmp['follow'] = flag
            res.append(tmp)
    else:
        query = Follows.select().where(Follows.user_id == u_id, Follows.be_user_id != u_id, Follows.is_active)
        result = await objects.execute(query)
        for i in result:
            if is_self:
                follow = Follows.select().where(Follows.be_user_id == request.user, Follows.user_id == i.be_user_id,
                                                Follows.is_active).exists()
            else:
                follow = Follows.select().where(Follows.user_id == request.user, Follows.be_user_id == i.be_user_id,
                                                Follows.is_active).exists()
            tmp = i.be_user_id.to_dict()
            flag = True if follow else False
            tmp['follow'] = flag
            res.append(tmp)

    return {'data': res}


async def save_bio(request: Request, bio: str):
    await objects.execute(Users.update(bio=bio).where(Users.id == request.user))
    return {'code': 200}
