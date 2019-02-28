#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:07:59 2019

@author: apple
"""

import numpy as np
import pandas as pd
from scipy import stats
import operator as op
import pprint
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import csv

pp = pprint.PrettyPrinter(indent=4)

class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

OH_YearOpioidsInStates = {'OH_OP_Reports': [19707, 20330, 23145, 26846, 30860, 37127, 42470, 46104]} 

OH_item = {
'HC01_VC18':  [1118706.0, 1135394.0, 1155991.0, 1178478.0, 1205631.0, 1236302.0, 1268584.0],
#'HC01_VC03':  [4552270.0, 4554007.0, 4555709.0, 4557655.0, 4570015.0, 4585084.0, 4601449.0],
'HC01_VC156':  [440761.0, 450847.0, 454587.0, 427284.0, 416299.0, 400400.0, 387111.0],
'HC01_VC65':  [23082.0, 23605.0, 24275.0, 21515.0, 20701.0, 19829.0, 19274.0],
'HC01_VC17':  [1460679.0, 1443749.0, 1424041.0, 1407968.0, 1397452.0, 1386454.0, 1382386.0],
#'HC01_VC04':  [2983500.0, 2975711.0, 2962217.0, 2949414.0, 2944097.0, 2937598.0, 2940153.0],
}

OH_item_dataframe = pd.DataFrame(data = OH_item)
OH_OP_dataframe = pd.DataFrame(data = OH_YearOpioidsInStates)
OH_total_dataframe = OH_item_dataframe.join(OH_OP_dataframe)

#print(OH_total_dataframe)
#pp.pprint(OH_total_dataframe.values.tolist())

lr = LinearRegression()

train_x = [
        OH_total_dataframe.values.tolist()[0][:4],
        OH_total_dataframe.values.tolist()[1][:4],
        OH_total_dataframe.values.tolist()[2][:4],
        OH_total_dataframe.values.tolist()[3][:4],
        OH_total_dataframe.values.tolist()[4][:4],
        OH_total_dataframe.values.tolist()[5][:4],
        OH_total_dataframe.values.tolist()[6][:4],
        ]
pp.pprint(train_x)


train_y = [[19707], [20330], [23145], [26846], [30860], [37127], [42470]]

x = [0, 1, 2, 3, 4, 5, 6]
plt.scatter(x, train_y)
lr.fit(train_x, train_y)



CO = lr.coef_
IN = lr.intercept_
pp.pprint(CO)
pp.pprint(IN)


print("YearOpioidsReports = " + str(CO[0][0]) + ' HC01_VC18 + '

                              + str(CO[0][1]) + ' HC01_VC156 + '
                              + str(CO[0][2]) + ' HC01_VC65 + '
                              + str(CO[0][3]) + ' HC01_VC17 + '
                              + str(IN[0]) )



print(lr.score([OH_total_dataframe.values.tolist()[6][:4]], [42470]))

#test‘39089’

everyYearItem39089 = Vividict()

for itemID in OH_item.keys():
        everyYearItem39089[itemID] = []
        

cFile = []
cFile.append(open("ACS_10_5YR_DP02_with_ann.csv", "r"))
cFile.append(open("ACS_11_5YR_DP02_with_ann.csv", "r"))
cFile.append(open("ACS_12_5YR_DP02_with_ann.csv", "r"))
cFile.append(open("ACS_13_5YR_DP02_with_ann.csv", "r"))
cFile.append(open("ACS_14_5YR_DP02_with_ann.csv", "r"))
cFile.append(open("ACS_15_5YR_DP02_with_ann.csv", "r"))
cFile.append(open("ACS_16_5YR_DP02_with_ann.csv", "r"))

reader = []
reader.append(csv.DictReader(cFile[0]))
reader.append(csv.DictReader(cFile[1]))
reader.append(csv.DictReader(cFile[2]))
reader.append(csv.DictReader(cFile[3]))
reader.append(csv.DictReader(cFile[4]))
reader.append(csv.DictReader(cFile[5]))
reader.append(csv.DictReader(cFile[6]))

#print(reader.fieldnames) 
#print(reader)
for i in range(0, 6 + 1):
    for row in reader[i]:
        if row['GEO.id2'] == '39089':
            for ID in row.keys():
                if ID in OH_item.keys():
                    everyYearItem39089[ID].append(float(row[ID]))
                

pp.pprint(everyYearItem39089)
everyYearItem39089 = { 

    'HC01_VC18': [15124.0,
                     15733.0,
                     16120.0,
                     16372.0,
                     16907.0,
                     17195.0,
                     17697.0],
  'HC01_VC156': [   2664.0, 2832.0, 2875.0, 2792.0, 2872.0, 2802.0, 2667.0],
    'HC01_VC65': [414.0, 400.0, 473.0, 332.0, 343.0, 305.0, 380.0],
            'HC01_VC17': [21773.0,
                     21828.0,
                     21688.0,
                     21553.0,
                     21224.0,
                     21363.0,
                     20896.0]}




everyYearOP39089 = [[], [], [], [], [], [], []]
OP_Sum_tidyData = np.load("OP_Sum_tidyData.npy").item()
#pp.pprint(OP_Sum_tidyData)

for year in range(2010, 2016 + 1):
    everyYearOP39089[year - 2010].append(OP_Sum_tidyData[year]['OH']['39089'])



OH_item_39089_dataframe = pd.DataFrame(data = everyYearItem39089)
OH_OP_39089_dataframe = pd.DataFrame(data = everyYearOP39089)
OH_total_39089_dataframe = OH_item_39089_dataframe.join(OH_OP_39089_dataframe)
print(OH_total_39089_dataframe)

test_39089_x = [
        OH_total_39089_dataframe.values.tolist()[0][:4],
        OH_total_39089_dataframe.values.tolist()[1][:4],
        OH_total_39089_dataframe.values.tolist()[2][:4],
        OH_total_39089_dataframe.values.tolist()[3][:4],
        OH_total_39089_dataframe.values.tolist()[4][:4],
        OH_total_39089_dataframe.values.tolist()[5][:4],
        OH_total_39089_dataframe.values.tolist()[6][:4],
        ]



predict_data_y = lr.predict(test_39089_x)

print(predict_data_y, lr.predict(train_x))
print(lr.score(test_39089_x, everyYearOP39089))
print(lr.score(train_x, train_y))



print(stats.chi2_contingency(np.array(train_x)))







