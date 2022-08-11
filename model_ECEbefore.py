#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 21:19:44 2022

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
tn=0
tn1=0
tn2=0
# 两个参数分别是实际值、预测值

#x=[1979+i for i in range(42)]
#r_ab=stats.pearsonr(x,frequency)[0]
#print(r_ab)
#print(len(frequency))
t = Dataset(r'/dpvhome/dpv16/CMIP6/ECMWF/TC-NH_TRACK_ECMWF-IFS-HR_highresSST-present_r1i1p1f1_gr_19500101-20141231.nc')
t2 = open_dataset(r'/dpvhome/dpv16/CMIP6/ECMWF/TC-NH_TRACK_ECMWF-IFS-HR_highresSST-present_r1i1p1f1_gr_19500101-20141231.nc',use_cftime=True)
date = t2.variables['time'][:]
f = list(np.array(date))
numyear=65
start=1950

#print(t.variables.keys())
a = t.variables['index'][:]
b = t.variables['lat_psl'][:]
c = t.variables['lon_psl'][:]
d = t.variables['time'][:]
e = t.variables['sfcWind'][:]#小于17剔除；100-180；5-40
k = t.variables['TRACK_ID']

track=[]
st=1
for i in range(len(a)-1):
    if a[i]==a[i+1]-1:
        track.append(st)
    else:
        track.append(st)
        st+=1
track.append(st)

t3 = Dataset(r'/dpvhome/dpv16/CMIP6/ECMWF/TC-NH_TRACK_ECMWF-IFS-HR_highresSST-present_r5i1p1f1_gr_19500101-20141231.nc')
t4 = open_dataset(r'/dpvhome/dpv16/CMIP6/ECMWF/TC-NH_TRACK_ECMWF-IFS-HR_highresSST-present_r5i1p1f1_gr_19500101-20141231.nc',use_cftime=True)
date1 = t4.variables['time'][:]
f1 = list(np.array(date1))
numyear1=65
start1=1950

#print(t.variables.keys())
a1 = t3.variables['index'][:]
b1 = t3.variables['lat_psl'][:]
c1 = t3.variables['lon_psl'][:]
d1 = t3.variables['time'][:]
e1 = t3.variables['sfcWind'][:]#小于17剔除；100-180；5-40
k1 = t3.variables['TRACK_ID']
#print(len(k))
#print(min(e[:1000]))
track1=[]
st1=1
for i in range(len(a1)-1):
    if a1[i]==a1[i+1]-1:
        track1.append(st1)
    else:
        track1.append(st1)
        st1+=1
track1.append(st1)

t5 = Dataset(r'/dpvhome/dpv16/CMIP6/ECMWF/TC-NH_TRACK_ECMWF-IFS-HR_highresSST-present_r6i1p1f1_gr_19500101-20141231.nc')
t6 = open_dataset(r'/dpvhome/dpv16/CMIP6/ECMWF/TC-NH_TRACK_ECMWF-IFS-HR_highresSST-present_r6i1p1f1_gr_19500101-20141231.nc',use_cftime=True)
date2 = t6.variables['time'][:]
f2 = list(np.array(date2))
numyear2=65
start2=1950

#print(t.variables.keys())
a2 = t5.variables['index'][:]
b2 = t5.variables['lat_psl'][:]
c2 = t5.variables['lon_psl'][:]
d2 = t5.variables['time'][:]
e2 = t5.variables['sfcWind'][:]#小于17剔除；100-180；5-40
k2 = t5.variables['TRACK_ID']
#print(len(k))
#print((d[:10]))
#print((d1[:10]))
#print((d2[:10]))
track2=[]
st2=1
for i in range(len(a2)-1):
    if a2[i]==a2[i+1]-1:
        track2.append(st2)
    else:
        track2.append(st2)
        st2+=1
track2.append(st2)



