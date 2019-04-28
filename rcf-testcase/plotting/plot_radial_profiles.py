#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 13:39:50 2018

@author: max
"""
# Plot the depth-average of viscosity from CitcomS and ASPECT calculations

import numpy as np
import matplotlib.pyplot as plt
import glob as glob

time = []
temperature = []
depth = []
labels=[]

files = glob.glob('../results/depth_average*')


def load_depthaverage(filename):
    depth_averages = np.loadtxt(filename)
    da=dict()
    da['time'] = depth_averages[:,0]
    da['temperature'] = depth_averages[:,2]
    da['depth'] = depth_averages[:,1]
    da['label'] = filename[filename.find('aspect'):]
    return da

files = sorted(glob.glob('../results/depth_average*.txt'))
depth_averages=[]
for file in files:
    depth_averages.append( load_depthaverage(file) )


# CitcomS averages from FESD Case05 final timestep
# viscosity profile from CitcomS
citcoms_data = np.loadtxt("citcoms_results/arr.horiz_avg.0.29090")
citcoms_r = citcoms_data[:,0]
citcoms_visc_nd = citcoms_data[:,4]
citcoms_T = citcoms_data[:,1]*2500.

plt.figure()
for da in depth_averages:
    target_time = 1.5e8;
    times = np.unique(da['time']);
    ii=np.argmin(np.abs(times-target_time))
    pmask = da['time'] == times[ii]
    
    plt.plot( da['temperature'][pmask],da['depth'][pmask] ,label=da['label']+' {:.0f} Myr'.format(times[ii]/1e6))


plt.plot(citcoms_T,(1-citcoms_r)*6336000.,':',label='citcoms final')
plt.ylabel('Depth (m)')
plt.xlabel('Temperature (K)')
plt.legend()
plt.gca().invert_yaxis()
plt.show()