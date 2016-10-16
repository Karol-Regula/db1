import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops


#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

students = open("peeps.csv") #open csv file
d=csv.DictReader(students) #read csv file into dictionary

c.execute("CREATE TABLE students (id INTEGER, name TEXT, age INTEGER);") #create table
for k in d:
    c.execute("INSERT INTO students VALUES(" + k['id'] + ",'" + k['name'] + "'," + k['age'] + ");") #add data to table

'''

q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)
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


