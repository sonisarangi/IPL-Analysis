import csv

datafile = open('OldBatProfile.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
batdata = []
for row in datareader:
	batdata.append(row)    

datafile = open('OldBowlProfile.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
bowldata = []
for row in datareader:
	bowldata.append(row)    

datafile = open('PlayerMapping.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
mapdata = []
for row in datareader:
	mapdata.append(row)

for i in xrange(0,len(batdata)-1):
	for j in xrange(0,len(mapdata)-1):
		if(batdata[i][0]==mapdata[j][1]):
			batdata[i][0]=mapdata[j][0]
			print (batdata[i][0],mapdata[j][0])
			break

for i in xrange(0,len(bowldata)-1):
	for j in xrange(0,len(mapdata)-1):
		if(bowldata[i][0]==mapdata[j][1]):
			bowldata[i][0]=mapdata[j][0]
			print (bowldata[i][0],mapdata[j][0])
			break

with open("BatProfile.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(batdata)

with open("BowlProfile.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(bowldata)
