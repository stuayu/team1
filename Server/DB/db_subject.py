from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from login.auth_pro import get_current_user_from_token
from DB import db


#ログインした人(教員)の担当科目を取り出す関数
def get_subject_teacher(token):
    user1 = get_current_user_from_token(token,'access_token') #ログインしたユーザを取得
    user2 = [] #DBからデータを収納
    subject =[] #担当教科を代入するためのタプル

    selectSql = "Select * from teacher_subject" #teacher_subjectから教員のデータを取り出す
    conn = db.createMysqlConnecter()
    user2 = db.selectData(conn, selectSql)

    for i in range(len(user2)): #user2の長さの分だけ繰り返す
        if user1.name == user2[i][1]:#ログインした人の名前とDBから取得したデータからユーザを探す
            subject.append(user2[i][4]) #履修教科を取得
            if user2[i][5] != None: #2つめの科目がある場合追加する
                subject.append(user2[i][5])
            
    return subject

#ログインした人(学生)の履修教科を取り出す関数
def get_subject_student(token):
    user1 = get_current_user_from_token(token,'access_token') #ログインしたユーザを取得
    user2 = [] #DBからデータを収納
    subject =[] #担当教科
    selectSql = "Select * from student_all" #student_allから学生のデータを取り出す
    conn = db.createMysqlConnecter()
    user2 = db.selectData(conn, selectSql)

    selectSql = "Select * from subject_rules" #subject_rulesからデータを取り出す。
    subject_data = db.selectData(conn, selectSql)

    for i in range(len(user2)): #user2の長さの分だけ繰り返す
        if user1.name == user2[i][1]:#ログインした人の名前とDBから取得したデータからユーザを探す
            subject = user2[i][5:] #履修教科を取得
            break
    t = [] # 空白を取り除いた教科(イニシャル)を代入するためのタプル
    for i in range(len(subject)):
        if len(subject[i]) > 0: #空白以外
            t.append(subject[i]) #空白以外を代入

    sub = [] #教科名を代入するためのタプル
    for i in range(len(subject_data)):
        for j in range(len(t)):
            if subject_data[i][0] == t[j]: #講義名と講義IDが同じ場合
                sub.append(subject_data[i][1]+","+t[j]) #subに講義名とそれに応じたIDを追加する(,は講義名とIDの区切り)。
                
    return sub







