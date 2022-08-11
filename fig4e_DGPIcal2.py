#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 09:29:19 2022

@author: fuzhenghang
"""

import u500data as u
import sheardata as s
import wapdata as w
import vordata as vo

import matplotlib.pyplot as plt###引入库包
import numpy as np
import matplotlib as mpl
import matplotlib.colors


import cartopy.mpl.ticker as cticker
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
import cartopy.feature as cfeature
import cmaps
import seaborn as sns
plt.rcParams['hatch.color'] = 'magenta' 
sns.reset_orig()



mpl.rcParams["font.family"] = 'Times New Roman'  
mpl.rcParams["mathtext.fontset"] = 'cm' 
mpl.rcParams["font.size"] = 6

#计算未来的逐月GPI
uy1f=np.zeros((133,73,144))
uy2f=np.zeros((133,73,144))
uy3f=np.zeros((133,73,144))
uy4f=np.zeros((133,73,144))
uy5f=np.zeros((133,73,144))
uy6f=np.zeros((133,73,144))
av1f=np.zeros((133,73,144))
av2f=np.zeros((133,73,144))
av3f=np.zeros((133,73,144))
av4f=np.zeros((133,73,144))
av5f=np.zeros((133,73,144))
av6f=np.zeros((133,73,144))
for t in range(133):
    for i in range(1,72):
        for j in range(144):
            uy1f[t,i,j]=(u.u500f1[t][i,j]-u.u500f1[t][i-1,j])/(2.5*110940)
            uy2f[t,i,j]=(u.u500f2[t][i,j]-u.u500f2[t][i-1,j])/(2.5*110940)
            uy3f[t,i,j]=(u.u500f3[t][i,j]-u.u500f3[t][i-1,j])/(2.5*110940)
            uy4f[t,i,j]=(u.u500f4[t][i,j]-u.u500f4[t][i-1,j])/(2.5*110940)
            uy5f[t,i,j]=(u.u500f5[t][i,j]-u.u500f5[t][i-1,j])/(2.5*110940)
            uy6f[t,i,j]=(u.u500f6[t][i,j]-u.u500f6[t][i-1,j])/(2.5*110940)
            av1f[t,i,j]=(vo.cmcc4[t][i,j]-vo.cmcc4[t][i,j-1])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(vo.cmcc2[t][i,j]-vo.cmcc2[t][i-1,j])/(2.5*110940)+2*7.292*0.00001*np.cos((i-36)*2.5/180*np.pi)
            av2f[t,i,j]=(vo.cnrm4[t][i,j]-vo.cnrm4[t][i,j-1])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(vo.cnrm2[t][i,j]-vo.cnrm2[t][i-1,j])/(2.5*110940)+2*7.292*0.00001*np.cos((i-36)*2.5/180*np.pi)
            av3f[t,i,j]=(vo.mri204[t][i,j]-vo.mri204[t][i,j-1])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(vo.mri202[t][i,j]-vo.mri202[t][i-1,j])/(2.5*110940)+2*7.292*0.00001*np.cos((i-36)*2.5/180*np.pi)
            av4f[t,i,j]=(vo.mri604[t][i,j]-vo.mri604[t][i,j-1])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(vo.mri602[t][i,j]-vo.mri602[t][i-1,j])/(2.5*110940)+2*7.292*0.00001*np.cos((i-36)*2.5/180*np.pi)
            av5f[t,i,j]=(vo.had4[t][i,j]-vo.had4[t][i,j-1])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(vo.had2[t][i,j]-vo.had2[t][i-1,j])/(2.5*110940)+2*7.292*0.00001*np.cos((i-36)*2.5/180*np.pi)
            av6f[t,i,j]=(vo.ece4[t][i,j]-vo.ece4[t][i,j-1])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(vo.ece2[t][i,j]-vo.ece2[t][i-1,j])/(2.5*110940)+2*7.292*0.00001*np.cos((i-36)*2.5/180*np.pi)


DGPIf1=np.zeros((133,73,144))
DGPIf2=np.zeros((133,73,144))
DGPIf3=np.zeros((133,73,144))
DGPIf4=np.zeros((133,73,144))
DGPIf5=np.zeros((133,73,144))
DGPIf6=np.zeros((133,73,144))
for t in range(133):
    for i in range(1,72):
        for j in range(144):
            DGPIf1[t,i,j]=((2+0.1*s.cmcc2[t][i,j])**(-1.7))*((5.5-uy1f[t,i,j]*100000)**(2.3))*((5.0-20*w.u500f1[t][i,j])**(3.4))*((5.5+abs(av1f[t,i,j]*100000))**(2.4))*np.exp(-11.8)-1
            DGPIf2[t,i,j]=((2+0.1*s.cnrm2[t][i,j])**(-1.7))*((5.5-uy2f[t,i,j]*100000)**(2.3))*((5.0-20*w.u500f2[t][i,j])**(3.4))*((5.5+abs(av2f[t,i,j]*100000))**(2.4))*np.exp(-11.8)-1
            DGPIf3[t,i,j]=((2+0.1*s.mri202[t][i,j])**(-1.7))*((5.5-uy2f[t,i,j]*100000)**(2.3))*((5.0-20*w.u500f3[t][i,j])**(3.4))*((5.5+abs(av3f[t,i,j]*100000))**(2.4))*np.exp(-11.8)-1
            DGPIf4[t,i,j]=((2+0.1*s.mri602[t][i,j])**(-1.7))*((5.5-uy2f[t,i,j]*100000)**(2.3))*((5.0-20*w.u500f4[t][i,j])**(3.4))*((5.5+abs(av4f[t,i,j]*100000))**(2.4))*np.exp(-11.8)-1
            DGPIf5[t,i,j]=((2+0.1*s.had2[t][i,j])**(-1.7))*((5.5-uy2f[t,i,j]*100000)**(2.3))*((5.0-20*w.u500f5[t][i,j])**(3.4))*((5.5+abs(av5f[t,i,j]*100000))**(2.4))*np.exp(-11.8)-1
            DGPIf6[t,i,j]=((2+0.1*s.ece2[t][i,j])**(-1.7))*((5.5-uy2f[t,i,j]*100000)**(2.3))*((5.0-20*w.u500f6[t][i,j])**(3.4))*((5.5+abs(av6f[t,i,j]*100000))**(2.4))*np.exp(-11.8)-1
    
    
    


#计算过去的逐月GPI
uy1h=np.zeros((145,73,144))
uy2h=np.zeros((145,73,144))
uy3h=np.zeros((145,73,144))
uy4h=np.zeros((145,73,144))
uy5h=np.zeros((145,73,144))
uy6h=np.zeros((145,73,144))
av1h=np.zeros((145,73,144))
av2h=np.zeros((145,73,144))
av3h=np.zeros((145,73,144))
av4h=np.zeros((145,73,144))
av5h=np.zeros((145,73,144))
av6h=np.zeros((145,73,144))
for t in range(145):
    for i in range(1,72):
        for j in range(144):
            uy1h[t,i,j]=(u.u500h1[t][i,j]-u.u500h1[t][i-1,j])/(2.5*110940)
            uy2h[t,i,j]=(u.u500h2[t][i,j]-u.u500h2[t][i-1,j])/(2.5*110940)
            uy3h[t,i,j]=(u.u500h3[t][i,j]-u.u500h3[t][i-1,j])/(2.5*110940)
            uy4h[t,i,j]=(u.u500h4[t][i,j]-u.u500h4[t][i-1,j])/(2.5*110940)
            uy5h[t,i,j]=(u.u500h5[t][i,j]-u.u500h5[t][i-1,j])/(2.5*110940)
            uy6h[t,i,j]=(u.u500h6[t][i,j]-u.u500h6[t][i-1,j])/(2.5*110940)
            av1h[t,i,j]=(vo.cmcc3[t][i,j]-vo.cmcc3[t][i,j-1])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(vo.cmcc1[t][i,j]-vo.cmcc1[t][i-1,j])/(2.5*110940)+2*7.292*0.00001*np.cos((i-36)*2.5/180*np.pi)
            av2h[t,i,j]=(vo.cnrm3[t][i,j]-vo.cnrm3[t][i,j-1])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(vo.cnrm1[t][i,j]-vo.cnrm1[t][i-1,j])/(2.5*110940)+2*7.292*0.00001*np.cos((i-36)*2.5/180*np.pi)
            av3h[t,i,j]=(vo.mri203[t][i,j]-vo.mri203[t][i,j-1])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(vo.mri201[t][i,j]-vo.mri201[t][i-1,j])/(2.5*110940)+2*7.292*0.00001*np.cos((i-36)*2.5/180*np.pi)
            av4h[t,i,j]=(vo.mri603[t][i,j]-vo.mri603[t][i,j-1])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(vo.mri601[t][i,j]-vo.mri601[t][i-1,j])/(2.5*110940)+2*7.292*0.00001*np.cos((i-36)*2.5/180*np.pi)
            av5h[t,i,j]=(vo.had3[t][i,j]-vo.had3[t][i,j-1])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(vo.had1[t][i,j]-vo.had1[t][i-1,j])/(2.5*110940)+2*7.292*0.00001*np.cos((i-36)*2.5/180*np.pi)
            av6h[t,i,j]=(vo.ece3[t][i,j]-vo.ece3[t][i,j-1])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(vo.ece1[t][i,j]-vo.ece1[t][i-1,j])/(2.5*110940)+2*7.292*0.00001*np.cos((i-36)*2.5/180*np.pi)

DGPIh1=np.zeros((145,73,144))
DGPIh2=np.zeros((145,73,144))
DGPIh3=np.zeros((145,73,144))
DGPIh4=np.zeros((145,73,144))
DGPIh5=np.zeros((145,73,144))
DGPIh6=np.zeros((145,73,144))
for t in range(145):
    for i in range(1,72):
        for j in range(144):
            DGPIh1[t,i,j]=((2+0.1*s.cmcc1[t][i,j])**(-1.7))*((5.5-uy1h[t,i,j]*100000)**(2.3))*((5.0-20*w.u500h1[t][i,j])**(3.4))*((5.5+abs(av1h[t,i,j]*100000))**(2.4))*np.exp(-11.8)-1
            DGPIh2[t,i,j]=((2+0.1*s.cnrm1[t][i,j])**(-1.7))*((5.5-uy2h[t,i,j]*100000)**(2.3))*((5.0-20*w.u500h2[t][i,j])**(3.4))*((5.5+abs(av2h[t,i,j]*100000))**(2.4))*np.exp(-11.8)-1
            DGPIh3[t,i,j]=((2+0.1*s.mri201[t][i,j])**(-1.7))*((5.5-uy2h[t,i,j]*100000)**(2.3))*((5.0-20*w.u500h3[t][i,j])**(3.4))*((5.5+abs(av3h[t,i,j]*100000))**(2.4))*np.exp(-11.8)-1
            DGPIh4[t,i,j]=((2+0.1*s.mri601[t][i,j])**(-1.7))*((5.5-uy2h[t,i,j]*100000)**(2.3))*((5.0-20*w.u500h4[t][i,j])**(3.4))*((5.5+abs(av4h[t,i,j]*100000))**(2.4))*np.exp(-11.8)-1
            DGPIh5[t,i,j]=((2+0.1*s.had1[t][i,j])**(-1.7))*((5.5-uy2h[t,i,j]*100000)**(2.3))*((5.0-20*w.u500h5[t][i,j])**(3.4))*((5.5+abs(av5h[t,i,j]*100000))**(2.4))*np.exp(-11.8)-1
            DGPIh6[t,i,j]=((2+0.1*s.ece1[t][i,j])**(-1.7))*((5.5-uy2h[t,i,j]*100000)**(2.3))*((5.0-20*w.u500h6[t][i,j])**(3.4))*((5.5+abs(av6h[t,i,j]*100000))**(2.4))*np.exp(-11.8)-1



proj = ccrs.PlateCarree(central_longitude=180)  #中国为左
leftlon, rightlon, lowerlat, upperlat = (100,358,0,45)
lon_formatter = cticker.LongitudeFormatter()
lat_formatter = cticker.LatitudeFormatter()
fig = plt.figure(figsize=(8,4),dpi=800)  

ax=[]
xx=[0.05,0.215,0.41,0.605]
yy=[0.9,0.64,0.64,0.64]
dx=[0.9,0.18,0.18,0.18]
dy=0.2
ax.append(fig.add_axes([xx[0],yy[0],dx[0],dy],projection = proj))
for i in range(1,4):
    ax.append(fig.add_axes([xx[i],yy[i],dx[i],dy]))

ax[0].set_extent([leftlon, rightlon, lowerlat, upperlat], crs=ccrs.PlateCarree())
ax[0].add_feature(cfeature.COASTLINE.with_scale('50m'),lw=0.2,zorder=10)
gl=ax[0].gridlines(draw_labels=True, linewidth=0.5, color='k', alpha=0.5, linestyle='--',zorder=10)
gl.xlocator = mticker.FixedLocator([-90,0,180])
gl.ylocator = mticker.FixedLocator([0,15,30,45])
ax[0].add_feature(cfeature.LAND.with_scale('50m'),color='lightgray',zorder=10)
gl.ypadding=20
gl.xpadding=20
gl.top_labels    = False    
gl.right_labels  = False
ax[0].text(-80,47,'(a) MME DGPI Change: Future minus Present')
  
levels = np.arange(-8, 8 + 0.0001,1)
DGPIhmean=(DGPIh1.mean(0)+DGPIh2.mean(0)+DGPIh3.mean(0)+DGPIh4.mean(0)+DGPIh5.mean(0)+DGPIh6.mean(0))/6
DGPIfmean=(DGPIf1.mean(0)+DGPIf2.mean(0)+DGPIf3.mean(0)+DGPIf4.mean(0)+DGPIf5.mean(0)+DGPIf6.mean(0))/6

from scipy.stats.mstats import ttest_ind
DGPIph=(DGPIh1+DGPIh2+DGPIh3+DGPIh4+DGPIh5+DGPIh6)/6
DGPIpf=(DGPIf1+DGPIf2+DGPIf3+DGPIf4+DGPIf5+DGPIf6)/6
_,p1 = ttest_ind(DGPIph,DGPIpf,equal_var=False)

cb=ax[0].contourf(w.lon1,w.lat1,DGPIfmean-DGPIhmean, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)
c1b = ax[0].contourf(w.lon1,w.lat1,p1,[0,0.1,1], zorder=1,hatches=['...', None],colors='none', transform=ccrs.PlateCarree())

position1=fig.add_axes([0.8, 0.9, 0.01, 0.2])
plt.colorbar(cb,position1,orientation='vertical',ticks=np.arange(-8,8+0.00001,4),aspect=20,shrink=0.2,pad=0.06)#方向  

lon = np.empty(4)
lat = np.empty(4)
lon[0],lat[0] = 110, 5  # lower left (ll)
lon[1],lat[1] = 160, 5  # lower right (lr)
lon[2],lat[2] = 160, 21  # upper right (ur)
lon[3],lat[3] = 110, 21  # upper left (ul)
x, y =  lon, lat
xy = list(zip(x,y))
print(xy)
poly = plt.Polygon(xy,edgecolor="k",linestyle='-',fc="none", lw=0.5, alpha=1,transform=ccrs.PlateCarree(),zorder=7)
ax[0].add_patch(poly)
lone = np.empty(4)
late = np.empty(4)
lone[0],late[0] = 230, 8  # lower left (ll)
lone[1],late[1] = 270, 8  # lower right (lr)
lone[2],late[2] = 270, 20  # upper right (ur)
lone[3],late[3] = 230, 20  # upper left (ul)
xe, ye =  lone, late
xye = list(zip(xe,ye))
print(xye)
polye = plt.Polygon(xye,edgecolor="k",linestyle='-',fc="none", lw=0.5, alpha=1,transform=ccrs.PlateCarree(),zorder=7)
ax[0].add_patch(polye)
lon = np.empty(4)
lat = np.empty(4)
lon[0],lat[0] = 280, 10  # lower left (ll)
lon[1],lat[1] = 340, 10  # lower right (lr)
lon[2],lat[2] = 340, 20  # upper right (ur)
lon[3],lat[3] = 280, 20  # upper left (ul)
x, y =  lon, lat
xy = list(zip(x,y))
print(xy)
poly = plt.Polygon(xy,edgecolor="k",linestyle='-',fc="none", lw=0.5, alpha=1,transform=ccrs.PlateCarree(),zorder=7)
ax[0].add_patch(poly)

ax[0].text(-79,-12,'(b) WNP')
ax[0].text(8,-12,'(c) ENP')
ax[0].text(96,-12,'(d) NA')

ax[1].patch.set_facecolor('lightblue')
ax[1].patch.set_alpha(0.3)

ax[2].patch.set_facecolor('lightgreen')
ax[2].patch.set_alpha(0.3)

ax[3].patch.set_facecolor('pink')
ax[3].patch.set_alpha(0.3)

tick1=[[-6,-4,-2,0,2],[-2,0,2,4],[-1,0,1,2]]

dgpit1=[-2.646065664209369, -5.118583619501794, -3.0991458265547687, -3.2392970753444104, -5.944639691029417, -2.799239582536617]
dgpit2=[1.9273790475273695, 0.0445670003205277, 1.7206679943442884, 0.7602961985358817, 3.365387141989563, -0.8845828810632528] 
dgpit3=[0.08488087762924745, 0.8640083070859456, 0.3839903152041219, 0.7404414178872848, -0.29001289320923906, 0.337673306984765] 
dgpit=[-3.807828576529396, 1.1556190836090627, 0.35349688859702094]

is1=[-0.1680255338193896, 1.2248602695560868, 0.8640149736713937, 0.5823787624215654, 0.1847009083897993, 0.5612651541135826] 
is2=[-1.095230412179003, 0.1422245424819276, -1.2939127954520564, -0.6936132253017688, -0.7726686810150601, -0.21184539340983624] 
is3=[0.7052354090967375, 1.0110376313962295, 0.7943492616055496, 1.1314828123040714, 0.8259312021894875, 0.9152942184306981] 
ist=[0.5415324223888397, -0.6541743274792995, 0.8972217558371288]

iw1=[-2.1264505060545633, -4.605330952027953, -2.3332458996447363, -3.052960745312127, -5.75669241459756, -2.320985930236172] 
iw2=[2.4107827140266824, 0.2523489608909263, 3.2848444705684283, 1.4136667133267349, 4.128425021116534, -0.25835646661461914] 
iw3=[-0.32493707192999843, 0.08917092321739928, -0.3019181464795483, 0.06133113484436853, -0.7953063431011801, -0.2058976878523139] 
iwt=[-3.365944407978852, 1.8719519022191144, -0.24625953188354552]

ia1=[-0.35240944035395333, -0.39959131303444484, -0.16526609228713662, -0.378839274347784, -0.48093419097607926, -0.19849325178730778] 
ia2=[0.07485238495063642, 0.14583140899218322, 0.27994080984676323, 0.27081113618100877, 0.30828056257108566, 0.17642783538497664] 
ia3=[0.06048793346687522, 0.043792139268910235, 0.004086441898595546, 0.01908960890230031, -0.01062557598935924, 0.02418243868635613] 
iat=[-0.3292555937977843, 0.20935735632110897, 0.0235021643722797]

iu1=[-0.1680255338193896, 1.2248602695560868, 0.8640149736713937, 0.5823787624215654, 0.1847009083897993, 0.5612651541135826] 
iu2=[-1.095230412179003, 0.1422245424819276, -1.2939127954520564, -0.6936132253017688, -0.7726686810150601, -0.21184539340983624] 
iu3=[0.7052354090967375, 1.0110376313962295, 0.7943492616055496, 1.1314828123040714, 0.8259312021894875, 0.9152942184306981] 
iut=[0.5415324223888397, -0.6541743274792995, 0.8972217558371288]

DATA=[[dgpit[0],ist[0],iwt[0],iat[0],iut[0]],[dgpit[1],ist[1],iwt[1],iat[1],iut[1]],[dgpit[2],ist[2],iwt[2],iat[2],iut[2]]]
data=[dgpit1,is1,iw1,ia1,iu1,dgpit2,is2,iw2,ia2,iu2,dgpit3,is3,iw3,ia3,iu3]
print(DATA[1])
for num in range(1,4):
# 准备数据
    x_data = ['Total','VWS','Omega','Vor','$\partial u $/$\partial y $']
    y_data = DATA[num-1]
    print(y_data)
    spread = np.zeros((2,5))
    ymedian=[]
    for i in range(5):
        a=data[i+5*(num-1)]
        print(a)
        a.sort()
        spread[0,i]=0.5*(a[2]+a[3])-a[0]
        #print(a)
        spread[1,i]=a[5]-0.5*(a[2]+a[3])
        ymedian.append(0.5*(a[2]+a[3]))
    #同号
    
    bb=ax[num].bar(x_data, y_data,width=0.3)
    ax[num].errorbar(x_data, ymedian,fmt='.',mec='w',mew=0.6,ms=6,mfc='k',yerr = spread,c='k',linewidth=0.8,capsize=2.5)
    ax[num].set_yticks(tick1[num-1])
    ax[num].set_xticks(x_data)
    ax[num].tick_params(pad=1)
    ax[num].axhline(y=0, color='black', linestyle='-',linewidth = 0.5)
    #ax[num].set_ylim(tick1[num-1][0],tick1[num-1][-1])
    ax[num].set_xlim(-0.5,4.5)
    ax[num].tick_params(length=1.8,width=0.4)
    for bar,height in zip(bb,y_data):
        if height<0:
            bar.set(color='royalblue')
        elif height>0:
            bar.set(color='r')



plt.show()




