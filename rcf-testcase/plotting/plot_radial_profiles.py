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


# load the citcoms time fle
citcoms_prefix = '../r660-zzs-citcoms/R660_ZZS'
citcoms_time = np.loadtxt(citcoms_prefix+'.time')
citcoms_stepnum = citcoms_time[:,0]
citcoms_tnd = citcoms_time[:,1]
Rearth = 6.371e6;
kappa = 1.0e-6;
seconds_in_Myr = 3.1556926e13;
dimensional_factor = Rearth**2/kappa/seconds_in_Myr;
citcoms_time_myr = dimensional_factor * citcoms_tnd
citcoms_time_yr = dimensional_factor * citcoms_tnd*1.0e6


def load_citcoms_depthaverage(filename):
    da = dict()
    # CitcomS averages from FESD Case05 final timestep
    # viscosity profile from CitcomS
    citcoms_data = np.loadtxt(filename)
    da['depth'] = Rearth*(1.0-citcoms_data[:,0])
    da['visc'] = citcoms_data[:,4]
    da['temperature'] = citcoms_data[:,1]*2500.
    da['filename'] = filename
    # This pulls out the step number from a citcoms file name
    da['stepnum'] = int(filename[(filename.rfind('.')+1):])
    return da

citcoms_files = sorted(glob.glob(citcoms_prefix+'.horiz_avg*'))
citcoms_da = []
for file in citcoms_files:
    citcoms_da.append(load_citcoms_depthaverage(file))

citcoms_file_tyr = []
for ii in range(len(citcoms_da)):
    da = citcoms_da[ii]
    idx = np.argwhere(citcoms_stepnum==da['stepnum'])[0][0]
    citcoms_file_tyr.append(citcoms_time_yr[idx])
citcoms_file_tyr = np.array(citcoms_file_tyr)


def comparison_figure(target_time,thresh=1e7):
    plt.figure()
    for da in depth_averages:
        times = np.unique(da['time']);
        ii=np.argmin(np.abs(times-target_time))
        pmask = da['time'] == times[ii]
        if(np.abs(times[ii]-target_time)<=thresh):
            plt.plot( da['temperature'][pmask],da['depth'][pmask] ,label=da['label']+' {:.0f} Myr'.format(times[ii]/1e6))
    ii = np.argmin(np.abs(citcoms_file_tyr-target_time))
    plt.plot(citcoms_da[ii]['temperature'],citcoms_da[ii]['depth'],label='citcoms {:.0f} Myr'.format(citcoms_file_tyr[ii]/1e6))
    plt.legend()
    plt.ylabel('Depth (m)')
    plt.xlabel('Temperature (K)')
    plt.gca().invert_yaxis()
    plt.show()
    
comparison_figure(0)
comparison_figure(0.74e8)
comparison_figure(1.5e8)
comparison_figure(2.56e8,thresh=1e7)
comparison_figure(4.0   e8,thresh=1e7)