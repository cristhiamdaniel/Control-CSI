#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 21:16:04 2022

@author: cristhiamdaniel
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importamos los datos de Matlab
#df = pd.read_csv("dataSunset72X.csv", header=None)
df = pd.read_csv("myFile.txt", header=None)
df.columns = ["V_pv","I_pv"]
df.insert(2,"P_pv",df["V_pv"]*df["I_pv"])


def curvaCaracteristica():
    v = df.V_pv
    i = df.I_pv
    p = df.P_pv
    
    fig, ax1 = plt.subplots()
    
    color = "tab:red"
    ax1.set_xlabel("Tension (V)")
    ax1.set_ylabel("Corriente (A)", color=color)
    ax1.plot(v, i, color=color)
    ax1.tick_params(axis="y", labelcolor=color)
    ax1.set_xlim(0,50)
    ax1.set_ylim(0,10)
    ax2 = ax1.twinx() 
    
    color = "tab:blue"
    ax2.set_ylabel("Potencia (W)", color=color)  
    ax2.plot(v, p, color=color)
    ax2.tick_params(axis="y", labelcolor=color)
    ax2.set_xlim(0,50)
    ax2.set_ylim(0,350)
    
    fig.tight_layout() 
    plt.grid()
    
    
    plt.show()

plt.plot(df.V_pv, df.I_pv)
plt.plot(37.44, 8.6684, marker ="o", color='red')
plt.xlim(0,50)
plt.ylim(0,10)
plt.grid()
plt.show()

x = df.P_pv.max()
r = df.loc[df.P_pv == x]
print(r)