da=[]
da1=[]
da2=[]
corr=[]
rmse=[]
frequency=[8,8,5,10,4,8,6,6,9,6,6,12,8,11,5,12,6,10,10,4,5,11,6,6,5,10,6,4,3,8,7,1,8,7,6,4]
for ua in range(17,18):
    for i in range(len(a)):
        if (e[i]>=ua) and (100<=c[i]<=180) and (0<=b[i]<=45):
            da.append([a[i],b[i],c[i],d[i],e[i],int(str(f[i]).split('-')[0]),int(str(f[i]).split('-')[1]),int(str(str(f[i]).split('-')[2]).split(' ')[0]),track[i]])
    for j in range(len(a1)):
        if (e1[j]>=ua) and (100<=c1[j]<=180) and (0<=b1[j]<=45):
            da1.append([a1[j],b1[j],c1[j],d1[j],e1[j],int(str(f1[j]).split('-')[0]),int(str(f1[j]).split('-')[1]),int(str(str(f1[j]).split('-')[2]).split(' ')[0]),track1[j]])
    for m in range(len(a2)):
        if (e2[m]>=ua) and (100<=c2[m]<=180) and (0<=b2[m]<=45):
            da2.append([a2[m],b2[m],c2[m],d2[m],e2[m],int(str(f2[m]).split('-')[0]),int(str(f2[m]).split('-')[1]),int(str(str(f2[m]).split('-')[2]).split(' ')[0]),track2[m]])
   
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    g1=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    g2=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    mday1=[[[]for i in range(12)]for i in range(numyear)]
    mday2=[[[]for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][3]==da[k][3]:
                aa+=1
        g[int((da[j][3]-tn)*4)]=[aa,da[j][5],da[j][6]]
        if aa>=2:
            mday[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][3]))
    for j in range(len(da1)):
        aa=0
        for k in range(len(da1)):
            if da1[j][3]==da1[k][3]:
                aa+=1
        g1[int((da1[j][3]-tn1)*4)]=[aa,da1[j][5],da1[j][6]]
        if aa>=2:
            mday1[int(da1[j][5])-start][int(da1[j][6])-1].append(int(da1[j][3]))
    for j in range(len(da2)):
        aa=0
        for k in range(len(da2)):
            if da2[j][3]==da2[k][3]:
                aa+=1
        g2[int((da2[j][3]-tn2)*4)]=[aa,da2[j][5],da2[j][6]]
        if aa>=2:
            mday2[int(da2[j][5])-start][int(da2[j][6])-1].append(int(da2[j][3]))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    mdayn1=[[]for i in range(numyear)]
    mdayn2=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            k1=set(mday1[i][j])
            k2=set(mday2[i][j])
            mdayn[i].append(len(k))
            mdayn1[i].append(len(k1))
            mdayn2[i].append(len(k2))
    #print(mdayn)
    day=[]
    day1=[]
    day2=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
        day1.append([max(g1[j][0] for j in range(j*4,(j+1)*4)),max(g1[j][1] for j in range(j*4,(j+1)*4)),max(g1[j][2] for j in range(j*4,(j+1)*4))])
        day2.append([max(g2[j][0] for j in range(j*4,(j+1)*4)),max(g2[j][1] for j in range(j*4,(j+1)*4)),max(g2[j][2] for j in range(j*4,(j+1)*4))])
    
   #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
                
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
    for i in range(1,len(day1)):
        if day1[i][2]==day1[i-1][2]:
            if day1[i-1][0]<=1 and day1[i][0]>=2:
                mtce[day1[i][1]-start][day1[i][2]-1]+=1
                
        else: 
            if day1[i-1][0]<=1 and day1[i][0]>=2:
                mtce[day1[i][1]-start][day1[i][2]-1]+=1
    for i in range(1,len(day2)):
        if day2[i][2]==day2[i-1][2]:
            if day2[i-1][0]<=1 and day2[i][0]>=2:
                mtce[day2[i][1]-start][day2[i][2]-1]+=1
                
        else: 
            if day2[i-1][0]<=1 and day2[i][0]>=2:
                mtce[day2[i][1]-start][day2[i][2]-1]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i])/3)
    corr.append(stats.pearsonr(number[29:65],frequency)[0])
    rmse.append((mean_squared_error(number[29:65],frequency))**(0.5))
    da=[]
    da1=[]
    da2=[]
#print('WNP:')
#print(corr)
#print(rmse)
#print(number)
file=open('/dpvhome/dpv16/output/ECb1','a')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close
  

