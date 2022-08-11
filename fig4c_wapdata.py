#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 22:14:27 2022

@author: fuzhenghang
"""

import numpy as np
import xarray as xr

def elewap(a,b):
    d1 = xr.open_dataset(a)
    d2 = xr.open_dataset(b)
    
    lon1 = d1['lon'][:]
    lat1 = d1['lat'][:]
   
    time1 = d2['time']
   
    #print(eracli.shape)
    cmccuh = np.array(d1.wap.loc[d1.time.dt.month.isin([6+i for i in range(5)])].loc['1981-01':'2010-12',50000])
    cmccuf = np.array(d2.wap.loc[d2.time.dt.month.isin([6+i for i in range(5)])].loc['2021-01':'2050-12',50000])
   
    
    return time1,cmccuh,cmccuf,lon1,lat1




t1,cmcc1,cmcc2,lon1,lat1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-CMCC-1948-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-CMCC-2015-2050.nc')
t2,cnrm1,cnrm2,lon1,lat1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-CNRM-1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-CNRM-2015-2050.nc')
t3,mri201,mri202,lon1,lat1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-MRI20–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-MRI20–2015-2050.nc')
t4,mri601,mri602,lon1,lat1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-MRI60–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-MRI60–2015-2050.nc')
t5,had1,had2,lon1,lat1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-HAD–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-HAD–2015-2050.nc')
t6,ece1,ece2,lon1,lat1 = elewap(r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-ECE2–1950-2014.nc',r'/Users/fuzhenghang/Documents/CMIP6/CombinedData/c-wap-ECE2–2015-2050.nc')
print(t1[310:])
print(cnrm2.shape)
print(mri202.shape)
print(mri602.shape)
print(had2.shape)
print(ece2.shape)

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
for i in range(144):
    if i not in [12,27,28,56,80,95,98,99,108,109,121]:
        u500f1.append(cmcc2[i])
for i in range(150):
    if i not in [12,27,28,56,62,63,82,97,98,101,103,104,108,114,115,127,128]:
        u500f6.append(ece2[i])
        u500f2.append(cnrm2[i])
        u500f3.append(mri202[i])
        u500f4.append(mri602[i])
        u500f5.append(had2[i])    
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
