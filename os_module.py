import sys,os
print (os.getcwd())
sys.path.append('C:\\Users\\Pruthvi\\Desktop\\aws\\scripts\\python_scripts')
#os.chdir('..')
print (os.getcwd())
print (os.listdir('../..'))
print (os.listdir('.'))
try:
	os.rename('test','testy')
except:
	exit
os.environ['G'] = "ddd"
print (os.environ)
print (os.getenv('APPDATA'))
print (os.getenv('G'))
print (os.fchdir(fd))