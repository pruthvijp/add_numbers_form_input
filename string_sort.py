#sort strings with commas 
items=[x for x in input("input string with comma").split(',')]
items.sort()

print (','.join(items))