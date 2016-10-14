import csv

fObj = open("peeps.csv") 
d=csv.DictReader(fObj)

print "Printing entire dictionary:"
for k in d:
    print k

print '\n'
fObj = open("peeps.csv") 
d=csv.DictReader(fObj)

print "Printing formatted dictionary:"
for k in d:
    print k['age'] + ", " + k['name'] + ", " + k['id']
    
print '\n'
fObj = open("courses.csv") 
d=csv.DictReader(fObj)

print "Printing formatted dictionary:"
for k in d:
    print k['code'] + ", " + k['mark'] + ", " + k['id']


    
#Q: What can you print here to make each line show only
#   a name and its ID?
#   eg,
#   sasha, 3
