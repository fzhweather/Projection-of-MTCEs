#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 20:58:30 2022

@author: fuzhenghang
"""



WNP=[0,0,0.047619048,0.071428571,0.19047619,0.261904762,0.928571429,1.880952381,1.642857143,1.261904762,0.523809524,0.214285714]
ENP=[0,0,0,0,0,0.285714286,0.904761905,1.30952381,0.952380952,0.523809524,0,0]
NA=[0,0,0,0,0,0.023809524,0.166666667,0.976190476,1.380952381,0.428571429,0.047619048,0]
basin=[WNP,ENP,NA]
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import xlrd
import seaborn as sns
from scipy.stats import pearsonr
sns.reset_orig()
yt=[[0,0.5,1,1.5,2,2.5],[0,0.5,1,1.5,2],[0,0.5,1,1.5]]
loc=[0.132,0.235,0.48]
yle=[2.6,2.5,1.5]
co=['royalblue','limegreen','tomato']
mpl.rcParams["font.family"] = 'Times New Roman'  
mpl.rcParams["mathtext.fontset"] = 'cm' 
mpl.rcParams["font.size"] = 12
data=[]
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/monthlybefore.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data.append(table.row_values(i))
data = [data[i] for i in range(0,len(data))]

data1=[]
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/monthlyafter.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data1.append(table.row_values(i))
data1 = [data1[i] for i in range(0,len(data1))]
fig = plt.figure(figsize=(8,6),dpi=600)

x1 = [0.1,0.1,0.1]
yy = [0.95,0.66,0.37]
dx = 0.8
dy = 0.25
ax = []
fuhao = [[] for i in range(3)]
label = ['(a) WNP','(b) ENP','(c) NA']
for i in range(3):
    ax.append(fig.add_axes([x1[i],yy[i],dx,dy]))
for num in range(3):
# 准备数据
    x_data = [i for i in range(1,13)]
    y_data = [data[i+num*14][9] for i in range(0,12)]
    y_data1 = [data1[i+num*14][9] for i in range(0,12)]
    print(y_data)
    spread = np.zeros((2,12))
    ymedian=[]
    spread1 = np.zeros((2,12))
    ymedian1=[]
    for i in range(12):
        a=data[i+14*num][1:9]
        a.sort()
        spread[0,i]=0.5*(a[4]+a[3])-a[2]
        #print(a)
        spread[1,i]=a[5]-0.5*(a[4]+a[3])
        ymedian.append(0.5*(a[4]+a[3]))
        
        a1=data1[i+14*num][1:9]
        a1.sort()
        spread1[0,i]=0.5*(a1[4]+a1[3])-a1[2]
        #print(a)
        spread1[1,i]=a1[5]-0.5*(a1[4]+a1[3])
        ymedian1.append(0.5*(a1[4]+a1[3]))
    #同号   
    for i in range(len(x_data)):  
        x_data[i] = x_data[i]-0.2
    bb=ax[num].bar(x_data, y_data1,width=0.3,color='royalblue',label='Model Output')
    ax[num].errorbar(x_data, ymedian1,fmt='.',mec='w',mew=0.8,ms=8,mfc='k',yerr = spread,c='k',linewidth=1,capsize=3)
    for i in range(len(x_data)):  
        x_data[i] = x_data[i]+0.4
    bb=ax[num].bar(x_data,basin[num] ,width=0.3,color='tomato',label='Observation')
    #ax[num].errorbar(x_data, ymedian1,fmt='.',mec='w',mew=0.8,ms=8,mfc='k',yerr = spread,c='k',linewidth=1,capsize=3)
    for i in range(len(x_data)):  
        x_data[i] = x_data[i]-0.2
    ax[num].bar(x_data, [0 for i in range(12)],width=0.2,color='gold')
    ax[num].set_yticks(yt[num])
    ax[num].tick_params(pad=2)
    ax[num].set_xticks(x_data)
    const1,p1 = pearsonr(y_data, basin[num])
    const2,p2 = pearsonr(y_data1, basin[num])
    #ax[num].text(3.5,yle[num]*0.83,float(format(const1,'.3g')),c='royalblue')
    #ax[num].text(3.5,yle[num]*0.72,float(format(const2,'.3g')),c='tomato')
# 设置x轴标签名
#plt.ylabel("Level, m")
#plt.xlabel("Time")
#for a,b in zip(x_data,y_data):   #柱子上的数字显示
#    plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=10);
# 设置y轴标签名

    ax[0].text(0.3,2.68-num*3.02,label[num])
   
    ax[num].set_ylabel('Frequency')
ax[0].patch.set_facecolor('lightblue')
ax[0].patch.set_alpha(0.3)

ax[1].patch.set_facecolor('lightgreen')
ax[1].patch.set_alpha(0.3)

ax[2].patch.set_facecolor('pink')
ax[2].patch.set_alpha(0.3)
ax[2].set_xlabel('Month')
ax[0].set_ylim(0,2.6)
ax[1].set_ylim(0,2.5)
ax[2].set_ylim(0,1.5)
ax[2].set_xticklabels([1+i for i in range(12)])
ax[0].set_xticklabels([])
ax[1].set_xticklabels([])
ax[2].legend(frameon=False)
plt.show()