import csv
from DB import db
from fastapi.responses import StreamingResponse
from login.auth_pro import get_current_user_from_token
from fastapi import HTTPException
from io import StringIO
from typing import List

def create_csv_from_associative_array(data: List[list], **settings) -> str:
    file = StringIO()
    writer = csv.writer(file, **settings)
    writer.writerows(data)
    csv_data = file.getvalue()
    StringIO().close()

    return csv_data


settings = {
    'delimiter': ',',
    'doublequote': True,
    'lineterminator': '\r\n',
    'quotechar': '"',
    'skipinitialspace': True,
    'quoting': csv.QUOTE_MINIMAL,
    'strict': True
}

def csv_create(token: str,id:str):
    userid = get_current_user_from_token(token, 'access_token')  # ログインしたユーザを取得
    selectSql_2 = "Select `ID` FROM `teacher_subject`"  # 　教員ID取得
    conn = db.createMysqlConnecter()
    temp1 = db.selectData(conn, selectSql_2)

    selectSql_1 = "Select * FROM `student_attend` WHERE `講義ID`='%s' && `学籍番号`='%s'" % (
        id, userid.name)

    selectSql_3 = "Select * FROM `student_attend` WHERE `講義ID`='%s'" % (
        id)

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

    #print(temp2[0].replace('()','[]'))
    data:list = []
    print(temp2)
    print(len(temp2)-1)
    print(list(temp2[0]))
    for i in range(len(temp2)):
        data.append(list(temp2[i]))
        print(data)

    csv_data = create_csv_from_associative_array(data=data, **settings)

    return StreamingResponse(csv_data, media_type="text/csv")
