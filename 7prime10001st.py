__author__ = "Manish J. Thapa"

from __future__ import division

from decimal import Decimal
import numpy as np

thnum=10001
primeornot=np.arange(1,1e6)
prime=[]
cnt=0
#while cnt<10:
for num in primeornot:
	mylist=np.arange(2,num-1)
	list=[num/x for x in mylist]
	listtruth=[]
	for i in list:
		truth=Decimal(str(i)) % 1 == 0
		#print truth
		listtruth.append(truth)
	#print listtruth
	if not any(listtruth)==True:
		prime.append(num)
		#print 'A PRIME!'
		cnt+=1
		if cnt==thnum+1:
			break
	

print 'thnum prime is', prime[-1]	
