#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 23:00:13 2019

@author: apple
"""

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6, 6))

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

OH_reports = [70999, 71282, 85415, 93747, 101423, 109150, 115276, 119349]
KY_reports = [29588, 28285, 27502, 26820, 27077, 25811, 26530, 28870]
WV_reports = [8668, 9310, 9429, 9062, 6926, 5345, 5405, 3672]
VA_reports = [41462, 28969, 32251, 47694, 32265, 27819, 33539, 36994]
PA_reports = [89981, 86793, 78577, 72096, 77318, 75351, 72376, 68751]

plt.title('The Trend of Every State\'s Total Drug Reports')
plt.xlabel('Year')
plt.ylabel('The Number of Reports')



y_ticks = np.arange(0, 120001, 10000)
plt.yticks(y_ticks)


plt.plot(years, OH_reports, 'c', label = 'OH')
plt.plot(years, KY_reports, 'r', label = 'KY')
plt.plot(years, WV_reports, 'b', label = 'WV')
plt.plot(years, VA_reports, 'g', label = 'VA')
plt.plot(years, PA_reports, 'k', label = 'PA')

plt.legend(bbox_to_anchor=(1, 0.88), loc='center left')

plt.grid()

plt.tight_layout()


plt.savefig("Every_State_Reports_Trend.jpg", dpi = 300)

plt.show()

