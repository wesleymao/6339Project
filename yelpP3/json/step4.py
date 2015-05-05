# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:51:53 2015

@author: Wes
"""

# partition the data into different city from the state json
from os import path
import json

cityList = {}
keyList = ['AZ', 'BW', 'EDH', 'ELN', 'FIF', 'IL', 'KHL', 'MLN', 'NC', 'NV', 'NW', 'ON', 'QC', 'RP', 'SC', 'WI', 'XGL', 'PA']

# open each of the state.json file and load it into data object
for state in keyList:
    ifilepath = state + ".json"
    file = open(ifilepath,'r')
    
    data = json.load(file)
    
    file.close()
    # replace the "/" in the city data with - 
    for item in data:
        if '/' in item['city']:
            print (item['city'])
            temp = item['city'].replace('/', '-')
            item['city'] = temp
            print (item['city'])
        # if city alreay exist in the citylist,we append item into that city's list    
        if item['city'] in cityList:
            cityList[item['city']].append(item)
        # if city does not exist in the citylist, we create the city then append the item to it 
        else:
            cityList[item['city']] = []
            cityList[item['city']].append(item)
    # output the data in each city as separate json file into the state folder    
    for key in cityList:
        ofilepath = state + "/"
        filepath = path.relpath( ofilepath + key + ".json")
        oFile = open(filepath, 'w')
        json.dump(cityList[key], oFile)
        oFile.close()
    cityList={}

#for item in data:
#    stateList[stateList.index(item['state'])].append(item)

    