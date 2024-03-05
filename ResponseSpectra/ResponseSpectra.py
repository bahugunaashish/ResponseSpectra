# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:48:45 2024

@author: abahugu
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

def RespSpec(Tn, dt, xi, factor, inp_acc, method, start_time):
    
    Sd = np.array([]) 
    Sv = np.array([])
    Sa = np.array([])
    Ts = np.array([])
    PSA = Sd
    PSV = Sd
    # print('Period (s)       PGA (g)')
    for T in Tn: 
    # Show progress indicator
        sys.stdout.write(f'>>----> Processing elapsed_time = {(t.time() - start_time):.2f} sec')
        sys.stdout.flush()
        t.sleep(0.5)
        # Clear the entire line
        sys.stdout.write("\r\033[K")
        sys.stdout.flush()
        t.sleep(0.1)
        # print('Time period', T)
        
        
        omega = 2*np.pi/T      # Natural Frequency
        m = 1       
        k = omega**2*m
        c = 2 * xi * omega*m 
        p = -m*inp_acc*factor

        U, V, A, dynStiffness, a, b, ti = NewmarkBetaMethod(m, k, c, p, dt, method, flag =1)
        
        Sa = np.append(Sa, max(abs(A))/factor)
        Sd = np.append(Sd, max(abs(U))) 
        Sv = np.append(Sv, max(abs(V)))
        Ts = np.append(Ts, T)
        Sd[0] = 0
        # Sv[0]= 0
        Sa[0]= max(abs(inp_acc))
        PSV = np.append(PSV, (2 * np.pi / T)*max(abs(U)))
        PSV[0] = 0 
        PSA = np.append(PSA, ((2 * np.pi / T)**2 *max(abs(U)))/factor)
        PSA[0] = max(abs(inp_acc))
  l      # print(f'{T:.3f}         {max(abs(A)):.3f}')
    
    return Sa, Ts, Sd, Sv, PSA, PSV
