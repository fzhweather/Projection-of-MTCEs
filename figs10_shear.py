#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 20:35:05 2022

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
def diffwind(a,b,c,d):
    d1 = xr.open_dataset(a)
    d2 = xr.open_dataset(b)
    d3 = xr.open_dataset(c)
    d4 = xr.open_dataset(d)
    time1 = d1['time']
    time2 = d2['time']
    time3 = d3['time']
    time4 = d4['time']
    #time = pd.to_datetime(d1['time'])
    #print(time1)

    cmccu1 = d1['ua'][(time1.dt.year <= 2010) & (time1.dt.year >=1981)].sel(plev=85000)
    cmccu2 = d2['ua'][(time2.dt.year <= 2050) & (time2.dt.year >=2021)].sel(plev=85000)
    cmccv1 = d3['va'][(time3.dt.year <= 2010) & (time3.dt.year >=1981)].sel(plev=85000)
    cmccv2 = d4['va'][(time4.dt.year <= 2050) & (time4.dt.year >=2021)].sel(plev=85000)
    cmccu12 = d1['ua'][(time1.dt.year <= 2010) & (time1.dt.year >=1981)].sel(plev=20000)
    cmccu22 = d2['ua'][(time2.dt.year <= 2050) & (time2.dt.year >=2021)].sel(plev=20000)
    cmccv12 = d3['va'][(time3.dt.year <= 2010) & (time3.dt.year >=1981)].sel(plev=20000)
    cmccv22 = d4['va'][(time4.dt.year <= 2050) & (time4.dt.year >=2021)].sel(plev=20000)
    lon1 = d1['lon'][:]
    lat1 = d1['lat'][:]




    cmccpu18 = np.array(d1.ua.loc[d1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2010-12-16',85000])
    cmccpu28 = np.array(d2.ua.loc[d2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2050-12-16',85000])
    cmccpv18 = np.array(d3.va.loc[d3.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2010-12-16',85000])
    cmccpv28 = np.array(d4.va.loc[d4.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2050-12-16',85000])
    cmccpu12 = np.array(d1.ua.loc[d1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2010-12-16',20000])
    cmccpu22 = np.array(d2.ua.loc[d2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2050-12-16',20000])
    cmccpv12 = np.array(d3.va.loc[d3.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2010-12-16',20000])
    cmccpv22 = np.array(d4.va.loc[d4.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2050-12-16',20000])
    
    cmccpu1 = cmccpu12-cmccpu18
    cmccpu2 = cmccpu22-cmccpu28
    cmccpv1 = cmccpv12-cmccpv18
    cmccpv2 = cmccpv22-cmccpv28
    #print(cmccpu1.shape)
    _,p1 = ttest_ind(cmccpu2,cmccpu1,equal_var=False)
    _,p2 = ttest_ind(cmccpv2,cmccpv1,equal_var=False)

    #print(cmccu1)
    cmccu1cli = cmccu1.groupby('time.month').mean(dim='time')
    cmccu2cli = cmccu2.groupby('time.month').mean(dim='time')
    cmccv1cli = cmccv1.groupby('time.month').mean(dim='time')
    cmccv2cli = cmccv2.groupby('time.month').mean(dim='time')
    cmccu1cli2 = cmccu12.groupby('time.month').mean(dim='time')
    cmccu2cli2 = cmccu22.groupby('time.month').mean(dim='time')
    cmccv1cli2 = cmccv12.groupby('time.month').mean(dim='time')
    cmccv2cli2 = cmccv22.groupby('time.month').mean(dim='time')
    #print(eracli.shape)
    cmccuh8 = cmccu1cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccuf8 = cmccu2cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccvh8 = cmccv1cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccvf8 = cmccv2cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccuh2 = cmccu1cli2.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccuf2 = cmccu2cli2.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccvh2 = cmccv1cli2.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccvf2 = cmccv2cli2.sel(month=[6,7,8,9,10]).mean(dim='month')

    cmccdu1 = cmccuh2 - cmccuh8
    cmccdv1 = cmccvh2 - cmccvh8
    cmccdu2 = cmccuf2 - cmccuf8
    cmccdv2 = cmccvf2 - cmccvf8
    cmccdw = (cmccdu2*cmccdu2+cmccdv2*cmccdv2)**(0.5)-(cmccdu1*cmccdu1+cmccdv1*cmccdv1)**(0.5)
    
   
    
    g1=np.zeros((73,144))
    for i in range(len(lat1)):
        for j in range(len(lon1)):
            if p1[i,j]<0.1 or p2[i,j]<0.1:
                g1[i,j]=cmccdw[i,j]
            else:
                g1[i,j]=np.nan
    
    return cmccdw,lon1,lat1,g1

def diffwindec(a,b,c,d,aa,bb,cc,dd):
    d1 = xr.open_dataset(a)
    d2 = xr.open_dataset(b)
    d3 = xr.open_dataset(c)
    d4 = xr.open_dataset(d)
    dd1 = xr.open_dataset(aa)
    dd2 = xr.open_dataset(bb)
    dd3 = xr.open_dataset(cc)
    dd4 = xr.open_dataset(dd)

    time1 = d1['time']
    time2 = d2['time']
    time3 = d3['time']
    time4 = d4['time']
    
    dtime1 = dd1['time']
    dtime2 = dd2['time']
    dtime3 = dd3['time']
    dtime4 = dd4['time']
    
    #time = pd.to_datetime(d1['time'])
    #print(time2)

    dcmccu1 = d1['ua'][(time1.dt.year <= 2010) & (time1.dt.year >=1981)].sel(plev=85000)
    dcmccu2 = d2['ua'][(time2.dt.year <= 2049) & (time2.dt.year >=2021)].sel(plev=85000)
    dcmccv1 = d3['va'][(time3.dt.year <= 2010) & (time3.dt.year >=1981)].sel(plev=85000)
    dcmccv2 = d4['va'][(time4.dt.year <= 2049) & (time4.dt.year >=2021)].sel(plev=85000)
    ddcmccu1 = dd1['ua'][(dtime1.dt.year <= 2010) & (dtime1.dt.year >=1981)].sel(plev=85000)
    ddcmccu2 = dd2['ua'][(dtime2.dt.year <= 2049) & (dtime2.dt.year >=2021)].sel(plev=85000)
    ddcmccv1 = dd3['va'][(dtime3.dt.year <= 2010) & (dtime3.dt.year >=1981)].sel(plev=85000)
    ddcmccv2 = dd4['va'][(dtime4.dt.year <= 2049) & (dtime4.dt.year >=2021)].sel(plev=85000)
    dcmccu12 = d1['ua'][(time1.dt.year <= 2010) & (time1.dt.year >=1981)].sel(plev=20000)
    dcmccu22 = d2['ua'][(time2.dt.year <= 2049) & (time2.dt.year >=2021)].sel(plev=20000)
    dcmccv12 = d3['va'][(time3.dt.year <= 2010) & (time3.dt.year >=1981)].sel(plev=20000)
    dcmccv22 = d4['va'][(time4.dt.year <= 2049) & (time4.dt.year >=2021)].sel(plev=20000)
    ddcmccu12 = dd1['ua'][(dtime1.dt.year <= 2010) & (dtime1.dt.year >=1981)].sel(plev=20000)
    ddcmccu22 = dd2['ua'][(dtime2.dt.year <= 2049) & (dtime2.dt.year >=2021)].sel(plev=20000)
    ddcmccv12 = dd3['va'][(dtime3.dt.year <= 2010) & (dtime3.dt.year >=1981)].sel(plev=20000)
    ddcmccv22 = dd4['va'][(dtime4.dt.year <= 2049) & (dtime4.dt.year >=2021)].sel(plev=20000)
    
    lon1 = d1['lon'][:]
    lat1 = d1['lat'][:]
   
    
    cmccu18=(dcmccu1+ddcmccu1)/2
    cmccu28=(dcmccu2+ddcmccu2)/2
    cmccv18=(dcmccv1+ddcmccv1)/2
    cmccv28=(dcmccv2+ddcmccv2)/2
    
    cmccu12=(dcmccu12+ddcmccu12)/2
    cmccu22=(dcmccu22+ddcmccu22)/2
    cmccv12=(dcmccv12+ddcmccv12)/2
    cmccv22=(dcmccv22+ddcmccv22)/2


    dcmccpu18 = np.array(d1.ua.loc[d1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',85000])
    dcmccpu28 = np.array(d2.ua.loc[d2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',85000])
    dcmccpv18 = np.array(d3.va.loc[d3.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',85000])
    dcmccpv28 = np.array(d4.va.loc[d4.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',85000])
    
    ddcmccpu18 = np.array(dd1.ua.loc[dd1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',85000])
    ddcmccpu28 = np.array(dd2.ua.loc[dd2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',85000])
    ddcmccpv18 = np.array(dd3.va.loc[dd3.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',85000])
    ddcmccpv28 = np.array(dd4.va.loc[dd4.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',85000])
    
    dcmccpu12 = np.array(d1.ua.loc[d1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',20000])
    dcmccpu22 = np.array(d2.ua.loc[d2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',20000])
    dcmccpv12 = np.array(d3.va.loc[d3.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',20000])
    dcmccpv22 = np.array(d4.va.loc[d4.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',20000])
    
    ddcmccpu12 = np.array(dd1.ua.loc[dd1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',20000])
    ddcmccpu22 = np.array(dd2.ua.loc[dd2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',20000])
    ddcmccpv12 = np.array(dd3.va.loc[dd3.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',20000])
    ddcmccpv22 = np.array(dd4.va.loc[dd4.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',20000])
    
   
    
    cmccpu18 = (dcmccpu18+ddcmccpu18)/2
    cmccpu28 = (dcmccpu28+ddcmccpu28)/2
    cmccpv18 = (dcmccpv18+ddcmccpv18)/2
    cmccpv28 = (dcmccpv28+ddcmccpv28)/2
    
    cmccpu12 = (dcmccpu12+ddcmccpu12)/2
    cmccpu22 = (dcmccpu22+ddcmccpu22)/2
    cmccpv12 = (dcmccpv12+ddcmccpv12)/2
    cmccpv22 = (dcmccpv22+ddcmccpv22)/2

    cmccpu1 = cmccpu12-cmccpu18
    cmccpu2 = cmccpu22-cmccpu28
    cmccpv1 = cmccpv12-cmccpv18
    cmccpv2 = cmccpv22-cmccpv28
    
    _,p1 = ttest_ind(cmccpu2,cmccpu1,equal_var=False)
    _,p2 = ttest_ind(cmccpv2,cmccpv1,equal_var=False)

    cmccu1cli = cmccu18.groupby('time.month').mean(dim='time')
    cmccu2cli = cmccu28.groupby('time.month').mean(dim='time')
    cmccv1cli = cmccv18.groupby('time.month').mean(dim='time')
    cmccv2cli = cmccv28.groupby('time.month').mean(dim='time')
    cmccu1cli2 = cmccu12.groupby('time.month').mean(dim='time')
    cmccu2cli2 = cmccu22.groupby('time.month').mean(dim='time')
    cmccv1cli2 = cmccv12.groupby('time.month').mean(dim='time')
    cmccv2cli2 = cmccv22.groupby('time.month').mean(dim='time')
    #print(eracli.shape)
    cmccuh8 = cmccu1cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccuf8 = cmccu2cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccvh8 = cmccv1cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccvf8 = cmccv2cli.sel(month=[6,7,8,9,10]).mean(dim='month')

    cmccuh2 = cmccu1cli2.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccuf2 = cmccu2cli2.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccvh2 = cmccv1cli2.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccvf2 = cmccv2cli2.sel(month=[6,7,8,9,10]).mean(dim='month')

    cmccdu1 = cmccuh2 - cmccuh8
    cmccdv1 = cmccvh2 - cmccvh8
    cmccdu2 = cmccuf2 - cmccuf8
    cmccdv2 = cmccvf2 - cmccvf8
    cmccdw = (cmccdu2*cmccdu2+cmccdv2*cmccdv2)**(0.5)-(cmccdu1*cmccdu1+cmccdv1*cmccdv1)**(0.5)
    
   
    
    g1=np.zeros((73,144))
    for i in range(len(lat1)):
        for j in range(len(lon1)):
            if p1[i,j]<0.1 or p2[i,j]<0.1:
                g1[i,j]=cmccdw[i,j]
            else:
                g1[i,j]=np.nan
                

    
    return cmccdw,lon1,lat1,g1


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
levels = np.arange(-3, 3 + 0.0001, 0.3)
sc=50
qb='k'
wid=0.003
cmcc1,lon1,lat1,g1 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CMCC-1948-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CMCC-2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-CMCC-1948-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-CMCC-2015-2050.nc') 
cb=ax[0].contourf(lon1,lat1,g1, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)
position1=fig.add_axes([0.9, 0.5, 0.012, 0.6])#位置[左,下,长度,宽度]
cbar=plt.colorbar(cb,cax=position1,orientation='vertical',ticks=np.arange(-3,3+0.00001,1),
                  aspect=20,shrink=0.2,pad=0.06)#方向  
ax[4].text(193,-33,'m/s',fontsize=6)

cnrm1,lon1,lat1,g1 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CNRM-1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CNRM-2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-CNRM-1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-CNRM-2015-2050.nc') 
#ax[1].quiver(lon1[::kk],lat1[::kk],cnrm1[::kk,::kk],cnrm2[::kk,::kk],color=qb,scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#ax[1].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color='silver',scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#cnrm1,lon1,lat1,g1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-rlus-CNRM-1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-rlus-CNRM-2015-2050.nc')
ax[1].contourf(lon1,lat1,g1, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)

mri201,lon1,lat1,g1 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI20–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI20–2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-MRI20–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-MRI20–2015-2050.nc') 
#ax[3].quiver(lon1[::kk],lat1[::kk],mri201[::kk,::kk],mri202[::kk,::kk],color=qb,scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#ax[3].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color='silver',scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#mri201,lon1,lat1,g1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-rlus-MRI20–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-rlus-MRI20–2015-2050.nc')
ax[3].contourf(lon1,lat1,g1, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)

mri601,lon1,lat1,g1 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI60–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI60–2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-MRI60–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-MRI60–2015-2050.nc') 
#ax[4].quiver(lon1[::kk],lat1[::kk],mri601[::kk,::kk],mri602[::kk,::kk],color=qb,scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#ax[4].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color='silver',scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#mri601,lon1,lat1,g1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-rlus-MRI60–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-rlus-MRI60–2015-2050.nc')
ax[4].contourf(lon1,lat1,g1, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)

had1,lon1,lat1,g1 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-HAD–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-HAD–2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-HAD–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-HAD–2015-2050.nc') 
#ax[5].quiver(lon1[::kk],lat1[::kk],had1[::kk,::kk],had2[::kk,::kk],color=qb,scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#ax[5].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color='silver',scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#had1,lon1,lat1,g1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-rlus-HAD–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-rlus-HAD–2015-2050.nc')
ax[5].contourf(lon1,lat1,g1, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)

ece1,lon1,lat1,g1 = diffwindec(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-ECE1–1950-2015.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-ECE1–2015-2049.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-ECE1–1950-2015.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-ECE1–2015-2049.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-ECE2–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-ECE2–2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-ECE2–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-ECE2–2015-2050.nc')
#ax[2].quiver(lon1[::kk],lat1[::kk],ece1[::kk,::kk],ece2[::kk,::kk],color=qb,scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#ax[2].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color='silver',scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#ece1,lon1,lat1,g1 = elewapec(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-rlus-ECE1–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-rlus-ECE1–2015-2049.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-rlus-ECE2–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-rlus-ECE2–2015-2050.nc')
ax[2].contourf(lon1,lat1,g1, levels=levels,cmap=cmaps.BlueDarkRed18,transform=ccrs.PlateCarree(),extend='both',zorder=0)

#ax[0].quiverkey(hh, X = 0.9, Y = 1.13, U = 2,angle = 0,label='2m/s',labelsep=0.03,labelpos='E', color = 'k',labelcolor = 'k')
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
shear1=[[] for i in range(6)]
shear2=[[] for i in range(6)]
shear3=[[] for i in range(6)]

for i in range(38,45):
    for j in range(44,65):
        shear1[0].append(cmcc1[i,j])
        shear1[1].append(cnrm1[i,j])
        shear1[2].append(ece1[i,j])
        shear1[3].append(mri201[i,j])
        shear1[4].append(mri601[i,j])
        shear1[5].append(had1[i,j])
for i in range(40,42):
    for j in range(92,109):
        shear2[0].append(cmcc1[i,j])
        shear2[1].append(cnrm1[i,j])
        shear2[2].append(ece1[i,j])
        shear2[3].append(mri201[i,j])
        shear2[4].append(mri601[i,j])
        shear2[5].append(had1[i,j])
for i in range(42,43):
    for j in range(92,108):
        shear2[0].append(cmcc1[i,j])
        shear2[1].append(cnrm1[i,j])
        shear2[2].append(ece1[i,j])
        shear2[3].append(mri201[i,j])
        shear2[4].append(mri601[i,j])
        shear2[5].append(had1[i,j])
for i in range(43,44):
    for j in range(92,104):
        shear2[0].append(cmcc1[i,j])
        shear2[1].append(cnrm1[i,j])
        shear2[2].append(ece1[i,j])
        shear2[3].append(mri201[i,j])
        shear2[4].append(mri601[i,j])
        shear2[5].append(had1[i,j])
for i in range(44,45):
    for j in range(92,103):
        shear2[0].append(cmcc1[i,j])
        shear2[1].append(cnrm1[i,j])
        shear2[2].append(ece1[i,j])
        shear2[3].append(mri201[i,j])
        shear2[4].append(mri601[i,j])
        shear2[5].append(had1[i,j])
for i in range(40,45):
    for j in range(112,125):
        shear3[0].append(cmcc1[i,j])
        shear3[1].append(cnrm1[i,j])
        shear3[2].append(ece1[i,j])
        shear3[3].append(mri201[i,j])
        shear3[4].append(mri601[i,j])
        shear3[5].append(had1[i,j])
        
shea1=[]
shea2=[]
shea3=[]

for i in range(6):
    shea1.append(sum(shear1[i])/len(shear1[i]))
    shea2.append(sum(shear2[i])/len(shear2[i]))
    shea3.append(sum(shear3[i])/len(shear3[i]))
   
    
sheardata=[sum(shea1)/len(shea1),sum(shea2)/len(shea2),sum(shea3)/len(shea3)]

print(sheardata)
  
plt.show()
    


