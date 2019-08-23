#to store count and word in string  as dictionary
import time 
dicta={}
s = input("enter sentence ")

for word in s.split():	
    
    print (word)
    count=s.count(word)
    dicta[word]=count
    print (count)
    time.sleep(2)
print (dicta)
