#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 19:55:52 2022

@author: fuzhenghang
"""

import numpy as np
import xarray as xr

def diffwind(a,b,c,d):
    d1 = xr.open_dataset(a)
    d2 = xr.open_dataset(b)
    d3 = xr.open_dataset(c)
    d4 = xr.open_dataset(d)

    lon1 = d1['lon'][:]
    lat1 = d1['lat'][:]
    lon1 = np.roll(lon1,72)
    
    cmccpu18 = np.array(d1.ua.loc[d1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2010-12-16',85000])
    cmccpu28 = np.array(d2.ua.loc[d2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2050-12-16',85000])
    cmccpv18 = np.array(d3.va.loc[d3.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2010-12-16',85000])
    cmccpv28 = np.array(d4.va.loc[d4.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2050-12-16',85000])
    cmccpu12 = np.array(d1.ua.loc[d1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2010-12-16',20000])
    cmccpu22 = np.array(d2.ua.loc[d2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2050-12-16',20000])
    cmccpv12 = np.array(d3.va.loc[d3.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01-16':'2010-12-16',20000])
    cmccpv22 = np.array(d4.va.loc[d4.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01-16':'2050-12-16',20000])
    
    cmccdu1 = cmccpu12-cmccpu18
    cmccdu2 = cmccpu22-cmccpu28
    cmccdv1 = cmccpv12-cmccpv18
    cmccdv2 = cmccpv22-cmccpv28

    cmccdu1d=[]
    cmccdu2d=[]
    cmccdv1d=[]
    cmccdv2d=[]
    if len(cmccdu1)==145:
        for i in range(145):
            cmccdu1d.append(cmccdu1[i])
            cmccdv1d.append(cmccdv1[i])
    else:
        for i in range(150):
            if i<25 or i>=30:
                cmccdu1d.append(cmccdu1[i])
                cmccdv1d.append(cmccdv1[i])
    if len(cmccdu2)==140:
        for i in range(140):
            if i not in[58,59,92,95,100,117,118]:
                cmccdu2d.append(cmccdu2[i])
                cmccdv2d.append(cmccdv2[i])
    else:
        for i in range(149):
            if i not in [12,27,28,56,62,63,82,97,98,101,103,104,108,114,115,127]:
                cmccdu2d.append(cmccdu2[i])
                cmccdv2d.append(cmccdv2[i])
    shh=[]
    shf=[]
    for i in range(145):
        shh.append((cmccdu1d[i]*cmccdu1d[i]+cmccdv1d[i]*cmccdv1d[i])**(0.5))
    for i in range(133):
        shf.append((cmccdu2d[i]*cmccdu2d[i]+cmccdv2d[i]*cmccdv2d[i])**(0.5))

    return shh,shf,lon1,lat1



cmcc1,cmcc2,lon1,lat1 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CMCC-1948-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CMCC-2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-CMCC-1948-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-CMCC-2015-2050.nc') 
cnrm1,cnrm2,lon1,lat1 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CNRM-1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CNRM-2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-CNRM-1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-CNRM-2015-2050.nc') 
mri201,mri202,lon1,lat1 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI20–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI20–2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-MRI20–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-MRI20–2015-2050.nc') 
mri601,mri602,lon1,lat1 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI60–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI60–2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-MRI60–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-MRI60–2015-2050.nc') 
had1,had2,lon1,lat1 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-HAD–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-HAD–2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-HAD–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-HAD–2015-2050.nc') 
ece1,ece2,lon1,lat1 = diffwind(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-ECE2–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-ECE2–2015-2050.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-ECE2–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-va-ECE2–2015-2050.nc')


