#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:32:26 2019

@author: apple
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 20:32:17 2019

@author: apple
"""

import math
import statistics as stcs
import numpy as np
import matplotlib.pyplot as plt


PA_reports = [89981, 86793, 78577, 72096, 77318, 75351, 72376, 68751]


everyYearOpioidsInStates = {'PA': [19814, 19987, 19959, 20409, 24904, 25651, 26164, 27894]}

x = [0, 1, 2, 3, 4, 5, 6, 7]
y = []
for i in range(0, 8):
    y.append(math.log(everyYearOpioidsInStates['PA'][i]))

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

k1 = 0.055862278328475935 
b1 = 9.842679053908535

'''
Y2 = []

for i in range(0, 8):
    Y2.append(everyYearOpioidsInStates['PA'][i] + k1 * x[i] * math.exp(k1 * x[i] + b1))

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

plt.title('The Trend of Every State\'s Opioids Reports (Original)')
plt.xlabel('Year')
plt.ylabel('The Number of Opioids Reports')

y_ticks = np.arange(0, 30001, 500)
plt.yticks(y_ticks)

pioidsWithPredicting = everyYearOpioidsInStates['PA']
pioidsWithPredicting.append(29424)
plt.plot(years[:8], pioidsWithPredicting[:8], 'k', label = 'PA')

plt.legend(bbox_to_anchor=(1, 0.88), loc='center left')

plt.grid()

plt.tight_layout()


plt.savefig("PA_Predicting_Opioids_Trend.jpg", dpi = 300)

plt.show()

    

