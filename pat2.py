

def pr():
	n=int (input("enter the numberin pattern :"))
	print (n)
	for i in range (1,n+1):
		for j in range (1,2*n):
			
			if i==n or i+j==n+1 or j-i==n-1 :
				print ("*", end ="")

			else :
				print (end=" ")
		print ()
if __name__ == "__main__":	
	pr()



