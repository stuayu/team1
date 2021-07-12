import csv
from DB import db
import codecs

def csv_create():
    f = open('student_attendance.csv','w')
    #sql = "Select * from student_all INTO OUTFILE ’student_attendance.csv’ "
    #conn = db.createMysqlConnecter()
    #c = conn.cursor()
    #c.execute(sql)
    
    w = csv.writer(f)

    selectSql = "Select * from student_all" 
    conn = db.createMysqlConnecter()
    data = db.selectData(conn, selectSql)

    for i in data:
        w.writerows(data)

    f.close()

    return print('csvファイル作成完了')



