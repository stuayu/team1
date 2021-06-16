import json     # DB->db.json内にあるデータベースへのログインデータの読み込みを行う
from peewee import *    #データベースの操作に必要

def db_login():
    with open('./DB/db.json', 'r', encoding='utf-8') as f:
        db_set = json.load(f)

    db = MySQLDatabase(
        host=db_set['mariadb']['host'],
        port=db_set['mariadb']['port'],
        user=db_set['mariadb']['user'],
        password=db_set['mariadb']['password'],
        database=db_set['mariadb']['dbname'],
    )
    return db