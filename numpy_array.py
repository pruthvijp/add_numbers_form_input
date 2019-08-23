#array of seq number multiply by column
import numpy as np
while True:
	a=input ("enter 2 numbers with comma")
	try:
		r,c= a.split(',')
		#int (r,c)
		break
	except :
		print ("enter valide 2 numbers with comma")
matrx=[]
k=0
for i in range(0,int(r)):
	for j in range(0,int(c)):
		#print (i,j)
		kj=i*j
		matrx.insert(k,kj)
		k+=1
#print (matrx,end=" ")
arr=np.array(matrx)
arr=arr.reshape((int(r),int(c)))
print (arr)