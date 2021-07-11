import csv
import db


f = open('student_attendance.csv','w')
#w = csv.writer(f)

#selectSql = "Select * from student_all" 
#conn = db.createMysqlConnecter()
#data = db.selectData(conn, selectSql)

#for i in data:
#    w.writerows(data)

#f.close()

sql = "SELECT * FROM student_all INTO OUTFILE’student_attendance.csv’ FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY ','"
conn = db.createMysqlConnecter()
c = conn.cursor()
c.execute(sql)

f.close()

