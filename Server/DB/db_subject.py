from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from login.auth_pro import get_current_user_from_token
from DB import db

#ログインした人の履修科目を取り出す
def get_subject(token):
    user1 = get_current_user_from_token(token,'access_token') #ログインしたユーザを取得
    #user2 = [] #DBからデータを収納
    #selectSql = "Select * from teacher_subject"
    #conn = db.createMysqlConnecter()
    #user2 = db.selectData(conn, selectSql)
    #for i in user2:
    #    if user1 == user2[i][0]:#ログインしたユーザを探す
    #        subject = user2[i][4,5] #履修教科を取得
    return user1
    #return subject





