

def pr():
	n=int (input("enter the numberin pattern :"))
	print (n)
	for i in range (0,n):
		for j in range (0,n-i-1):
			print (end =" ")
			#print (i,j)
        	#print (j)
		for j in range (0,i+1):
			print ("*" , end ="  ")
		print () 

if __name__ == "__main__":	
	pr()



