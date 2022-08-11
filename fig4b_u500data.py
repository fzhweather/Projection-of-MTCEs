#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 18:59:18 2022

@author: fuzhenghang
"""

import numpy as np
import xarray as xr

def u500(a,b):
    d1 = xr.open_dataset(a)
    d2 = xr.open_dataset(b)
    
    lon1 = d1['lon'][:]
    lat1 = d1['lat'][:]
    lon1 = np.roll(lon1,72)
    time1 = d1['time']
   
    #print(eracli.shape)
    cmccuh = np.array(d1.ua.loc[d1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01':'2010-12',50000])
    cmccuf = np.array(d2.ua.loc[d2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01':'2050-12',50000])
   
    
    return time1,cmccuh,cmccuf,lon1,lat1




t1,cmcc1,cmcc2,lon1,lat1 = u500(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CMCC-1948-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CMCC-2015-2050.nc') 
t2,cnrm1,cnrm2,lon1,lat1 = u500(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CNRM-1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-CNRM-2015-2050.nc') 
t3,mri201,mri202,lon1,lat1 = u500(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI20–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI20–2015-2050.nc') 
t4,mri601,mri602,lon1,lat1 = u500(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI60–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-MRI60–2015-2050.nc') 
t5,had1,had2,lon1,lat1 = u500(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-HAD–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-HAD–2015-2050.nc') 
t6,ece1,ece2,lon1,lat1 = u500(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-ECE2–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-ua-ECE2–2015-2050.nc')
u500h1=[]
u500h2=[]
u500h3=[]
u500h4=[]
u500h5=[]
u500h6=[]
for i in range(145):
    u500h6.append(ece1[i])
for i in range(150):
    if i<25 or i>=30:
        u500h1.append(cmcc1[i])
        u500h2.append(cnrm1[i])
        u500h3.append(mri201[i])
        u500h4.append(mri601[i])
        u500h5.append(had1[i])
u500f1=[]
u500f2=[]
u500f3=[]
u500f4=[]
u500f5=[]
u500f6=[]
for i in range(140):
    if i not in [58,59,92,95,100,117,118]:
        u500f1.append(cmcc2[i])
for i in range(150):
    if i not in [12,27,28,56,62,63,82,97,98,101,103,104,108,114,115,127,128]:
        u500f6.append(ece2[i])
        u500f2.append(cnrm2[i])
        u500f3.append(mri202[i])
        u500f4.append(mri602[i])
        u500f5.append(had2[i])       
print(u500f1[0].shape)
print(len(u500h1))
print(len(u500h2))
print(len(u500h3))
print(len(u500h4))
print(len(u500h5))
print(len(u500h6))

print(len(u500f1))
print(len(u500f2))
print(len(u500f3))
print(len(u500f4))
print(len(u500f5))
print(len(u500f6))