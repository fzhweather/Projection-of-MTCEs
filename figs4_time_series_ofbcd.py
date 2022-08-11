#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 21:54:01 2022

@author: fuzhenghang
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import xlrd
from scipy.stats import pearsonr
from scipy import optimize
mpl.rcParams["font.family"] = 'Times New Roman'  
mpl.rcParams["mathtext.fontset"] = 'cm' 
mpl.rcParams["font.size"] = 7
mpl.rcParams["axes.linewidth"] = 0.5

def f_1(x, A, B):
 return A * x + B

data=[[8,8,5,10,4,8,6,6,9,6,6,12,8,11,5,12,6,10,10,4,5,11,6,6,5,10,6,4,3,8,7,1,8,7,6,4,7,7,7,9,6,8],[1, 2, 2, 7, 7, 5, 10, 2, 7, 3, 4, 6, 6, 7, 5, 6, 0, 1, 3, 2, 2, 2, 3, 5, 2, 1, 3, 7, 1, 7, 5, 2, 2, 2, 3, 7, 6, 8, 2, 5, 3, 3],[2, 1, 1, 0, 0, 4, 3, 0, 2, 1, 5, 5, 1, 2, 2, 0, 4, 2, 0, 3, 4, 6, 3, 4, 4, 5, 6, 3, 3, 2, 1, 4, 7, 8, 3, 1, 0, 4, 4, 4, 5, 8]
     ,[23, 30, 19, 50, 13, 40, 29, 26, 37, 17, 32, 47, 46, 64, 28, 72, 32, 61, 48, 15, 12, 30, 30, 33, 21, 44, 25, 9, 13, 11, 24, 6, 27, 36, 23, 14, 38, 22, 25, 37, 29, 18],[3, 5, 4, 21, 23, 21, 31, 9, 18, 19, 10, 38, 29, 44, 26, 16, 0, 1, 10, 6, 11, 7, 11, 18, 8, 5, 17, 26, 1, 21, 13, 8, 10, 10, 4, 24, 34, 37, 19, 37, 15, 7],[14, 6, 11, 0, 0, 11, 7, 0, 6, 4, 16, 12, 4, 8, 5, 0, 25, 10, 0, 24, 23, 21, 11, 18, 15, 29, 20, 11, 5, 16, 3, 25, 22, 24, 7, 2, 0, 18, 28, 21, 17, 35],
      [0.652173913,0.625,0.428571429,0.84,0.391304348,0.666666667,0.538461538,0.464285714,0.708333333,0.52,0.516129032,0.774193548,0.620689655
      ,0.774193548,0.344827586,0.852941176,0.653846154,0.806451613,0.733333333,0.529411765,0.409090909,0.76
      ,0.518518519,0.565217391,0.454545455,0.689655172,0.5,0.428571429,0.318181818,0.545454545,0.545454545,0.214285714
      ,0.722222222,0.56,0.444444444,0.35,0.576923077,0.56,0.615384615,0.75862069,0.535714286,0.652173913],
      [0.2, 0.26666666666666666, 0.3333333333333333, 0.6521739130434783, 0.47619047619047616, 0.5238095238095238, 0.7083333333333334, 0.29411764705882354, 0.7, 0.625, 0.3888888888888889, 0.6363636363636364, 0.7142857142857143, 0.6296296296296297, 0.6470588235294118, 0.55, 0.0, 0.18181818181818182, 0.3684210526315789, 0.3076923076923077, 0.3333333333333333, 0.2631578947368421, 0.4375, 0.6666666666666666, 0.29411764705882354, 0.16666666666666666, 0.5333333333333333, 0.7894736842105263, 0.18181818181818182, 0.6470588235294118, 0.5, 0.3333333333333333, 0.36363636363636365, 0.29411764705882354, 0.2, 0.5454545454545454, 0.6923076923076923, 0.6818181818181818, 0.3888888888888889, 0.6956521739130435, 0.42105263157894735, 0.35294117647058826],
      [0.5, 0.36363636363636365, 0.36363636363636365, 0.0, 0.0, 0.75, 0.45454545454545453, 0.0, 0.5714285714285714, 0.25, 0.6363636363636364, 0.6428571428571429, 0.375, 0.6666666666666666, 0.5, 0.0, 0.631578947368421, 0.3076923076923077, 0.0, 0.6428571428571429, 0.75, 0.7857142857142857, 0.4666666666666667, 0.6666666666666666, 0.4375, 0.7857142857142857, 0.48148148148148145, 0.5, 0.42857142857142855, 0.4375, 0.3333333333333333, 0.5789473684210527, 0.631578947368421, 0.7894736842105263, 0.35714285714285715, 0.25, 0.0, 0.5333333333333333, 0.5, 0.6666666666666666, 0.6875, 0.7586206896551724]]

fig = plt.figure(figsize=(4,4),dpi=600)

