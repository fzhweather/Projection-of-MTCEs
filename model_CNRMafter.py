#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:04:32 2022

@author: fuzhenghang
"""



from xarray import open_dataset
import numpy as np
from netCDF4 import Dataset
from scipy import stats
from sklearn.metrics import mean_squared_error
import collections
# 两个参数分别是实际值、预测值

#x=[1979+i for i in range(42)]
#r_ab=stats.pearsonr(x,frequency)[0]
#print(r_ab)
#print(len(frequency))
t = Dataset(r'/dpvhome/dpv16/CMIP6/CNRM/TC-NH_TRACK_CNRM-CM6-1-HR_highresSST-present_r1i1p1f2_gr_19500101-20141231.nc')
t2 = open_dataset(r'/dpvhome/dpv16/CMIP6/CNRM/TC-NH_TRACK_CNRM-CM6-1-HR_highresSST-present_r1i1p1f2_gr_19500101-20141231.nc',use_cftime=True)
date = t2.variables['time'][:]
f = list(np.array(date))
numyear=65
start=1950
tn = 36524
#print(t.variables.keys())
a = t.variables['index'][:]
b = t.variables['lat_psl'][:]
c = t.variables['lon_psl'][:]
d = t.variables['time'][:]
e = t.variables['sfcWind'][:]#小于17剔除；100-180；5-40
k = t.variables['TRACK_ID']
w = t.variables['warm_core_indicator'][:]
#print(d[0:10])
#print(set(w))
#print(len(k))
#print(min(e[:1000]))
track=[]
st=1
for i in range(len(a)-1):
    if a[i]==a[i+1]-1:
        track.append(st)
    else:
        track.append(st)
        st+=1
track.append(st)
#print(track[:1000])
#print(b[100:200])
#print(np.array(date))
#print(b[1:10])

dayn=2
data=[]
dat=[]
da=[]
corr=[]
rmse=[]
frequency=[8,8,5,10,4,8,6,6,9,6,6,12,8,11,5,12,6,10,10,4,5,11,6,6,5,10,6,4,3,8,7,1,8,7,6,4]
for ua in range(13,14,1):
    for i in range(0,len(a)):
        if (e[i]>=ua) and (100<=c[i]<=180) and (0<=b[i]<=45):
            data.append([a[i],b[i],c[i],d[i],e[i],int(str(f[i]).split('-')[0]),int(str(f[i]).split('-')[1]),int(str(str(f[i]).split('-')[2]).split(' ')[0]),track[i]])
    if data[0][1]<=35:
        dat.append(data[0])
    for i1 in range(1,len(data)):
        if data[i1][-1]==data[i1-1][-1]:
            dat.append(data[i1])
        else:
            if data[i1][1]<=35:
                dat.append(data[i1])
            else:
                data[i1][-1]==data[i1-1][-1]
    track0=[]
    for i2 in range(len(dat)):
        track0.append(dat[i2][-1])
    c0 = collections.Counter(track0)
    c0 =dict(c0)
    for i3 in range(len(dat)):
        if int(c0.get(dat[i3][-1]))>=dayn:
            da.append(dat[i3])
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    mtcen=[[[] for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][3]==da[k][3]:
                aa+=1
        g[int((da[j][3]-tn)*4)]=[aa,da[j][5],da[j][6]]
        if aa>=2:
            mday[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][3]))
            mtcen[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][-1]))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            mdayn[i].append(len(k))
    nday=[]
    for i in range(numyear):
        nday.append(sum(mdayn[i]))
    #print(mdayn)
    day=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
    #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i]))
    corr.append(stats.pearsonr(number[29:65],frequency)[0])
    rmse.append((mean_squared_error(number[29:65],frequency))**(0.5))

#print('WNP:')
#print(corr)
#print(rmse)
#print(number)
stce=[[[] for i in range(12)]for i in range(numyear)]
stcn=[[] for i in range(numyear)]

for i in range(len(da)):
    if int(da[i][5])<=2050:
        stce[int(da[i][5])-start][int(da[i][6])-1].append(da[i][-1])
for i in range(numyear):
    for j in range(12):
        stcn[i].append(len(set(stce[i][j])))
mtcn=[[] for i in range(numyear)]
for i in range(numyear):
    for j in range(12):
        mtcn[i].append(len(set(mtcen[i][j])))        
file=open('/dpvhome/dpv16/output/CNRM1','a')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close
  
data=[]
dat=[]
da=[]
time=[]
corr=[]
rmse=[]
num=[]
frequency=[1,2,2,7,7,5,10,2,7,3,4,6,6,7,5,6,0,1,3,2,2,2,3,5,2,1,3,7,1,7,5,2,2,2,3,7]
for ua in range(13,14,1):
    for i in range(len(a)):
        if (e[i]>=ua) and (180<c[i]<=270) and (0<=b[i]<=45):
            data.append([a[i],b[i],c[i],d[i],e[i],int(str(f[i]).split('-')[0]),int(str(f[i]).split('-')[1]),int(str(str(f[i]).split('-')[2]).split(' ')[0]),track[i]])
    if data[0][1]<=35:
        dat.append(data[0])
    for i1 in range(1,len(data)):
        if data[i1][-1]==data[i1-1][-1]:
            dat.append(data[i1])
        else:
            if data[i1][1]<=35:
                dat.append(data[i1])
            else:
                data[i1][-1]==data[i1-1][-1]
    track0=[]
    for i2 in range(len(dat)):
        track0.append(dat[i2][-1])
    c0 = collections.Counter(track0)
    c0 =dict(c0)
    for i3 in range(len(dat)):
        if int(c0.get(dat[i3][-1]))>=dayn:
            da.append(dat[i3])
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    mtcen=[[[] for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][3]==da[k][3]:
                aa+=1
        g[int((da[j][3]-tn)*4)]=[aa,da[j][5],da[j][6]]
        if aa>=2:
            mday[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][3]))
            mtcen[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][-1]))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            mdayn[i].append(len(k))
    nday=[]
    for i in range(numyear):
        nday.append(sum(mdayn[i]))
    #print(mdayn)
    day=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
    #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i]))
    corr.append(stats.pearsonr(number[29:65],frequency)[0])
    rmse.append((mean_squared_error(number[29:65],frequency))**(0.5))

#print('EP:')
#print(number)
#print(rmse)
#print(num)
stce=[[[] for i in range(12)]for i in range(numyear)]
stcn=[[] for i in range(numyear)]
mtcn=[[] for i in range(numyear)]
for i in range(numyear):
    for j in range(12):
        mtcn[i].append(len(set(mtcen[i][j])))
for i in range(len(da)):
    if int(da[i][5])<=2050:
        stce[int(da[i][5])-start][int(da[i][6])-1].append(da[i][-1])
for i in range(numyear):
    for j in range(12):
        stcn[i].append(len(set(stce[i][j])))
file=open('/dpvhome/dpv16/output/CNRM2','a')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close

data=[]
dat=[]
da=[]
time=[]
corr=[]
rmse=[]
num=[]
frequency=[2,1,1,0,0,4,3,0,2,1,5,5,1,2,2,0,4,2,0,3,4,6,3,4,4,5,6,3,3,2,1,4,7,8,3,1]
for ua in range(13,14,1):
    for i in range(len(a)):
        if (e[i]>=ua) and (270<c[i]<=360) and (0<=b[i]<=45):
            data.append([a[i],b[i],c[i],d[i],e[i],int(str(f[i]).split('-')[0]),int(str(f[i]).split('-')[1]),int(str(str(f[i]).split('-')[2]).split(' ')[0]),track[i]])
    if data[0][1]<=35:
        dat.append(data[0])
    for i1 in range(1,len(data)):
        if data[i1][-1]==data[i1-1][-1]:
            dat.append(data[i1])
        else:
            if data[i1][1]<=35:
                dat.append(data[i1])
            else:
                data[i1][-1]==data[i1-1][-1]
    track0=[]
    for i2 in range(len(dat)):
        track0.append(dat[i2][-1])
    c0 = collections.Counter(track0)
    c0 =dict(c0)
    for i3 in range(len(dat)):
        if int(c0.get(dat[i3][-1]))>=dayn:
            da.append(dat[i3])
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    mtcen=[[[] for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][3]==da[k][3]:
                aa+=1
        g[int((da[j][3]-tn)*4)]=[aa,da[j][5],da[j][6]]
        if aa>=2:
            mday[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][3]))
            mtcen[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][-1]))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            mdayn[i].append(len(k))
    nday=[]
    for i in range(numyear):
        nday.append(sum(mdayn[i]))
    #print(mdayn)
    day=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
    #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i]))
    corr.append(stats.pearsonr(number[29:65],frequency)[0])
    rmse.append((mean_squared_error(number[29:65],frequency))**(0.5))

#print('NA:')
#print(number)
#print(rmse)
#print(num)
stce=[[[] for i in range(12)]for i in range(numyear)]
stcn=[[] for i in range(numyear)]
mtcn=[[] for i in range(numyear)]
for i in range(numyear):
    for j in range(12):
        mtcn[i].append(len(set(mtcen[i][j])))
for i in range(len(da)):
    if int(da[i][5])<=2050:
        stce[int(da[i][5])-start][int(da[i][6])-1].append(da[i][-1])
for i in range(numyear):
    for j in range(12):
        stcn[i].append(len(set(stce[i][j])))
file=open('/dpvhome/dpv16/output/CNRM3','a')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close

t = Dataset(r'/dpvhome/dpv16/CMIP6/CNRM/TC-NH_TRACK_CNRM-CM6-1-HR_highresSST-future_r1i1p1f2_gr_20150101-20501231.nc')
t2 = open_dataset(r'/dpvhome/dpv16/CMIP6/CNRM/TC-NH_TRACK_CNRM-CM6-1-HR_highresSST-future_r1i1p1f2_gr_20150101-20501231.nc',use_cftime=True)
date = t2.variables['time'][:]
f = list(np.array(date))
numyear=36
start=2015
tn = 60265
#print(t.variables.keys())
a = t.variables['index'][:]
b = t.variables['lat_psl'][:]
c = t.variables['lon_psl'][:]
d = t.variables['time'][:]
e = t.variables['sfcWind'][:]#小于17剔除；100-180；5-40
k = t.variables['TRACK_ID']
w = t.variables['warm_core_indicator'][:]
#print(d[0:10])
#print(set(w))
#print(len(k))
#print(min(e[:1000]))
track=[]
st=1
for i in range(len(a)-1):
    if a[i]==a[i+1]-1:
        track.append(st)
    else:
        track.append(st)
        st+=1
track.append(st)
#print(track[:1000])
#print(b[100:200])
#print(np.array(date))
#print(b[1:10])
dayn=2
data=[]
dat=[]
da=[]
corr=[]
rmse=[]
frequency=[8,8,5,10,4,8,6,6,9,6,6,12,8,11,5,12,6,10,10,4,5,11,6,6,5,10,6,4,3,8,7,1,8,7,6,4]
for ua in range(13,14,1):
    for i in range(0,len(a)):
        if (e[i]>=ua) and (100<=c[i]<=180) and (0<=b[i]<=45):
            data.append([a[i],b[i],c[i],d[i],e[i],int(str(f[i]).split('-')[0]),int(str(f[i]).split('-')[1]),int(str(str(f[i]).split('-')[2]).split(' ')[0]),track[i]])
    if data[0][1]<=35:
        dat.append(data[0])
    for i1 in range(1,len(data)):
        if data[i1][-1]==data[i1-1][-1]:
            dat.append(data[i1])
        else:
            if data[i1][1]<=35:
                dat.append(data[i1])
            else:
                data[i1][-1]==data[i1-1][-1]
    track0=[]
    for i2 in range(len(dat)):
        track0.append(dat[i2][-1])
    c0 = collections.Counter(track0)
    c0 =dict(c0)
    for i3 in range(len(dat)):
        if int(c0.get(dat[i3][-1]))>=dayn:
            da.append(dat[i3])
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    mtcen=[[[] for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][3]==da[k][3]:
                aa+=1
        g[int((da[j][3]-tn)*4)]=[aa,da[j][5],da[j][6]]
        if aa>=2:
            mday[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][3]))
            mtcen[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][-1]))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            mdayn[i].append(len(k))
    nday=[]
    for i in range(numyear):
        nday.append(sum(mdayn[i]))
    #print(mdayn)
    day=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
    #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i]))
 
#print('WNP:')
#print(corr)
#print(rmse)
#print(number)
stce=[[[] for i in range(12)]for i in range(numyear)]
stcn=[[] for i in range(numyear)]
mtcn=[[] for i in range(numyear)]
for i in range(numyear):
    for j in range(12):
        mtcn[i].append(len(set(mtcen[i][j])))
for i in range(len(da)):
    if int(da[i][5])<=2050:
        stce[int(da[i][5])-start][int(da[i][6])-1].append(da[i][-1])
for i in range(numyear):
    for j in range(12):
        stcn[i].append(len(set(stce[i][j])))
file=open('/dpvhome/dpv16/output/CNRM1','a')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close
 
data=[]
dat=[]
da=[]
time=[]
corr=[]
rmse=[]
num=[]
frequency=[1,2,2,7,7,5,10,2,7,3,4,6,6,7,5,6,0,1,3,2,2,2,3,5,2,1,3,7,1,7,5,2,2,2,3,7]
for ua in range(13,14,1):
    for i in range(len(a)):
        if (e[i]>=ua) and (180<c[i]<=270) and (0<=b[i]<=45):
            data.append([a[i],b[i],c[i],d[i],e[i],int(str(f[i]).split('-')[0]),int(str(f[i]).split('-')[1]),int(str(str(f[i]).split('-')[2]).split(' ')[0]),track[i]])
    if data[0][1]<=35:
        dat.append(data[0])
    for i1 in range(1,len(data)):
        if data[i1][-1]==data[i1-1][-1]:
            dat.append(data[i1])
        else:
            if data[i1][1]<=35:
                dat.append(data[i1])
            else:
                data[i1][-1]==data[i1-1][-1]
    track0=[]
    for i2 in range(len(dat)):
        track0.append(dat[i2][-1])
    c0 = collections.Counter(track0)
    c0 =dict(c0)
    for i3 in range(len(dat)):
        if int(c0.get(dat[i3][-1]))>=dayn:
            da.append(dat[i3])
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    mtcen=[[[] for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][3]==da[k][3]:
                aa+=1
        g[int((da[j][3]-tn)*4)]=[aa,da[j][5],da[j][6]]
        if aa>=2:
            mday[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][3]))
            mtcen[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][-1]))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            mdayn[i].append(len(k))
    nday=[]
    for i in range(numyear):
        nday.append(sum(mdayn[i]))
    #print(mdayn)
    day=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
    #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i]))

    
#print('EP:')
#print(number)
#print(rmse)
#print(num)
stce=[[[] for i in range(12)]for i in range(numyear)]
stcn=[[] for i in range(numyear)]
mtcn=[[] for i in range(numyear)]
for i in range(numyear):
    for j in range(12):
        mtcn[i].append(len(set(mtcen[i][j])))
for i in range(len(da)):
    if int(da[i][5])<=2050:
        stce[int(da[i][5])-start][int(da[i][6])-1].append(da[i][-1])
for i in range(numyear):
    for j in range(12):
        stcn[i].append(len(set(stce[i][j])))
file=open('/dpvhome/dpv16/output/CNRM2','a')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close

data=[]
dat=[]
da=[]
time=[]
corr=[]
rmse=[]
num=[]
frequency=[2,1,1,0,0,4,3,0,2,1,5,5,1,2,2,0,4,2,0,3,4,6,3,4,4,5,6,3,3,2,1,4,7,8,3,1]
for ua in range(13,14,1):
    for i in range(len(a)):
        if (e[i]>=ua) and (270<c[i]<=360) and (0<=b[i]<=45):
            data.append([a[i],b[i],c[i],d[i],e[i],int(str(f[i]).split('-')[0]),int(str(f[i]).split('-')[1]),int(str(str(f[i]).split('-')[2]).split(' ')[0]),track[i]])
    if data[0][1]<=35:
        dat.append(data[0])
    for i1 in range(1,len(data)):
        if data[i1][-1]==data[i1-1][-1]:
            dat.append(data[i1])
        else:
            if data[i1][1]<=35:
                dat.append(data[i1])
            else:
                data[i1][-1]==data[i1-1][-1]
    track0=[]
    for i2 in range(len(dat)):
        track0.append(dat[i2][-1])
    c0 = collections.Counter(track0)
    c0 =dict(c0)
    for i3 in range(len(dat)):
        if int(c0.get(dat[i3][-1]))>=dayn:
            da.append(dat[i3])
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    mtcen=[[[] for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][3]==da[k][3]:
                aa+=1
        g[int((da[j][3]-tn)*4)]=[aa,da[j][5],da[j][6]]
        if aa>=2:
            mday[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][3]))
            mtcen[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][-1]))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            mdayn[i].append(len(k))
    nday=[]
    for i in range(numyear):
        nday.append(sum(mdayn[i]))
    #print(mdayn)
    day=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
    #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i]))

#print('NA:')
#print(number)
#print(rmse)
#print(num)
stce=[[[] for i in range(12)]for i in range(numyear)]
stcn=[[] for i in range(numyear)]
mtcn=[[] for i in range(numyear)]
for i in range(numyear):
    for j in range(12):
        mtcn[i].append(len(set(mtcen[i][j])))
for i in range(len(da)):
    if int(da[i][5])<=2050:
        stce[int(da[i][5])-start][int(da[i][6])-1].append(da[i][-1])
for i in range(numyear):
    for j in range(12):
        stcn[i].append(len(set(stce[i][j])))
file=open('/dpvhome/dpv16/output/CNRM3','a')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close


