#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 20:28:35 2019

@author: apple
"""


import math
import statistics as stcs
import numpy as np
import matplotlib.pyplot as plt

VA_reports = [41462, 28969, 32251, 47694, 32265, 27819, 33539, 36994]


everyYearOpioidsInStates = {'VA': [8685, 6749, 7831, 11675, 9037, 8810, 10195, 10448]}

x = [0, 1, 2, 3, 4, 5, 6, 7]
y = []
for i in range(0, 8):
    y.append(math.log(VA_reports[i] - everyYearOpioidsInStates['VA'][i]))

Xmean = stcs.mean(x)
Ymean = stcs.mean(y)

xi_Xmeanyi_Ymean = []
xi_Xmean2 = []

for i in range(0, 8):
    xi_Xmeanyi_Ymean.append((x[i] - Xmean) * (y[i] - Ymean))
    xi_Xmean2.append((x[i] - Xmean)**2)
    
print(xi_Xmean2)

k1 = sum(xi_Xmeanyi_Ymean) / sum(xi_Xmean2)
b1 = Ymean - k1 * Xmean

print("S for 7", math.exp(y[6]))
print("S_fitting for 8", math.exp(k1 * 8 + b1))
print("k1: ", k1, "b1: ", b1)

k1 = -0.028801876820961417 
b1 = 10.244769216296627

def fit(x):
    return (#-28.7961538461547 * math.pow(x, 5) + 
            #47.4848484848487 * math.pow(x, 4) + 
            -9.66666666666662 * math.pow(x, 3) + 
            85.9761904761897 * math.pow(x, 2) + 
            198.428571428575 * math.pow(x, 1) + 
           7927.00000000000)
    
print(fit(8))

'''
Y2 = []

for i in range(0, 8):
    Y2.append(everyYearOpioidsInStates['VA'][i] + k1 * x[i] * math.exp(k1 * x[i] + b1))

Y2mean = stcs.mean(Y2)

xi_Xmeany2i_Y2mean = []

for i in range(0, 8):
    xi_Xmeany2i_Y2mean.append((x[i] - Xmean) * (Y2[i] - Y2mean))
    
k2 = sum(xi_Xmeany2i_Y2mean) / sum(xi_Xmean2)
b2 = Y2mean - k2 * Xmean

print(xi_Xmean2)

print(k2, b2)
print("i_fitting for 8", k2 * 8 + b2 - k1 * x[i] * math.exp(k1 * x[i] + b1))
'''
plt.figure(figsize=(6, 6))

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
xV = list(np.linspace(2010, 2018, 1000))
print(type(xV))
yV = []
for i in range(0, len(xV)):
    yV.append(fit(xV[i] - 2010))

plt.title('The Trend of Every State\'s Opioids Reports (with predicting)')
plt.xlabel('Year')
plt.ylabel('The Number of Opioids Reports')

y_ticks = np.arange(0, 11501, 200)
plt.yticks(y_ticks)

pioidsWithPredicting = everyYearOpioidsInStates['VA']
pioidsWithPredicting.append(10067)

plt.plot(xV,yV,label = 'Predict Curve',color = 'm',linewidth = 2)
plt.plot(years, pioidsWithPredicting, 'g', label = 'VA')

plt.legend(bbox_to_anchor=(1, 0.88), loc='center left')

plt.grid()

plt.tight_layout()


plt.savefig("VA_Predicting_Opioids_Trend.jpg", dpi = 300)

plt.show()

    

