#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 21:32:50 2022

@author: fuzhenghang
"""


import numpy as np
import pandas as pd
import xlwt
import xlrd
from datetime import datetime
from scipy import stats
from sklearn.metrics import mean_squared_error
import collections
numyear=101
start=1950
data1=[]
table=xlrd.open_workbook('/dpvhome/dpv16/CMIP6/MRItable/mri-60km.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data1.append(table.row_values(i))
data1 = [data1[i] for i in range(0,len(data1))]
time=[]
num=[]
corr=[]
rmse=[]
frequency=[8,8,5,10,4,8,6,6,9,6,6,12,8,11,5,12,6,10,10,4,5,11,6,6,5,10,6,4,3,8,7,1,8,7,6,4]
for ua in range(17,18):
    da=[]
    for i in range(len(data1)):
        if (100<=data1[i][4]<=180) and data1[i][9]>=ua:
            da.append(data1[i])
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][0]==da[k][0]:
                aa+=1
        g[int((int(da[j][0])+175328)/6)]=[aa,da[j][-4],da[j][-3]]
        if aa>=2:
            mday[int(da[j][-4])-start][int(da[j][-3])-1].append(int((int(da[j][0])+175328)/24))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            mdayn[i].append(len(k))
    #print(mdayn)
    day=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
    #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[int(day[i][1]-start)][int(day[i][2]-1)]+=1
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[int(day[i][1]-start)][int(day[i][2]-1)]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i]))
    corr.append(stats.pearsonr(number[29:65],frequency)[0])
    rmse.append((mean_squared_error(number[29:65],frequency))**(0.5))
#print('WNP:')
#print(corr)
#print(rmse)
#print(number)
file=open('/dpvhome/dpv16/output/mri60b1','w')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close
  
time=[]
num=[]
corr=[]
rmse=[]
frequency=[1,2,2,7,7,5,10,2,7,3,4,6,6,7,5,6,0,1,3,2,2,2,3,5,2,1,3,7,1,7,5,2,2,2,3,7]
for ua in range(17,18):
    da=[]
    for i in range(len(data1)):
        if (180<data1[i][4]<=270) and data1[i][9]>=ua:
            da.append(data1[i])
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][0]==da[k][0]:
                aa+=1
        g[int((int(da[j][0])+175328)/6)]=[aa,da[j][-4],da[j][-3]]
        if aa>=2:
            mday[int(da[j][-4])-start][int(da[j][-3])-1].append(int((int(da[j][0])+175328)/24))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            mdayn[i].append(len(k))
    #print(mdayn)
    day=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
    #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[int(day[i][1]-start)][int(day[i][2]-1)]+=1
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[int(day[i][1]-start)][int(day[i][2]-1)]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i]))
    corr.append(stats.pearsonr(number[29:65],frequency)[0])
    rmse.append((mean_squared_error(number[29:65],frequency))**(0.5))
#print('ENP:')
#print(corr)
#print(rmse)
#print(number)  
file=open('/dpvhome/dpv16/output/mri60b2','w') 
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close
 
time=[]
num=[]
corr=[]
rmse=[]
frequency=[2,1,1,0,0,4,3,0,2,1,5,5,1,2,2,0,4,2,0,3,4,6,3,4,4,5,6,3,3,2,1,4,7,8,3,1]
for ua in range(17,18):
    da=[]
    for i in range(len(data1)):
        if (270<data1[i][4]<=360) and data1[i][9]>=ua:
            da.append(data1[i])
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][0]==da[k][0]:
                aa+=1
        g[int((int(da[j][0])+175328)/6)]=[aa,da[j][-4],da[j][-3]]
        if aa>=2:
            mday[int(da[j][-4])-start][int(da[j][-3])-1].append(int((int(da[j][0])+175328)/24))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            mdayn[i].append(len(k))
    #print(mdayn)
    day=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
    #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[int(day[i][1]-start)][int(day[i][2]-1)]+=1
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[int(day[i][1]-start)][int(day[i][2]-1)]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i]))
    corr.append(stats.pearsonr(number[29:65],frequency)[0])
    rmse.append((mean_squared_error(number[29:65],frequency))**(0.5))
#print('NA:')
#print(corr)
#print(rmse)
#print(number)  
file=open('/dpvhome/dpv16/output/mri60b3','w')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close
    
    
