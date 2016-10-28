import csv
with open('train.csv','rb')as train:
	lines=csv.reader(train)
	for line in lines:
		print line
