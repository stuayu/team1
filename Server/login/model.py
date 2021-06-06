#peeweeを使ってsqliteでの実装
#MariaDBでの実装に変更が必要

from peewee import SqliteDatabase, Model, AutoField, CharField, TextField

db = SqliteDatabase('db.sqlite3')


class User(Model):
    id = AutoField(primary_key=True)
    name = CharField(100)
    password = CharField(100)
    refresh_token = TextField(null=True)

    class Meta:
        database = db


db.create_tables([User])

# ユーザ(先生)のデータ挿入
#とりあえず一人だけ挿入
User.create(name='秋場紀明', password='akiba')