from utils.db_session import db
from datetime import datetime
import peewee as pw


class BaseModel(pw.Model):
    create_time = pw.DateTimeField(default=datetime.now, formats=['%Y-%m-%d %H:%M:%S'], verbose_name='创建时间')
    update_time = pw.DateTimeField(default=datetime.now, formats=['%Y-%m-%d %H:%M:%S'], verbose_name='更新时间')
    is_active = pw.BooleanField(null=True, default=True)

    class Meta:
        database = db
