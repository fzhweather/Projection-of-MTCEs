#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 22:09:10 2022

@author: fuzhenghang
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import xlrd
import seaborn as sns
sns.set(color_codes=True,font_scale=0.8)
mpl.rcParams["font.family"] = 'Times New Roman'
mpl.rcParams["font.weight"] = 'normal'
mpl.rcParams["mathtext.fontset"] = 'cm' 
mpl.rcParams["font.size"] = 8

fig = plt.figure(figsize=(10,5),dpi=600)
x1 = [0.05,0.35,0.65,0.05,0.35,0.65,0.05,0.35,0.65]
yy = [0.95,0.95,0.95,0.65,0.65,0.65,0.35,0.35,0.35]
dx = 0.25
dy = 0.25
ax = []
for i in range(9):
    ax.append(fig.add_axes([x1[i],yy[i],dx,dy]))


fuhao = [[] for i in range(3)]
label = ['(a) WNP-Frequency','(d) ENP-Frequency','(g) NA-Frequency']
data=[]
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/差值变化.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data.append(table.row_values(i))
data = [data[i] for i in range(0,len(data))]
for num in range(3):
# 准备数据
    x_data = ['CMCC','CNRM','EC-Earth','MRI-S','MRI-H','NICAM-8S','NICAM-7S','HadGEM','MME']
    y_data = [data[101][1+num+i*3] for i in range(9)]
    print(y_data)
    
    bb=ax[3*num].bar(x_data, y_data,width=0.4)
    ax[3*num].set_yticks([-2,-1,0,1,2])
    ax[3*num].set_yticklabels([-2,-1,0,1,2],fontsize=8)
    ax[3*num].tick_params(pad=-3)
    for bar,height in zip(bb,y_data):
        if height<0:
            bar.set(color='royalblue')
        elif height>0:
            bar.set(color='r')
    for a,b,c in zip(x_data,y_data,[data[104][1+num+i*3] for i in range(9)]):   #柱子上的数字显示
        if c>1.672:
            ax[3*num].text(a,b,'*',ha='center',fontsize=8)
        elif c<-1.672:
            ax[3*num].text(a,b-0.4,'*',ha='center',fontsize=8)
# 设置x轴标签名
#plt.ylabel("Level, m")
#plt.xlabel("Time")
#for a,b in zip(x_data,y_data):   #柱子上的数字显示
#    plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=10);
# 设置y轴标签名
    ax[3*num].axhline(y=0, color='black', linestyle='-',linewidth = 0.5)
    ax[3*num].text(-0.5,2.31,label[num],fontweight='bold')
    ax[3*num].set_ylim(-2.2,2.2)

ax[3].set_ylabel('Frequency Change',fontsize=8,fontweight='bold',labelpad=2)
ax[0].set_xticklabels([])
ax[3].set_xticklabels([])
ax[6].set_xticklabels(x_data,fontsize=7,rotation=30)


data=[]
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/差值变化天数.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data.append(table.row_values(i))
data = [data[i] for i in range(0,len(data))]
fuhao = [[] for i in range(3)]
label = ['(b) WNP-Duration','(e) ENP-Duration','(h) NA-Duration']
for num in range(3):
# 准备数据
    x_data = ['CMCC','CNRM','EC-Earth','MRI-S','MRI-H','NICAM-8S','NICAM-7S','HadGEM','MME']
    y_data = [data[101][1+num+i*3] for i in range(9)]
    print(y_data)
    ax[3*num+1].tick_params(pad=-3)
    bb=ax[3*num+1].bar(x_data, y_data,width=0.4)
    ax[3*num+1].set_yticks([-20,-10,0,10])
    ax[3*num+1].set_yticklabels([-20,-10,0,10],fontsize=8)
    for bar,height in zip(bb,y_data):
        if height<0:
            bar.set(color='royalblue')
        elif height>0:
            bar.set(color='r')
    for a,b,c in zip(x_data,y_data,[data[104][1+num+i*3] for i in range(9)]):   #柱子上的数字显示
        if c>1.672:
            ax[3*num+1].text(a,b,'*',ha='center',fontsize=8)
        elif c<-1.672:
            ax[3*num+1].text(a,b-3.5,'*',ha='center',fontsize=8)
# 设置x轴标签名
#plt.ylabel("Level, m")
#plt.xlabel("Time")
#for a,b in zip(x_data,y_data):   #柱子上的数字显示
#    plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=10);
# 设置y轴标签名
    ax[1+3*num].axhline(y=0, color='black', linestyle='-',linewidth = 0.5)
    ax[1+3*num].text(-0.5,16,label[num],fontweight='bold')
    ax[1+3*num].set_ylim(-25,15)
    
ax[4].set_ylabel('Duration Change, day',fontsize=8,fontweight='bold',labelpad=1) 
ax[7].set_xlabel('Model',fontsize=10,fontweight='bold')
ax[1].set_xticklabels([])
ax[4].set_xticklabels([])
ax[7].set_xticklabels(x_data,fontsize=7,rotation=30)

data=[]
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/差值变化比例.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data.append(table.row_values(i))
data = [data[i] for i in range(0,len(data))]
fuhao = [[] for i in range(3)]
label = ['(c) WNP-Ratio','(f) ENP-Ratio','(i) NA-Ratio']

for num in range(3):
# 准备数据
    x_data = ['CMCC','CNRM','EC-Earth','MRI-S','MRI-H','NICAM-8S','NICAM-7S','HadGEM','MME']
    y_data = [data[101][1+num+i*3] for i in range(9)]
    print(y_data)
    
    bb=ax[2+3*num].bar(x_data, y_data,width=0.4)
    ax[2+3*num].set_yticks([-0.1,-0.05,0,0.05,0.1])
    ax[2+3*num].tick_params(pad=-3)
    for bar,height in zip(bb,y_data):
        if height<0:
            bar.set(color='royalblue')
        elif height>0:
            bar.set(color='r')
    for a,b,c in zip(x_data,y_data,[data[104][1+num+i*3] for i in range(9)]):   #柱子上的数字显示
        if c>1.672:
            ax[2+3*num].text(a,b,'*',ha='center',fontsize=8)
        elif c<-1.672:
            ax[2+3*num].text(a,b-0.025,'*',ha='center',fontsize=8)
    ax[2+3*num].set_yticklabels([-10,-5,0,5,10])
# 设置x轴标签名
#plt.ylabel("Level, m")
#plt.xlabel("Time")
#for a,b in zip(x_data,y_data):   #柱子上的数字显示
#    plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=10);
# 设置y轴标签名
    ax[2+3*num].axhline(y=0, color='black', linestyle='-',linewidth = 0.5)
    ax[2+3*num].text(-0.5,0.14175,label[num],fontweight='bold')
    ax[2+3*num].set_ylim(-0.135,0.135)

ax[5].set_ylabel('Ratio Change, %',fontsize=8,fontweight='bold',labelpad=1)
ax[2].set_xticklabels([])
ax[5].set_xticklabels([])
ax[8].set_xticklabels(x_data,fontsize=7,rotation=30)
plt.show()
