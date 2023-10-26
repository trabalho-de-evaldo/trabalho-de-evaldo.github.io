
#!/usr/bin/python3
import time
import os
import re

c = 0
while True:
	c = c + 1
	arq = open('.resultado')

	os.system('rm -rf .nomes')

	lre = ''

	for l in arq.readlines():
		l = l.replace('\n', '')
		try:
			if re.search('GET /resultado', l):
				l = l.replace('GET /resultado?ponto=', '             f                ')
				l = l.replace('&nome=', ':   ')
				l = l.replace(' HTTP/1.1" 404 -', '')
				l = l.replace(' HTTP/1.1" 200 -', '')
				l = l.replace(' HTTP/1.1" 301 -', '')
				l = l.replace('%20', ' ')
				l = l.replace("'", "")
				l = l.replace('"', '')
				list = l.split('             f                ', 100000)
				os.system("echo '%s' >> .nomes"%list[1])
		except:
			pass

	os.system('cp .nomes .nomes2;cat .nomes | sort --numeric-sort -r | head -n 5 > .egetgr; mv .egetgr .nomes')

	arq2 = open('.nomes')
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
			l = ("""<h5 style="color: white"><font color="red">%s</font><font color="blue">:</font>%s</h5>"""%(listl[0], listl[1]))
			lre = ("""%s\n%s"""%(lre, l))

	os.system('rm -rf .nomes')

	os.system('echo "" > ../resultado.html')

	arq3 = open('../resultado.html', 'w')

	arq3.write(lre)
	arq3.close()

	time.sleep(0.1)
	print ('Rank atualizado: c=%s'%c)

	try:
		arq.seek(0)
		arq2.seek(0)
		arq3.seek(0)
	except:
		pass
