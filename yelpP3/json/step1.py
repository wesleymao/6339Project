# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:18:24 2015

@author: Wes
"""

#change the file format to be in [] and separated by ,
#output the new json into jsonformat.json

file = open('yelpBusiness.json')
lines = file.read()

line = lines.split('\n')
#print (line)
print (len(line))

oFile = open('jsonformat.json', 'w')
oFile.write('[')
for i in range (0, len(line)-1):
    if i != len(line)-2:
        oFile.write('%s,\n' % (line[i]))
    else:
        oFile.write('%s' % (line[i]))
    
oFile.write(']')
oFile.close()