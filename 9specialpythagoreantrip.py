__author__ = "Manish J. Thapa"

from __future__ import division

from decimal import Decimal
import numpy as np

a=np.arange(1000)
b=np.arange(1000)
c=np.arange(1000)

def is_whole(n):
    return n % 1 == 0
#can you think of doing this with while loop

for ai in a:
	for bi in b:
		ci=np.sqrt(ai**2+bi**2)		
		if ci>bi>ai and is_whole(ci)==True and ai+bi+ci==1000:
			print ai,bi,ci
			break

			

#From Forum
#!/usr/bin/python 

#c=0
#while True:
#	for b in range(0,c):
#		for a in range(0,b):
#			if a**2 + b**2 == c**2:
#				if a+b+c == 1000:
#					print "a=%d, b=%d, c=%d a*b*c=%d" % (a,b,c,a*b*c)
#	c+=1
