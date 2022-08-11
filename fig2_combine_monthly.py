#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 23:08:56 2022

@author: fuzhenghang
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import xlrd
import seaborn as sns
sns.set(color_codes=True)
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
    
yt=[[-0.4,-0.2,0,0.2],[-0.4,-0.2,0,0.2],[-0.2,0,0.2,0.4]]
loc=[0.132,0.235,0.48]
data=[]
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/逐月变化.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data.append(table.row_values(i))
data = [data[i] for i in range(0,len(data))]
fuhao = [[] for i in range(3)]
label = ['(a) WNP-Frequency','(d) ENP-Frequency','(g) NA-Frequency']
for num in range(3):
# 准备数据
    x_data = [i for i in range(1,13)]
    y_data = [data[i+num*14][9] for i in range(0,12)]
    print(y_data)
    spread = np.zeros((2,12))
    ymedian=[]
    for i in range(12):
        a=data[i+14*num][1:9]
        a.sort()
        spread[0,i]=0.5*(a[4]+a[3])-a[2]
        #print(a)
        spread[1,i]=a[5]-0.5*(a[4]+a[3])
        ymedian.append(0.5*(a[4]+a[3]))
    #同号
    for mon in range(12):
        count=0
        for k in range(1,9):
            if data[mon+num*14][k]*data[mon+num*14][9]>0:
                count+=1
        fuhao[num].append(count)    
    bb=ax[num*3].bar(x_data, y_data,width=0.4)
    ax[3*num].errorbar(x_data, ymedian,fmt='.',mec='w',mew=0.6,ms=6,mfc='k',yerr = spread,c='k',linewidth=0.8,capsize=2.5)
    ax[3*num].set_yticks(yt[num])
    ax[3*num].set_yticklabels(yt[num],fontsize=8)
    ax[3*num].tick_params(pad=-3)
    ax[3*num].set_xticks(x_data)
    
    for bar,height in zip(bb,y_data):
        if height<0:
            bar.set(color='royalblue')
        elif height>0:
            bar.set(color='r')   
# 设置x轴标签名
#plt.ylabel("Level, m")
#plt.xlabel("Time")
#for a,b in zip(x_data,y_data):   #柱子上的数字显示
#    plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=10);
# 设置y轴标签名
    ax[3*num].axhline(y=0, color='black', linestyle='-',linewidth = 0.5)
    ax[0].text(0.5,0.22-num*0.879,label[num],fontsize=8,fontweight='bold')
   
    for i in range(12):
        if fuhao[num][i]>4:
            if y_data[i]>0:
                ax[3*num].text(i+1,loc[num],fuhao[num][i],color='r',horizontalalignment='center',fontsize=8,fontweight='bold')
            elif y_data[i]<0:
                ax[3*num].text(i+1,loc[num],fuhao[num][i],color='b',horizontalalignment='center',fontsize=8,fontweight='bold')

print(fuhao)
ax[3].set_ylabel('Frequency Change',fontsize=8,fontweight='bold',labelpad=2)
ax[6].set_xticklabels(x_data,fontsize=8)
ax[0].set_xticklabels([])
ax[3].set_xticklabels([])
ax[6].set_ylim(-0.2,0.55)
ax[3].set_ylim(-0.45,0.3)

yt=[[-4,-2,0,2],[-2,-1,0,1],[-1,0,1,2]]
loc=[1.37,0.72,2.07]
mpl.rcParams["font.family"] = 'Times New Roman'  
mpl.rcParams["mathtext.fontset"] = 'cm' 
mpl.rcParams["font.size"] = 10
data=[]
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/逐月变化天数.xlsx')
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
    x_data = [i for i in range(1,13)]
    y_data = [data[i+num*14][9] for i in range(0,12)]
    print(y_data)
    spread = np.zeros((2,12))
    ymedian=[]
    for i in range(12):
        a=data[i+14*num][1:9]
        a.sort()
        spread[0,i]=0.5*(a[4]+a[3])-a[2]
        #print(a)
        spread[1,i]=a[5]-0.5*(a[4]+a[3])
        ymedian.append(0.5*(a[4]+a[3]))
    #同号
    for mon in range(12):
        count=0
        for k in range(1,9):
            if data[mon+num*14][k]*data[mon+num*14][9]>0:
                count+=1
        fuhao[num].append(count)    
    bb=ax[1+3*num].bar(x_data, y_data,width=0.4)
    ax[1+3*num].errorbar(x_data, ymedian,fmt='.',mec='w',mew=0.6,ms=6,mfc='k',yerr = spread,c='k',linewidth=0.8,capsize=2.5)
    ax[1+3*num].set_yticks(yt[num])
    ax[1+3*num].set_yticklabels(yt[num],fontsize=8)
    ax[1+3*num].tick_params(pad=-3)
    ax[1+3*num].set_xticks(x_data)
    ax[1].text(0.5,2.2-num*8.2,label[num],fontsize=8,fontweight='bold')
    for bar,height in zip(bb,y_data):
        if height<0:
            bar.set(color='royalblue')
        elif height>0:
            bar.set(color='r')

    ax[1+3*num].axhline(y=0, color='black', linestyle='-',linewidth = 0.5)
    #ax[num].set_ylim(-5,3.125)

    for i in range(12):
        if fuhao[num][i]>4:
            if y_data[i]>0:
                ax[1+3*num].text(i+1,loc[num],fuhao[num][i],color='r',horizontalalignment='center',fontsize=8,fontweight='bold')
            elif y_data[i]<0:
                ax[1+3*num].text(i+1,loc[num],fuhao[num][i],color='b',horizontalalignment='center',fontsize=8,fontweight='bold')
