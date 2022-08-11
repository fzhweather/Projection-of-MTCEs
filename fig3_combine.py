#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 12:39:45 2022

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
import matplotlib.ticker as mticker
import cartopy.mpl.ticker as cticker
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cmaps
import seaborn as sns
sns.reset_orig()

mpl.rcParams["font.family"] = 'Times New Roman'  #默认字体类型
mpl.rcParams["mathtext.fontset"] = 'cm' #数学文字字体
mpl.rcParams["font.size"] = 5
mpl.rcParams["axes.linewidth"] = 0.5

proj = ccrs.PlateCarree(central_longitude=180)  #中国为左
leftlon, rightlon, lowerlat, upperlat = (100,358,-10,45)
lon_formatter = cticker.LongitudeFormatter()
lat_formatter = cticker.LatitudeFormatter()
fig = plt.figure(figsize=(5,3),dpi=800)  
x1 = [0.15,0.15,0.15,0.15]
yy = [0.99,0.73,0.47,0.21]
dx = 0.6
dy = 0.24
ax = []
label = ['(a) 850hPa Wind & 500hPa Vertical Velocity MME Change','(b) Vertical Shear & 600hPa Specific Humidity MME Change','(c) Surface Temperature MME Change','(d) OLR MME Change']
for i in range(4):
    ax.append(fig.add_axes([x1[i],yy[i],dx,dy],projection = proj))
for i in range(4):
    ax[i].set_extent([leftlon, rightlon, lowerlat, upperlat], crs=ccrs.PlateCarree())
    ax[i].add_feature(cfeature.COASTLINE.with_scale('50m'),lw=0.2)
    gl=ax[i].gridlines(draw_labels=True, linewidth=0.5, color='k', alpha=0.5, linestyle='--')
    gl.xlocator = mticker.FixedLocator([-90,0,180])
    gl.ylocator = mticker.FixedLocator(np.arange(-15,60,15))
    gl.ypadding=2
    gl.xpadding=2
    if i != 3:
        gl.bottom_labels    = False
    gl.top_labels    = False    
    gl.right_labels  = False
    ax[i].text(-80,48,label[i],fontweight='bold')

levels = np.arange(-0.01, 0.01 + 0.0001, 0.001)
sc=25
wid=0.003
qb='k'
kk=2
cb=ax[0].contourf(wf.lon1,wf.lat1,(wf.cmcc3+wf.cnrm3+wf.ece3+wf.mri203+wf.mri603+wf.had3)/6, levels=levels,cmap=cmaps.GMT_red2green_r,transform=ccrs.PlateCarree(),extend='both',zorder=0)
position1=fig.add_axes([0.77, 1.03, 0.012, 0.16])#位置[左,下,长度,宽度]
cbar=plt.colorbar(cb,cax=position1,orientation='vertical',ticks=np.arange(-0.01,0.01+0.0001,0.01),
                  aspect=20,shrink=0.2,pad=0.06)#方向
w850u=(wf.cmcc1+wf.cnrm1+wf.ece1+wf.mri201+wf.mri601+wf.had1)/6
w850v=(wf.cmcc2+wf.cnrm2+wf.ece2+wf.mri202+wf.mri602+wf.had2)/6
hh=ax[0].quiver(np.roll(wf.lon1,72)[::kk],wf.lat1[::kk],w850u[::kk,::kk],w850v[::kk,::kk],color=qb,scale=sc,width=wid,edgecolor='w',linewidth=0.15)
ax[0].quiverkey(hh, X = 0.9, Y = 1.1, U = 1,angle = 0,label='1m/s',labelsep=0.03,labelpos='E', color = qb,labelcolor = 'k')
cbar.ax.tick_params(length=1.8,width=0.4)
ax[0].text(185,-10,'Pa/s',fontsize=5)

position2=fig.add_axes([0.77, 0.77, 0.012, 0.16])#位置[左,下,长度,宽度]
levels2 = np.arange(-3, 3 + 0.0001, 0.3)
cb=ax[1].contourf(wf.lon1,wf.lat1,(sr.cmcc1+sr.cnrm1+sr.ece1+sr.mri201+sr.mri601+sr.had1)/6, levels=levels2,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)
cbar=plt.colorbar(cb,cax=position2,orientation='vertical',ticks=np.arange(-3,3+0.00001,3),
                  aspect=20,shrink=0.2,pad=0.06)#方向  
cbar.ax.tick_params(length=1.8,width=0.4)
ax[1].text(185,-10,'m/s',fontsize=5)


levels21 = np.arange(-1, 1 + 0.000001, 0.1)
aaa = (hus.cmcc1+hus.cnrm1+hus.ece1+hus.mri201+hus.mri601+hus.had1)/6
print(aaa.shape)
C=ax[1].contour(wf.lon1,wf.lat1,1000*aaa[0,:,:],levels=levels21,cmap=cmaps.NMCVel_r,transform=ccrs.PlateCarree(),extend='both',zorder=1,linewidths=0.55)
ax[1].clabel(C,inline=True,fontsize=5,colors='k')

position3=fig.add_axes([0.77, 0.51, 0.012, 0.16])#位置[左,下,长度,宽度]
levels3 = np.arange(-2, 2 + 0.0001, 0.2)
cb=ax[2].contourf(wf.lon1,wf.lat1,(ts.cmcc1+ts.cnrm1+ts.ece1+ts.mri201+ts.mri601+ts.had1)/6, levels=levels3,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)
cbar=plt.colorbar(cb,cax=position3,orientation='vertical',ticks=np.arange(-2,2+0.00001,2),
                  aspect=20,shrink=0.2,pad=0.06)#方向  
cbar.ax.tick_params(length=1.8,width=0.4)
ax[2].text(187,-10,'K',fontsize=5)

position4=fig.add_axes([0.77, 0.25, 0.012, 0.16])#位置[左,下,长度,宽度]
levels4 = np.arange(-12, 12 + 0.0001, 1.5)
cb=ax[3].contourf(wf.lon1,wf.lat1,(olr.cnrm1+olr.ece1+olr.mri201+olr.mri601+olr.had1)/5, levels=levels4,cmap=cmaps.GMT_haxby,transform=ccrs.PlateCarree(),extend='both',zorder=0)
cbar=plt.colorbar(cb,cax=position4,orientation='vertical',ticks=np.arange(-10,10+0.00001,10),
                  aspect=20,shrink=0.2,pad=0.06)#方向  
cbar.ax.tick_params(length=1.8,width=0.4)
ax[3].text(185,-10,'W/m$^2$',fontsize=5)

for i in range(4):
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
    ax[i].add_patch(poly)
for i in range(4):
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
    ax[i].add_patch(polye)
for i in range(4):
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
    ax[i].add_patch(poly)

plt.show()


