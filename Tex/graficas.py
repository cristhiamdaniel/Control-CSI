import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importamos los datos de Matlab
df = pd.read_csv("dataSunset72X.csv", header=None)
df.columns = ["V_pv","I_pv"]
df.insert(2,"P_pv",df["V_pv"]*df["I_pv"])

# Creacion de la grafica

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
    ax1.set_xlim(0,195)
    ax1.set_ylim(0,30)
    ax2 = ax1.twinx() 
    
    color = "tab:blue"
    ax2.set_ylabel("Potencia (W)", color=color)  
    ax2.plot(v, p, color=color)
    ax2.tick_params(axis="y", labelcolor=color)
    ax2.set_xlim(0,195)
    ax2.set_ylim(0,4000)
    
    fig.tight_layout() 
    plt.grid()
    
    plt.savefig("./imagenes/curvacaracteristica.png")
    plt.show()


def curvasAjuste():
    #fit polynomial models up to degree 5
    model1 = np.poly1d(np.polyfit(df.V_pv, df.I_pv, 1))
    model2 = np.poly1d(np.polyfit(df.V_pv, df.I_pv, 2))
    model3 = np.poly1d(np.polyfit(df.V_pv, df.I_pv, 3))
    model4 = np.poly1d(np.polyfit(df.V_pv, df.I_pv, 4))
    model5 = np.poly1d(np.polyfit(df.V_pv, df.I_pv, 5))
    
    #create scatterplot
    polyline = np.linspace(1, 200, 100)
    plt.scatter(df.V_pv, df.I_pv)
    
    #add fitted polynomial lines to scatterplot 
    plt.plot(polyline, model1(polyline), color='green', label= 'Funcion grado 1')
    plt.plot(polyline, model2(polyline), color='red', label= 'Funcion grado 2')
    plt.plot(polyline, model3(polyline), color='purple', label= 'Funcion grado 3')
    plt.plot(polyline, model4(polyline), color='blue', label= 'Funcion grado 4')
    plt.plot(polyline, model5(polyline), color='orange', label= 'Funcion grado 5')
    
    plt.legend()
    plt.grid()
    plt.savefig("./imagenes/curvaajuste.png")
    plt.show()



if __name__ == "__main__":
    curvaCaracteristica()
    curvasAjuste()
						