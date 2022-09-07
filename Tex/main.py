#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 12:29:39 2022

@author: cristhiamdaniel
"""

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

path = "/home/cristhiamdaniel/Developer/Github/Control-CSI/Data/outputPV.txt"
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

""" 
Modelos del primer trozo:
    
modelo 0 :
            3           2
-0.0003277 x + 0.05629 x + 25.34 x + 25.09

modelo 1 :
            3           2
-0.0003279 x + 0.05635 x + 25.34 x + 25.11

modelo 2 :
            3          2
-0.0003282 x + 0.0564 x + 25.33 x + 25.14

modelo 3 :
            3           2
-0.0003285 x + 0.05645 x + 25.33 x + 25.16

modelo 4 :
            3          2
-0.0003287 x + 0.0565 x + 25.33 x + 25.19

modelo 5 :
            5             4            3          2
-9.224e-08 x + 2.863e-05 x - 0.003155 x + 0.1441 x + 25.48 x + 10.2

modelo 6 :
           5             4            3          2
-9.23e-08 x + 2.865e-05 x - 0.003158 x + 0.1442 x + 25.48 x + 10.21

modelo 7 :
            5             4            3          2
-9.237e-08 x + 2.867e-05 x - 0.003161 x + 0.1444 x + 25.48 x + 10.22

modelo 8 :
            5             4            3          2
-9.243e-08 x + 2.869e-05 x - 0.003163 x + 0.1445 x + 25.48 x + 10.23

modelo 9 :
           5             4            3          2
-9.25e-08 x + 2.871e-05 x - 0.003166 x + 0.1446 x + 25.47 x + 10.24

modelo 10 :
            7            6             5             4            3
-1.481e-11 x + 6.51e-09 x - 1.139e-06 x + 0.0001002 x - 0.004614 x
           2
 + 0.1031 x + 27.05 x + 2.176

modelo 11 :
            7             6            5             4            3
-1.482e-11 x + 6.514e-09 x - 1.14e-06 x + 0.0001002 x - 0.004618 x
           2
 + 0.1032 x + 27.05 x + 2.178

modelo 12 :
            7             6            5             4            3
-1.483e-11 x + 6.518e-09 x - 1.14e-06 x + 0.0001003 x - 0.004621 x
           2
 + 0.1033 x + 27.05 x + 2.18

modelo 13 :
            7             6             5             4            3
-1.484e-11 x + 6.522e-09 x - 1.141e-06 x + 0.0001004 x - 0.004625 x
           2
 + 0.1034 x + 27.05 x + 2.182

modelo 14 :
            7             6             5             4            3
-1.484e-11 x + 6.526e-09 x - 1.142e-06 x + 0.0001005 x - 0.004628 x
           2
 + 0.1035 x + 27.05 x + 2.185
"""   

"""
Modelos del segundo trozo:
    
modelo 0 :
           3           2
-0.005694 x - 0.04569 x + 412.8 x - 3.782e+04

modelo 1 :
           3           2
-0.005703 x - 0.04091 x + 411.9 x - 3.777e+04

modelo 2 :
           3           2
-0.005712 x - 0.03614 x + 411.1 x - 3.772e+04

modelo 3 :
           3           2
-0.005721 x - 0.03136 x + 410.2 x - 3.767e+04

modelo 4 :
          3           2
-0.00573 x - 0.02659 x + 409.4 x - 3.762e+04

modelo 5 :
           5            4         3         2
-4.23e-06 x + 0.004113 x - 1.586 x + 300.3 x - 2.787e+04 x + 1.018e+06

modelo 6 :
            5            4         3         2
-4.226e-06 x + 0.004109 x - 1.585 x + 300.1 x - 2.785e+04 x + 1.018e+06

modelo 7 :
            5            4         3         2
-4.222e-06 x + 0.004105 x - 1.583 x + 299.9 x - 2.783e+04 x + 1.017e+06

modelo 8 :
            5            4         3         2
-4.218e-06 x + 0.004101 x - 1.582 x + 299.6 x - 2.781e+04 x + 1.016e+06

modelo 9 :
            5            4         3         2
-4.213e-06 x + 0.004098 x - 1.581 x + 299.4 x - 2.779e+04 x + 1.015e+06

modelo 10 :
           7             6            5          4         3
