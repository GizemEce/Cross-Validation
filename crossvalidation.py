"""Gizem Ece Yilmaz"""


data=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


"Contract: list->list"
"Purpose: remove same element from a list"
"Examples:[1,2,3],[1,2,3,4,5,6]->[4,5,6]"
def removelement(lon1,lon2):
	for i in lon1:
		for j in lon2:
			if(i==j):
				lon2.remove(j);
	return lon2



print removelement([1,2,3],[1,2,3,4,5,6])
print removelement([0,3,6,9],[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print "Now crossvalidation function is working"


"Contract: list,number->list"
"Purpose: seperates data into traning and test sets according to k value "
"Examples:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]->[[0, 3, 6, 9], [1, 4, 7], [2, 5, 8]]"

def crossvalidation(lon,n):
	grande=[]
	x=0
	while(x<n):
		piccolo=[]
		for i in lon:
			if(i%n==x):
				piccolo.append(i)
		grande.append(piccolo)
		x=x+1
	return grande

print crossvalidation(data,3)
print crossvalidation(data,4)
print "Now returnlists function is working"



"Contract:list number->list list"
"Purpose: print traning and test sets together"
"""Example: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 3-> [1, 2, 4, 5, 7, 8] [0, 3, 6, 9]
                                               [2, 5, 8, 0, 3, 6, 9] [1, 4, 7]
                                               [0, 3, 6, 9, 1, 4, 7] [2, 5, 8]"""

def returnlists(lon,n):
	d=crossvalidation(lon,n)
	print "Traning Sets"," "*9,"Test Sets"
	for i in d:
		print removelement(i,lon),i
		for j in i:
			lon.append(j)

returnlists(data,2)
print"****************"
returnlists(data,3)
print"****************"
returnlists(data,4)
print"****************"
returnlists(data,5)
print"****************"
returnlists(data,10)
