# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:48:34 2016

@author: mpnun
"""

import os
import sys

HomePath = os.path.expanduser('~')
sys.path.append(os.path.join(HomePath, 'Programs', 'Zacros-Wrapper'))
sys.path.append(os.path.join(HomePath, 'Programs', 'pMuTT'))
import zacros_wrapper as zw


''' ------------ User input section ------------ '''
RunPath = os.getcwd()
''' -------------------------------------------- '''

''' Set up data '''
y = zw.kmc_traj()
y.Path = RunPath
y.ReadAllOutput(build_lattice = True)

''' Analyze '''
n_Pd = 48 * 48                                                      # number of Pd atoms for normalization
y.PlotSurfSpecVsTime(site_norm = n_Pd)                              # Plots species coverages
y.PlotGasSpecVsTime()                                               # Plots total counts of gas species
y.PlotElemStepFreqs(site_norm = n_Pd, time_norm = True)             # Plots elementary step frequencies
y.PlotLattice()                                                     # Plots a picture of the bare lattice
y.LatticeMovie()                                                    # creates a subfolder and makes images of each snapshot