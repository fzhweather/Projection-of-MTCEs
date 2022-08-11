#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 17:38:18 2022

@author: fuzhenghang
"""

import windFUNCTION as wf
import shear as sr
import shearolr as olr
import ts
import hus600 as hus
import matplotlib.pyplot as plt###引入库包
import numpy as np
import matplotlib as mpl
import matplotlib.colors
import cmaps
import seaborn as sns
sns.set(color_codes=True,font_scale=0.55)
mpl.rcParams["font.family"] = 'Times New Roman'  
mpl.rcParams["mathtext.fontset"] = 'cm' 
mpl.rcParams["font.size"] = 8


fig = plt.figure(figsize=(6,3),dpi=1000)

x1 = [0.05,0.35,0.65,0.05,0.35,0.65]
yy = [0.9,0.9,0.9,0.5,0.5,0.5]
dx = 0.26
dy = 0.33
ax = []

label = ['(e) 850hPa Vertical Vorticity','(f) 500hPa Vertical Velocity','(g) Vertical Shear','(h) 600hPa Specific Humidity','(i) Surface Temperature','(j) OLR']
for i in range(6):
    ax.append(fig.add_axes([x1[i],yy[i],dx,dy]))
for i in range(3):
    ax[i].set_xticklabels([])
tick1=[[-10,-5,0,5],[-3,0,3,6],[-2,-1,0,1],[0,2,4,6],[0.6,0.7,0.8,0.9,1.0],[-3,0,3,6]]
print(tick1[0])
DATA=[wf.vordata,wf.wapdata,sr.sheardata,hus.husdata,ts.tsdata,olr.olrdata]
data=[wf.vo1,wf.vo2,wf.vo3,wf.wa1,wf.wa2,wf.wa3,sr.shea1,sr.shea2,sr.shea3,hus.hu1,hus.hu2,hus.hu3,ts.t1,ts.t2,ts.t3,olr.ol1,olr.ol2,olr.ol3]
print(data[0])
cof=[10000000,1000,1,10000,1,1]

for i in range(6):
    for j in range(3):
        DATA[i][j]=DATA[i][j]*cof[i]
for i in range(18):
    for k in range(len(data[i])):
        data[i][k]=data[i][k]*cof[int(i/3)]
for i in range(6):
    ax[i].text(-0.5,tick1[i][-1]+0.04*(tick1[i][-1]-tick1[i][0]),label[i],fontweight='bold') 
ax[0].text(-0.4,tick1[0][-1]-0.1*(tick1[0][-1]-tick1[0][0]),'×10$^-$$^7$ /s',fontweight='bold') 
ax[1].text(-0.4,tick1[1][-1]-0.1*(tick1[1][-1]-tick1[1][0]),'×10$^-$$^3$ Pa/s',fontweight='bold')
ax[2].text(-0.4,tick1[2][-1]-0.1*(tick1[2][-1]-tick1[2][0]),'m/s',fontweight='bold')
ax[3].text(-0.4,tick1[3][-1]-0.1*(tick1[3][-1]-tick1[3][0]),'×10$^-$$^4$',fontweight='bold') 
ax[4].text(-0.4,tick1[4][-1]-0.1*(tick1[4][-1]-tick1[4][0]),'K',fontweight='bold') 
ax[5].text(-0.4,tick1[5][-1]-0.1*(tick1[5][-1]-tick1[5][0]),'W/m$^2$',fontweight='bold') 
for num in range(5):
# 准备数据
    x_data = ['WNP','ENP','NA']
    y_data = DATA[num]
    print(y_data)
    spread = np.zeros((2,3))
    ymedian=[]
    for i in range(3):
        a=data[i+3*num]
        a.sort()
        spread[0,i]=0.5*(a[2]+a[3])-a[0]
        #print(a)
        spread[1,i]=a[5]-0.5*(a[2]+a[3])
        ymedian.append(0.5*(a[2]+a[3]))
    #同号
    
    bb=ax[num].bar(x_data, y_data,width=0.25)
    ax[num].errorbar(x_data, ymedian,fmt='.',mec='w',mew=0.6,ms=6,mfc='k',yerr = spread,c='k',linewidth=0.8,capsize=2.5)
    ax[num].set_yticks(tick1[num])
    ax[num].set_yticklabels(tick1[num],fontsize=8)
    ax[num].set_xticks(x_data)
    ax[num].tick_params(pad=-3)
    ax[num].axhline(y=0, color='black', linestyle='-',linewidth = 0.5)
    ax[num].set_ylim(tick1[num][0],tick1[num][-1])
    ax[num].set_xlim(-0.5,2.5)
    for bar,height in zip(bb,y_data):
        if height<0:
            bar.set(color='royalblue')
        elif height>0:
            bar.set(color='r')
for num in range(5,6):
# 准备数据
    x_data = ['WNP','ENP','NA']
    y_data = DATA[num]
    print(y_data)
    spread = np.zeros((2,3))
    ymedian=[]
    for i in range(3):
        a=data[i+3*num]
        a.sort()
        spread[0,i]=a[2]-a[0]
        #print(a)
        spread[1,i]=a[4]-a[2]
        ymedian.append(a[2])
    #同号
    
    bb=ax[num].bar(x_data, y_data,width=0.25)
    ax[num].errorbar(x_data, ymedian,fmt='.',mec='w',mew=0.6,ms=6,mfc='k',yerr = spread,c='k',linewidth=0.8,capsize=2.5)
    ax[num].set_yticks(tick1[num])
    ax[num].set_yticklabels(tick1[num],fontsize=8)
    ax[num].set_xticks(x_data)
    ax[num].set_xticklabels(x_data,fontsize=8)
    ax[num].tick_params(pad=-3)
    ax[num].axhline(y=0, color='black', linestyle='-',linewidth = 0.5)
    ax[num].set_ylim(tick1[num][0],tick1[num][-1])
    ax[num].set_xlim(-0.5,2.5)
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
    """
    ax[num].axhline(y=0, color='black', linestyle='-',linewidth = 0.5)
    ax[num].text(0.5,0.44,label[num])
    ax[num].set_ylim(-0.55,0.55)
    ax[num].set_ylabel('Frequency Change')
    """
for i in range(3):
    ax[i].set_xticklabels([])
ax[3].set_xticklabels(x_data,fontsize=8)
ax[4].set_xticklabels(x_data,fontsize=8)
ax[4].set_xlabel('Basin',fontweight='bold',fontsize=8)

plt.show()


