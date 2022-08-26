import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Importamos los datos de Matlab
df = pd.read_csv("dataSunset72X.csv", header=None)
df.columns = ['V_pv','I_pv']
df.insert(2,'P_pv',df['V_pv']*df['I_pv'])
			
# Curva caracteristica
	
def curvaVI(x,y):
    global fig
    			
    fig = plt.figure(figsize=(8, 6))
    plt.plot(x,y)
    plt.title('Curva caracteristica VI',fontsize=25)
    plt.xlabel("V",fontsize=18)
    plt.ylabel("A",fontsize=18)
    plt.xlim(0,195)
    plt.ylim(0,30)
    plt.grid()
	
    return plt.show()
		
def curvaVP(x,y):
    global fig
    			
    fig = plt.figure(figsize=(8, 6))
    plt.plot(x,y)
    plt.title('Curva caracteristica PV',fontsize=25)
    plt.xlabel("V",fontsize=18)
    plt.ylabel("W",fontsize=18)
    plt.xlim(0,195)
    plt.ylim(0,4000)
    plt.grid()
    			
    return plt.show()

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
    plt.plot(polyline, model1(polyline), color='green')
    plt.plot(polyline, model2(polyline), color='red')
    plt.plot(polyline, model3(polyline), color='purple')
    plt.plot(polyline, model4(polyline), color='blue')
    plt.plot(polyline, model5(polyline), color='orange')
    return plt.show()

#define function to calculate adjusted r-squared
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
    plt.show()


if __name__ == "__main__":
    x = df['V_pv']
    curvaVI(x,df['I_pv'])
    curvaVP(x,df['P_pv'])		
    curvasAjuste()
    
    #calculated adjusted R-squared of each model
    print(adjR(df.V_pv, df.I_pv, 1))
    print(adjR(df.V_pv, df.I_pv, 2))
    print(adjR(df.V_pv, df.I_pv, 3))
    print(adjR(df.V_pv, df.I_pv, 4))
    print(adjR(df.V_pv, df.I_pv, 5))	
			