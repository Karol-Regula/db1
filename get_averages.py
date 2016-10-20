
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f ="discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops


#pre: name must exist 
def computeAvg(name):
	getTemp = "SELECT name, mark FROM students, courses WHERE students.id = courses.id;"
        d = db.cursor()
	dataTemp = (d.execute(getTemp))
	total = 0.0
	tally = 0.0
	for record in dataTemp:
		if record[0] == name:
		        total += record[1]
		        tally += 1.0
	avg = total / tally
	return avg


def displayAverages():
	get = "SELECT name, mark, students.id FROM students, courses WHERE students.id = courses.id;"
	data = (c.execute(get))
	name = ""
	for record in data:
		if not (record[0] == name): #if name hasn't come up before
			print '%s (id %d) has an average of %f'%(record[0], record[2], computeAvg(record[0]))
			name = record[0]


displayAverages()
#print computeAvg('kruder')
db.commit() #save changes
db.close()  #close database
