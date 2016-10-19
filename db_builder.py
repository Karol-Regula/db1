import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops


#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

students = open("peeps.csv") #open csv file
d1 = csv.DictReader(students) #read csv file into dictionary

c.execute("CREATE TABLE students (id INTEGER, name TEXT, age INTEGER);") #create table
for k in d1:
    c.execute("INSERT INTO students VALUES(" + k['id'] + ",'" + k['name'] + "'," + k['age'] + ");") #add data to table

courses = open("courses.csv")
d2 = csv.DictReader(courses)

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")
for k in d2:
	c.execute("INSERT INTO courses VALUES('" + k['code'] + "'," + k['mark'] + "," + k['id'] + ");")

'''
cmd = "SELECT * FROM courses WHERE mark = 80"
sel = c.execute(cmd)
for record in sel:
    print record
'''
#==========================================================
db.commit() #save changes
db.close()  #close database


'''
testing protocol:
$ sqlite3 discobandit.db
$ .mode column
$ .header on
$ SELECT * from students;
$ SELECT * from courses;
'''
