# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:33:59 2015

@author: Wes
"""

from os import path
import json

# load json in the data object
iFilePath = path.realpath("AZ/PHOENIX.json")
iFile = open(iFilePath,'r')
data = json.load(iFile)

#create a list object for the clean data, logitude and latitude
cleanList = []
longList = []
latList = []

# remove 'hours' and 'attribute' field
for i in range (0, len(data)):
    data[i]['hours'] = []
    data[i]['attributes'] = []
# get the list of logitude and latitude from the data    
for item in data:
    longList.append(item['longitude'])
    latList.append(item['latitude'])
# get minimun for the longtitude and latitude    
minLong = min(longList)
minLat = min(latList)

#calculate the offset to shift the longitude and latitude to 10
offsetLong = 10-minLong
offsetLat = 10-minLat

#calculate the multiplier for longitude with canvas size 1000 and 20px margin
maxLong = max(longList) + offsetLong
diffLong = (maxLong) - 10
factorLong = 980/diffLong

#calculate the multiplier for the latitude with canvas size 700 and 20px margin
maxLat = max(latList) + offsetLat
diffLat = (maxLat) - 10
factorLat = 680/diffLat

#re assign the longitude and latitude with the new numbers
for item in data:
    newLong = (maxLong - (item['longitude'] + offsetLong))*factorLong + 10
    newLat = (maxLat - (item['latitude'] + offsetLat))*factorLat + 10
    item['longitude'] = newLong
    item['latitude'] = newLat
 
#assign all the cuisine to its color   
American = '#fe3e64'
Southern = '#eb4847'
Mexican = '#d73765'
Cajun = '#c83f69'
Latin_American = '#e03e9c'
Peruvian = '#dda0f6'
Cuban = '#8058bd'
Caribbean = '#8e7de5'
Hawaiian = '#6c7ae0'
Asian = '#4272d7'
Korean = '#2489b0'
Japanese = '#00b5e9'
Chinese = '#4ec8f7'
Thai = '#46d9f9'
Vietnamese = '#00c2d1'
Malaysian = '#28cacc'
Filipino = '#62d8b6'
Indian = '#00b26f'
Middle_Eastern = '#63c76a'
Afghan = '#57b846'
Cambodian = '#83d160'
Pakistani = '#c2e254'
Russian = '#ffe048'
German = '#ffd84f'
Polish = '#faca57'
French = '#ffd965'
Italian = '#ffa037'
Spanish = '#e98c38'
Greek = '#875546'
Mediterranean = '#955542'
Moroccan = '#b45b3e'
African = '#e45d27'
Ethiopian = '#ff5f3d'
British = '#ff8e50'
Irish = '#ff9584'

#re-assign the cuisine for each restaurant
for item in data:
    if 'Mexican' in item['categories']:
        item['categories'] = Mexican
    if 'Moroccan' in item['categories']:
        item['categories'] = Moroccan
    if 'Japanese' in item['categories']:
        item['categories'] = Japanese
    if 'Thai' in item['categories']:
        item['categories'] = Thai
    if 'Indian' in item['categories']:
        item['categories'] = Indian
    if 'Afghan' in item['categories']:
        item['categories'] = Afghan
    if 'American (Traditional)' in item['categories']:
        item['categories'] = American   
    if 'American (New)' in item['categories']:
        item['categories'] = American    
    if 'Vietnamese' in item['categories']:
        item['categories'] = Vietnamese   
    if 'Chinese' in item['categories']:
        item['categories'] = Chinese  
    if 'Pizza' in item['categories']:
        item['categories'] = Italian  
    if 'Barbeque' in item['categories']:
        item['categories'] = American  
    if 'Italian' in item['categories']:
        item['categories'] = Italian  
    if 'Burgers' in item['categories']:
        item['categories'] = American          
    if 'Mediterranean' in item['categories']:
        item['categories'] = Mediterranean 
    if 'Middle Eastern' in item['categories']:
        item['categories'] = Middle_Eastern 
    if 'Latin American' in item['categories']:
        item['categories'] = Latin_American 
    if 'Peruvian' in item['categories']:
        item['categories'] = Peruvian 
    if 'French' in item['categories']:
        item['categories'] = French 
    if 'Sushi Bars' in item['categories']:
        item['categories'] = Japanese 
    if 'Greek' in item['categories']:
        item['categories'] = Greek 
    if 'Chicken Wings' in item['categories']:
        item['categories'] = American 
    if 'Sandwiches' in item['categories']:
        item['categories'] = American 
    if 'Steakhouses' in item['categories']:
        item['categories'] = American         
    if 'Korean' in item['categories']:
        item['categories'] = Korean 
    if 'Tex-Mex' in item['categories']:
        item['categories'] = Mexican 
    if 'Cajun/Creole' in item['categories']:
        item['categories'] = Cajun 
    if 'Hawaiian' in item['categories']:
        item['categories'] = Hawaiian
    if 'Soul Food' in item['categories']:
        item['categories'] = Southern 
    if 'Southern' in item['categories']:
        item['categories'] = Southern
    if 'Caribbean' in item['categories']:
        item['categories'] = Caribbean 
    if 'Cuban' in item['categories']:
        item['categories'] = Cuban        
    if 'Hot Dogs' in item['categories']:
        item['categories'] = American   
    if 'Delis' in item['categories']:
        item['categories'] = American   
    if 'Asian Fusion' in item['categories']:
        item['categories'] = Asian
    if 'Comfort Food' in item['categories']:
        item['categories'] = American  
    if 'Ethiopian' in item['categories']:
        item['categories'] = Ethiopian  
    if 'Fish & Chips' in item['categories']:
        item['categories'] = British  
    if 'Cambodian' in item['categories']:
        item['categories'] = Cambodian
    if 'African' in item['categories']:
        item['categories'] = African 
    if 'Creperies' in item['categories']:
        item['categories'] = French 
    if 'Irish' in item['categories']:
        item['categories'] = Irish 
    if 'Russian' in item['categories']:
        item['categories'] = Russian 
    if 'German' in item['categories']:
        item['categories'] = German 
    if 'Mongolian' in item['categories']:
        item['categories'] = Chinese 
    if 'Pakistani' in item['categories']:
        item['categories'] = Pakistani 
    if 'Polish' in item['categories']:
        item['categories'] = Polish 
    if 'British' in item['categories']:
        item['categories'] = British 
    if 'Spanish' in item['categories']:
        item['categories'] = Spanish 
    if 'Tapas Bars' in item['categories']:
        item['categories'] = Spanish 
    if 'Filipino' in item['categories']:
        item['categories'] = Filipino 
    if 'Malaysian' in item['categories']:
        item['categories'] = Malaysian 
    if 'Taiwanese' in item['categories']:
        item['categories'] = Chinese 
    if 'Tapas/Small Plates' in item['categories']:
        item['categories'] = Spanish 
    if 'Hookah Bar' in item['categories']:
        item['categories'] = Middle_Eastern 
    if 'Bagels' in item['categories']:
        item['categories'] = American 
    if 'Cheasesteaks' in item['categories']:
        item['categories'] = American 
    if type (item['categories']) is list:
        print (item['categories'])
    if type(item['categories']) is not list:
        cleanList.append(item)

for i in range (0, len(cleanList)):
    cleanList[i]['rest_id']= i

#output the new json data into a _clean.json        
oFilePath = path.realpath("AZ/Phoenix_clean.json")
with open (oFilePath, 'w') as oFile:
    json.dump(cleanList, oFile)
    