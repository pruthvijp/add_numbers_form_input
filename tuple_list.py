#to store comma sepeated stings to tuples and list 
a =(input("enter numbers seperated by comma"))
print (a)
l=[]
t=()
for i in a.split(','):
	#print (i)
	l.append(i)
t=tuple(l)
	#t.append(i)

print (l,t)