da=[]
da1=[]
da2=[]
corr=[]
rmse=[]
frequency=[1,2,2,7,7,5,10,2,7,3,4,6,6,7,5,6,0,1,3,2,2,2,3,5,2,1,3,7,1,7,5,2,2,2,3,7]
for ua in range(17,18):
    for i in range(len(a)):
        if (e[i]>=ua) and (180<c[i]<=270) and (0<=b[i]<=45):
            da.append([a[i],b[i],c[i],d[i],e[i],int(str(f[i]).split('-')[0]),int(str(f[i]).split('-')[1]),int(str(str(f[i]).split('-')[2]).split(' ')[0]),track[i]])
    for j in range(len(a1)):
        if (e1[j]>=ua) and (180<c1[j]<=270) and (0<=b1[j]<=45):
            da1.append([a1[j],b1[j],c1[j],d1[j],e1[j],int(str(f1[j]).split('-')[0]),int(str(f1[j]).split('-')[1]),int(str(str(f1[j]).split('-')[2]).split(' ')[0]),track1[j]])
    for m in range(len(a2)):
        if (e2[m]>=ua) and (180<c2[m]<=270) and (0<=b2[m]<=45):
            da2.append([a2[m],b2[m],c2[m],d2[m],e2[m],int(str(f2[m]).split('-')[0]),int(str(f2[m]).split('-')[1]),int(str(str(f2[m]).split('-')[2]).split(' ')[0]),track2[m]])
    
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    g1=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    g2=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    mday1=[[[]for i in range(12)]for i in range(numyear)]
    mday2=[[[]for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][3]==da[k][3]:
                aa+=1
        g[int((da[j][3]-tn)*4)]=[aa,da[j][5],da[j][6]]
        if aa>=2:
            mday[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][3]))
    for j in range(len(da1)):
        aa=0
        for k in range(len(da1)):
            if da1[j][3]==da1[k][3]:
                aa+=1
        g1[int((da1[j][3]-tn1)*4)]=[aa,da1[j][5],da1[j][6]]
        if aa>=2:
            mday1[int(da1[j][5])-start][int(da1[j][6])-1].append(int(da1[j][3]))
    for j in range(len(da2)):
        aa=0
        for k in range(len(da2)):
            if da2[j][3]==da2[k][3]:
                aa+=1
        g2[int((da2[j][3]-tn2)*4)]=[aa,da2[j][5],da2[j][6]]
        if aa>=2:
            mday2[int(da2[j][5])-start][int(da2[j][6])-1].append(int(da2[j][3]))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    mdayn1=[[]for i in range(numyear)]
    mdayn2=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            k1=set(mday1[i][j])
            k2=set(mday2[i][j])
            mdayn[i].append(len(k))
            mdayn1[i].append(len(k1))
            mdayn2[i].append(len(k2))
    #print(mdayn)
    day=[]
    day1=[]
    day2=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
        day1.append([max(g1[j][0] for j in range(j*4,(j+1)*4)),max(g1[j][1] for j in range(j*4,(j+1)*4)),max(g1[j][2] for j in range(j*4,(j+1)*4))])
        day2.append([max(g2[j][0] for j in range(j*4,(j+1)*4)),max(g2[j][1] for j in range(j*4,(j+1)*4)),max(g2[j][2] for j in range(j*4,(j+1)*4))])
    
   #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
                
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
    for i in range(1,len(day1)):
        if day1[i][2]==day1[i-1][2]:
            if day1[i-1][0]<=1 and day1[i][0]>=2:
                mtce[day1[i][1]-start][day1[i][2]-1]+=1
                
        else: 
            if day1[i-1][0]<=1 and day1[i][0]>=2:
                mtce[day1[i][1]-start][day1[i][2]-1]+=1
    for i in range(1,len(day2)):
        if day2[i][2]==day2[i-1][2]:
            if day2[i-1][0]<=1 and day2[i][0]>=2:
                mtce[day2[i][1]-start][day2[i][2]-1]+=1
                
        else: 
            if day2[i-1][0]<=1 and day2[i][0]>=2:
                mtce[day2[i][1]-start][day2[i][2]-1]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i])/3)
    corr.append(stats.pearsonr(number[29:65],frequency)[0])
    rmse.append((mean_squared_error(number[29:65],frequency))**(0.5))
    da=[]
    da1=[]
    da2=[]
#print('EP:')
#print(number)
#print(rmse)
#print(num)
file=open('/dpvhome/dpv16/output/ECb2','a')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close
  

