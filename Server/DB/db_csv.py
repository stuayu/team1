from DB import db
import csv

#file = open('student_attendance.csv','w')
#w = csv.writer(file)

selectSql = "Select * from student_all"
conn = db.createMysqlConnecter()
c = conn.cursor()

with open('./Server/student_attendance.csv',"w",encoding="utf-8") as f:
    for row in c.execute('SELECT * FROM student_attendance ORDER BY No DESC'):
        f.write(','.join([str(c) for c in row]) + '\n')

conn.close()


