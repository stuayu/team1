from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from auth_pro import get_current_user
from login.auth_pro import get_current_user
from DB import db

#ログインした人の履修科目を取り出す
def get_subject(tokens):
    user1 = get_current_user(tokens) #ログインしたユーザを取得
    user2 = [] #DBからデータを収納
    selectSql = 'Select * from %s' % table
    conn = db.createMysqlConnecter()
    user2 = db.selectData(conn, selectSql)
    for i in user2:
        if user1 == user2[i][0]:#ログインしたユーザを探す
            subject = user2[i][4,5] #履修教科を取得
    return subject





