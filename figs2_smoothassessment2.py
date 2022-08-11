#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 19:02:06 2022

@author: fuzhenghang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:54:25 2022

@author: fuzhenghang
"""

import matplotlib.pyplot as plt###引入库包
import numpy as np
import matplotlib as mpl
import netCDF4 as nc
import matplotlib.colors
import xlrd
import seaborn as sns
sns.reset_orig()

mpl.rcParams["font.family"] = 'Times New Roman'  
mpl.rcParams["mathtext.fontset"] = 'cm' #数学文字字体
mpl.rcParams["font.size"] = 8
mpl.rcParams["axes.linewidth"] = 1
plt.rcParams['ytick.direction'] = 'in'#将y轴的刻度方向设置向内

data=[]
start=8
table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/afterMTCEs.xlsx')
#table=xlrd.open_workbook('/Users/fuzhenghang/Documents/大三下/望道/数据结果/beforeMTCEs.xlsx')
table=table.sheets()[0]
nrows=table.nrows
for i in range(nrows):
    if i ==0:
        continue
    data.append(table.row_values(i))
data = [data[i] for i in range(0,len(data))]
nan=data[0][-1]
for i in range(0,len(data),2):
    for j in range(len(data[i])):
        if data[i][-1]==nan:
            del(data[i][-1])
            del(data[i+1][-1])

fig = plt.figure(figsize=(6,8),dpi=600)
ax=[]
ax2=[]
label1=['(a) CMCC','(b) CNRM','(c) EC-Earth','(d) ECMWF','(e) MRI - S','(f) MRI - H','(g) NICAM - 8S','(h) NICAM - 7S','(i) HadGEM']
xbefore=[start+i for i in range(len(data[6]))]

x1 = [0.05,0.35,0.65,0.05,0.35,0.65,0.05,0.35,0.65]
yy = [0.95,0.95,0.95,0.7,0.7,0.7,0.45,0.45,0.45]
dx = 0.27
dy = 0.22
w=1
m=3
c=1.5
c1=2
for i in range(9):
    ax.append(fig.add_axes([x1[i],yy[i],dx,dy]))
    ax2.append(ax[i].twinx())
for i in range(6):
    ax[i].axvline(x=13,  linestyle='-',linewidth = 5,color='k',alpha=0.2)
for i in range(6,9):
    ax[i].axvline(x=17,  linestyle='-',linewidth = 5,color='k',alpha=0.2)
for i in range(9):
    ax[i].plot(xbefore[0:len(data[i*6])],data[i*6],'o-',color='royalblue',linewidth=c,markersize=m,label='WNP')
    ax[i].plot(xbefore[0:len(data[i*6+2])],data[i*6+2],'o-',color='limegreen',linewidth=c,markersize=m,label='ENP')
    ax[i].plot(xbefore[0:len(data[i*6+4])],data[i*6+4],'o-',color='tomato',linewidth=c,markersize=m,label='NA')
    ax[i].axis([8,24,-0.25,0.65])
    ax[i].plot(xbefore,[0.2785 for i in range(len(xbefore))],'--',color='gray',linewidth=c*0.6)
    ax[i].plot(xbefore,[0.329 for i in range(len(xbefore))],'-',color='gray',linewidth=c*0.6)
    ax2[i].plot(xbefore[0:len(data[i*6+1])],data[i*6+1],':',color='royalblue',linewidth=c1,label='WNP')
    ax2[i].plot(xbefore[0:len(data[i*6+3])],data[i*6+3],':',color='limegreen',linewidth=c1,label='ENP')
    ax2[i].plot(xbefore[0:len(data[i*6+5])],data[i*6+5],':',color='tomato',linewidth=c1,label='NA')
    ax2[i].axis([8,24,1,8])
    ax2[i].set_yticks([2,4,6,8])
    ax[i].text(8,0.68,label1[i])
    if i in [0,1,2,3,4,5]:
        ax[i].set_xticklabels([])
    if i in [1,2,4,5,7,8]:
        ax[i].set_yticklabels([])
    if i in [0,1,3,4,6,7]:
        ax2[i].set_yticklabels([])
    if i in [0,3,6]:
        ax[i].set_ylabel('Correlation',labelpad=3)
    if i in [6,7,8]:
        ax[i].set_xlabel('Velocity, m/s',labelpad=3)
    if i in [2,5,8]:
        ax2[i].set_ylabel('RMSE',labelpad=3)
ax[0].legend(frameon=False,bbox_to_anchor=(1,1,0.35,0.2),ncol=3)
ax2[0].legend(frameon=False,bbox_to_anchor=(1,1,2.25,0.2),ncol=3)
ax[1].text(-1.5,0.8,'Correlation')
ax[1].text(28,0.8,'RMSE')
plt.show()


