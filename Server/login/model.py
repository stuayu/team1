# peeweeを使ってsqliteでの実装
# MariaDBでの実装に変更が必要

from peewee import *
import json

with open('./DB/db.json', 'r', encoding='utf-8') as f:
    db_set = json.load(f)

db = MySQLDatabase(
    host=db_set['mariadb']['host'],
    port=db_set['mariadb']['port'],
    user=db_set['mariadb']['user'],
    password=db_set['mariadb']['password'],
    database=db_set['mariadb']['dbname'],
)


class User(Model):
    id = AutoField(primary_key=True)
    name = CharField(100)
    password = CharField(100)
    refresh_token = TextField(null=True)

    class Meta:
        database = db


db.create_tables([User])

# ユーザ(先生)のデータ挿入
# とりあえず一人だけ挿入
#User.create(name='秋場紀明', password='akiba')
