import csv
with open('event_type.csv','rb')as event_type:
	lines=csv.reader(event_type)
	for line in lines:
		print line
