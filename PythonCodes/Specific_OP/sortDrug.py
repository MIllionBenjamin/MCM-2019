#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 23:12:46 2019

@author: apple
"""
import xlrd
import numpy as np
import matplotlib.pyplot as plt

class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

sort = {'Opiates': {'Heroin','6-monoacetylmorphine','6-MAM','Nicomorphine','morphine dinicotinate','dipropanoylmorphine','morphine dipropionate','desomorphine','di-hydro-desoxy-morphine','methyldesorphine',
                               'acetylpropionylmorphine','dibenzoylmorphine','Opiates',
                               'diacetyldihydromorphine'},
        'Semisynthetic opioids': {'7-PET','Acetorphine','Acetyldihydrocodeine','Acetylmorphone','Acetylpropionylmorphine','Azidomorphine','Bentley compounds','Benzhydrocodone','Benzylmorphine','BU-48','Buprenorphine',
                                  'Buprenorphine','naloxone','Buprenorphine/naltrexone','Buprenorphine/samidorphan','Chlornaltrexamine','Chloromorphide','14-Cinnamoyloxycodeinone','Co-dydramol','Codeinone','Codoxime',
                                  'Conorfone','Cyprenorphine','18','19-Dehydrobuprenorphine','Desomorphine','Diacetyldihydromorphine','Diacetylnalorphine','Dibenzoylmorphine','Dibutyrylmorphine','Dihydrocodeine',
                                  'Dihydroetorphine','Dihydromorphine','Dinalbuphine sebacate','2','4-Dinitrophenylmorphine','Diprenorphine','Dipropanoylmorphine','Drotebanol','6','14-Endoethenotetrahydrooripavine',
                                  'Eseroline','14-Ethoxymetopon','Ethylmorphine','Etorphine','5-Guanidinonaltrindole','6-Guanidinonaltrindole','Herkinorin','Heroin','Heterocodeine','Hydrocodone','Hydrocodone/paracetamol',
                                  'Hydromorphinol','Hydromorphone','14-Hydroxydihydrocodeine','IBNtxA','1-Iodomorphine','Levomethorphan','14-Methoxydihydromorphinone','14-Methoxymetopon','Methyldesorphine','Methyldihydromorphine',
                                  '6-Methylenedihydrodesoxymorphine','Methylnaltrexone','Metopon','6-Monoacetylmorphine','Morphine','naltrexone','Morphinone','MR-2096','Myrophine','Nalbuphine','Nalfurafine','Nalmexone','Nalorphine',
                                  'Nalorphine dinicotinate','Naloxazone','Naloxonazine','6β-Naltrexol-d4','6β-Naltrexol','Naltriben','Naltrindole','Nicocodeine','Nicodicodine','Nicomorphine','Noroxymorphone','Oxycodone','Oxycodone',
                                  'naloxone','Oxymorphazone','Oxymorphol','Oxymorphone','Oxytrex','Pentamorphone','N-Phenethyl-14-ethoxymetopon','N-Phenethylnordesomorphine','N-Phenethylnormorphine','14-Phenylpropoxymetopon','Codeine',
                                  'Pholcodine','RAM-378','SoRI-9409','Thebacon','Thienorphine','Xorphanol','Zyklophin'},


        'Synthetic opioids': {'3-HO-PCP','Acetoxyketobemidone','Acetylfentanyl','Acetylmethadol','Acrylfentanyl','AD-1211','AH-7921','Alfentanil','Alimadol','3-Allylfentanyl','Allylnorpethidine','Allylprodine','Alphacetylmethadol',
                              'Alphamethadol','Alphamethylthiofentanyl','Anileridine','Asimadoline','AT-076','Azaprocin','BDPC','Benzethidine','Benzodioxolefentanyl','Benzoylfentanyl','Betacetylmethadol','Betahydroxyfentanyl',
                              'Betahydroxythiofentanyl','Betamethadol','Bezitramide','Bremazocine','Brifentanil','BRL-52537','Bromadoline','BTRX-246040','BU09059','Buprenorphine/samidorphan','Butorphanol','Butyrfentanyl','BW373U86',
                              'C-8813','8-Carboxamidocyclazocine','Carfentanil','CERC-501','4-Chloroisobutyrylfentanyl','Ciprefadol','Ciramadol','Clonitazene','Cyclazocine','Cyclopentylfentanyl','Cyclopropylfentanyl','Cyclorphan',
                              'Cyprodime','DADLE','DAMGO','Desmethylprodine','Desmetramadol','Dextromoramide','Dextropropoxyphene','Diampromide','Dibenzoylmorphine','Diethylthiambutene','Difenoxin','2','2-Difluorofentanyl','Dimenoxadol',
                              'Dimepheptanol','Dimethylthiambutene','Dioxaphetyl butyrate','Diphenoxylate','Dipipanone','Doxpicomine','DPDPE','DPI-221','DPI-287','DPI-3290','Enadoline','Ethoheptazine','Ethylmethylthiambutene',
                              'Etonitazene','Etoxeridine','Faxeladol','Fentanyl','4-Fluorobutyrfentanyl','4-Fluoroisobutyrfentanyl','4-Fluoropethidine','Furanylfentanyl','Furethidine','GR-89696','Hydroxypethidine','IC-26','ICI-199',
                              '441','ICI-204','448','Isobutyrylfentanyl','Isofentanyl','Isomethadone','J-113','397','JDTic','JTC-801','Ketazocine','Ketobemidone','Levacetylmethadol','Levallorphan','Levomethadone','Levomoramide',
                              'Levophenacylmorphan','Levopropoxyphene','Levorphanol','List of fentanyl analogues','Lofentanil','Loperamide','Loperamide/simethicone','LPK-26','LY-2459989','Meprodine','Meptazinol','Metazocine',
                              'Metethoheptazine','Methadone','Methadone intermediate','Metheptazine','Methorphan','Methoxyacetylfentanyl','4-Methoxybutyrfentanyl','Α-Methylacetylfentanyl','3-Methylbutyrfentanyl','N-Methylcarfentanil',
                              '3-Methylfentanyl','Beta-Methylfentanyl','Methylketobemidone','4-Methylphenethylacetylfentanyl','3-Methylthiofentanyl','Metofoline','Mirfentanil','Morpheridine','MT-45','Naloxegol','Nexeridine','NFEPP',
                              'Noracymethadol','Norlevorphanol','Normethadone','Norpethidine','Norpropoxyphene','Ocfentanil','Ohmefentanyl','Orthofluorofentanyl','Oxilorphan','Oxpheneridine','Parafluorofentanyl','Pentazocine','PEPAP',
                              'Pethidine','Pethidine intermediate A','Pethidinic acid','Phenadoxone','Phenampromide','Phenaridine','Phenazocine','Pheneridine','Phenomorphan','4-Phenylfentanyl','3-Phenylpropanoylfentanyl','Picenadol',
                              'Properidine','Prosidol','R-30490','RB-64','Salvinorin B methoxymethyl ether','Sameridine','Samidorphan','Tetrahydrofuranylfentanyl','Tetramethylcyclopropylfentanyl','Thiafentanil','Trimeperidine','Propoxyphene',
                              'U-47700','U-77891','U-48800', 'U-49900', 'U-51754','3,4-Methylenedioxy U-47700','Valerylfentanyl','Cyclopropyl/Crotonyl Fentanyl','Crotonyl fentanyl','Acetyl fentanyl', 'Butyryl fentanyl', 'Furanyl fentanyl', 'p-Fluorobutyryl fentanyl', 
                              'Acryl fentanyl', 'Cyclopropyl fentanyl', 'Fluorofentanyl', '4-Fluoroisobutyryl fentanyl', 'Fluoroisobutyryl fentanyl', 'o-Fluorofentanyl', 'p-Fluorofentanyl', 'Tetrahydrofuran fentanyl', 'Valeryl fentanyl', 
                              'cis-3-methylfentanyl', 'p-methoxybutyryl fentanyl', 'trans-3-Methylfentanyl', '3-Fluorofentanyl', 'Fluorobutyryl fentanyl ', 'Furanyl/3-Furanyl fentanyl', 'Cyclopentyl fentanyl', 'Methoxyacetyl fentanyl', 
                              '4-Methylfentanyl', 'Benzylfentanyl', 'Isobutyryl fentanyl', 'Phenyl fentanyl','ANPP'},
        }

print(type(sort['Synthetic opioids']))

OP_tidyData = np.load("OP_tidyData.npy").item()

OP_Sort_Data = Vividict()

for OPname in OP_tidyData.keys():
    if OPname in sort['Opiates']:
        OP_Sort_Data['Opiates'][OPname] = OP_tidyData[OPname]
        continue
        
    if OPname in sort['Semisynthetic opioids']:
        OP_Sort_Data['Semisynthetic opioids'][OPname] = OP_tidyData[OPname]
        continue
        
    if OPname in sort['Synthetic opioids']:
        OP_Sort_Data['Synthetic opioids'][OPname] = OP_tidyData[OPname]
        continue
    else:
        OP_Sort_Data['Unsorted'][OPname] = OP_tidyData[OPname]
        continue

print(len(OP_Sort_Data['Opiates']), OP_Sort_Data['Opiates'].keys()) 
print(len(OP_Sort_Data['Semisynthetic opioids']), OP_Sort_Data['Semisynthetic opioids'].keys())
print(len(OP_Sort_Data['Synthetic opioids']), OP_Sort_Data['Synthetic opioids'].keys())
print(len(OP_Sort_Data['Unsorted']), OP_Sort_Data['Unsorted'].keys())

ESorts_Total = [0, 0, 0, 0]

for sortName in OP_Sort_Data.keys():
    for OPname in OP_Sort_Data[sortName].keys():
        for year in OP_Sort_Data[sortName][OPname].keys():
            for stateName in OP_Sort_Data[sortName][OPname][year].keys():
                for countyID in OP_Sort_Data[sortName][OPname][year][stateName].keys():
                    if sortName == 'Opiates':
                        ESorts_Total[0] += OP_Sort_Data[sortName][OPname][year][stateName][countyID]
                    elif sortName == "Semisynthetic opioids":
                        ESorts_Total[1] += OP_Sort_Data[sortName][OPname][year][stateName][countyID]
                    elif sortName == "Synthetic opioids":
                        ESorts_Total[2] += OP_Sort_Data[sortName][OPname][year][stateName][countyID]
                    elif sortName == "Unsorted":
                        ESorts_Total[3] += OP_Sort_Data[sortName][OPname][year][stateName][countyID]
                        
print(ESorts_Total)
print(type(ESorts_Total))
print(type(OP_Sort_Data))
#np.save("OP_Sort_Data.npy", OP_Sort_Data)

'''
d = Vividict()

dataTable = xlrd.open_workbook("./OP_Order_MCM_NFLIS_Data.xlsx")

table = dataTable.sheet_by_name("Data")

everyData = []
OP_tidyData = Vividict()

nrows = table.nrows
ncols = table.ncols

for i in range(1, nrows):
    everyData.append(list(table.row_values(i)))

print(everyData[0])

for i in range(0, nrows-1):
    OP_tidyData[everyData[i][6]][int(everyData[i][0])][everyData[i][1]][everyData[i][5]] = int(everyData[i][7])#.append(everyData[i][7])

print(OP_tidyData)
np.save("OP_tidyData.npy", OP_tidyData)
'''

