from fastapi import HTTPException
from DB import db
from login.auth_pro import get_current_user_from_token

def print_attend(subject_id: str, token: str):
    """教科IDと学籍番号(教員ID)と講義回数から出欠状況を取得"""
    userid = get_current_user_from_token(token, 'access_token')  # ログインしたユーザを取得

    #selectSql_1 = "Select * FROM `student_attend` WHERE `講義ID`='%s' && `回数`='%s' && `学籍番号`='%s'" % (
    #    subject_id, number, userid)

    selectSql_1 = "Select * FROM `student_attend` WHERE `講義ID`='%s' && `学籍番号`='%s'" % (
        subject_id, userid.name)

    selectSql_2 = "Select `ID` FROM `teacher_subject`"  # 　教員ID取得

    #selectSql_3 = "Select * FROM `student_attend` WHERE `講義ID`='%s' && `回数`='%s'" % (
    #    subject_id, number)

    selectSql_3 = "Select * FROM `student_attend` WHERE `講義ID`='%s'" % (subject_id)

    conn = db.createMysqlConnecter()
    temp1 = db.selectData(conn, selectSql_2)

    key = 0
    for i in range(len(temp1)):
        if temp1[i][0] == userid.name:
            key = 1  # 教員がログインしている場合の確認

    #raise HTTPException(status_code=401, detail=print(temp))
    if key == 0:
        temp2 = db.selectData(conn, selectSql_1)
    elif key == 1:
        temp2 = db.selectData(conn, selectSql_3)
    else:
        raise HTTPException(status_code=401, detail="不明なエラーが発生しました1")
    
    print(temp1)
    print(temp2)
    print(len(temp2))
    id = []
    name = []
    attend = []
    num = [] #授業回数
    
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
        num.append(temp2[i][0])
        
    return {'student_id': id, 'name': name, 'attend': attend, 'num':num}
