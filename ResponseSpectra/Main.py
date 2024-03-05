# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:38:57 2024

@author: Ashish Bahuguna

"""
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib.pyplot as plt
from NewmarkBetaMethod import *
from ProcessNGA import *
import sys
import os
import time as t
from ResponseSpectra import *
#%%
start_time = t.time()
Tn = np.linspace(0.0, 5.0, num=100)

files = np.array(['RSN1063_NORTHR_RRS318.AT2', 'RSN765_LOMAP_G01090.AT2'])

# desc, npts, dt, time, inp_acc = processNGAfile(p, scalefactor=None)
factor  = 386.089   # g in in/s2
xi =np.array([0.02, 0.05, 0.1, 0.2])
# xi =np.array([0.05])
method = 'Linear' # option Average or Linear

for p in files:
    desc, npts, dt, time, inp_acc = processNGAfile(p, scalefactor=None)
    fig, axs = plt.subplots(5, 1, figsize=(10, 20))  # Create one figure with five subplots
    
    for v in xi:
        Sa, T, Sd, Sv, PSA, PSV = RespSpec(Tn, dt, v, factor, inp_acc, method, start_time)
        index_0_3 = np.abs(T - 0.3).argmin()
        
        axs[0].plot(T, Sa, label='$\\xi = $' + str(v * 100)+'%')  # Plot Sa
        axs[0].set_ylabel("Sa (g)")
        if v==0.1:
            axs[0].axvline(0.3, color='blue', linestyle='--', linewidth=1)  # Add vertical line at 0.3
            axs[0].axhline(Sa[index_0_3], color='blue', linestyle='--', linewidth=1)  # Add vertical line at 0.3
            axs[0].text(0.2, 0.5, f'T={T[index_0_3]:.2f} s', color='blue', fontsize=10, ha='left', va='bottom')
            axs[0].text(2, Sa[index_0_3], f'Sa={Sa[index_0_3]:.2f} g', color='blue', fontsize=10, ha='center', va='bottom')
    
        axs[1].plot(T, Sv, label='$\\xi = $' + str(v * 100)+'%')  # Plot Sv
        if v==0.1:
            axs[1].axvline(0.3, color='blue', linestyle='--', linewidth=1)  # Add vertical line at 0.3
            axs[1].axhline(Sv[index_0_3], color='blue', linestyle='--', linewidth=1)  # Add vertical line at 0.3
            axs[1].text(2, Sv[index_0_3], f'Sv={Sv[index_0_3]:.2f} in/s', color='blue', fontsize=10, ha='center', va='bottom')
    
        axs[1].set_ylabel("Sv (in/s)")
        
        axs[2].plot(T, Sd, label='$\\xi = $' + str(v * 100)+'%')  # Plot Sd
        if v==0.1:
            axs[2].axvline(0.3, color='blue', linestyle='--', linewidth=1)  # Add vertical line at 0.3
            axs[2].axhline(Sd[index_0_3], color='blue', linestyle='--', linewidth=1)  # Add vertical line at 0.3
            axs[2].text(2, Sd[index_0_3], f'Sd={Sd[index_0_3]:.2f} in', color='blue', fontsize=10, ha='center', va='bottom')
    
        axs[2].set_ylabel("Sd (in)")
        
        
        axs[3].plot(T, PSA, label='$\\xi = $' + str(v * 100)+'%')  # Plot PSA
        if v==0.1:
            axs[3].axvline(0.3, color='blue', linestyle='--', linewidth=1)  # Add vertical line at 0.3
            axs[3].axhline(PSA[index_0_3], color='blue', linestyle='--', linewidth=1)  # Add vertical line at 0.3
            axs[3].text(2, PSA[index_0_3], f'PSA={PSA[index_0_3]:.2f} g', color='blue', fontsize=10, ha='center', va='bottom')
        axs[3].set_ylabel("PSA (g)")
        
        axs[4].plot(T, PSV, label='$\\xi = $' + str(v * 100)+'%')  # Plot PSV
        if v==0.1:
            axs[4].axvline(0.3, color='blue', linestyle='--', linewidth=1)  # Add vertical line at 0.3
            axs[4].axhline(PSV[index_0_3], color='blue', linestyle='--', linewidth=1)  # Add vertical line at 0.3
            axs[4].text(2, PSV[index_0_3], f'PSV={PSV[index_0_3]:.2f} in/s', color='blue', fontsize=10, ha='center', va='bottom')
    
        axs[4].set_ylabel("PSV (in/s)")
    # Setting labels, limits, legends, and titles for each subplot
    for i in range(5):
        axs[i].set_xlabel("Period (s)")
        axs[i].grid(color='grey', linestyle='--', linewidth=0.5)
        axs[i].set_xlim([0., 5.0])
        axs[i].legend()
        axs[i].set_title(f'{desc} ')
    
    plt.tight_layout()
    plt.show()
    