da=[]
da1=[]
da2=[]
corr=[]
rmse=[]
frequency=[2,1,1,0,0,4,3,0,2,1,5,5,1,2,2,0,4,2,0,3,4,6,3,4,4,5,6,3,3,2,1,4,7,8,3,1]
for ua in range(17,18):
    for i in range(len(a)):
        if (e[i]>=ua) and (270<c[i]<=360) and (0<=b[i]<=45):
            da.append([a[i],b[i],c[i],d[i],e[i],int(str(f[i]).split('-')[0]),int(str(f[i]).split('-')[1]),int(str(str(f[i]).split('-')[2]).split(' ')[0]),track[i]])
    for j in range(len(a1)):
        if (e1[j]>=ua) and (270<c1[j]<=360) and (0<=b1[j]<=45):
            da1.append([a1[j],b1[j],c1[j],d1[j],e1[j],int(str(f1[j]).split('-')[0]),int(str(f1[j]).split('-')[1]),int(str(str(f1[j]).split('-')[2]).split(' ')[0]),track1[j]])
    for m in range(len(a2)):
        if (e2[m]>=ua) and (270<c2[m]<=360) and (0<=b2[m]<=45):
            da2.append([a2[m],b2[m],c2[m],d2[m],e2[m],int(str(f2[m]).split('-')[0]),int(str(f2[m]).split('-')[1]),int(str(str(f2[m]).split('-')[2]).split(' ')[0]),track2[m]])
    
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    g1=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    g2=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    mday1=[[[]for i in range(12)]for i in range(numyear)]
    mday2=[[[]for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][3]==da[k][3]:
                aa+=1
        g[int((da[j][3]-tn)*4)]=[aa,da[j][5],da[j][6]]
        if aa>=2:
            mday[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][3]))
    for j in range(len(da1)):
        aa=0
        for k in range(len(da1)):
            if da1[j][3]==da1[k][3]:
                aa+=1
        g1[int((da1[j][3]-tn1)*4)]=[aa,da1[j][5],da1[j][6]]
        if aa>=2:
            mday1[int(da1[j][5])-start][int(da1[j][6])-1].append(int(da1[j][3]))
    for j in range(len(da2)):
        aa=0
        for k in range(len(da2)):
            if da2[j][3]==da2[k][3]:
                aa+=1
        g2[int((da2[j][3]-tn2)*4)]=[aa,da2[j][5],da2[j][6]]
        if aa>=2:
            mday2[int(da2[j][5])-start][int(da2[j][6])-1].append(int(da2[j][3]))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    mdayn1=[[]for i in range(numyear)]
    mdayn2=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            k1=set(mday1[i][j])
            k2=set(mday2[i][j])
            mdayn[i].append(len(k))
            mdayn1[i].append(len(k1))
            mdayn2[i].append(len(k2))
    #print(mdayn)
    day=[]
    day1=[]
    day2=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
        day1.append([max(g1[j][0] for j in range(j*4,(j+1)*4)),max(g1[j][1] for j in range(j*4,(j+1)*4)),max(g1[j][2] for j in range(j*4,(j+1)*4))])
        day2.append([max(g2[j][0] for j in range(j*4,(j+1)*4)),max(g2[j][1] for j in range(j*4,(j+1)*4)),max(g2[j][2] for j in range(j*4,(j+1)*4))])
    
   #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
                
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
    for i in range(1,len(day1)):
        if day1[i][2]==day1[i-1][2]:
            if day1[i-1][0]<=1 and day1[i][0]>=2:
                mtce[day1[i][1]-start][day1[i][2]-1]+=1
                
        else: 
            if day1[i-1][0]<=1 and day1[i][0]>=2:
                mtce[day1[i][1]-start][day1[i][2]-1]+=1
    for i in range(1,len(day2)):
        if day2[i][2]==day2[i-1][2]:
            if day2[i-1][0]<=1 and day2[i][0]>=2:
                mtce[day2[i][1]-start][day2[i][2]-1]+=1
                
        else: 
            if day2[i-1][0]<=1 and day2[i][0]>=2:
                mtce[day2[i][1]-start][day2[i][2]-1]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i])/3)
    corr.append(stats.pearsonr(number[29:65],frequency)[0])
    rmse.append((mean_squared_error(number[29:65],frequency))**(0.5))
    da=[]
    da1=[]
    da2=[]
#print('NA:')
#print(number)
#print(rmse)
#print(num)
file=open('/dpvhome/dpv16/output/ECb3','a')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close


