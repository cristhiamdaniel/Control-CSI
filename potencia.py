#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 11:58:40 2022

@author: cristhiamdaniel
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importamos los datos:
path = "./Data/outputPV.txt"
df = pd.read_csv(path, header=None)
df.columns = ["V_pv","I_pv"]
df.insert(2,"P_pv",df["V_pv"]*df["I_pv"])

# Puntos de maxima potencia
def PMM():
    df_mask = df['P_pv']== df['P_pv'].max()
    filtered_df = df[df_mask]
    return filtered_df

df1 = df.iloc[:149755]

def curvasAjuste():
    #fit polynomial models up to degree 5
    model1 = np.poly1d(np.polyfit(df1.V_pv, df1.P_pv, 1))
    model2 = np.poly1d(np.polyfit(df1.V_pv, df1.P_pv, 2))
    model3 = np.poly1d(np.polyfit(df1.V_pv, df1.P_pv, 3))
    model4 = np.poly1d(np.polyfit(df1.V_pv, df1.P_pv, 4))
    model5 = np.poly1d(np.polyfit(df1.V_pv, df1.P_pv, 5))
    
    
    #create scatterplot
    polyline = np.linspace(0, 150, 1000)
    plt.scatter(df1.V_pv, df1.P_pv)
    
    #add fitted polynomial lines to scatterplot 
    plt.plot(polyline, model1(polyline), color='green', label= 'Funcion grado 1')
    plt.plot(polyline, model2(polyline), color='red', label= 'Funcion grado 2')
    plt.plot(polyline, model3(polyline), color='purple', label= 'Funcion grado 3')
    plt.plot(polyline, model4(polyline), color='blue', label= 'Funcion grado 4')
    plt.plot(polyline, model5(polyline), color='orange', label= 'Funcion grado 5')
    
    plt.legend()
    plt.grid()
    #plt.savefig("./imagenes/curvaajuste.png")
    plt.show()
    
if __name__ == "__main__":
    pmm = PMM()
    print(pmm)
    curvasAjuste()