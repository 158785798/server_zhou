from apps.users import models as user_models
from apps.blogs import models as blog_models

from utils.db_session import db
from peewee_migrate import Router

if __name__ == '__main__':
    db.connect()
    router = Router(db, ignore='basemodel')
    router.create(auto=[user_models, blog_models])
    # router.run()
    router.run(fake=True)
    db.close()
