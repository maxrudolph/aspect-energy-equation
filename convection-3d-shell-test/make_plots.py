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
    if( filename.find('_3') != -1 ):
        style += '-'
    elif( filename.find('_4') != -1 ):
        style +=  ':'
    elif( filename.find('_5') != -1):
        style += '--'
    return style

files = glob.glob('results/depth_average*.txt')
depth_averages=[]
for file in files:
    depth_averages.append( load_depthaverage(file) )

plt.figure(figsize=(8,8))

tplot=2.5e9

for da in depth_averages:
    # select only the entries corresponding to the last time.
    times = np.unique(da['time'])
    idx = np.argmin(np.abs(times-tplot))
    pmask = da['time'] == times[idx]
    style = linestyle( da['label'] )
    plt.plot(ro-da['depth'][pmask],da['temperature'][pmask],style,label=da['label'] + ', time ={:e}'.format(times[idx]))



plt.legend()
plt.savefig('T_vs_r.eps')
plt.savefig('T_vs_r.png')
plt.show()
print("Thermal diffusion timescale {:e} years".format((ro-ri)**2/(1e-6)/3.15e7)) #in years


def load_statistics(filename):
    s=dict()
    sol = np.loadtxt(filename,usecols=(1,14,17,18,4,11),unpack=False)
    s['time']=sol[:,0]
    s['Tavg']=sol[:,1]
    s['qbtm']=sol[:,2]
    s['qsurf']=sol[:,3]
    s['ndof']=sol[:,4]
    s['vrms']=sol[:,5]
    s['label']=filename
    return s

files = glob.glob('results/statistics*')
statistics = []
for file in files:
    statistics.append( load_statistics(file) )


f,(ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,1)
f.set_size_inches([8,20])
for s in statistics:
    ax1.plot(s['time'],-s['qbtm'],linestyle(s['label']),label=s['label']+' CMB HF')
    ax1.plot(s['time'],s['qsurf'],linestyle(s['label']),label=s['label']+' SURF HF') 
    ax2.plot(s['time'],(s['qsurf']- -s['qbtm'])/s['qsurf'],linestyle(s['label']),label=s['label']+' fractional imbalance' )
    ax3.plot(s['time'],s['ndof'],linestyle(s['label']),label=s['label'])
    ax4.plot(s['time'],s['Tavg'],linestyle(s['label']),label=s['label'])
    ax5.plot(s['time'],s['vrms'],linestyle(s['label']),label=s['label'])

ax1.set_ylabel('Heat Flow (W)')
ax1.set_xlabel('time (year)')
ax2.set_ylabel('|(qsurf-qcmb)|/qsurf')
ax3.set_ylabel('# Stokes DOF')
ax4.set_ylabel('Average Temperature')
ax5.set_ylabel('RMS velocity')
ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()
ax5.legend()
plt.savefig('heat_flow_vs_time.eps')
plt.savefig('heat_flow_vs_time.png')
plt.show()


