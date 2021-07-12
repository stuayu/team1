from fastapi import HTTPException
from DB import db


def get_number(subject_id: str):
    """教科IDから授業回数を検索"""
    dic = {}
    # 登録されている最大講義回数を取得
    selectSql_1 = "Select MAX(回数) FROM `student_attend` WHERE `講義ID`='%s'" % (
        subject_id)
    conn = db.createMysqlConnecter()
    temp = db.selectData(conn, selectSql_1)

    number: int = temp[0][0]

    number_list = list(range(1, number+1))

    dic = {'subject_id': subject_id, 'number': number_list}

    return dic


def print_attend(subject_id: str, number: int, userid: str):
    """教科IDと学籍番号(教員ID)と講義回数から出欠状況を取得"""

    selectSql_1 = "Select * FROM `student_attend` WHERE `講義ID`='%s' && `回数`='%s' && `学籍番号`='%s'" % (
        subject_id, number, userid)

    selectSql_2 = "Select `ID` FROM `teacher_subject`"  # 　教員ID取得

    selectSql_3 = "Select * FROM `student_attend` WHERE `講義ID`='%s' && `回数`='%s'" % (
        subject_id, number)
    conn = db.createMysqlConnecter()
    temp1 = db.selectData(conn, selectSql_2)

    key = 0
    for i in range(len(temp1)):
        if temp1[i][0] == userid:
            key = 1  # 教員がログインしている場合の確認

    #raise HTTPException(status_code=401, detail=print(temp))
    if key == 0:
        temp2 = db.selectData(conn, selectSql_1)
    elif key == 1:
        temp2 = db.selectData(conn, selectSql_3)
    else:
        raise HTTPException(status_code=401, detail="不明なエラーが発生しました1")
    
    print(temp2)
    print(len(temp2))
    id = []
    name = []
    attend = []
    
    for i in range(len(temp2)):
        print(temp2[i][4])
        if temp2[i][4] == '0':
            message = '遅刻'

        elif temp2[i][4] == '1':
            message = '出席'
        else:
            raise HTTPException(status_code=401, detail="不明なエラーが発生しました2")

        id.append(temp2[i][2])
        name.append(temp2[i][3])
        attend.append(message)
        
    return {'学籍番号': id, '名前': name, '出欠': attend}
