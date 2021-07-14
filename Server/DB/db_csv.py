import csv
from DB import db
from fastapi.responses import StreamingResponse

def csv_create():
    path = 'student_attendance.csv'
    f = open(path, 'w', encoding='utf-8')  # csvファイルを作成する
    w = csv.writer(f)

    #student_allからデータを取り出す
    selectSql = "Select * from student_all" 
    conn = db.createMysqlConnecter()
    data = db.selectData(conn, selectSql)

    w.writerows(data)  # データを書き込む

    f.close()

    f = open(path, mode="r", encoding='utf-8')
    #return print('csv作成')
    return StreamingResponse(f, media_type="text/csv")