import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

students = open("peeps.csv") #open csv file
d=csv.DictReader(students) #read csv file into dictionary

c.execute("CREATE TABLE students (name TEXT, id INTEGER, age INTEGER);") #create table
for k in d:
    c.execute("INSERT INTO students VALUES('" + k['name'] + "'," + k['id'] + "," + k['age'] + ")") #add data to table
    
for row in c.execute('SELECT * FROM students'):
        print row #print data from table
        #data printed with 'u' in front, however when the table is inpected in sqlite3 it is fine
# print (c.execute("SELECT * FROM students;")) #this seems to be useless
#c.execute(q)    #run SQL query #I did this separately for each line



'''

q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)
'''

#==========================================================
db.commit() #save changes
db.close()  #close database


