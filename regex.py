import re
inputw ='''pruthvi.j.pallagatti@gmail.com
        punga_puc@rediff.in
        pruthvi.j.pallagatti1@huawei.commy'''
pattern=re.compile (r'[a-zA-Z._0-9]+@[a-zA-Z-]+\.([a-z][a-z]([a-z]?$))')
matches = pattern.finditer(inputw)

for match in matches:
	print (match)