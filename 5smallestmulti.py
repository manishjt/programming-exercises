__author__ = "Manish J. Thapa"

from __future__ import division

import numpy as np
lastnum=21

myList=np.arange(1,lastnum)
summ=1
myInt=1
myIntlist=[]
while summ!=0:
	list=[myInt % x for x in myList]
	summ=sum(list)
	myInt=myInt+1
	myIntlist.append(myInt-1)

print 'smallest',myIntlist[-1]

	
