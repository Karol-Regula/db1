import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

def printer():
    get = "SELECT name




db.commit() #save changes
db.close()  #close database
