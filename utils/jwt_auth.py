from datetime import datetime
from jose import jwt
from apps.users.models import Users
from settings import SECRET_KEY, JWT_AUTH
from passlib.context import CryptContext

from utils.db_session import objects

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_password(password):
    """
    哈希来自用户的密码
    :param password: 原密码
    :return: 哈希后的密码
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """
    校验接收的密码是否与存储的哈希值匹配
    :param plain_password: 原密码
    :param hashed_password: 哈希后的密码
    :return: 返回值为bool类型，校验成功返回True,反之False
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_token(payload):
    """

    :param payload:
    :param data: 需要进行JWT令牌加密的数据（解密的时候会用到）
    :return: token
    """
    claims = payload.copy()

    expire = datetime.utcnow() + JWT_AUTH['JWT_EXPIRATION_DELTA']
    # 添加失效时间
    claims.update({"exp": expire})
    # SECRET_KEY：密钥
    # ALGORITHM：JWT令牌签名算法
    token = jwt.encode(claims, SECRET_KEY, algorithm=JWT_AUTH['JWT_ALGORITHM'])
    return {'token': token}


async def verify_token(token):
    """
    验证token
    :param token:
    :return: 返回用户信息
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=JWT_AUTH['JWT_ALGORITHM'])
        return await objects.get(Users, id=payload['id'])
    except:
        return None
