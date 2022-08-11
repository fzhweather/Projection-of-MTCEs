#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 09:15:08 2022

@author: fuzhenghang
"""


import matplotlib.pyplot as plt###引入库包
import numpy as np
import matplotlib as mpl
import matplotlib.colors
import xarray as xr
import matplotlib.ticker as mticker
import cartopy.mpl.ticker as cticker
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cmaps
from cartopy.io.shapereader import Reader
from scipy.stats.mstats import ttest_ind
import seaborn as sns
sns.reset_orig()
kk=2
mpl.rcParams["font.family"] = 'Times New Roman'  #默认字体类型
mpl.rcParams["mathtext.fontset"] = 'cm' #数学文字字体
mpl.rcParams["font.size"] = 5
mpl.rcParams["axes.linewidth"] = 0.6


def elewap(a,b):
    d1 = xr.open_dataset(a)
    d2 = xr.open_dataset(b)
   
    time1 = d1['time']
    time2 = d2['time']
   
    #time = pd.to_datetime(d1['time'])
    #print(time1)

    cmccu1 = d1['ts'][(time1.dt.year <= 2010) & (time1.dt.year >=1981)]
    cmccu2 = d2['ts'][(time2.dt.year <= 2050) & (time2.dt.year >=2021)]

    lon1 = d1['lon'][:]
    lat1 = d1['lat'][:]
  
    #print(a,time2[72:])

    cmccpu1 = np.array(d1.ts.loc[(d1.time.dt.year.isin([1981+i for i in range(30)]))&(d1.time.dt.month.isin([6+i for i in range(5)]))])
    cmccpu2 = np.array(d2.ts.loc[(d2.time.dt.year.isin([2021+i for i in range(30)]))&(d2.time.dt.month.isin([6+i for i in range(5)]))])
   
    #print(cmccpu1.shape)
    _,p1 = ttest_ind(cmccpu2,cmccpu1,equal_var=False)

    print(p1)
    #print(cmccu1)
    cmccu1cli = cmccu1.groupby('time.month').mean(dim='time')
    cmccu2cli = cmccu2.groupby('time.month').mean(dim='time')
   
    #print(eracli.shape)
    cmccuh = cmccu1cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccuf = cmccu2cli.sel(month=[6,7,8,9,10]).mean(dim='month')
   

    cmccdu = cmccuf - cmccuh
    
    g1=np.zeros((73,144))
    
    for i in range(len(lat1)):
        for j in range(len(lon1)):
            if p1[i,j]<0.1:
                g1[i,j]=cmccdu[i,j]
            else:
                g1[i,j]=np.nan
              
               
    
    return cmccdu,lon1,lat1,g1

def elewapec(a,b,c,d):
    d1 = xr.open_dataset(a)
    d2 = xr.open_dataset(b)
    dd1 = xr.open_dataset(c)
    dd2 = xr.open_dataset(d)
   
    time1 = d1['time']
    time2 = d2['time']
    dtime1 = dd1['time']
    dtime2 = dd2['time']
    
    #time = pd.to_datetime(d1['time'])
    print(dtime2)

    dcmccu1 = d1['ts'][(time1.dt.year <= 2010) & (time1.dt.year >=1981)]
    dcmccu2 = d2['ts'][(time2.dt.year <= 2049) & (time2.dt.year >=2021)]
    ddcmccu1 = dd1['ts'][(dtime1.dt.year <= 2010) & (dtime1.dt.year >=1981)]
    ddcmccu2 = dd2['ts'][(dtime2.dt.year <= 2049) & (dtime2.dt.year >=2021)]
   
    cmccu1 = (dcmccu1+ddcmccu1)/2
    cmccu2 = (dcmccu2+ddcmccu2)/2

    
    lon1 = d1['lon'][:]
    lat1 = d1['lat'][:]



    
    cmccpu1 = np.array(dd1.ts.loc[dd1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16'])
    cmccpu2 = np.array(dd2.ts.loc[dd2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16'])
   
   
    #print(cmccpu1.shape)
    _,p1 = ttest_ind(cmccpu2,cmccpu1,equal_var=False)


    #print(cmccu1)
    cmccu1cli = cmccu1.groupby('time.month').mean(dim='time')
    cmccu2cli = cmccu2.groupby('time.month').mean(dim='time')
   
    #print(eracli.shape)
    cmccuh = cmccu1cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccuf = cmccu2cli.sel(month=[6,7,8,9,10]).mean(dim='month')
   

    cmccdu = cmccuf - cmccuh
    
    g1=np.zeros((73,144))
    
    for i in range(len(lat1)):
        for j in range(len(lon1)):
            if p1[i,j]<0.1:
                g1[i,j]=cmccdu[i,j]
            else:
                g1[i,j]=np.nan
            
               
    
    return cmccdu,lon1,lat1,g1


proj = ccrs.PlateCarree(central_longitude=180)  #中国为左
leftlon, rightlon, lowerlat, upperlat = (100,358,0,45)
lon_formatter = cticker.LongitudeFormatter()
lat_formatter = cticker.LatitudeFormatter()
fig = plt.figure(figsize=(7,1.5),dpi=600)  
x1 = [0.15,0.15,0.15,0.5,0.5,0.5]
yy = [0.98,0.63,0.28,0.98,0.63,0.28]
dx = 0.432
dy = 0.27
ax = []
label = ['(a) CMCC','(b) CNRM','(c) EC-Earth','(d) MRI-S','(e) MRI-H','(f) HadGEM']
for i in range(6):
    ax.append(fig.add_axes([x1[i],yy[i],dx,dy],projection = proj))
for i in range(6):
    ax[i].set_extent([leftlon, rightlon, lowerlat, upperlat], crs=ccrs.PlateCarree())
    ax[i].add_feature(cfeature.COASTLINE.with_scale('50m'),lw=0.2)
    gl=ax[i].gridlines(draw_labels=True, linewidth=0.5, color='k', alpha=0.5, linestyle='--')
    gl.xlocator = mticker.FixedLocator([-90,0,180])
    gl.ylocator = mticker.FixedLocator(np.arange(-15,60,15))
    gl.ypadding=2
    gl.xpadding=2
    if i!=0 and i!=2 and i!=1:
        gl.left_labels    = False
    if i != 2 and i != 5:
        gl.bottom_labels    = False
    gl.top_labels    = False    
    gl.right_labels  = False
    ax[i].text(-80,49,label[i])   
levels = np.arange(-2, 2 + 0.0001, 0.2)

cmcc1,lon1,lat1,g1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-CMCC–1948-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-CMCC–2015-2050.nc')
cb=ax[0].contourf(lon1,lat1,g1, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)
position1=fig.add_axes([0.9, 0.5, 0.012, 0.6])#位置[左,下,长度,宽度]
cbar=plt.colorbar(cb,cax=position1,orientation='vertical',ticks=np.arange(-2,2+0.00001,1),
                  aspect=20,shrink=0.2,pad=0.06)#方向  
ax[4].text(193,-33,'K',fontsize=6)

cnrm1,lon1,lat1,g1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-CNRM–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-CNRM–2015-2050.nc')
ax[1].contourf(lon1,lat1,g1, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)

mri201,lon1,lat1,g1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-MRI20–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-MRI20–2015-2050.nc')
ax[3].contourf(lon1,lat1,g1, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)

mri601,lon1,lat1,g1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-MRI60–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-MRI60–2015-2050.nc')
ax[4].contourf(lon1,lat1,g1, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)

had1,lon1,lat1,g1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-HAD–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-HAD–2015-2050.nc')
ax[5].contourf(lon1,lat1,g1, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)

ece1,lon1,lat1,g1 = elewapec(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-ECE1–1950-2015.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-ECE1–2015-2049.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-ECE2–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ts-ECE2–2015-2050.nc')
ax[2].contourf(lon1,lat1,g1, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)

for i in range(6):
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
for i in range(6):
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
for i in range(6):
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
    
    
ts1=[[] for i in range(6)]
ts2=[[] for i in range(6)]
ts3=[[] for i in range(6)]

for i in range(38,45):
    for j in range(44,65):
        ts1[0].append(cmcc1[i,j])
        ts1[1].append(cnrm1[i,j])
        ts1[2].append(ece1[i,j])
        ts1[3].append(mri201[i,j])
        ts1[4].append(mri601[i,j])
        ts1[5].append(had1[i,j])
for i in range(40,42):
    for j in range(92,109):
        ts2[0].append(cmcc1[i,j])
        ts2[1].append(cnrm1[i,j])
        ts2[2].append(ece1[i,j])
        ts2[3].append(mri201[i,j])
        ts2[4].append(mri601[i,j])
        ts2[5].append(had1[i,j])
for i in range(42,43):
    for j in range(92,108):
        ts2[0].append(cmcc1[i,j])
        ts2[1].append(cnrm1[i,j])
        ts2[2].append(ece1[i,j])
        ts2[3].append(mri201[i,j])
        ts2[4].append(mri601[i,j])
        ts2[5].append(had1[i,j])
for i in range(43,44):
    for j in range(92,104):
        ts2[0].append(cmcc1[i,j])
        ts2[1].append(cnrm1[i,j])
        ts2[2].append(ece1[i,j])
        ts2[3].append(mri201[i,j])
        ts2[4].append(mri601[i,j])
        ts2[5].append(had1[i,j])
for i in range(44,45):
    for j in range(92,103):
        ts2[0].append(cmcc1[i,j])
        ts2[1].append(cnrm1[i,j])
        ts2[2].append(ece1[i,j])
        ts2[3].append(mri201[i,j])
        ts2[4].append(mri601[i,j])
        ts2[5].append(had1[i,j])
for i in range(40,45):
    for j in range(112,125):
        ts3[0].append(cmcc1[i,j])
        ts3[1].append(cnrm1[i,j])
        ts3[2].append(ece1[i,j])
        ts3[3].append(mri201[i,j])
        ts3[4].append(mri601[i,j])
        ts3[5].append(had1[i,j])
t1=[]
t2=[]
t3=[]

for i in range(6):
    t1.append(sum(ts1[i])/len(ts1[i]))
    t2.append(sum(ts2[i])/len(ts2[i]))
    t3.append(sum(ts3[i])/len(ts3[i]))
   
    
tsdata=[sum(t1)/len(t1),sum(t2)/len(t2),sum(t3)/len(t3)]

print(t1,t2,t3,tsdata)
plt.show()

