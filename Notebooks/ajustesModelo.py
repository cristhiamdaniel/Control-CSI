#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:54:51 2022

@author: cristhiamdaniel
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Importar datos

path = "./Data/outputPV.txt"
# Creacion de un Dataframe
df = pd.read_csv(path, header=None)
# Insetar las columnas de tension y corriente
df.columns = ["V_pv","I_pv"]
# Insertar la columna de potencia
df.insert(2,"P_pv",df["V_pv"]*df["I_pv"])
    


# Funcion obtencion de puntos de maxima potencia
def PMM():
    df_mask = df['P_pv']==df['P_pv'].max()
    filtered_df = df[df_mask]
    
    return filtered_df

# Funcion para obtener el indice del PMM
def index_pmm():
    pmm = PMM()
    index = pmm.index.values[0]
    return index

# Funcion para obtener las curvas caracteristicas
# VI - PV
def curvaCaracteristica():
    global vpp, ipp, ppp
    pmm = PMM()
    v = df.V_pv
    i = df.I_pv
    p = df.P_pv
    vpp = pmm['V_pv']
    ipp = pmm['I_pv']
    ppp = pmm['P_pv']
    
    fig, ax1 = plt.subplots()
    
    color = "tab:red"
    ax1.set_xlabel("Tension (V)")
    ax1.set_ylabel("Corriente (A)", color=color)
    ax1.plot(v, i, color=color)
    ax1.plot(vpp, ipp, marker="o", color="black")
    ax1.tick_params(axis="y", labelcolor=color)
    ax1.set_xlim(0,200)
    ax1.set_ylim(0,40)
    ax2 = ax1.twinx() 
    
    color = "tab:blue"
    ax2.set_ylabel("Potencia (W)", color=color)  
    ax2.plot(v, p, color=color)
    ax2.plot(vpp, ppp, marker="o", color="black")
    ax2.tick_params(axis="y", labelcolor=color)
    ax2.set_xlim(0,200)
    ax2.set_ylim(0,4000)
    
    fig.tight_layout() 
    plt.grid()
  
    plt.show()

# Funcion para calcular el R-cuadrado ajustado
def adjR(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    results['r_squared'] = 1- (((1-(ssreg/sstot))*(len(y)-1))/(len(y)-degree-1))

    return results

# Funcion para graficar la curva ajustada
def curvasAjuste(x,y,a,b,degree):
    #fit polynomial models 
    
    model = np.poly1d(np.polyfit(x,y, degree))
           
    #create scatterplot
    polyline = np.linspace(a,b)
    plt.scatter(x, y)
    
    #add fitted polynomial lines to scatterplot 
    plt.plot(polyline, model(polyline), color='red', label= f'Funcion grado {degree}')
      
    
    plt.legend()
    plt.ylim(0,4500)
    plt.grid()
    plt.show()

# funcion para calcular el modelo de la curva ajustada
def model(x,y,degree):
    model = np.poly1d(np.polyfit(x, y, degree))
    return model
    


def main():
    global df1, df2, model1, model2
    
    i = index_pmm()
    
    # V_pv, I_pv, P_pv = 149.76,  25.944,  3885.3734
    
    rangos = [10, 20, 30, 40, 50]
    grados = [3,5,7]
    model1 = []
    model2 = []
    r2_1 = []
    r2_2 = []
    
    for g in grados:
        for r in rangos:   
            df1 = df.iloc[:i+r]
            df2 = df.iloc[i-r:]
            
            v1 = df1.V_pv
            p1 = df1.P_pv
            v2 = df2.V_pv
            p2 = df2.P_pv
               
            m1 = model(v1,p1,g)
            m2 = model(v2,p2,g)
                
            model1.append(m1)
            model2.append(m2)
            
            ad1 = adjR(v1, p1, g)
            ad2 = adjR(v2, p2, g)
            
            r2_1.append(ad1)
            r2_2.append(ad2)
            
    for x in range(len(model2)):
        print(f"modelo {x} :")
        print(model2[x])
        print()
    
    
    

if __name__ == "__main__":
    main()