ax[7].set_xlabel('Month',fontsize=10,fontweight='bold')
ax[7].set_xticklabels(x_data,fontsize=8)
ax[1].set_xticklabels([])
ax[4].set_xticklabels([])
ax[7].set_ylim(-1,2.4)
ax[4].set_ylabel('Duration Change, day',fontsize=8,fontweight='bold',labelpad=1)


yt=[[-0.2,-0.1,0,0.1],[-0.1,0,0.1],[-0.1,0,0.1,0.2]]
loc=[0.113,0.112,0.17]
mpl.rcParams["font.family"] = 'Times New Roman'  
mpl.rcParams["mathtext.fontset"] = 'cm' 
mpl.rcParams["font.size"] = 10
data=[]
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/逐月比例.xlsx')
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
    x_data = [i for i in range(1,13)]
    y_data = [data[i+num*14][9] for i in range(0,12)]
    print(y_data)
    spread = np.zeros((2,12))
    ymedian=[]
    for i in range(12):
        a=data[i+14*num][1:9]
        a.sort()
        spread[0,i]=0.5*(a[4]+a[3])-a[2]
        #print(a)
        spread[1,i]=a[5]-0.5*(a[4]+a[3])
        ymedian.append(0.5*(a[4]+a[3]))
    #同号
    for mon in range(12):
        count=0
        for k in range(1,9):
            if data[mon+num*14][k]*data[mon+num*14][9]>0:
                count+=1
        fuhao[num].append(count)    
    bb=ax[2+3*num].bar(x_data, y_data,width=0.4)
    ax[2+3*num].errorbar(x_data, ymedian,fmt='.',mec='w',mew=0.6,ms=6,mfc='k',yerr = spread,c='k',linewidth=0.8,capsize=2.5)
    ax[2+3*num].set_yticks(yt[num])
    ax[2+3*num].set_yticklabels(yt[num],fontsize=8)
    ax[2+3*num].tick_params(pad=-3)
    ax[2+3*num].set_xticks(x_data,fontize=8)
    
    for bar,height in zip(bb,y_data):
        if height<0:
            bar.set(color='royalblue')
        elif height>0:
            bar.set(color='r')   
# 设置x轴标签名
#plt.ylabel("Level, m")
#plt.xlabel("Time")
#for a,b in zip(x_data,y_data):   #柱子上的数字显示
#    plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=10);
# 设置y轴标签名
    ax[2+3*num].axhline(y=0, color='black', linestyle='-',linewidth = 0.5)
    ax[2].text(0.5,0.16-num*0.443,label[num],fontsize=8,fontweight='bold')
   
    for i in range(12):
        if fuhao[num][i]>4:
            if y_data[i]>0:
                ax[2+3*num].text(i+1,loc[num],fuhao[num][i],color='r',horizontalalignment='center',fontsize=8,fontweight='bold')
            elif y_data[i]<0:
                ax[2+3*num].text(i+1,loc[num],fuhao[num][i],color='b',horizontalalignment='center',fontsize=8,fontweight='bold')
ax[5].set_ylabel('Ratio Change, %',fontsize=8,fontweight='bold',labelpad=1)
ax[8].set_xticklabels(x_data,fontsize=8)
ax[2].set_xticklabels([])
ax[5].set_xticklabels([])
ax[2].set_yticklabels([-20,-10,0,10])
ax[5].set_yticklabels([-10,0,10])
ax[8].set_yticklabels([-10,0,10,20])
ax[8].set_ylim(-0.1,0.2)
ax[5].set_ylim(-0.14,0.14)
ax[2].set_ylim(-0.22,0.15)



plt.show()