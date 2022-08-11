#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:04:03 2022

@author: fuzhenghang
"""

import matplotlib.pyplot as plt###引入库包
import numpy as np
import matplotlib as mpl
import netCDF4 as nc
import matplotlib.colors
import xlrd

mpl.rcParams["mathtext.fontset"] = 'cm' #数学文字字体
mpl.rcParams["font.size"] = 12
mpl.rcParams["axes.linewidth"] = 1.5
plt.rcParams['ytick.direction'] = 'in'#将y轴的刻度方向设置向内
mpl.rcParams["font.family"] = 'Times New Roman' 
data=[]
#table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/afterMTCEs.xlsx')
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/beforeMTCEs.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data.append(table.row_values(i))
data = [data[i][0:15] for i in range(0,len(data))]

data1=[]
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/afterMTCEs.xlsx')
#table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/beforeMTCEs.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data1.append(table.row_values(i))
data1 = [data1[i][2:] for i in range(0,len(data1))]

nan=data1[0][-1]
for i in range(0,len(data),2):
    for j in range(len(data[i])):
        if data[i][-1]==nan:
            del(data[i][-1])
            del(data[i+1][-1])
            del(data1[i][-1])
            del(data1[i+1][-1])
for i in range(0,len(data1),2):
    for j in range(len(data1[i])):
        if data1[i][-1]==nan:
            del(data[i][-1])
            del(data[i+1][-1])
            del(data1[i][-1])
            del(data1[i+1][-1])
diff=[]
for i in range(36):
    diff.append(data1[i][3]-data[i][7])
for i in range(36,54):
    diff.append(data1[i][7]-data[i][0])
fig = plt.figure(figsize=(6,6),dpi=600)
ax=plt.gca()
ax.spines['right'].set_color('none') #只保留一条纵坐标轴，形成象限图
ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
ax.set_xlim((-0.5,0.5))
ax.set_xticks([-0.4,-0.2,0.2,0.4])
ax.set_ylim((-5.5, 5.5))
ax.set_yticks([-4,-2,2,4])
label1=['CMCC','CNRM','EC-Earth','ECMWF','MRI-S','MRI-H','NICAM-8S','NICAM-7S','HadGEM']
lab=['^','P','X','D','o','s','*','v','>']
ax.plot(diff[0],diff[0],' ',color='royalblue',label=' ')
ax.plot(diff[0],diff[0],' ',color='green',label=' ')
ax.plot(diff[0],diff[0],' ',color='r',label=' ')
for i in range(9):
    ax.plot(diff[6*i],diff[6*i+1],lab[i],color='k',label=label1[i])
    ax.plot(diff[6*i],diff[6*i+1],lab[i],color='royalblue')
    ax.plot(diff[6*i+2],diff[6*i+3],lab[i],color='green')
    ax.plot(diff[6*i+4],diff[6*i+5],lab[i],color='r')
x1=0
x2=0
x3=0
x4=0
for i in range(27):
    if diff[2*i]>0 and diff[2*i+1]>0:
        x1+=1
    if diff[2*i]>0 and diff[2*i+1]<0:
        x4+=1
    if diff[2*i]<0 and diff[2*i+1]>0:
        x2+=1
    if diff[2*i]<0 and diff[2*i+1]<0:
        x3+=1
print(x1,x2,x3,x4)
ax.legend(frameon=False,bbox_to_anchor=(1,0.65,0.35,0.2))
ax.text(0.65,3.25,'WNP',color='royalblue')
ax.text(0.65,2.7,'ENP',color='green')
ax.text(0.65,2.15,'NA',color='r')
ax.text(0.35,0.2,'$\Delta$ correlation',color='k')
ax.text(0.02,5,'$\Delta$ RMSE',color='k')
mpl.rcParams["font.family"] = 'cm' 
ax.text(0.2,-3,'12 / 27',fontsize=15)
ax.text(0.2,3,'0 / 27',fontsize=15)
ax.text(-0.25,3,'7 / 27',fontsize=15)
ax.text(-0.25,-3,'8 / 27',fontsize=15)
plt.show()


