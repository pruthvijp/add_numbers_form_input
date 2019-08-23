x="global x"


def test(z):
	globals () {x} ='wqwqw' 
	x="localx"
	print(z)


test("local-z")
print (x)