tn=0
tn1=23741
tn2=60265
#x=[1979+i for i in range(42)]
#r_ab=stats.pearsonr(x,frequency)[0]
#print(r_ab)
#print(len(frequency))
t = Dataset(r'/dpvhome/dpv16/CMIP6/EC-Earth/TC-NH_TRACK_EC-Earth3P-HR_highresSST-future_r2i1p1f1_gr_20150101-20501231.nc')
t2 = open_dataset(r'/dpvhome/dpv16/CMIP6/EC-Earth/TC-NH_TRACK_EC-Earth3P-HR_highresSST-future_r2i1p1f1_gr_20150101-20501231.nc',use_cftime=True)
date = t2.variables['time'][:]
f = list(np.array(date))
numyear=36
start=2015

#print(t.variables.keys())
a = t.variables['index'][:]
b = t.variables['lat_psl'][:]
c = t.variables['lon_psl'][:]
d = t.variables['time'][:]
e = t.variables['sfcWind'][:]#小于17剔除；100-180；5-40
k = t.variables['TRACK_ID']

track=[]
st=1
for i in range(len(a)-1):
    if a[i]==a[i+1]-1:
        track.append(st)
    else:
        track.append(st)
        st+=1
track.append(st)

t3 = Dataset(r'/dpvhome/dpv16/CMIP6/EC-Earth/TC-NH_TRACK_EC-Earth3P-HR_highresSST-future_r1i1p1f1_gr_20150101-20491231.nc')
t4 = open_dataset(r'/dpvhome/dpv16/CMIP6/EC-Earth/TC-NH_TRACK_EC-Earth3P-HR_highresSST-future_r1i1p1f1_gr_20150101-20491231.nc',use_cftime=True)
date1 = t4.variables['time'][:]
f1 = list(np.array(date1))
numyear1=35
start1=2015

#print(t.variables.keys())
a1 = t3.variables['index'][:]
b1 = t3.variables['lat_psl'][:]
c1 = t3.variables['lon_psl'][:]
d1 = t3.variables['time'][:]
e1 = t3.variables['sfcWind'][:]#小于17剔除；100-180；5-40
k1 = t3.variables['TRACK_ID']
#print(len(k))
#print(min(e[:1000]))
track1=[]
st1=1
for i in range(len(a1)-1):
    if a1[i]==a1[i+1]-1:
        track1.append(st1)
    else:
        track1.append(st1)
        st1+=1
track1.append(st1)

t5 = Dataset(r'/dpvhome/dpv16/CMIP6/EC-Earth/TC-NH_TRACK_EC-Earth3P-HR_highresSST-future_r3i1p1f1_gr_20150101-20501231.nc')
t6 = open_dataset(r'/dpvhome/dpv16/CMIP6/EC-Earth/TC-NH_TRACK_EC-Earth3P-HR_highresSST-future_r3i1p1f1_gr_20150101-20501231.nc',use_cftime=True)
date2 = t6.variables['time'][:]
f2 = list(np.array(date2))
numyear2=36
start2=2015

#print(t.variables.keys())
a2 = t5.variables['index'][:]
b2 = t5.variables['lat_psl'][:]
c2 = t5.variables['lon_psl'][:]
d2 = t5.variables['time'][:]
e2 = t5.variables['sfcWind'][:]#小于17剔除；100-180；5-40
k2 = t5.variables['TRACK_ID']
#print(len(k))
#print(min(e[:1000]))
track2=[]
st2=1
for i in range(len(a2)-1):
    if a2[i]==a2[i+1]-1:
        track2.append(st2)
    else:
        track2.append(st2)
        st2+=1
track2.append(st2)