3.314e-09 x - 4.157e-06 x + 0.002226 x - 0.6593 x + 116.6 x
             2
 - 1.23e+04 x + 7.167e+05 x - 1.781e+07

modelo 11 :
           7             6            5          4         3
3.313e-09 x - 4.156e-06 x + 0.002226 x - 0.6591 x + 116.5 x
              2
 - 1.229e+04 x + 7.165e+05 x - 1.78e+07

modelo 12 :
           7             6            5          4         3
3.312e-09 x - 4.155e-06 x + 0.002225 x - 0.6589 x + 116.5 x
              2
 - 1.229e+04 x + 7.163e+05 x - 1.779e+07

modelo 13 :
           7             6            5          4         3
3.311e-09 x - 4.154e-06 x + 0.002224 x - 0.6587 x + 116.5 x
              2
 - 1.229e+04 x + 7.161e+05 x - 1.779e+07

modelo 14 :
          7             6            5          4         3
3.31e-09 x - 4.152e-06 x + 0.002224 x - 0.6585 x + 116.4 x
              2
 - 1.228e+04 x + 7.159e+05 x - 1.778e+07

"""
    
################### Trozo 1  #######################

def p1_1(x):
    return -0.0003277*x**3 + 0.05629*x**2 + 25.34*x + 25.09
def p1_2(x):
    return -0.0003279*x**3 + 0.05635*x**2 + 25.34*x + 25.11
def p1_3(x):
    return -0.0003282*x**3 + 0.0564*x**2 + 25.33*x + 25.14
def p1_4(x):
    return -0.0003285*x**3 + 0.05645*x**2 + 25.33*x + 25.16
def p1_5(x):
    return -0.0003287*x**3 + 0.0565*x**2 + 25.33*x + 25.19
def p1_6(x):
    return -9.224e-08*x**5 + 2.863e-05*x**4 - 0.003155*x**3 + 0.1441*x**2 + 25.48*x + 10.2
def p1_7(x):
    return -9.23e-08*x**5 + 2.865e-05*x**4 - 0.003158*x**3 + 0.144*x**2 + 25.48*x + 10.21
def p1_8(x):
    return -9.237e-08*x**5 + 2.867e-05*x**4 - 0.003161*x**3 + 0.1444*x**2 + 25.48*x + 10.22
def p1_9(x):
    return -9.243e-08*x**5 + 2.869e-05*x**4 - 0.003163*x**3 + 0.1445*x**2 + 25.48*x + 10.23
def p1_10(x):
    return -9.25e-08*x**5 + 2.871e-05*x**4 - 0.003166 *x**3 + 0.1446*x**2 + 25.47*x + 10.24
def p1_11(x):
    return -1.481e-11*x**7 + 6.51e-09*x**6 - 1.139e-06*x**5 + 0.0001002*x**4 - 0.004614*x**3  + 0.1031*x**2 + 27.05*x + 2.176
def p1_12(x):
    return -1.482e-11*x**7 + 6.514e-09*x**6- 1.14e-06*x**5 + 0.0001002*x**4 - 0.004618*x**3  + 0.1032*x**2 + 27.05*x + 2.178
def p1_13(x):
    return -1.483e-11*x**7 + 6.518e-09*x**6 - 1.14e-06*x**5 + 0.0001003*x**4 - 0.004621*x**3 + 0.1033*x**2 + 27.05 *x + 2.18
def p1_14(x):
    return -1.484e-11*x**7 + 6.522e-09*x**6 - 1.141e-06*x**5 + 0.0001004*x**4 - 0.004625*x**3  + 0.1034*x**2 + 27.05*x + 2.182
def p1_15(x):
    return -1.484e-11*x**7 + 6.526e-09*x**6 - 1.142e-06*x**5 + 0.0001005*x**4 - 0.004628*x**3  + 0.1035*x**2 + 27.05*x + 2.185

################### Trozo 2  #######################

def p2_1(x):
    return -0.005694*x**3 - 0.04569*x**2 + 412.8*x - 3.782e+04
def p2_2(x):
    return -0.005703*x**3 - 0.04091*x**2 + 411.9 *x - 3.777e+04
def p2_3(x):
    return -0.005712*x**3 - 0.03614*x**2 + 411.1 *x - 3.772e+04
def p2_4(x):
    return -0.005721*x**3 - 0.03136 *x**2 + 410.2 *x - 3.767e+04
def p2_5(x):
    return -0.00573*x**3 - 0.02659 *x**2 + 409.4 *x - 3.762e+04
def p2_6(x):
    return -4.23e-06*x**5 + 0.004113*x**4 - 1.586 *x**3 + 300.3 *x**2 - 2.787e+04 *x + 1.018e+06
def p2_7(x):
    return -4.226e-06*x**5 + 0.004109*x**4 - 1.585 *x**3 + 300.1 *x**2 - 2.785e+04 *x + 1.018e+06
def p2_8(x):
    return -4.222e-06*x**5 + 0.004105*x**4 - 1.583 *x**3 + 299.9 *x**2 - 2.783e+04 *x + 1.017e+06
def p2_9(x):
    return -4.218e-06*x**5 + 0.004101*x**4 - 1.582 *x**3 + 299.6 *x**2- 2.781e+04 *x + 1.016e+06
def p2_10(x):
    return -4.213e-06*x**5 + 0.004098 *x**4- 1.581 *x**3 + 299.4 *x**2 - 2.779e+04 *x + 1.015e+06
def p2_11(x):
    return 3.314e-09*x**7 - 4.157e-06*x**6 + 0.002226*x**5 - 0.6593*x**4 + 116.6 *x**3 - 1.23e+04 *x**2 + 7.167e+05 *x - 1.781e+07
def p2_12(x):
    return 3.313e-09*x**7 - 4.156e-06*x**6 + 0.002226 *x**5 - 0.6591*x**4 + 116.5 *x**3 - 1.229e+04 *x**2 + 7.165e+05 *x - 1.78e+07
def p2_13(x):
    return 3.312e-09*x**7 - 4.155e-06*x**6 + 0.002225 *x**5- 0.6589 *x**4 + 116.5 *x**3 - 1.229e+04 *x**2 + 7.163e+05 *x - 1.779e+07
def p2_14(x):
    return 3.311e-09*x**7 - 4.154e-06*x**6 + 0.002224 *x**5 - 0.6587 *x**4 + 116.5 *x**3 - 1.229e+04 *x**2 + 7.161e+05 *x - 1.779e+07
def p2_15(x):
    return 3.31e-09*x**7 - 4.152e-06*x**6 + 0.002224 *x**5 - 0.6585 *x**4 + 116.4 *x**3 - 1.228e+04 *x**2 + 7.159e+05 *x - 1.778e+07


pmm = 3885.37344

def error(a):
    return round(((abs(a - pmm))/pmm)*100,2)

def main():
    #curvaCaracteristica()
    #print(PMM())
    
    '''
    vmm = 149.76
    
    print(error(p1_1(vmm)))
    print(error(p1_2(vmm)))
    print(error(p1_3(vmm)))
    print(error(p1_4(vmm)))
    print(error(p1_5(vmm)))
    print(error(p1_6(vmm)))
    print(error(p1_7(vmm)))
    print(error(p1_8(vmm)))
    print(error(p1_9(vmm)))
    print(error(p1_10(vmm)))
    print(error(p1_11(vmm)))
    print(error(p1_12(vmm)))
    print(error(p1_13(vmm)))
    print(error(p1_14(vmm)))
    print(error(p1_15(vmm)))
    print('----------------')    
    print(error(p2_1(vmm)))
    print(error(p2_2(vmm)))
    print(error(p2_3(vmm)))
    print(error(p2_4(vmm)))
    print(error(p2_5(vmm)))
    print(error(p2_6(vmm)))
    print(error(p2_7(vmm)))
    print(error(p2_8(vmm)))
    print(error(p2_9(vmm)))
    print(error(p2_10(vmm)))
    print(error(p2_11(vmm)))
    print(error(p2_12(vmm)))
    print(error(p2_13(vmm)))
    print(error(p2_14(vmm)))
    print(error(p2_15(vmm)))
    '''
    x = np.linspace(0, 200)
    y = np.piecewise(x, [ (x <= 149.76) & (x >= 0), (x <= 200) & (x > 149.76)], [lambda x: p1_11(x), lambda x: p2_1(x)])
    plt.plot(x, y, "b-")
    
    plt.plot(df.V_pv,df.P_pv,"r--")
    plt.ylim(0,4000)
    plt.grid()
    plt.show()
    

    

if __name__ == "__main__":
    main()