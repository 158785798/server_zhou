import datetime
import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, 'static')
WHITE_LIST = ['static', 'login', 'get_email_code', 'signUp', 'check_user', 'password_reset', 'get_emojis']


# if sys.platform == 'win32':
#     SERVER = 'http://127.0.0.1:8090/api/static/'
# else:


OUR_PREFIX = SERVER + 'our/'
EMOJI_PREFIX = SERVER + 'emoji/'
AVATAR_URI_PREFIX = SERVER + 'avatar/'
LARGE_URI_PREFIX = SERVER + 'blog_images/large/'
MIDDLE_URI_PREFIX = SERVER + 'blog_images/middle/'
SMALL_URI_PREFIX = SERVER + 'blog_images/small/'

AVATAR_PATH = os.path.join(STATIC_DIR, 'avatar')

LARGE_PATH = os.path.join(os.path.join(STATIC_DIR, 'blog_images'), 'large')
MIDDLE_PATH = os.path.join(os.path.join(STATIC_DIR, 'blog_images'), 'middle')
SMALL_PATH = os.path.join(os.path.join(STATIC_DIR, 'blog_images'), 'small')

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_ALGORITHM': 'HS256',
}

