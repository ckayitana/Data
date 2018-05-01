#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 17:34:33 2018

@author: celinekayitana
"""
# Importing libraries

import numpy as np
import pandas as pd


## Q2 A.Proportion of male drivers stop

#Reading Montana (MT) and Vermont(VT) data respectively

MT_cleaned=pd.read_csv('MT_cleaned.csv',index_col=0) #Montana
VT_cleaned=pd.read_csv('VT_cleaned.csv',index_col=0) #Vermont

#Extracting gender and Male data

gender_drivers=MT_cleaned['driver_gender']
male_index=gender_drivers=='M'
male_drivers=gender_drivers[male_index] #Male data only
proportion_of_male=round((len(male_drivers)/len(gender_drivers)),10)

#Printing male drivers proportion of all drivers stops

print("Proportion of Male traffic stops in Montana is: " + str(proportion_of_male))
 
## Q2.B Performing χ2 test for populations are equality
 
# Getting arrest data in both cities

MT_arrest_raw=MT_cleaned[MT_cleaned['is_arrested']]
VT_arrest_raw=VT_cleaned[VT_cleaned['is_arrested']]

MT_arrest=MT_arrest_raw.loc[:,['is_arrested']]
VT_arrest=VT_arrest_raw.loc[:,['is_arrested']]

# Getting total number stops in both cities

MT_tot_stop_count=len(MT_cleaned)
VT_tot_stop_count=len(MT_cleaned)

# Getting total number arrestation in both cities

MT_tot_arrest=len(MT_arrest)
VT_tot_arrest=len(VT_arrest)


# Computing the chisquare test

import scipy.stats as stats
observation = np.array([[MT_tot_arrest, MT_tot_stop_count], [VT_tot_arrest,VT_tot_stop_count]])
chisqaure, pvalue, DOF, Expected = stats.chi2_contingency(observation)

#Printing the pvalue

ttest=round(chisqaure,10)
print("The t statistic is: "+ str(ttest))

## Q2 C likelihood of DUI traffic stop in Montana than in Vermont

#importing regular expression library
import re

#Getting violation data in both cities

MT_violation=MT_cleaned.loc[:,['violation']]
VT_violation=VT_cleaned.loc[:,['violation']]

#Compiling the regular expression to find DUI violations
regex=re.compile(r"\bDUI\b")

#Creating function to count DUI violations...
#passing in the violation data with the corresponding regular expression

def count_DUI(column,regex):
    count_DUI=0 #initialize the empty variable to count
    for lab,row in column.iterrows(): #looping over each row
        #strs2=(row[0])
        if (str(row[0]))!='nan': #ignoring empty rows
            if regex.findall(row[0]):
                count_DUI+=1
    return count_DUI

#Calling the function with Montana data
    
counts_DUI_MT=count_DUI(MT_violation,regex)  
print("The number of DUI stops in Montana is :" + str(counts_DUI_MT))

#Calling the function with Vermont data

counts_DUI_VT=count_DUI(VT_violation,regex)  
print("The number of DUI stops in Vermont is :" + str(counts_DUI_VT))

## Getting counts
all_stops_MT=(len(MT_violation))

#Getting proportion of DUI stops in Montana

MT_DUI_Prop=counts_DUI_MT/all_stops_MT

#Getting proportion of DUI stops in Vermont

VT_DUI_Prop=counts_DUI_VT/(len(VT_violation))
#Getting proportion of Montana DUI stops versus Vermont DUI Stops
MT_VT_Proportion=round((MT_DUI_Prop/VT_DUI_Prop),10)
print("The likelihoot of Montana DUI stops is : " + str(MT_VT_Proportion))

        