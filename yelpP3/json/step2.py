# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:38:35 2015

@author: Wes
"""

#partition the data in to restaurant and the others
#output the restaurants json into restList.json

import json

file = open('jsonformat.json')

restList = []
data = json.load(file)

#get a list of item that has restaurants in the "categories" field
for item in data:
    if 'Restaurants' in item['categories']:
        restList.append(item)

for i in range (0, len(restList)):
    restList[i]['rest_id'] = i
    print (restList[i])

with open('restList.json','w') as oFile: 
    json.dump(restList, oFile)
