# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:38:47 2020

@author: Juni Asrini
"""

import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt

df1 = pd.read_excel(r'DataProcessed10.xlsx')
df2 = pd.read_excel(r'DataProcessed11.xlsx')

all_df_list = [df2 , df1]

data 	= pd.concat (all_df_list)
var 	= []
mean 	= []
var1 	= []
mu1 	= []
stdev1 	= []
ucl 	= []
lcl 	= []
center 	= []
x 		= 0
variablelist 	= ['Y1_1','Y1_2','Y2_1','Y2_2','Y3','Y4']

for i in variablelist:
    var.append(data[[i,'subgroup']])
    
    mean.append(var[x].groupby('subgroup').mean()) ## mean sample by subgroup
    var1.append(data[i])
    
    mu1.append(stat.mean(var1[x])) ## population mean
    stdev1.append(stat.stdev(var1[x]))
    
    a = mu1[x]+ 3*stdev1[x]
    b = mu1[x]- 3*stdev1[x]
    
    ucl.append(a)
    lcl.append(b)
    
    center.append(stat.mean(mean[x][i]))
    mean[x].plot ()
    plt.title('X-bar Chart Variable ' + i) 
    ucl1 = plt.axhline(ucl[x], linestyle = '--', color = 'r', linewidth = 2)
    ctr = plt.axhline(center[x], color = 'r', linewidth = 2)
    lcl1 = plt.axhline(lcl[x], linestyle = '--', color = 'r', linewidth = 2)
    spec = plt.axhline(0, linestyle = '--', color = 'y', linewidth = 3)
    plt.show()
    
    print('UCL variable ' + i, '=' , a)
    print('LCL variable ' + i, '=' , b)
    
    x += 1
