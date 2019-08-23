#to store o/p of factorial in reverse order and store in dictonary
def fact(n):
	if n==0:
		return 1
	else :
		return (n*fact(n-1))


a =int(input ("enter max number for fact"))

dict={}
for i in range (a,0,-1):
	dict[i]=fact(i)
print (dict)	#print (fact(i))