#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:16:52 2019

@author: apple
"""

import numpy as np
import pandas as pd
from scipy import stats
import operator as op
import pprint

pp = pprint.PrettyPrinter(indent=4)


class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value
    
everyYearOpioidsInStates = {'OH': [19707, 20330, 23145, 26846, 30860, 37127, 42470, 46104], 
                            'KY': [10453, 10289, 10722, 11148, 11081, 9865, 9093, 9394], 
                            'WV': [2890, 3271, 3376, 4046, 3280, 2571, 2548, 1614], 
                            'VA': [8685, 6749, 7831, 11675, 9037, 8810, 10195, 10448], 
                            'PA': [19814, 19987, 19959, 20409, 24904, 25651, 26164, 27894]}

ESF_2010 = np.load("ES_Family_2010.npy").item()
ESF_2011 = np.load("ES_Family_2011.npy").item()
ESF_2012 = np.load("ES_Family_2012.npy").item()
ESF_2013 = np.load("ES_Family_2013.npy").item()
ESF_2014 = np.load("ES_Family_2014.npy").item()
ESF_2015 = np.load("ES_Family_2015.npy").item()
ESF_2016 = np.load("ES_Family_2016.npy").item()

AllData = [ESF_2010, ESF_2011, ESF_2012, ESF_2013, ESF_2014, ESF_2015, ESF_2016]
everyYearESF = Vividict()

for stateID in ESF_2010.keys():
    for itemID in ESF_2010[stateID].keys():
        everyYearESF[stateID][itemID] = []
        
for year in range(0, 6 + 1):
    for stateID in everyYearESF.keys():
        for itemID in everyYearESF[stateID].keys():
            if isinstance(AllData[year][stateID][itemID], float):
                everyYearESF[stateID][itemID].append(AllData[year][stateID][itemID])

pp.pprint(everyYearESF['OH'])
Relations = Vividict()
'''
a = [1.2, 1.5, 1.9]; b = [2.2, 2.5, 3.1]

print(stats.pearsonr(a,b))
print(type(stats.pearsonr(a,b)))
print(stats.pearsonr(a,b)[0])

'''
for stateID in everyYearESF.keys():
    for itemID in everyYearESF[stateID].keys():
        if len(everyYearESF[stateID][itemID]) == 7:
            Relations[stateID][itemID] = stats.pearsonr(everyYearESF[stateID][itemID], everyYearOpioidsInStates[stateID][0:7])[0]

ES_topRelation = Vividict()
ES_highRelation = Vividict()
ES_littleRelation = Vividict()

for stateID in Relations.keys():
    for itemID in Relations[stateID].keys():
        if abs(Relations[stateID][itemID]) >= 0.95:
            ES_topRelation[stateID][itemID] = Relations[stateID][itemID]
        if abs(Relations[stateID][itemID]) >= 0.85:
            ES_highRelation[stateID][itemID] = Relations[stateID][itemID]
        if abs(Relations[stateID][itemID]) <= 0.3:
            ES_littleRelation[stateID][itemID] = Relations[stateID][itemID]

#print(ES_topRelation)
#print(ES_highRelation)
'''
#print(ES_littleRelation)
d = {'a':3, 'b':2, 'c':6}
print(min(zip(d.values(), d.keys()))[0])
'''

ES_TOP_5_R = Vividict()
Elect = Vividict()

for stateID in Relations.keys():
    for itemID in Relations[stateID].keys():
        Elect[stateID][itemID] = abs(Relations[stateID][itemID])

for stateID in Relations.keys():
    for i in range(0, 5 + 1):
        ES_TOP_5_R[stateID][max(zip(Elect[stateID].values(), Elect[stateID].keys()))[1]] = Relations[stateID][max(zip(Elect[stateID].values(), Elect[stateID].keys()))[1]]
        Elect[stateID][max(zip(Elect[stateID].values(), Elect[stateID].keys()))[1]] = 0;

#print(ES_TOP_5_R)
pp.pprint(ES_TOP_5_R)
for itemID in ES_TOP_5_R['OH']:
    print(itemID + ": ", everyYearESF['OH'][itemID])
    
