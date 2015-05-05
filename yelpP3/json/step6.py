# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:15:23 2015

@author: Wes
"""
from os import path
import json


iFilePath = path.relpath("AZ/Peoria_clean.json")
iFile = open(iFilePath, 'r')
data = json.load(iFile)

cleanList=[]

for item in data:
    cleanList.append(item)

#for i in range (0, len(data)):
#    data[i]['rest_id'] = i
#    data[i]['hours'] = []
#    data[i]['attributes'] = []
    
#longList = []
#latList = []

#for item in data:
#    longList.append(item['longitude'])
#    latList.append(item['latitude'])
    
#minLong = min(longList)
#minLat = min(latList)

#offsetLong = 10-minLong
#offsetLat = 10-minLat

#maxLong = max(longList) + offsetLong
#diffLong = maxLong - 10

#factorLong = 480 / diffLong

#maxLat = max(latList) + offsetLat
#diffLat = maxLat - 10

#factorLat = 680 / diffLat

#for item in data:
#    item['longitude'] = (maxLong - (item['longitude'] + offsetLong))*factorLong + 10
#    item['latitude'] = (maxLong - (item['latitude'] + offsetLat))*factorLat + 10
   
oFilePath = path.relpath("AZ/Peoria_clean.json")
with open (oFilePath, 'w') as oFile:
    json.dump(cleanList, oFile)


    
