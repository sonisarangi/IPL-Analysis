import csv

datafile = open('Match.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
matchorder = []
for row in datareader:
	matchorder.append(row)

batlist = []
bowllist = []
array1d = []
array2d = []

datafile = open('./ProfileData/BowlProfile.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
temp = []
for row in datareader:
	temp.append(row)

datafile = open('ClusterVCluster.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
tempcluster = []
for row in datareader:
	tempcluster.append(row)

datafile = open('./ClusterData/BatsmanClusterData.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
tempbatcluster = []
for row in datareader:
	tempbatcluster.append(row)

datafile = open('./ClusterData/BowlerClusterData.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
tempbowlcluster = []
for row in datareader:
	tempbowlcluster.append(row)

for i in xrange(1,len(matchorder[5])):
	if(matchorder[5][i]==''):
		break
	for j in xrange(1,len(temp)):
		if(matchorder[5][i]==temp[j][0]):
			array1d.append(matchorder[5][i])
			array1d.append(float(temp[j][11]))
			array1d.append(float(temp[j][11]))
			break
	bowllist.append(array1d)
	array1d = []

for i in xrange(1,len(matchorder[0])):
	if(matchorder[0][i]==''):
		break
	datafile = open('./PlayerProbabilities/'+matchorder[0][i]+'.csv', 'r')
	datareader = csv.reader(datafile,delimiter=',')
	temp = []
	for row in datareader:
		temp.append(row)

	for l in xrange(1,len(tempbatcluster)):
		if(matchorder[0][i]==tempbatcluster[l][0]):
			batcluster=tempbatcluster[l][3]

	for j in xrange(0,len(bowllist)):

		for l in xrange(1,len(tempbowlcluster)):
			if(bowllist[j][0]==tempbowlcluster[l][0]):
				bowlcluster=tempbowlcluster[l][4]

		for k in xrange(1,len(temp)):
			if(matchorder[0][i]==temp[k][0]) and (bowllist[j][0]==temp[k][1]):
				array1d.append(matchorder[0][i])
				array1d.append(bowllist[j][0])
				if(temp[k][2]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][2]))
							array1d.append(float(tempcluster[l][2]))	
				else:				
					array1d.append(float(temp[k][2]))
					array1d.append(float(temp[k][2]))
				if(temp[k][3]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][3]))
							array1d.append(float(tempcluster[l][3]))	
				else:				
					array1d.append(float(temp[k][3]))
					array1d.append(float(temp[k][3]))
				if(temp[k][4]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][4]))
							array1d.append(float(tempcluster[l][4]))	
				else:				
					array1d.append(float(temp[k][4]))
					array1d.append(float(temp[k][4]))
				if(temp[k][5]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][5]))
							array1d.append(float(tempcluster[l][5]))	
				else:				
					array1d.append(float(temp[k][5]))
					array1d.append(float(temp[k][5]))
				if(temp[k][6]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][6]))
							array1d.append(float(tempcluster[l][6]))	
				else:				
					array1d.append(float(temp[k][6]))
					array1d.append(float(temp[k][6]))
				if(temp[k][7]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][7]))
							array1d.append(float(tempcluster[l][7]))	
				else:				
					array1d.append(float(temp[k][7]))
					array1d.append(float(temp[k][7]))
				if(temp[k][8]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][8]))
							array1d.append(float(tempcluster[l][8]))
				else:				
					array1d.append(float(temp[k][8]))
					array1d.append(float(temp[k][8]))
				if(temp[k][9]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(1-float(tempcluster[l][9]))
							array1d.append(float(tempcluster[l][9]))	
				else:				
					array1d.append(1-float(temp[k][9]))
					array1d.append(float(temp[k][9]))
				break
		if(len(array1d)==0):
			for l in xrange(1,len(tempcluster)):
				if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
					array1d.append(matchorder[0][i])
					array1d.append(bowllist[j][0])
					array1d.append(float(tempcluster[l][2]))
					array1d.append(float(tempcluster[l][2]))
					array1d.append(float(tempcluster[l][3]))
					array1d.append(float(tempcluster[l][3]))
					array1d.append(float(tempcluster[l][4]))
					array1d.append(float(tempcluster[l][4]))
					array1d.append(float(tempcluster[l][5]))
					array1d.append(float(tempcluster[l][5]))
					array1d.append(float(tempcluster[l][6]))
					array1d.append(float(tempcluster[l][6]))
					array1d.append(float(tempcluster[l][7]))
					array1d.append(float(tempcluster[l][7]))
					array1d.append(float(tempcluster[l][8]))
					array1d.append(float(tempcluster[l][8]))
					array1d.append(1-float(tempcluster[l][9]))
					array1d.append(float(tempcluster[l][9]))
		array2d.append(array1d)
		array1d = []
	batlist.append(array2d)
	array2d = []



for i in xrange(0,len(batlist)):
	for j in xrange(0, len(batlist[i])):
		print (batlist[i][j])

#for i in xrange(0,len(bowllist)):
#	print (bowllist[i])



strike = 1
nonstrike = 2
#for i in xrange(1,20):
	
