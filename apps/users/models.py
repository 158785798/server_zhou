import peewee as pw
from utils.baseModel import BaseModel
import settings


class Users(BaseModel):
    username = pw.CharField(null=False, unique=True)
    password = pw.CharField(null=False)
    email = pw.CharField(null=False, unique=True)
    phoneNum = pw.CharField(null=True, default='')
    avatarUrl = pw.CharField(null=True, default='img.png')
    warZone = pw.CharField(null=True, default='')
    bio = pw.CharField(null=True, default='超级帅')

    def to_dict(self):
        self.create_time = str(self.create_time)
        self.update_time = str(self.update_time)
        self.avatarUrl = settings.AVATAR_URI_PREFIX + self.avatarUrl
        self.__data__.pop('password')
        return self.__data__


class OurImages(BaseModel):
    imgName = pw.CharField(null=False, unique=True)
    desc = pw.TextField(null=True, default='')


class Follows(BaseModel):
    user_id = pw.ForeignKeyField(Users, on_delete='CASCADE', related_name='follow_user')
    be_user_id = pw.ForeignKeyField(Users, on_delete='CASCADE', related_name='be_follow_user')
    clicked = pw.BooleanField(null=True, default=False)

    class Meta:
        table_name = 'tb_follows'

if __name__ == '__main__':
    u = Users.get(id=1)
    print(u.be_follow_user.select().where(Follows.user_id == 1, Follows.is_active).exists())
