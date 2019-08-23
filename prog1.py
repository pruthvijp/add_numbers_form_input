import time 
a=[]
n=int(input("enter number of integers"))
for i in range (0,n):
	q=int(input("enter numbers"))
	a.insert(i,q)
#print (a)
sum=0
for i in a:
	suminloop=0

	if len(str(i))==1:
		sum=sum+i
	else :
		while (i>0):
			suminloop=suminloop+(i%10) 
			i=int (i/10)
	sum=suminloop+sum
print (sum)