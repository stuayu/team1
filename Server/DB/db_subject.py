from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from login.auth_pro import get_current_user_from_token
from DB import db


#ログインした人(先生)の担当科目を取り出す関数
def get_subject(token):
    user1 = get_current_user_from_token(token,'access_token') #ログインしたユーザを取得
    user2 = [] #DBからデータを収納
    subject =[] #担当教科

    selectSql = "Select * from teacher_subject" #teacher_subjectから先生のデータを取り出す
    conn = db.createMysqlConnecter()
    user2 = db.selectData(conn, selectSql)

    for i in range(len(user2)): #user2の長さの分だけ繰り返す
        if user1.name == user2[i][1]:#ログインした人の名前とDBから取得したデータからユーザを探す
            subject.append(user2[i][4]) #履修教科を取得
            if user2[i][5] != None: #2つめの科目がある場合追加する
                subject.append(user2[i][5])

    return subject





