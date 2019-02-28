#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:40:22 2019

@author: apple
"""

import numpy as np
import matplotlib.pyplot as plt

class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

tidyData2 = np.load("tidyData.npy")
OH_reports = [70999, 71282, 85415, 93747, 101423, 109150, 115276, 119349]
KY_reports = [29588, 28285, 27502, 26820, 27077, 25811, 26530, 28870]
WV_reports = [8668, 9310, 9429, 9062, 6926, 5345, 5405, 3672]
VA_reports = [41462, 28969, 32251, 47694, 32265, 27819, 33539, 36994]
PA_reports = [89981, 86793, 78577, 72096, 77318, 75351, 72376, 68751]

everyYearTotalReportsInStates = {'OH': [70999, 71282, 85415, 93747, 101423, 109150, 115276, 119349], 
                                 'KY': [29588, 28285, 27502, 26820, 27077, 25811, 26530, 28870],
                                 'WV': [8668, 9310, 9429, 9062, 6926, 5345, 5405, 3672], 
                                 'VA': [41462, 28969, 32251, 47694, 32265, 27819, 33539, 36994], 
                                 'PA': [89981, 86793, 78577, 72096, 77318, 75351, 72376, 68751]}

everyYearOpioidsInStates = {'OH': [19707, 20330, 23145, 26846, 30860, 37127, 42470, 46104], 
                            'KY': [10453, 10289, 10722, 11148, 11081, 9865, 9093, 9394], 
                            'WV': [2890, 3271, 3376, 4046, 3280, 2571, 2548, 1614], 
                            'VA': [8685, 6749, 7831, 11675, 9037, 8810, 10195, 10448], 
                            'PA': [19814, 19987, 19959, 20409, 24904, 25651, 26164, 27894]}

everyYearOpioidsPercentInStates = {'OH': [], 
                                   'KY': [], 
                                   'WV': [], 
                                   'VA': [], 
                                   'PA': []}

PRE_everyYearOpioidsInStates = {'OH': [19707, 20330, 23145, 26846, 30860, 37127, 42470, 46104, 53545], 
                            'KY': [10453, 10289, 10722, 11148, 11081, 9865, 9093, 9394, 9396], 
                            'WV': [2890, 3271, 3376, 4046, 3280, 2571, 2548, 1614, 2106], 
                            'VA': [8685, 6749, 7831, 11675, 9037, 8810, 10195, 10448, 10067], 
                            'PA': [19814, 19987, 19959, 20409, 24904, 25651, 26164, 27894, 29424]}

for stateID in everyYearOpioidsInStates:
    for i in range(0, 8):
        everyYearOpioidsPercentInStates[stateID].append(everyYearOpioidsInStates[stateID][i] / everyYearTotalReportsInStates[stateID][i])

print(everyYearOpioidsPercentInStates)        


plt.figure(figsize=(6, 6))

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

plt.title('(Prediction) The Trend of Every State\'s Opioids Percent')
plt.xlabel('Year')
plt.ylabel('The Number of Opioids Reports')

y_ticks = np.arange(0, 50001, 5000)
plt.yticks(y_ticks)

plt.plot(years, PRE_everyYearOpioidsInStates['OH'], 'c', label = 'OH')
plt.plot(years, PRE_everyYearOpioidsInStates['KY'], 'r', label = 'KY')
plt.plot(years, PRE_everyYearOpioidsInStates['WV'], 'b', label = 'WV')
plt.plot(years, PRE_everyYearOpioidsInStates['VA'], 'g', label = 'VA')
plt.plot(years, PRE_everyYearOpioidsInStates['PA'], 'k', label = 'PA')

plt.legend(bbox_to_anchor=(1, 0.88), loc='center left')

plt.grid()

plt.tight_layout()


plt.savefig("Prediction_Every_State_Opioids_Percent_Trend.jpg", dpi = 300)

plt.show()
