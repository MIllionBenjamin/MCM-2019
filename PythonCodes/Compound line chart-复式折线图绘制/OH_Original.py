#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:26:51 2019

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

OH_reports = [70999, 71282, 85415, 93747, 101423, 109150, 115276, 119349]
KY_reports = [29588, 28285, 27502, 26820, 27077, 25811, 26530, 28870]
WV_reports = [8668, 9310, 9429, 9062, 6926, 5345, 5405, 3672]
VA_reports = [41462, 28969, 32251, 47694, 32265, 27819, 33539, 36994]
PA_reports = [89981, 86793, 78577, 72096, 77318, 75351, 72376, 68751]

everyYearOpioidsInStates = {'OH': [19707, 20330, 23145, 26846, 30860, 37127, 42470, 46104], 
                            'KY': [10453, 10289, 10722, 11148, 11081, 9865, 9093, 9394], 
                            'WV': [2890, 3271, 3376, 4046, 3280, 2571, 2548, 1614], 
                            'VA': [8685, 6749, 7831, 11675, 9037, 8810, 10195, 10448], 
                            'PA': [19814, 19987, 19959, 20409, 24904, 25651, 26164, 27894]}

x = [0, 1, 2, 3, 4, 5, 6, 7]
y = []
for i in range(0, 8):
    #y.append(math.log(OH_reports[i] - everyYearOpioidsInStates['OH'][i]))
    y.append(math.log(everyYearOpioidsInStates['OH'][i]))

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

print("S for 7", math.exp(y[7]))
print("S_fitting for 8", math.exp(k1 * 8 + b1))
print("k1: ", k1, "b1: ", b1)

k1 = 0.13321456377277363
b1 = 9.822563069763381

op = []
for i in range(0, 8):
    op.append(math.log(everyYearOpioidsInStates['OH'][i]))
    
OPmean = stcs.mean(op)

xi_Xmeanopi_OPmean = []
for i in range(0, 8):
    xi_Xmeanopi_OPmean.append((x[i] - Xmean) * (op[i] - OPmean))

kOP = sum(xi_Xmeanopi_OPmean) / sum(xi_Xmean2)
bOP = OPmean - kOP * Xmean

print("OP for 7", math.exp(op[7]))
print("OP_fitting for 8", math.exp(kOP * 8 + bOP))
print("kOP: ", k1, "bOP: ", b1)



Y2 = []

for i in range(0, 8):
    Y2.append(everyYearOpioidsInStates['OH'][i] + k1 * x[i] * math.exp(k1 * x[i] + b1))

Y2mean = stcs.mean(Y2)

xi_Xmeany2i_Y2mean = []

for i in range(0, 8):
    xi_Xmeany2i_Y2mean.append((x[i] - Xmean) * (Y2[i] - Y2mean))
    
k2 = sum(xi_Xmeany2i_Y2mean) / sum(xi_Xmean2)
b2 = Y2mean - k2 * Xmean

print(xi_Xmean2)

print(k2, b2)
print("i_fitting for 8", k2 * 8 + b2 - k1 * x[i] * math.exp(k1 * x[i] + b1))

plt.figure(figsize=(6, 6))

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

plt.title('The Trend of Every State\'s Opioids Reports (Original)')
plt.xlabel('Year')
plt.ylabel('The Number of Opioids Reports')

y_ticks = np.arange(0, 55001, 5000)
plt.yticks(y_ticks)

pioidsWithPredicting = everyYearOpioidsInStates['OH']
pioidsWithPredicting.append(53545)

plt.plot(years[:8], pioidsWithPredicting[:8], 'c', label = 'OH')

plt.legend(bbox_to_anchor=(1, 0.88), loc='center left')

plt.grid()

plt.tight_layout()


plt.savefig("OH_Original_Opioids_Trend.jpg", dpi = 300)

plt.show()

    

