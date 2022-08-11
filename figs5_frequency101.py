#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 19:58:09 2022

@author: fuzhenghang
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import xlrd
from scipy.stats import pearsonr
from scipy import optimize
import seaborn as sns
sns.reset_orig()
mpl.rcParams["font.family"] = 'Times New Roman'  
mpl.rcParams["mathtext.fontset"] = 'cm' 
mpl.rcParams["font.size"] = 10

def f_1(x, A, B):
 return A * x + B

data=[]
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/多模式频数.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data.append(table.row_values(i))
data = [data[i] for i in range(0,len(data))]

data1=[]
table1=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/basin.xlsx')
table1=table1.sheets()[0]
nrows1=table1.nrows
for i in range(nrows1):
    if i ==0:
        continue
    data1.append(table1.row_values(i))
data1 = [data1[i][1:] for i in range(0,len(data1))]
print(data1)
fig = plt.figure(figsize=(5,6),dpi=600)

x1 = [0.1,0.1,0.1]
yy = [0.95,0.65,0.35]
dx = 0.8
dy = 0.25
ax = []
fuhao = [[] for i in range(3)]
label = ['(a) WNP','(b) ENP','(c) NA']
for i in range(3):
    ax.append(fig.add_axes([x1[i],yy[i],dx,dy]))
lon=[17.7,10.62,7.08]
for num in range(3):
# 准备数据
    x_data = [i for i in range(1950,2051)]
    y=[]
    y2=[]
    y3=[]
    for i in range(8):
        y.append(data[i*3+num][1:])
    y_data = []
    for i in range(101):
        rank=[]
        for j in range(8):
            rank.append(y[j][i])
        rank.sort()
        y2.append(rank[5])
        y3.append(rank[2])
        
        y_data.append(sum(rank)/8)
    const,p = pearsonr(y_data[29:71], data1[num])
    A1, B1 = optimize.curve_fit(f_1, x_data, y_data)[0]
    xn = np.arange(1950, 2051, 1)#30和75要对应x0的两个端点，0.01为步长
    yn = A1 * xn + B1
    ax[num].plot(xn, yn, '--',color='r',linewidth=1.5,zorder=3)
    A1, B1 = optimize.curve_fit(f_1, x_data[29:71], data1[num])[0]
    xn = np.arange(1950, 2051, 1)#30和75要对应x0的两个端点，0.01为步长
    yn = A1 * xn + B1
    ax[num].plot(xn, yn, '--',color='k',linewidth=1.5,zorder=3)
    ax[num].plot(x_data,y_data,'-',linewidth = 1.5,color='r',label='MME',zorder=3)
    ax[num].plot(x_data[29:71],data1[num],'-',linewidth = 1.5,color='k',label='Observation',zorder=2)
    ax[num].plot(x_data,y2,'-',linewidth = 1,color='gray',zorder=1)
    ax[num].plot(x_data,y3,'-',linewidth = 1,color='gray',zorder=1)
    ax[num].fill_between(x_data, y2, y3, color='steelblue', alpha=0.4,zorder=0)
    ax[num].set_xticks([1950,1975,2000,2025,2050])
    ax[num].set_xlim(1950,2050)
    ax[num].fill_between([1979,2020], 24, 0, color='peachpuff', alpha=0.4,zorder=0)
    ax[num].fill_between([2020,2050], 24, 0, color='sandybrown', alpha=0.4,zorder=0)
    ax[num].text(1951.5,lon[num],label[num])
    ax[num].text(1990,lon[num]*0.98,'r = ',color='b',fontsize=10,fontweight='bold')
    ax[num].text(1990,lon[num]*0.88,'p = ',color='b',fontsize=10,fontweight='bold')
    ax[num].text(1995,lon[num]*0.98,float(format(const,'.3g')) ,color='b',fontsize=10,zorder=4,fontweight='bold')
    ax[num].text(1995,lon[num]*0.88,float(format(p,'.3g')),color='b',fontsize=10,zorder=4,fontweight='bold')
    print(const,p)
#ax[0].text(1995,lon[0]*0.88,'0.400',color='b',fontsize=10,zorder=4,fontweight='bold')
ax[0].set_ylim(0,20)
ax[1].set_ylim(0,12)
ax[2].set_ylim(0,8)
ax[0].set_yticks([0,5,10,15,20])
ax[1].set_yticks([0,3,6,9,12])
ax[2].set_yticks([0,2,4,6,8])
ax[0].legend(frameon=False,loc='lower left',fontsize=8)
ax[2].set_xlabel('Year')
print(rank)