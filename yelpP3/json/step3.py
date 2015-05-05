# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:51:53 2015

@author: Wes
"""

# partition the data into different state

import json

stateList = {}

# load the json into data object
file = open('restList.json','r')

data = json.load(file)

file.close()

for item in data:
    # if state is already in the list, append the json item into that state
    if item['state'] in stateList:
        stateList[item['state']].append(item)
    # if the state does not exist in the list, create the state then append the item to it
    else:
        stateList[item['state']] = []
        stateList[item['state']].append(item)
# output each item in statelist into a seprate json file        
for key in stateList:
    oFile = open('%s.json' % (key), 'w')
    json.dump(stateList[key], oFile)
    oFile.close()


    