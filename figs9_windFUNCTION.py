#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:52:48 2022

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
    lon1 = d1['lon'][:]
    lat1 = d1['lat'][:]
    lon1 = np.roll(lon1,72)



    cmccpu1 = np.array(d1.ua.loc[d1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2010-12-16',85000])
    cmccpu2 = np.array(d2.ua.loc[d2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2050-12-16',85000])
    cmccpv1 = np.array(d3.va.loc[d3.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2010-12-16',85000])
    cmccpv2 = np.array(d4.va.loc[d4.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2050-12-16',85000])

    print(cmccpu1.shape)
    _,p1 = ttest_ind(cmccpu2,cmccpu1,equal_var=False)
    _,p2 = ttest_ind(cmccpv2,cmccpv1,equal_var=False)

    #print(cmccu1)
    cmccu1cli = cmccu1.groupby('time.month').mean(dim='time')
    cmccu2cli = cmccu2.groupby('time.month').mean(dim='time')
    cmccv1cli = cmccv1.groupby('time.month').mean(dim='time')
    cmccv2cli = cmccv2.groupby('time.month').mean(dim='time')
    print(cmccu1cli.shape)
    #print(eracli.shape)
    cmccuh = cmccu1cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccuf = cmccu2cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccvh = cmccv1cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccvf = cmccv2cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccdu = cmccuf - cmccuh
    cmccdv = cmccvf - cmccvh
    
    sum1=0
    sum2=0
    for i in range(44,49):
        for j in range(44,47):
            sum1+=cmccdu[i,j]
    for i in range(38,43):
        for j in range(40,53):
            sum2+=cmccdu[i,j]
    print(sum2-sum1)
    
    g1=np.zeros((73,144))
    g2=np.zeros((73,144))
    for i in range(len(lat1)):
        for j in range(len(lon1)):
            if p1[i,j]<0.1 or p2[i,j]<0.1:
                g1[i,j]=cmccdu[i,j]
                g2[i,j]=cmccdv[i,j]
            else:
                g1[i,j]=np.nan
                g2[i,j]=np.nan
    
    return cmccdu,cmccdv,lon1,lat1,g1,g2

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

    lon1 = d1['lon'][:]
    lat1 = d1['lat'][:]
    lon1 = np.roll(lon1,72)
    
    cmccu1=(dcmccu1+ddcmccu1)/2
    cmccu2=(dcmccu2+ddcmccu2)/2
    cmccv1=(dcmccv1+ddcmccv1)/2
    cmccv2=(dcmccv2+ddcmccv2)/2


    dcmccpu1 = np.array(d1.ua.loc[d1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',85000])
    dcmccpu2 = np.array(d2.ua.loc[d2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',85000])
    dcmccpv1 = np.array(d3.va.loc[d3.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',85000])
    dcmccpv2 = np.array(d4.va.loc[d4.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',85000])
    
    ddcmccpu1 = np.array(dd1.ua.loc[dd1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',85000])
    ddcmccpu2 = np.array(dd2.ua.loc[dd2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',85000])
    ddcmccpv1 = np.array(dd3.va.loc[dd3.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',85000])
    ddcmccpv2 = np.array(dd4.va.loc[dd4.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',85000])
    
   
    
    cmccpu1 = (dcmccpu1+ddcmccpu1)/2
    cmccpu2 = (dcmccpu2+ddcmccpu2)/2
    cmccpv1 = (dcmccpv1+ddcmccpv1)/2
    cmccpv2 = (dcmccpv2+ddcmccpv2)/2
    print(cmccpu1.shape)
    _,p1 = ttest_ind(cmccpu2,cmccpu1,equal_var=False)
    _,p2 = ttest_ind(cmccpv2,cmccpv1,equal_var=False)

    #print(cmccu1)
    cmccu1cli = cmccu1.groupby('time.month').mean(dim='time')
    cmccu2cli = cmccu2.groupby('time.month').mean(dim='time')
    cmccv1cli = cmccv1.groupby('time.month').mean(dim='time')
    cmccv2cli = cmccv2.groupby('time.month').mean(dim='time')
    #print(eracli.shape)
    cmccuh = cmccu1cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccuf = cmccu2cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccvh = cmccv1cli.sel(month=[6,7,8,9,10]).mean(dim='month')
    cmccvf = cmccv2cli.sel(month=[6,7,8,9,10]).mean(dim='month')

    cmccdu = cmccuf - cmccuh
    cmccdv = cmccvf - cmccvh
    g1=np.zeros((73,144))
    g2=np.zeros((73,144))
    for i in range(len(lat1)):
        for j in range(len(lon1)):
            if p1[i,j]>0.1 and p2[i,j]>0.1:
                g1[i,j]=cmccdu[i,j]
                g2[i,j]=cmccdv[i,j]
            else:
                g1[i,j]=np.nan
                g2[i,j]=np.nan
                
    return cmccdu,cmccdv,lon1,lat1,g1,g2

def elewap(a,b):
    d1 = xr.open_dataset(a)
    d2 = xr.open_dataset(b)
   
    time1 = d1['time']
    time2 = d2['time']
   
    #time = pd.to_datetime(d1['time'])
    #print(time1)

    cmccu1 = d1['wap'][(time1.dt.year <= 2010) & (time1.dt.year >=1981)].sel(plev=85000)
    cmccu2 = d2['wap'][(time2.dt.year <= 2050) & (time2.dt.year >=2021)].sel(plev=85000)
   
    lon1 = d1['lon'][:]
    lat1 = d1['lat'][:]



    cmccpu1 = np.array(d1.wap.loc[d1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2010-12-16',85000])
    cmccpu2 = np.array(d2.wap.loc[d2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2050-12-16',85000])
   

    print(cmccpu1.shape)
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
    #print(time1)

    dcmccu1 = d1['wap'][(time1.dt.year <= 2010) & (time1.dt.year >=1981)].sel(plev=85000)
    dcmccu2 = d2['wap'][(time2.dt.year <= 2049) & (time2.dt.year >=2021)].sel(plev=85000)
    ddcmccu1 = dd1['wap'][(dtime1.dt.year <= 2010) & (dtime1.dt.year >=1981)].sel(plev=85000)
    ddcmccu2 = dd2['wap'][(dtime2.dt.year <= 2049) & (dtime2.dt.year >=2021)].sel(plev=85000)
   
    cmccu1 = (dcmccu1+ddcmccu1)/2
    cmccu2 = (dcmccu2+ddcmccu2)/2
    
    lon1 = d1['lon'][:]
    lat1 = d1['lat'][:]



    dcmccpu1 = np.array(d1.wap.loc[d1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',85000])
    dcmccpu2 = np.array(d2.wap.loc[d2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',85000])
    ddcmccpu1 = np.array(dd1.wap.loc[dd1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2009-12-16',85000])
    ddcmccpu2 = np.array(dd2.wap.loc[dd2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2049-12-16',85000])
   
    cmccpu1 = (dcmccpu1+ddcmccpu1)/2
    cmccpu2 = (dcmccpu2+ddcmccpu2)/2
    print(cmccpu1.shape)
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
    gl.ylocator = mticker.FixedLocator([0,15,30,45])
    gl.ypadding=2
    gl.xpadding=2
    if i!=0 and i!=2 and i!=1:
        gl.left_labels    = False
    if i != 2 and i != 5:
        gl.bottom_labels    = False
    gl.top_labels    = False    
    gl.right_labels  = False
    ax[i].text(-80,49,label[i])   
levels = np.arange(-0.01, 0.01 + 0.0001, 0.001)
sc=25
wid=0.003
qb='k'
cmcc1,cmcc2,lon1,lat1,g1,g2 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CMCC-1948-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CMCC-2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-CMCC-1948-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-CMCC-2015-2050.nc') 
hh=ax[0].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color=qb,scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#ax[0].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color='silver',scale=sc,width=wid,edgecolor='w',linewidth=0.15)

cmcc3,lon1,lat1,wg1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-CMCC-1948-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-CMCC-2015-2050.nc')
cb=ax[0].contourf(lon1,lat1,wg1, levels=levels,cmap=cmaps.GMT_red2green_r,transform=ccrs.PlateCarree(),extend='both',zorder=0)
position1=fig.add_axes([0.9, 0.5, 0.012, 0.6])#位置[左,下,长度,宽度]
cbar=plt.colorbar(cb,cax=position1,orientation='vertical',ticks=np.arange(-0.01,0.01+0.00001,0.005),
                  aspect=20,shrink=0.2,pad=0.06)#方向  
ax[4].text(193,-33,'Pa/s',fontsize=6)

cnrm1,cnrm2,lon1,lat1,g1,g2 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CNRM-1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CNRM-2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-CNRM-1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-CNRM-2015-2050.nc') 
ax[1].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color=qb,scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#ax[1].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color='silver',scale=sc,width=wid,edgecolor='w',linewidth=0.15)
cnrm3,lon1,lat1,wg2 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-CNRM-1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-CNRM-2015-2050.nc')
ax[1].contourf(lon1,lat1,wg2, levels=levels,cmap=cmaps.GMT_red2green_r,transform=ccrs.PlateCarree(),extend='both',zorder=0)

mri201,mri202,lon1,lat1,g1,g2 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI20–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI20–2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-MRI20–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-MRI20–2015-2050.nc') 
ax[3].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color=qb,scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#ax[3].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color='silver',scale=sc,width=wid,edgecolor='w',linewidth=0.15)
mri203,lon1,lat1,wg3 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-MRI20–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-MRI20–2015-2050.nc')
ax[3].contourf(lon1,lat1,wg3, levels=levels,cmap=cmaps.GMT_red2green_r,transform=ccrs.PlateCarree(),extend='both',zorder=0)

mri601,mri602,lon1,lat1,g1,g2 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI60–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI60–2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-MRI60–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-MRI60–2015-2050.nc') 
ax[4].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color=qb,scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#ax[4].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color='silver',scale=sc,width=wid,edgecolor='w',linewidth=0.15)
mri603,lon1,lat1,wg4 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-MRI60–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-MRI60–2015-2050.nc')
ax[4].contourf(lon1,lat1,wg4, levels=levels,cmap=cmaps.GMT_red2green_r,transform=ccrs.PlateCarree(),extend='both',zorder=0)

had1,had2,lon1,lat1,g1,g2 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-HAD–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-HAD–2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-HAD–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-HAD–2015-2050.nc') 
ax[5].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color=qb,scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#ax[5].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color='silver',scale=sc,width=wid,edgecolor='w',linewidth=0.15)
had3,lon1,lat1,wg5 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-HAD–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-HAD–2015-2050.nc')
ax[5].contourf(lon1,lat1,wg5, levels=levels,cmap=cmaps.GMT_red2green_r,transform=ccrs.PlateCarree(),extend='both',zorder=0)

ece1,ece2,lon1,lat1,g1,g2 = diffwindec(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-ECE1–1950-2015.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-ECE1–2015-2049.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-ECE1–1950-2015.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-ECE1–2015-2049.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-ECE2–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-ECE2–2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-ECE2–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-ECE2–2015-2050.nc')
ax[2].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color=qb,scale=sc,width=wid,edgecolor='w',linewidth=0.15)
#ax[2].quiver(lon1[::kk],lat1[::kk],g1[::kk,::kk],g2[::kk,::kk],color='silver',scale=sc,width=wid,edgecolor='w',linewidth=0.15)
ece3,lon1,lat1,wg6 = elewapec(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-ECE1–1950-2015.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-ECE1–2015-2049.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-ECE2–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-ECE2–2015-2050.nc')
ax[2].contourf(lon1,lat1,wg6, levels=levels,cmap=cmaps.GMT_red2green_r,transform=ccrs.PlateCarree(),extend='both',zorder=0)

ax[0].quiverkey(hh, X = 0.9, Y = 1.13, U = 1,angle = 0,label='1m/s',labelsep=0.03,labelpos='E', color = qb,labelcolor = 'k')
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
#print(lat1[40:45])
#print(lon1[112:125])
#print(cmcc3[38,44])

wap1=[[] for i in range(6)]
wap2=[[] for i in range(6)]
wap3=[[] for i in range(6)]
vor1=[[] for i in range(6)]
vor2=[[] for i in range(6)]
vor3=[[] for i in range(6)]
for i in range(38,39):
    for j in range(44,65):
        wap1[0].append(cmcc3[i,j])
        wap1[1].append(cnrm3[i,j])
        wap1[2].append(ece3[i,j])
        wap1[3].append(mri203[i,j])
        wap1[4].append(mri603[i,j])
        wap1[5].append(had3[i,j])
        vor1[0].append(2*(cmcc2[i,j+1]-cmcc2[i,j])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cmcc1[i+1,j]-cmcc1[i,j])/(5*110940))
        vor1[1].append(2*(cnrm2[i,j+1]-cnrm2[i,j])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cnrm1[i+1,j]-cnrm1[i,j])/(5*110940))
        vor1[2].append(2*(ece2[i,j+1]-ece2[i,j])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(ece1[i+1,j]-ece1[i,j])/(5*110940))
        vor1[3].append(2*(mri202[i,j+1]-mri202[i,j])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri201[i+1,j]-mri201[i,j])/(5*110940))
        vor1[4].append(2*(mri602[i,j+1]-mri602[i,j])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri601[i+1,j]-mri601[i,j])/(5*110940))
        vor1[5].append(2*(had2[i,j+1]-had2[i,j])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(had1[i+1,j]-had1[i,j])/(5*110940))
for i in range(39,45):
    for j in range(44,65):
        wap1[0].append(cmcc3[i,j])
        wap1[1].append(cnrm3[i,j])
        wap1[2].append(ece3[i,j])
        wap1[3].append(mri203[i,j])
        wap1[4].append(mri603[i,j])
        wap1[5].append(had3[i,j])
        vor1[0].append((cmcc2[i,j+1]-cmcc2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cmcc1[i+1,j]-cmcc1[i-1,j])/(5*110940))
        vor1[1].append((cnrm2[i,j+1]-cnrm2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cnrm1[i+1,j]-cnrm1[i-1,j])/(5*110940))
        vor1[2].append((ece2[i,j+1]-ece2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(ece1[i+1,j]-ece1[i-1,j])/(5*110940))
        vor1[3].append((mri202[i,j+1]-mri202[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri201[i+1,j]-mri201[i-1,j])/(5*110940))
        vor1[4].append((mri602[i,j+1]-mri602[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri601[i+1,j]-mri601[i-1,j])/(5*110940))
        vor1[5].append((had2[i,j+1]-had2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(had1[i+1,j]-had1[i-1,j])/(5*110940))
for i in range(40,41):
    for j in range(92,109):
        wap2[0].append(cmcc3[i,j])
        wap2[1].append(cnrm3[i,j])
        wap2[2].append(ece3[i,j])
        wap2[3].append(mri203[i,j])
        wap2[4].append(mri603[i,j])
        wap2[5].append(had3[i,j])
        vor2[0].append((cmcc2[i,j+1]-cmcc2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cmcc1[i+1,j]-cmcc1[i-1,j])/(5*110940))
        vor2[1].append((cnrm2[i,j+1]-cnrm2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cnrm1[i+1,j]-cnrm1[i-1,j])/(5*110940))
        vor2[2].append((ece2[i,j+1]-ece2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(ece1[i+1,j]-ece1[i-1,j])/(5*110940))
        vor2[3].append((mri202[i,j+1]-mri202[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri201[i+1,j]-mri201[i-1,j])/(5*110940))
        vor2[4].append((mri602[i,j+1]-mri602[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri601[i+1,j]-mri601[i-1,j])/(5*110940))
        vor2[5].append((had2[i,j+1]-had2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(had1[i+1,j]-had1[i-1,j])/(5*110940))
for i in range(41,42):
    for j in range(92,109):
        wap2[0].append(cmcc3[i,j])
        wap2[1].append(cnrm3[i,j])
        wap2[2].append(ece3[i,j])
        wap2[3].append(mri203[i,j])
        wap2[4].append(mri603[i,j])
        wap2[5].append(had3[i,j])
        vor2[0].append(2*(cmcc2[i,j]-cmcc2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cmcc1[i,j]-cmcc1[i-1,j])/(5*110940))
        vor2[1].append(2*(cnrm2[i,j]-cnrm2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cnrm1[i,j]-cnrm1[i-1,j])/(5*110940))
        vor2[2].append(2*(ece2[i,j]-ece2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(ece1[i,j]-ece1[i-1,j])/(5*110940))
        vor2[3].append(2*(mri202[i,j]-mri202[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri201[i,j]-mri201[i-1,j])/(5*110940))
        vor2[4].append(2*(mri602[i,j]-mri602[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri601[i,j]-mri601[i-1,j])/(5*110940))
        vor2[5].append(2*(had2[i,j]-had2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(had1[i,j]-had1[i-1,j])/(5*110940))
for i in range(42,43):
    for j in range(92,108):
        wap2[0].append(cmcc3[i,j])
        wap2[1].append(cnrm3[i,j])
        wap2[2].append(ece3[i,j])
        wap2[3].append(mri203[i,j])
        wap2[4].append(mri603[i,j])
        wap2[5].append(had3[i,j])
        vor2[0].append(2*(cmcc2[i,j]-cmcc2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cmcc1[i,j]-cmcc1[i-1,j])/(5*110940))
        vor2[1].append(2*(cnrm2[i,j]-cnrm2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cnrm1[i,j]-cnrm1[i-1,j])/(5*110940))
        vor2[2].append(2*(ece2[i,j]-ece2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(ece1[i,j]-ece1[i-1,j])/(5*110940))
        vor2[3].append(2*(mri202[i,j]-mri202[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri201[i,j]-mri201[i-1,j])/(5*110940))
        vor2[4].append(2*(mri602[i,j]-mri602[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri601[i,j]-mri601[i-1,j])/(5*110940))
        vor2[5].append(2*(had2[i,j]-had2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(had1[i,j]-had1[i-1,j])/(5*110940))
for i in range(43,44):
    for j in range(92,104):
        wap2[0].append(cmcc3[i,j])
        wap2[1].append(cnrm3[i,j])
        wap2[2].append(ece3[i,j])
        wap2[3].append(mri203[i,j])
        wap2[4].append(mri603[i,j])
        wap2[5].append(had3[i,j])
        vor2[0].append(2*(cmcc2[i,j]-cmcc2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cmcc1[i,j]-cmcc1[i-1,j])/(5*110940))
        vor2[1].append(2*(cnrm2[i,j]-cnrm2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cnrm1[i,j]-cnrm1[i-1,j])/(5*110940))
        vor2[2].append(2*(ece2[i,j]-ece2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(ece1[i,j]-ece1[i-1,j])/(5*110940))
        vor2[3].append(2*(mri202[i,j]-mri202[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri201[i,j]-mri201[i-1,j])/(5*110940))
        vor2[4].append(2*(mri602[i,j]-mri602[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri601[i,j]-mri601[i-1,j])/(5*110940))
        vor2[5].append(2*(had2[i,j]-had2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(had1[i,j]-had1[i-1,j])/(5*110940))
for i in range(44,45):
    for j in range(92,103):
        wap2[0].append(cmcc3[i,j])
        wap2[1].append(cnrm3[i,j])
        wap2[2].append(ece3[i,j])
        wap2[3].append(mri203[i,j])
        wap2[4].append(mri603[i,j])
        wap2[5].append(had3[i,j])
        vor2[0].append(2*(cmcc2[i,j]-cmcc2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cmcc1[i,j]-cmcc1[i-1,j])/(5*110940))
        vor2[1].append(2*(cnrm2[i,j]-cnrm2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cnrm1[i,j]-cnrm1[i-1,j])/(5*110940))
        vor2[2].append(2*(ece2[i,j]-ece2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(ece1[i,j]-ece1[i-1,j])/(5*110940))
        vor2[3].append(2*(mri202[i,j]-mri202[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri201[i,j]-mri201[i-1,j])/(5*110940))
        vor2[4].append(2*(mri602[i,j]-mri602[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri601[i,j]-mri601[i-1,j])/(5*110940))
        vor2[5].append(2*(had2[i,j]-had2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(had1[i,j]-had1[i-1,j])/(5*110940))
for i in range(41,45):
    for j in range(112,125):
        wap3[0].append(cmcc3[i,j])
        wap3[1].append(cnrm3[i,j])
        wap3[2].append(ece3[i,j])
        wap3[3].append(mri203[i,j])
        wap3[4].append(mri603[i,j])
        wap3[5].append(had3[i,j])
        vor3[0].append((cmcc2[i,j+1]-cmcc2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cmcc1[i+1,j]-cmcc1[i-1,j])/(5*110940))
        vor3[1].append((cnrm2[i,j+1]-cnrm2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(cnrm1[i+1,j]-cnrm1[i-1,j])/(5*110940))
        vor3[2].append((ece2[i,j+1]-ece2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(ece1[i+1,j]-ece1[i-1,j])/(5*110940))
        vor3[3].append((mri202[i,j+1]-mri202[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri201[i+1,j]-mri201[i-1,j])/(5*110940))
        vor3[4].append((mri602[i,j+1]-mri602[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri601[i+1,j]-mri601[i-1,j])/(5*110940))
        vor3[5].append((had2[i,j+1]-had2[i,j-1])/(5*110940*np.cos((i-36)*2.5/180*np.pi))-(had1[i+1,j]-had1[i-1,j])/(5*110940))
for i in range(40,41):
    for j in range(112,125):
        wap3[0].append(cmcc3[i,j])
        wap3[1].append(cnrm3[i,j])
        wap3[2].append(ece3[i,j])
        wap3[3].append(mri203[i,j])
        wap3[4].append(mri603[i,j])
        wap3[5].append(had3[i,j])
        vor3[0].append((cmcc2[i,j+1]-cmcc2[i,j])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(cmcc1[i+1,j]-cmcc1[i,j])/(2.5*110940))
        vor3[1].append((cnrm2[i,j+1]-cnrm2[i,j])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(cnrm1[i+1,j]-cnrm1[i,j])/(2.5*110940))
        vor3[2].append((ece2[i,j+1]-ece2[i,j])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(ece1[i+1,j]-ece1[i,j])/(2.5*110940))
        vor3[3].append((mri202[i,j+1]-mri202[i,j])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri201[i+1,j]-mri201[i,j])/(2.5*110940))
        vor3[4].append((mri602[i,j+1]-mri602[i,j])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(mri601[i+1,j]-mri601[i,j])/(2.5*110940))
        vor3[5].append((had2[i,j+1]-had2[i,j])/(2.5*110940*np.cos((i-36)*2.5/180*np.pi))-(had1[i+1,j]-had1[i,j])/(2.5*110940))
wa1=[]
wa2=[]
wa3=[]
vo1=[]
vo2=[]
vo3=[]
for i in range(6):
    wa1.append(sum(wap1[i])/len(wap1[i]))
    wa2.append(sum(wap2[i])/len(wap2[i]))
    wa3.append(sum(wap3[i])/len(wap3[i]))
    vo1.append(sum(vor1[i])/len(vor1[i]))
    vo2.append(sum(vor2[i])/len(vor2[i]))
    vo3.append(sum(vor3[i])/len(vor3[i]))
    
wapdata=[sum(wa1)/len(wa1),sum(wa2)/len(wa2),sum(wa3)/len(wa3)]
vordata=[sum(vo1)/len(vo1),sum(vo2)/len(vo2),sum(vo3)/len(vo3)]

#print(wa1,wa2,wa3,wapdata)

plt.show()
    
    
    