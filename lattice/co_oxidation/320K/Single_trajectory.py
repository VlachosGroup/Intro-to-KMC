# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:48:34 2016

@author: mpnun
"""

import os
import sys

sys.path.append('/home/vlachos/mpnunez/bin/Zacros-Wrapper/PythonCode')

import Core as zw

''' ------------ User input section ------------ '''
RunPath = '/home/vlachos/wangyf/CO_oxidation/23'
''' -------------------------------------------- '''

''' Set up data '''
y = zw.KMC_Run()
y.Path = RunPath
y.ReadAllOutput()

''' Analyze '''
n_Pd = 48 * 48                                                      # number of Pd atoms for normalization
y.PlotSurfSpecVsTime(site_norm = n_Pd)                              # Plots species coverages
y.PlotGasSpecVsTime()                                               # Plots total counts of gas species
y.PlotElemStepFreqs(site_norm = n_Pd, time_norm = True)             # Plots elementary step frequencies
y.PlotLattice()                                                     # Plots a picture of the bare lattice
y.LatticeMovie()                                                    # creates a subfolder and makes images of each snapshot