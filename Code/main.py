import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importamos los datos:
path = "../Data/outputPV.txt"
df = pd.read_csv(path, header=None)
df.columns = ["V_pv","I_pv"]
df.insert(2,"P_pv",df["V_pv"]*df["I_pv"])

# Puntos Maximos

def PMM():
    df_mask = df['P_pv']==df['P_pv'].max()
    filtered_df = df[df_mask]
    return filtered_df


def curvaCaracteristica():
    global vpp, ipp, ppp
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
    
    
    plt.savefig("../Imagenes/curvacaracteristica.png")
    plt.show()
    


if __name__ == "__main__":
    pmm = PMM()
    curvaCaracteristica()
    