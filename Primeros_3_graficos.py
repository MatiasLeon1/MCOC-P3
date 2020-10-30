# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:15:26 2020

@author: 56977
"""

from matplotlib.pylab import *
def graficar_normal(dt,imprimir):
    L = 1.04
    n = 20
    dx = L/n # ==> largo del intervalo en x barra de hormigon
    
    x = linspace(0,L,n+1) # los puntos en que se evalua la temperatura dentro de la barra de hormigon
    # print(x)
    #arreglo com la solución
    # dt = 5. # delta t
    Nt = 90000 # 25 horas en segundos
    lista_tiempo=arange(0,Nt,dt)
    u = zeros((len(lista_tiempo),n+1)) # matriz de 90000 x 11 ==> (tiempo, distancia)
                        # me indica por ejemplo que en la distancia=0 me varía la temperatura 90000 veces
                        # si es que el intervalo de tiempo es igual a 1
    
    
    # Condiciones de borde
    u[:,0] = 0. # condicion de borde izquierda
    u[:,-1] = 0. # condicion de borde derecha
    
    #Condicion inicial
    u[0,1:n] = 20
    
    K = 0.001495   # kW/m*C
    c = 1.023    # kJ/kg*C
    rho = 2476. # kg/m^3
    # K = 79.5    # m^2/s
    # c = 450.    # J/kg*C
    # rho = 7800. # kg/m^3
    alfa = K*dt/(c*rho*dx**2) # constante
    
    for k in range(len(lista_tiempo)-1): # k va recorriendo el intervalo de tiempo 
                          # el k va de 0 al 89999
        t = dt*k # me indica que segundo se evaluó
        # print(f"k = {k} t = {t}")
        for i in range (1,n): # esta recorriendo la barra de hormigon en terminos de distancia,
                              # parte del 1 pues partir de 0 significa no tener el u[0,-1]
            u[k+1,i] = u[k,i] + alfa*(u[k,i+1] - 2*u[k,i] + u[k,i-1])
        # if k%89999==0 and k!=0:
    # plot(x,u[k,:])
    plot(lista_tiempo,u[:,imprimir])
    
    segs=[0,5*3600,10*3600,15*3600,20*3600,25*3600]
    horas=[str(f/3600) for f in segs]
    xticks(segs,horas)
    grid()
    title("x = {}m".format(round(x[imprimir],3)))
    xlabel("Tiempo [horas]")
    ylabel("Temperatura [C]")
    legend([f"Malla 20 ∆t=1 (s)",f"Malla 20 ∆t=5 (s)",f"Malla 20 ∆t=10 (s)",f"Malla 20 ∆t=50 (s)",f"Malla 20 ∆t=100 (s)"])
def graficar_fourier():
    L = 1.04
    n = 20
    dx = L/n # ==> largo del intervalo en x barra de hormigon
    
    x = linspace(0,L,n+1) # los puntos en que se evalua la temperatura dentro de la barra de hormigon
    # print(x)
    #arreglo com la solución
    dt = 1. # delta t
    Nt = 90000 # 25 horas en segundos
    lista_tiempo=arange(0,Nt,dt)
    u = zeros((len(lista_tiempo),n+1)) # matriz de 90000 x 11 ==> (tiempo, distancia)
                        # me indica por ejemplo que en la distancia=0 me varía la temperatura 90000 veces
                        # si es que el intervalo de tiempo es igual a 1
    
    
    # Condiciones de borde
    u[:,0] = 0. # condicion de borde izquierda
    u[:,-1] = 0. # condicion de borde derecha
    
    #Condicion inicial
    u[0,1:n] = 20
    
    K = 0.001495   # kW/m*C
    c = 1.023    # kJ/kg*C
    rho = 2476. # kg/m^3
    # K = 79.5    # m^2/s
    # c = 450.    # J/kg*C
    # rho = 7800. # kg/m^3
    alfa = K*dt/(c*rho*dx**2) # constante
    lista_suma=[20]
    for k in range(len(lista_tiempo)-1): # k va recorriendo el intervalo de tiempo 
                          # el k va de 0 al 89999
        t = dt*k # me indica que segundo se evaluó
        # print(f"k = {k} t = {t}")
        suma=0 
        c=1
        for dis in x:
            for i in range (1,n): # esta recorriendo la barra de hormigon en terminos de distancia,
                                  # parte del 1 pues partir de 0 significa no tener el u[0,-1]
                suma+=((40*(1-(-1)*i))/(i*np.pi))*np.sin((i*np.pi*dis)/L)*np.exp(k-alfa*((i*np.pi)/L)**2)
                if i==n-1:
                    u[k,c]=suma
                    c+=1
        # lista_suma.append(suma)
        # if k%89999==0 and k!=0:
    # plot(x,u[k,:])
    plot(lista_tiempo,u[:,2])
    
    segs=[0,5*3600,10*3600,15*3600,20*3600,25*3600]
    horas=[str(f/3600) for f in segs]
    xticks(segs,horas)
    title("k = {}   t = {} s".format(k,k*dt))
    
    xlabel("Tiempo [horas]")
    ylabel("Temperatura [C]")

lista_delta=[1,5,10,50,100]
figure(1)
for i in lista_delta:
    graficar_normal(i,2)
# graficar_fourier()
show()
figure(2)
lista_delta=[1,5,10,50,100]
for i in lista_delta:
    graficar_normal(i,4)
# graficar_fourier()
show()
figure(3)
lista_delta=[1,5,10,50,100]
for i in lista_delta:
    graficar_normal(i,8)
# graficar_fourier()
show()