#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import re
import codecs

newfile = codecs.open('ru.strings', 'w', 'utf-8')
with open('en.strings', 'r') as f:
	for line in f:
		matches = re.findall(r'"[^"]+"', line)
		if matches:
			key = matches[0].strip('"')
			value = matches[1].strip('"')

			csvfile = open('a.csv', 'r')
			reader = csv.reader(csvfile)

			inrow = []
			for row in reader:
				if row[0] == value:
					inrow = row
					break

			if len(inrow) == 0:
				s = '"'+key+'" = "'+value+'";\n'
				print s
				newfile.write(s.decode('UTF-8'))
			else:
				s1 = '// '+inrow[1]+'\n'
				s2 = '"'+key+'" = "'+inrow[2]+'";\n'
				newfile.write(s1.decode('GBK'))
				newfile.write(s2.decode('GBK'))
		else:
			newfile.write('\n')
newfile.close()