da=[]
da1=[]
da2=[]
corr=[]
rmse=[]
frequency=[8,8,5,10,4,8,6,6,9,6,6,12,8,11,5,12,6,10,10,4,5,11,6,6,5,10,6,4,3,8,7,1,8,7,6,4]
for ua in range(17,18):
    for i in range(len(a)):
        if (e[i]>=ua) and (100<=c[i]<=180) and (0<=b[i]<=45):
            da.append([a[i],b[i],c[i],d[i],e[i],int(str(f[i]).split('-')[0]),int(str(f[i]).split('-')[1]),int(str(str(f[i]).split('-')[2]).split(' ')[0]),track[i]])
    for j in range(len(a1)):
        if (e1[j]>=ua) and (100<=c1[j]<=180) and (0<=b1[j]<=45):
            da1.append([a1[j],b1[j],c1[j],d1[j],e1[j],int(str(f1[j]).split('-')[0]),int(str(f1[j]).split('-')[1]),int(str(str(f1[j]).split('-')[2]).split(' ')[0]),track1[j]])
    for m in range(len(a2)):
        if (e2[m]>=ua) and (100<=c2[m]<=180) and (0<=b2[m]<=45):
            da2.append([a2[m],b2[m],c2[m],d2[m],e2[m],int(str(f2[m]).split('-')[0]),int(str(f2[m]).split('-')[1]),int(str(str(f2[m]).split('-')[2]).split(' ')[0]),track2[m]])
   
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    g1=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    g2=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    mday1=[[[]for i in range(12)]for i in range(numyear)]
    mday2=[[[]for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][3]==da[k][3]:
                aa+=1
        g[int((da[j][3]-tn)*4)]=[aa,da[j][5],da[j][6]]
        if aa>=2:
            mday[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][3]))
    for j in range(len(da1)):
        aa=0
        for k in range(len(da1)):
            if da1[j][3]==da1[k][3]:
                aa+=1
        g1[int((da1[j][3]-tn1)*4)]=[aa,da1[j][5],da1[j][6]]
        if aa>=2:
            mday1[int(da1[j][5])-start][int(da1[j][6])-1].append(int(da1[j][3]))
    for j in range(len(da2)):
        aa=0
        for k in range(len(da2)):
            if da2[j][3]==da2[k][3]:
                aa+=1
        g2[int((da2[j][3]-tn2)*4)]=[aa,da2[j][5],da2[j][6]]
        if aa>=2:
            mday2[int(da2[j][5])-start][int(da2[j][6])-1].append(int(da2[j][3]))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    mdayn1=[[]for i in range(numyear)]
    mdayn2=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            k1=set(mday1[i][j])
            k2=set(mday2[i][j])
            mdayn[i].append(len(k))
            mdayn1[i].append(len(k1))
            mdayn2[i].append(len(k2))
    #print(mdayn)
    day=[]
    day1=[]
    day2=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
        day1.append([max(g1[j][0] for j in range(j*4,(j+1)*4)),max(g1[j][1] for j in range(j*4,(j+1)*4)),max(g1[j][2] for j in range(j*4,(j+1)*4))])
        day2.append([max(g2[j][0] for j in range(j*4,(j+1)*4)),max(g2[j][1] for j in range(j*4,(j+1)*4)),max(g2[j][2] for j in range(j*4,(j+1)*4))])
    
   #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
                
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
    for i in range(1,len(day1)):
        if day1[i][2]==day1[i-1][2]:
            if day1[i-1][0]<=1 and day1[i][0]>=2:
                mtce[day1[i][1]-start][day1[i][2]-1]+=1
                
        else: 
            if day1[i-1][0]<=1 and day1[i][0]>=2:
                mtce[day1[i][1]-start][day1[i][2]-1]+=1
    for i in range(1,len(day2)):
        if day2[i][2]==day2[i-1][2]:
            if day2[i-1][0]<=1 and day2[i][0]>=2:
                mtce[day2[i][1]-start][day2[i][2]-1]+=1
                
        else: 
            if day2[i-1][0]<=1 and day2[i][0]>=2:
                mtce[day2[i][1]-start][day2[i][2]-1]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i])/3)

    da=[]
    da1=[]
    da2=[]
#print('WNP:')
#print(corr)
#print(rmse)
#print(number)
file=open('/dpvhome/dpv16/output/ECb1','a')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close
  

