__author__ = "Manish J. Thapa"

import numpy as np

digit=3
smallest=101
biggest=999
numrange=np.arange(smallest,biggest+1)
palandromicarr=[]
prod=[]

for i in numrange:
	for j in numrange:
		num=i*j
		strg=str(num)[0:digit]
		if str(num)==strg+strg[::-1]:
			palandromicarr.append(str(num))
			prod.append(str(j)+''+str(i))


maxarg=max(palandromicarr)
print 'max arg',maxarg
