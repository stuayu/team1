from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from login.auth_pro import get_current_user_from_token
from DB import db


# ログインした人(教員)の担当科目とログインした人(学生)の履修教科を取り出す関数
def get_subject(token):
    user1 = get_current_user_from_token(token, 'access_token')  # ログインしたユーザを取得
    teacher = []  # DBからデータを収納
    subject = []  # 担当教科を代入するためのタプル

    selectSql_2 = "Select `ID` FROM `teacher_subject`"  # 　教員ID取得

    conn = db.createMysqlConnecter()
    temp1 = db.selectData(conn, selectSql_2)

    key = 0
    for i in range(len(temp1)):
        if temp1[i][0] == user1.name:
            key = 1  # 教員がログインしている場合の確認

    print(key)
    if key == 1:
        selectSql = "Select * from teacher_subject"  # teacher_subjectから教員のデータを取り出す
        teacher = db.selectData(conn, selectSql)
        print(teacher)
        for i in range(len(teacher)):  # teacherの長さの分だけ繰り返す
            if user1.name == teacher[i][0]:  # ログインした人の名前とDBから取得したデータからユーザを探す
                subject.append(teacher[i][4])  # 履修教科を取得
                if teacher[i][5] != None:  # 2つめの科目がある場合追加する
                    subject.append(teacher[i][5])

        return subject

    elif key == 0:
        selectSql = "Select * from student_all"  # student_allから学生のデータを取り出す
        student = db.selectData(conn, selectSql)

        selectSql = "Select * from subject_rules"  # subject_rulesからデータを取り出す。
        subject_data = db.selectData(conn, selectSql)

        for i in range(len(student)):  # studentの長さの分だけ繰り返す
            if user1.name == student[i][0]:  # ログインした人の名前とDBから取得したデータからユーザを探す
                subject = student[i][5:]  # 履修教科を取得
                print(subject)
                break
        t = []  # 空白を取り除いた教科(イニシャル)を代入するためのタプル
        for i in range(len(subject)):
            if len(subject[i]) > 0:  # 空白以外
                t.append(subject[i])  # 空白以外を代入
                
        sub = []  # 教科名を代入するためのタプル
        for i in range(len(subject_data)):
            for j in range(len(t)):
                if subject_data[i][0] == t[j]:  # 講義名と講義IDが同じ場合
                    # subに講義名とそれに応じたIDを追加する(,は講義名とIDの区切り)。
                    #  + "," + t[j]
                    sub.append(subject_data[i][1])
        sub_json = {'id': t, 'sub_name': sub}

        return sub_json

    else:
        return {"message": "不明なエラーが発生しました"}