da=[]
da1=[]
da2=[]
corr=[]
rmse=[]
frequency=[1,2,2,7,7,5,10,2,7,3,4,6,6,7,5,6,0,1,3,2,2,2,3,5,2,1,3,7,1,7,5,2,2,2,3,7]
for ua in range(17,18):
    for i in range(len(a)):
        if (e[i]>=ua) and (180<c[i]<=270) and (0<=b[i]<=45):
            da.append([a[i],b[i],c[i],d[i],e[i],int(str(f[i]).split('-')[0]),int(str(f[i]).split('-')[1]),int(str(str(f[i]).split('-')[2]).split(' ')[0]),track[i]])
    for j in range(len(a1)):
        if (e1[j]>=ua) and (180<c1[j]<=270) and (0<=b1[j]<=45):
            da1.append([a1[j],b1[j],c1[j],d1[j],e1[j],int(str(f1[j]).split('-')[0]),int(str(f1[j]).split('-')[1]),int(str(str(f1[j]).split('-')[2]).split(' ')[0]),track1[j]])
    for m in range(len(a2)):
        if (e2[m]>=ua) and (180<c2[m]<=270) and (0<=b2[m]<=45):
            da2.append([a2[m],b2[m],c2[m],d2[m],e2[m],int(str(f2[m]).split('-')[0]),int(str(f2[m]).split('-')[1]),int(str(str(f2[m]).split('-')[2]).split(' ')[0]),track2[m]])
    
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    g1=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    g2=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    mday1=[[[]for i in range(12)]for i in range(numyear)]
    mday2=[[[]for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][3]==da[k][3]:
                aa+=1
        g[int((da[j][3]-tn)*4)]=[aa,da[j][5],da[j][6]]
        if aa>=2:
            mday[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][3]))
    for j in range(len(da1)):
        aa=0
        for k in range(len(da1)):
            if da1[j][3]==da1[k][3]:
                aa+=1
        g1[int((da1[j][3]-tn1)*4)]=[aa,da1[j][5],da1[j][6]]
        if aa>=2:
            mday1[int(da1[j][5])-start][int(da1[j][6])-1].append(int(da1[j][3]))
    for j in range(len(da2)):
        aa=0
        for k in range(len(da2)):
            if da2[j][3]==da2[k][3]:
                aa+=1
        g2[int((da2[j][3]-tn2)*4)]=[aa,da2[j][5],da2[j][6]]
        if aa>=2:
            mday2[int(da2[j][5])-start][int(da2[j][6])-1].append(int(da2[j][3]))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    mdayn1=[[]for i in range(numyear)]
    mdayn2=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            k1=set(mday1[i][j])
            k2=set(mday2[i][j])
            mdayn[i].append(len(k))
            mdayn1[i].append(len(k1))
            mdayn2[i].append(len(k2))
    #print(mdayn)
    day=[]
    day1=[]
    day2=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
        day1.append([max(g1[j][0] for j in range(j*4,(j+1)*4)),max(g1[j][1] for j in range(j*4,(j+1)*4)),max(g1[j][2] for j in range(j*4,(j+1)*4))])
        day2.append([max(g2[j][0] for j in range(j*4,(j+1)*4)),max(g2[j][1] for j in range(j*4,(j+1)*4)),max(g2[j][2] for j in range(j*4,(j+1)*4))])
    
   #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
                
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
    for i in range(1,len(day1)):
        if day1[i][2]==day1[i-1][2]:
            if day1[i-1][0]<=1 and day1[i][0]>=2:
                mtce[day1[i][1]-start][day1[i][2]-1]+=1
                
        else: 
            if day1[i-1][0]<=1 and day1[i][0]>=2:
                mtce[day1[i][1]-start][day1[i][2]-1]+=1
    for i in range(1,len(day2)):
        if day2[i][2]==day2[i-1][2]:
            if day2[i-1][0]<=1 and day2[i][0]>=2:
                mtce[day2[i][1]-start][day2[i][2]-1]+=1
                
        else: 
            if day2[i-1][0]<=1 and day2[i][0]>=2:
                mtce[day2[i][1]-start][day2[i][2]-1]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i])/3)

    da=[]
    da1=[]
    da2=[]
#print('EP:')
#print(number)
#print(rmse)
#print(num)
file=open('/dpvhome/dpv16/output/ECb2','a')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close
  