x1 = [0.1,0.1,0.1]
yy = [0.95,0.65,0.35]
dx = 0.8
dy = 0.25
ax = []
fuhao = [[] for i in range(3)]
label = ['(b) Frequency','(c) Duration','(d) MTCs/TTCs']
for i in range(3):
    ax.append(fig.add_axes([x1[i],yy[i],dx,dy]))
lon=[13,75,1]
for num in range(3):
# 准备数据
    x_data = [i for i in range(1979,2021)]
    y1=data[3*num]
    y2=data[3*num+1]
    y3=data[3*num+2]

    const1,p1 = pearsonr(y1, [1+i for i in range(42)])
    const2,p2 = pearsonr(y2, [1+i for i in range(42)])
    const3,p3 = pearsonr(y3, [1+i for i in range(42)])
    pv=[p1,p2,p3]
    A1, B1 = optimize.curve_fit(f_1, x_data, y1)[0]
    xn1 = np.arange(1979, 2021, 1)#30和75要对应x0的两个端点，0.01为步长
    yn1 = A1 * xn1 + B1
    ax[num].plot(xn1, yn1, '--',color='royalblue',linewidth=1,zorder=3)
    A2, B2 = optimize.curve_fit(f_1, x_data, y2)[0]
    xn2 = np.arange(1979, 2021, 1)#30和75要对应x0的两个端点，0.01为步长
    yn2 = A2 * xn2 + B2
    ax[num].plot(xn2, yn2, '--',color='limegreen',linewidth=1,zorder=3)
    A3, B3 = optimize.curve_fit(f_1, x_data, y3)[0]
    xn3 = np.arange(1979, 2021, 1)#30和75要对应x0的两个端点，0.01为步长
    yn3 = A3 * xn3 + B3
    ax[num].plot(xn3, yn3, '--',color='tomato',linewidth=1,zorder=3)
    AA=[A1,A2,A3]
    
    ax[num].plot(x_data,y1,'-',linewidth = 1,color='royalblue',label='WNP',zorder=1)
    ax[num].plot(x_data,y2,'-',linewidth = 1,color='limegreen',label='ENP',zorder=1)
    ax[num].plot(x_data,y3,'-',linewidth = 1,color='tomato',label='NA',zorder=1)
    ax[num].set_xticks([1980,1990,2000,2010,2020])
    ax[num].set_xlim(1979,2020)
    ax[num].text(1979.5,lon[num]*1.03,label[num])
    
    ax[num].text(1980,lon[num]*0.92,'trend1 = ',color='royalblue',fontsize=6,fontweight='bold')
    ax[num].text(1994,lon[num]*0.92,'trend2 = ',color='g',fontsize=6,fontweight='bold')
    ax[num].text(2007,lon[num]*0.92,'trend3 = ',color='tomato',fontsize=6,fontweight='bold')
    
    ax[num].text(1981.9,lon[num]*0.84,'p1 = ',color='royalblue',fontsize=6,fontweight='bold')
    ax[num].text(1995.9,lon[num]*0.84,'p2 = ',color='g',fontsize=6,fontweight='bold')
    ax[num].text(2008.9,lon[num]*0.84,'p3 = ',color='tomato',fontsize=6,fontweight='bold')

    ax[num].text(1984.5,lon[num]*0.92,float(format(float(AA[0])*10,'.3g')),color='royalblue',fontsize=6,zorder=4,fontweight='bold')
    ax[num].text(1998.5,lon[num]*0.92,float(format(float(AA[1])*10,'.3g')),color='g',fontsize=6,zorder=4,fontweight='bold')
    ax[num].text(2011.5,lon[num]*0.92,float(format(float(AA[2])*10,'.3g')),color='tomato',fontsize=6,zorder=4,fontweight='bold')
    
    ax[num].text(1984.5,lon[num]*0.84,float(format(pv[0],'.3g')),color='royalblue',fontsize=6,zorder=4,fontweight='bold')
    ax[num].text(1998.5,lon[num]*0.84,float(format(pv[1],'.3g')),color='g',fontsize=6,zorder=4,fontweight='bold')
    ax[num].text(2011.5,lon[num]*0.84,float(format(pv[2],'.3g')),color='tomato',fontsize=6,zorder=4,fontweight='bold')
  
    ax[num].grid(ls="-",c='gray',alpha=0.5,linewidth=0.2)
    
ax[0].set_ylim(0,13)
ax[1].set_ylim(0,75)
ax[2].set_ylim(0,1)
ax[0].set_yticks([0,3,6,9,12])
ax[1].set_yticks([0,15,30,45,60,75])
ax[2].set_yticks([0,0.2,0.4,0.6,0.8,1])
ax[0].set_xticklabels([])
ax[1].set_xticklabels([])



ax[0].legend(frameon=False,bbox_to_anchor=(1,1,0,0.18),ncol=3,fontsize=7)
ax[2].set_xlabel('Year')





