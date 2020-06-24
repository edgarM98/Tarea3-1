#########################################
#########################################
#####                               #####
#####    Maria Paula Ruiz Segura    ##### 
#####             B76878            #####
#####                               #####
#####            Tarea 3            #####
#####                               #####
#####            Grupo 2            #####
#####                               #####
#########################################
#########################################

# Paquetes que serán de utilidad. 
import numpy as np
from scipy import stats
from scipy import mean
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from mpl_toolkits import mplot3d

# Lectura de los dos documentos csv a utilizar
import pandas as pd
dataXY = pd.read_csv('xy.csv', header  = 0)
datosXY = dataXY.drop(['Unnamed: 0'], axis=1)

datosXY2 = pd.read_csv('xyp.csv')
datosX = datosXY2['x']
datosY = datosXY2['y']
datosP = datosXY2['p']

# Vectores de valores en X y Y y su tamaño 

X = np.arange(5, 16, 1)
Y = np.arange(5, 26, 1)

totalX = len(X)
totalY = len(Y)

# Para obtener las funciones de densidad marginales en X y en Y
# Se suman las probabilidades primero para X5, X6, X7 ...en X
# Y luego para Y se suman Y5, Y6, Y7....

denMargX = np.sum(datosXY, axis=1)
denMargY = np.sum(datosXY, axis=0)
         
# Se grafican las funciones de densidad para X y Y     
plt.figure(0)  
plt.plot(X, denMargX, color='lightcoral')

plt.figure(1)
plt.plot(Y, denMargY, color='lightcoral')

# Función para curva de ajuste gaussiana
def gauss(x, mu, sigma):
    return 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-((x-mu)**2/(2*sigma**2)))

# Obtener la curva de mejor ajuste para X
param1, _ = curve_fit(gauss, X, denMargX)

print('Los parámetros mu y sigma para la curva de X son: ', param1)

# Grafica la curva de mejor ajuste para X
plt.figure(0)
plt.plot(X, gauss(X, *param1), label='fit', color='k')

# Obtener la curva de mejor ajuste para Y
param2, _ = curve_fit(gauss, Y, denMargY)

print('Los parámetros mu y sigma para la curva de Y son: ', param2)

# Grafica la curva de mejor ajuste para Y
plt.figure(1)
plt.plot(Y, gauss(Y, *param2), label='fit',  color='k')

# Para obtener la función de densidad conjunta 
# Se crea la lista que va a almacenar todos los valores
denConjunta = np.zeros(231)
rangoC = len(denConjunta)
m = 0

# Como son independientes se toma en cuenta que 
# fx,y(x,y) = fx(xn) * fy(yn) 
if m in range(rangoC):        
    for i in range(totalX):
        for n in range(totalY):
            denConjunta[m] = denMargX[i] * denMargY[n]
            m = m+1
            
# Para graficar la función de densidad conjunta en 3D
plt.figure(2)
ax = plt.axes(projection='3d')
ax.scatter3D(datosX, datosY, denConjunta, c=denConjunta, cmap='plasma', edgecolor='k');
plt.show()

# Para obtener la Correlación entre X y Y

h = len(datosX)
correlacion = 0

for i in range(h):
    correlacion = correlacion + (datosX[i] * datosY[i] * datosP[i])
    
print('La correlación es: ', correlacion, '\n')

# Se obtiene el valor esperado de X y de Y por aparte
# Los valores esperados se multiplican para compararlos con la correlacion

esperadoX = 0
esperadoY = 0

for i in range(h):
    esperadoX = esperadoX + (datosX[i] * datosP[i])
    esperadoY = esperadoY + (datosY[i] * datosP[i])

num = esperadoX * esperadoY

print('Como E[X]*E[Y] = ', num, ' se confirma que las variables no están correlacionadas \n')

# Para obtener la media de los datos de X y Y
meanX = param1[0]
meanY = param2[0]

# Para obtener la covarianza
covarianza = 0

for i in range(h):
    covarianza = covarianza + ((datosX[i] - meanX)*(datosY[i]-meanY)*datosP[i])
    
print('La covarianza es: ', covarianza, ', el cual es un valor muy cercano a cero, tal y como se esperaba dada la independencia de las variables.\n')

#Para obtener los parámetros sigma del modelo
sigmaX = param1[1]
sigmaY = param2[1]

# Para el coeficiente de correlación
coefCorr = 0

for i in range(h): 
    coefCorr = coefCorr + (((datosX[i] - meanX) / sigmaX)*((datosY[i]-meanY) / sigmaY)*datosP[i])

print('El coeficiente de correlación es: ', coefCorr, ', que igualmente es un valor muy cercano a cero, confirmando que no hay relación entre las variables.\n')