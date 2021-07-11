import csv
import db

selectSql = "Select * from student_all"
conn = db.createMysqlConnecter()
data = db.selectdata(conn,selectSql)

with open('student_attendance.csv','a') as f:
    w = csv.writer(f)
    for i in range(len(data)):
        w.writerow(data[i])

