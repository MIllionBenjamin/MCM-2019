#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:29:50 2019

@author: apple
"""

import numpy as np
import pandas as pd
import csv

'''

'''

class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value




ES_Family = Vividict()

cFile = open("ACS_16_5YR_DP02_with_ann.csv", "r")
reader = csv.DictReader(cFile)

#print(reader.fieldnames) 
#print(reader)

for row in reader:
    if row['GEO.id2'][0:2] == '21':
        for ID in row.keys():
            if ID[0:4] == 'HC01':
                ES_Family['KY'][ID] = 0
        
    if row['GEO.id2'][0:2] == '54':
        for ID in row.keys():
            if ID[0:4] == 'HC01':
                ES_Family['WV'][ID] = 0
        
        
    if row['GEO.id2'][0:2] == '39':
        for ID in row.keys():
            if ID[0:4] == 'HC01':
                ES_Family['OH'][ID] = 0
        
    if row['GEO.id2'][0:2] == '51':
        for ID in row.keys():
            if ID[0:4] == 'HC01':
                ES_Family['VA'][ID] = 0
        
    if row['GEO.id2'][0:2] == '42':
        for ID in row.keys():
            if ID[0:4] == 'HC01':
                ES_Family['PA'][ID] = 0

cFile = open("ACS_16_5YR_DP02_with_ann.csv", "r")
reader = csv.DictReader(cFile)

for row in reader:
    if row['GEO.id2'][0:2] == '21':
        for ID in row.keys():
            if ID[0:4] == 'HC01':
                if row[ID] != '(X)':
                    ES_Family['KY'][ID] += float(row[ID])
        
    if row['GEO.id2'][0:2] == '54':
        for ID in row.keys():
            if ID[0:4] == 'HC01':
                if row[ID] != '(X)':
                    ES_Family['WV'][ID] += float(row[ID])
        
        
    if row['GEO.id2'][0:2] == '39':
        for ID in row.keys():
            if ID[0:4] == 'HC01':
                if row[ID] != '(X)':
                    ES_Family['OH'][ID] += float(row[ID])
        
    if row['GEO.id2'][0:2] == '51':
        for ID in row.keys():
            if ID[0:4] == 'HC01':
                if row[ID] != '(X)':
                    ES_Family['VA'][ID] += float(row[ID])
        
    if row['GEO.id2'][0:2] == '42':
        for ID in row.keys():
            if ID[0:4] == 'HC01':
                if row[ID] != '(X)':
                    ES_Family['PA'][ID] += float(row[ID])
                
print(ES_Family)
np.save("ES_Family_2016.npy", ES_Family)
