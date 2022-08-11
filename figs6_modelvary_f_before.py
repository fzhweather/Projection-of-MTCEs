#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 21:47:14 2022

@author: fuzhenghang
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import xlrd
import seaborn as sns
sns.set(color_codes=True,font_scale=0.8)
mpl.rcParams["font.family"] = 'Times New Roman'  
mpl.rcParams["mathtext.fontset"] = 'cm' 
mpl.rcParams["font.size"] = 8
#mpl.rcParams["font.weight"] = 'bold'
data=[]
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/差值变化before.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data.append(table.row_values(i))
data = [data[i] for i in range(0,len(data))]
sp=[8.7,4.4,4.4]
print(data[101][1:])
print(data[104][1:])

fig = plt.figure(figsize=(4,6),dpi=600)

x1 = [0.1,0.1,0.1]
yy = [0.95,0.7,0.45]
dx = 0.8
dy = 0.23
ax = []
fuhao = [[] for i in range(3)]
label = ['(a) WNP','(b) ENP','(c) NA']
for i in range(3):
    ax.append(fig.add_axes([x1[i],yy[i],dx,dy]))
for num in range(3):
# 准备数据
    x_data = ['CMCC','CNRM','EC-Earth','MRI-S','MRI-H','NICAM-8S','NICAM-7S','HadGEM','MME']
    y_data = [data[101][1+num+i*3] for i in range(9)]
    print(y_data)
    
    bb=ax[num].bar(x_data, y_data,width=0.4)
    ax[num].tick_params(pad=-3)
    for bar,height in zip(bb,y_data):
        if height<0:
            bar.set(color='royalblue')
        elif height>0:
            bar.set(color='r')
    for a,b,c in zip(x_data,y_data,[data[104][1+num+i*3] for i in range(9)]):   #柱子上的数字显示
        if c>1.672:
            ax[num].text(a,b,'*',ha='center',fontsize=10)
        elif c<-1.672:
            ax[num].text(a,b-0.09*sp[num],'*',ha='center',fontsize=10)
# 设置x轴标签名
#plt.ylabel("Level, m")
#plt.xlabel("Time")
#for a,b in zip(x_data,y_data):   #柱子上的数字显示
#    plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=10);
# 设置y轴标签名
    ax[num].axhline(y=0, color='black', linestyle='-',linewidth = 0.5)
    ax[num].text(-0.4,2.2-0.09*sp[num],label[num])
    ax[num].set_ylabel('Frequency Change')
ax[0].set_ylim(-6.5,2.2)
ax[1].set_ylim(-2.2,2.2)
ax[2].set_ylim(-2.2,2.2)
ax[2].set_xlabel('Model')
ax[0].set_xticklabels([])
ax[0].set_yticks([-6,-4,-2,0,2])
ax[1].set_yticks([-2,-1,0,1,2])
ax[2].set_yticks([-2,-1,0,1,2])
ax[1].set_xticklabels([])
ax[2].set_xticklabels(x_data,fontsize=6,rotation=30)
plt.show()
