#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 14:52:04 2019

@author: apple
"""

import numpy as np
#import matplotlib.pyplot as plt

class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

tidyData2 = np.load("tidyData.npy")

OH_everyYear = {}

for year in range(2010, 2017 + 1):
    OH_everyYear[year] = tidyData2.item()[year]['OH']

for year in range(2010, 2017 + 1):
    for countyID in OH_everyYear[year]:
        OH_everyYear[year][countyID] = sum(OH_everyYear[year][countyID])
        
for year in range(2010, 2017 + 1):
    print(year, len(OH_everyYear[year]))
    
for countyID in OH_everyYear[2011]:
    if countyID not in OH_everyYear[2010]:
        OH_everyYear[2010][countyID] = 0
        print(2010, countyID)
    if countyID not in OH_everyYear[2014]:
        OH_everyYear[2014][countyID] = 0
        print(2014, countyID)

for year in range(2010, 2017 + 1):
    print(year, len(OH_everyYear[year]))

countyList = sorted(OH_everyYear[2010])
print(countyList)
print(len(countyList))
'''
plt.title('The Trend of Every State\'s Opioids Reports')
plt.xlabel('Year')
plt.ylabel('The Number of Opioids Reports')

y_ticks = np.arange(0, 0.501, 0.05)
plt.yticks(y_ticks)
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="two", color='g')
#print(sorted(tidyData2.item()[2010]['OH']))
'''