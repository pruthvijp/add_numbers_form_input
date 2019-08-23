import time 
a=[]
n=int(input("enter number of integers"))
for i in range (0,n):
	q=int(input("enter numbers"))
	a.insert(i,q)
#print (a)
sum=""
for i in a:
	sum= sum+str(i)
print (''.join(sorted(sum)))
		