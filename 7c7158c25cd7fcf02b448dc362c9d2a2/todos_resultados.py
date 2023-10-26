
#!/usr/bin/python3
import time
import os
import re

c = 0
while True:
	c = c + 1

	os.system('cat .nomes2 | sort --numeric-sort -r > .egetgr2')

	arq2 = open('.egetgr2')
	for l in arq2.readlines():
		l = l.replace('\\n', '')
		l = l.replace('\\r', '')
		l = l.replace('\n', '')
		l = l.replace('\r', '')
		l = l.replace('\t', '')
		l = l.replace('\\t', '')
		l = l.replace('<', '')
		l = l.replace('>', '')
		l = l.replace('/', '')
		l = l.replace('&', '')
		l = l.replace('$', '')
		l = l.replace('#', '')
		l = l.replace('!', '')
		l = l.replace(';', '')
		l = l.replace('?', '')
		if len(l) > 0:
			listl = l.split(':   ', 2)
			if listl[0] != "00000" and listl[0] != 00000:
				l = ("""Pontos: %s ----- Usuario: %s"""%(listl[0], listl[1]))
				print (l)


	time.sleep(2)
	os.system("clear")
