#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 20:13:07 2019

@author: apple
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:09:23 2019

@author: apple
"""

import math
import statistics as stcs
import numpy as np
import matplotlib.pyplot as plt


KY_reports = [29588, 28285, 27502, 26820, 27077, 25811, 26530, 28870]




everyYearOpioidsInStates = {'KY': [10453, 10289, 10722, 11148, 11081, 9865, 9093, 9394]}

x = [0, 1, 2, 3, 4, 5, 6, 7]
y = []
for i in range(0, 8):
    y.append(everyYearOpioidsInStates['KY'][i])

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

print("S for 7", y[7])
print("S_fitting for 8", k1 * 8 + b1)
print("k1: ", k1, "b1: ", b1)

k1 = -190.8452380952381
b1 = 10923.583333333334

'''
Y2 = []

for i in range(0, 8):
    Y2.append(everyYearOpioidsInStates['KY'][i] + k1 * x[i] * math.exp(k1 * x[i] + b1))

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
    yV.append((xV[i] - 2010) * k1 + b1)

plt.title('The Trend of Every State\'s Opioids Reports (with predicting)')
plt.xlabel('Year')
plt.ylabel('The Number of Opioids Reports')

y_ticks = np.arange(0, 15001, 100)
plt.yticks(y_ticks)

pioidsWithPredicting = everyYearOpioidsInStates['KY']
pioidsWithPredicting.append(9396)

plt.plot(xV,yV,label = 'Predict Curve',color = 'm',linewidth = 2)
plt.plot(years, pioidsWithPredicting, 'r', label = 'KY')

plt.legend(bbox_to_anchor=(1, 0.88), loc='center left')

plt.grid()

plt.tight_layout()


plt.savefig("KY_Predicting_Opioids_Trend.jpg", dpi = 300)

plt.show()

    