da=[]
da1=[]
da2=[]
corr=[]
rmse=[]
frequency=[2,1,1,0,0,4,3,0,2,1,5,5,1,2,2,0,4,2,0,3,4,6,3,4,4,5,6,3,3,2,1,4,7,8,3,1]
for ua in range(17,18):
    for i in range(len(a)):
        if (e[i]>=ua) and (270<c[i]<=360) and (0<=b[i]<=45):
            da.append([a[i],b[i],c[i],d[i],e[i],int(str(f[i]).split('-')[0]),int(str(f[i]).split('-')[1]),int(str(str(f[i]).split('-')[2]).split(' ')[0]),track[i]])
    for j in range(len(a1)):
        if (e1[j]>=ua) and (270<c1[j]<=360) and (0<=b1[j]<=45):
            da1.append([a1[j],b1[j],c1[j],d1[j],e1[j],int(str(f1[j]).split('-')[0]),int(str(f1[j]).split('-')[1]),int(str(str(f1[j]).split('-')[2]).split(' ')[0]),track1[j]])
    for m in range(len(a2)):
        if (e2[m]>=ua) and (270<c2[m]<=360) and (0<=b2[m]<=45):
            da2.append([a2[m],b2[m],c2[m],d2[m],e2[m],int(str(f2[m]).split('-')[0]),int(str(f2[m]).split('-')[1]),int(str(str(f2[m]).split('-')[2]).split(' ')[0]),track2[m]])
    
    g=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    g1=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    g2=[[0,0,0] for i in range(numyear*4*366)]#设置多一点
    mday=[[[]for i in range(12)]for i in range(numyear)]
    mday1=[[[]for i in range(12)]for i in range(numyear)]
    mday2=[[[]for i in range(12)]for i in range(numyear)]
    for j in range(len(da)):
        aa=0
        for k in range(len(da)):
            if da[j][3]==da[k][3]:
                aa+=1
        g[int((da[j][3]-tn)*4)]=[aa,da[j][5],da[j][6]]
        if aa>=2:
            mday[int(da[j][5])-start][int(da[j][6])-1].append(int(da[j][3]))
    for j in range(len(da1)):
        aa=0
        for k in range(len(da1)):
            if da1[j][3]==da1[k][3]:
                aa+=1
        g1[int((da1[j][3]-tn1)*4)]=[aa,da1[j][5],da1[j][6]]
        if aa>=2:
            mday1[int(da1[j][5])-start][int(da1[j][6])-1].append(int(da1[j][3]))
    for j in range(len(da2)):
        aa=0
        for k in range(len(da2)):
            if da2[j][3]==da2[k][3]:
                aa+=1
        g2[int((da2[j][3]-tn2)*4)]=[aa,da2[j][5],da2[j][6]]
        if aa>=2:
            mday2[int(da2[j][5])-start][int(da2[j][6])-1].append(int(da2[j][3]))
    #print(mday)
    mdayn=[[]for i in range(numyear)]
    mdayn1=[[]for i in range(numyear)]
    mdayn2=[[]for i in range(numyear)]
    for i in range(numyear):
        for j in range(12):
            k=set(mday[i][j])
            k1=set(mday1[i][j])
            k2=set(mday2[i][j])
            mdayn[i].append(len(k))
            mdayn1[i].append(len(k1))
            mdayn2[i].append(len(k2))
    #print(mdayn)
    day=[]
    day1=[]
    day2=[]
    for j in range(numyear*366):
        day.append([max(g[j][0] for j in range(j*4,(j+1)*4)),max(g[j][1] for j in range(j*4,(j+1)*4)),max(g[j][2] for j in range(j*4,(j+1)*4))])
        day1.append([max(g1[j][0] for j in range(j*4,(j+1)*4)),max(g1[j][1] for j in range(j*4,(j+1)*4)),max(g1[j][2] for j in range(j*4,(j+1)*4))])
        day2.append([max(g2[j][0] for j in range(j*4,(j+1)*4)),max(g2[j][1] for j in range(j*4,(j+1)*4)),max(g2[j][2] for j in range(j*4,(j+1)*4))])
    
   #print(day)
    mtce=[[0 for i in range(12)]for i in range(numyear)]
    for i in range(1,len(day)):
        if day[i][2]==day[i-1][2]:
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
                
        else: 
            if day[i-1][0]<=1 and day[i][0]>=2:
                mtce[day[i][1]-start][day[i][2]-1]+=1
    for i in range(1,len(day1)):
        if day1[i][2]==day1[i-1][2]:
            if day1[i-1][0]<=1 and day1[i][0]>=2:
                mtce[day1[i][1]-start][day1[i][2]-1]+=1
                
        else: 
            if day1[i-1][0]<=1 and day1[i][0]>=2:
                mtce[day1[i][1]-start][day1[i][2]-1]+=1
    for i in range(1,len(day2)):
        if day2[i][2]==day2[i-1][2]:
            if day2[i-1][0]<=1 and day2[i][0]>=2:
                mtce[day2[i][1]-start][day2[i][2]-1]+=1
                
        else: 
            if day2[i-1][0]<=1 and day2[i][0]>=2:
                mtce[day2[i][1]-start][day2[i][2]-1]+=1
    number=[]
    for i in range(numyear):
        number.append(sum(mtce[i])/3)

    da=[]
    da1=[]
    da2=[]
#print('NA:')
#print(number)
#print(rmse)
#print(num)
file=open('/dpvhome/dpv16/output/ECb3','a')
for i in mtce:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close




