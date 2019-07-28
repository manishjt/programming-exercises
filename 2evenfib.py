__author__ = "Manish J. Thapa"

import numpy as np

def fib(i):

	if i==0:
		return 0
	elif i==1:
		return 1
	elif i>1:
		return fib(i-1)+fib(i-2)
	
fibarray=[]
for i in range(40):
	if fib(i)<4000000:
		print fib(i)
		fibarray.append(fib(i))
	else:
		 break
print 'sum', sum(j for j in fibarray if j%2==0)

#elegant
#ls = [1,2]
#while ls[-1] < 4000000:
#    ls.append(ls[-1]+ls[-2])
#print(sum([x for x in ls if x%2==0 ]))

