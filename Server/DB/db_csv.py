import csv
from DB import db

def csv_create():
    f = open('student_attendance.csv','w') #csvファイルを作成する 
    w = csv.writer(f)

    #student_allからデータを取り出す
    selectSql = "Select * from student_all" 
    conn = db.createMysqlConnecter()
    data = db.selectData(conn, selectSql)

    #取り出したデータの長さ分だけ繰り返す
    for i in range(len(data)):
        w.writerows(data) #データを書き込む
        break

    f.close()

    return print('csv作成')



