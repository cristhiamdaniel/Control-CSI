import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importamos los datos de Matlab
#df = pd.read_csv("dataSunset72X.csv", header=None)
df = pd.read_csv("/Tex/myFile.txt", header=None)
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
    
    plt.savefig("./imagenes/curvacaracteristica.png")
    plt.show()

models = []
for i in range(1,10):
    model = np.poly1d(np.polyfit(df.V_pv, df.I_pv, i))
    models.append(models)

def curvasAjuste():
    #fit polynomial models up to degree 5
    model1 = np.poly1d(np.polyfit(df.V_pv, df.I_pv, 1))
    model2 = np.poly1d(np.polyfit(df.V_pv, df.I_pv, 2))
    model3 = np.poly1d(np.polyfit(df.V_pv, df.I_pv, 3))
    model4 = np.poly1d(np.polyfit(df.V_pv, df.I_pv, 4))
    model5 = np.poly1d(np.polyfit(df.V_pv, df.I_pv, 5))
    model9 = np.poly1d(np.polyfit(df.V_pv, df.I_pv, 9))
    
    #create scatterplot
    polyline = np.linspace(0, 50, 1000)
    plt.scatter(df.V_pv, df.I_pv)
    
    #add fitted polynomial lines to scatterplot 
    plt.plot(polyline, model1(polyline), color='green', label= 'Funcion grado 1')
    plt.plot(polyline, model2(polyline), color='red', label= 'Funcion grado 2')
    plt.plot(polyline, model3(polyline), color='purple', label= 'Funcion grado 3')
    plt.plot(polyline, model4(polyline), color='blue', label= 'Funcion grado 4')
    plt.plot(polyline, model5(polyline), color='orange', label= 'Funcion grado 5')
    plt.plot(polyline, model9(polyline), color='black', label= 'Funcion grado 9')
    
    plt.legend()
    plt.grid()
    #plt.savefig("./imagenes/curvaajuste.png")
    plt.show()


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

# Modelo 5
#define scatterplot
def graficaModelo(x,y, model):
    polyline = np.linspace(1, 200, 100)
    plt.scatter(x, y)
    
    #add fitted polynomial curve to scatterplot
    plt.plot(polyline, model(polyline), '--', color='red')
    #plt.savefig("./imagenes/modeloSel.png")
    plt.show()

def funcion(x):
    return (-8.713*10**(-10))*(x**5) + (2.213*10**(-7))* (x**4) + (- 1.538 * 10**(-5))* (x**3) + (7.92*10**(-5))* (x**2) + 0.01166 *x + 27.93

def graficaModelo5():
    x = np.linspace(0,200,100)
    y = funcion(x)
    plt.plot(x,y, label="Funcion polinomica")
    plt.plot(df['V_pv'],df['I_pv'], label = "Curva VI")
    plt.plot(37.44,8.6684, marker="o", color='red', label='mpp')
    plt.xlim(0,50)
    plt.ylim(0,10)
    plt.legend()
    plt.grid()
    
    plt.show()
    
    
if __name__ == "__main__":
    #curvaCaracteristica()
    #curvasAjuste()
    
    v = df.V_pv
    i = df.I_pv
    p = df.P_pv
    
    
    '''
    for x in range(1,6):
        print(adjR(v, i, x))
    '''
    #model5 = np.poly1d(np.polyfit(v, i, 5))
    #graficaModelo(v, i, model5)
    #print(model5)
    #graficaModelo5()
    
    