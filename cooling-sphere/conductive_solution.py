#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 16:42:42 2018

@author: max
"""

# analyze conductive solutions
import numpy as np
import matplotlib.pyplot as plt
import glob as glob

ri = 3481000.
ro = 6336000.
Ti = 1973.
To = 973.
c1 = (Ti-To)/(1-ri/ro)*ri
c2 = Ti-(Ti-To)/(1-ri/ro)
r = np.linspace(ri,ro)
T = c1/r+c2
dtdr_cmb = -c1/ri**2
kThermal = 4.7
qcmb = 4.*np.pi*ri**2 * kThermal *dtdr_cmb


def load_depthaverage(filename):
    depth_averages = np.loadtxt(filename)
    da=dict()
    da['time'] = depth_averages[:,0]
    da['temperature'] = depth_averages[:,2]
    da['depth'] = depth_averages[:,1]
    da['label'] = filename
    return da

def linestyle(filename):
    style=''
    if( filename.find('head') != -1 ):
        style += 'k'
    else:
        style += 'r'
    if( filename.find('gr3') != -1 ):
        style += '-'
    elif( filename.find('gr4') != -1 ):
        style +=  '.'
    elif( filename.find('gr5') != -1):
        style += '--'
    return style

files = glob.glob('results/depth_average*.txt')
depth_averages=[]
for file in files:
    depth_averages.append( load_depthaverage(file) )

plt.figure(figsize=(8,8))
for da in depth_averages:
    # select only the entries corresponding to the last time.
    times = np.unique(da['time'])
    pmask = da['time'] == times[-1]
    style = linestyle( da['label'] )
    plt.plot(ro-da['depth'][pmask],da['temperature'][pmask],style,label=da['label'] + ', time ={:e}'.format(times[i]))

plt.plot(r,T,'g+',label='analytic')

plt.legend()
plt.savefig('T_vs_r.eps')
plt.savefig('T_vs_r.png')
plt.show()
print("Thermal diffusion timescale {:e} years".format((ro-ri)**2/(1e-6)/3.15e7)) #in years


def load_statistics(filename):
    s=dict()
    sol = np.loadtxt(filename,usecols=(1,14,17,18),unpack=False)
    s['time']=sol[:,0]
    s['Tavg']=sol[:,1]
    s['qbtm']=sol[:,2]
    s['qsurf']=sol[:,3]
    s['label']=filename
    return s

files = glob.glob('results/statistics*')
statistics = []
for file in files:
    statistics.append( load_statistics(file) )


f,(ax1,ax2) = plt.subplots(1,2)
f.set_size_inches([16,8])
for s in statistics:
    ax1.plot(s['time'],-s['qbtm'],linestyle(s['label']),label=s['label'])
    ax2.plot(s['time'],s['qsurf'],linestyle(s['label']),label=s['label']) 
    

ax1.plot([0,2e11],[-qcmb,-qcmb],label='Analytic')
ax1.set_ylim([0,1e12])
ax1.set_xlim([0, 2e11])
ax1.set_ylabel('Heat Flow (W)')
ax1.set_xlabel('time (year)')

ax2.plot([0,2e11],[-qcmb,-qcmb],label='Analytic')
ax2.set_ylim([0,1e12])
ax2.set_xlim([0,2e11])
ax2.legend()
plt.savefig('heat_flow_vs_time.eps')
plt.savefig('heat_flow_vs_time.png')
plt.show()


