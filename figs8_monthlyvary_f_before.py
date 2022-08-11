#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:30:19 2022

@author: fuzhenghang
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import xlrd
import seaborn as sns
sns.set(color_codes=True)
yt=[[-0.6,-0.4,-0.2,0,0.2],[-0.4,-0.2,0,0.2],[-0.2,0,0.2,0.4,0.6]]
loc=[0.132,0.235,0.48]
mpl.rcParams["font.family"] = 'Times New Roman'  
mpl.rcParams["mathtext.fontset"] = 'cm' 
mpl.rcParams["font.size"] = 10
data=[]
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/逐月变化before.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data.append(table.row_values(i))
data = [data[i] for i in range(0,len(data))]

print(data[0][1:9])
fig = plt.figure(figsize=(5,6),dpi=600)

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
    bb=ax[num].bar(x_data, y_data,width=0.4)
    ax[num].errorbar(x_data, ymedian,fmt='.',mec='w',mew=0.8,ms=8,mfc='k',yerr = spread,c='k',linewidth=1,capsize=3)
    ax[num].set_yticks(yt[num])
    ax[num].tick_params(pad=-3)
    ax[num].set_xticks(x_data)
    
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
    ax[num].axhline(y=0, color='black', linestyle='-',linewidth = 0.5)
    ax[0].text(0.5,0.22-num*0.96,label[num])
   
    ax[num].set_ylabel('Frequency Change')
    for i in range(12):
        if fuhao[num][i]>4:
            if y_data[i]>0:
                ax[num].text(i+1,loc[num],fuhao[num][i],color='r',horizontalalignment='center')
            elif y_data[i]<0:
                ax[num].text(i+1,loc[num],fuhao[num][i],color='b',horizontalalignment='center')
ax[2].set_xlabel('Month')
print(fuhao)
ax[2].set_xticklabels(x_data)
ax[0].set_xticklabels([])
ax[1].set_xticklabels([])
ax[2].set_ylim(-0.2,0.55)
ax[1].set_ylim(-0.45,0.3)
plt.show()