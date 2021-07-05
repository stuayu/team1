# peeweeを使ってmariaDBでの実装

from peewee import *
from DB.db_access import db_login

db=db_login()  # データベースにアクセスするには必ず必要


class User(Model):
    id = AutoField(primary_key=True)
    name = CharField(100)
    password = CharField(100)
    refresh_token = TextField(null=True)

    class Meta:
        database = db


db.create_tables([User])

