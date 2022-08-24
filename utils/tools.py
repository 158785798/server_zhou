import datetime
import math


def parse_time(t):
    timeDelta = datetime.datetime.now() - t
    if 30 < timeDelta.days <= 365:
        pub_time = f'{math.ceil(timeDelta.days / 30)}月前'
    elif 1 <= timeDelta.days <= 30:
        pub_time = f'{timeDelta.days}天前'
    elif 60**2 <=timeDelta.seconds < 60 ** 2 * 24:
        pub_time = f'{int(timeDelta.seconds / 60 ** 2)}小时前'
    elif 60 ** 2 > timeDelta.seconds > 60:
        pub_time = f'{math.ceil(timeDelta.seconds / 60)}分钟前'
    else:
        pub_time = f'{timeDelta.seconds}秒前'
    return pub_time
