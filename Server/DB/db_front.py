from fastapi import HTTPException
from DB import db


def get_number(subject_id: str):
    """教科IDから授業回数を検索"""
    dic = {}
    # 登録されている最大講義回数を取得
    selectSql_1 = "Select MAX(回数) FROM `student-attend` WHERE `講義ID`='%s'" % (
        subject_id)
    conn = db.createMysqlConnecter()
    temp = db.selectData(conn, selectSql_1)

    number: int = temp[0][0]

    number_list = list(range(1, number))

    dic = {'subject_id': subject_id, 'number': number_list}

    return dic


def print_attend(subject_id: str, number: int, userid: str):
    """教科IDと学籍番号(教員ID)と講義回数から出欠状況を取得"""

    dic = {}
    selectSql_1 = "Select * FROM `student-attend` WHERE `講義ID`='%s' && `回数`='%s' && `学籍番号`='%s'" % (
        subject_id, number, userid)

    selectSql_2 = "Select `ID` FROM `teacher_subject`"  # 　教員ID取得
    conn = db.createMysqlConnecter()
    temp1 = db.selectData(conn, selectSql_2)

    for i in range(len(temp1)):
        if temp1[i][0] == userid:
            key = 1  # 教員がログインしている場合の確認

    #raise HTTPException(status_code=401, detail=print(temp))

    temp = db.selectData(conn, selectSql_1)
