class InputOutString():
    def __init__(self,ww):
        self.s = ""
        self.ww=ww

    def getString(self):
        self.s = input()

    def printString(self):
        print (self.s.upper(), self.ww.upper())

strObj = InputOutString("bin")
strObj.getString()
strObj.printString()