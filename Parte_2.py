# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:16:09 2020

@author: 56977
"""

from matplotlib.pylab import *

L = 1.0
n = 100
dx = L / n

x = linspace (0,L,n+1)

dt = 2.
Nt = 50000
u = zeros((Nt, n+1))

u[:,0] = 5.
u[:,-1] = 20.

u[0,1:n] = 20.

print("Matriz inicial")
print (u)
K = 79.5
c = 450
rho = 7800
alpha = K*dt/(c*rho*dx**2)
Nskip=1
for k in range(Nt-1):
    t = dt*k
    u[k,n] = 10*dx+u[k,n-1]
    for i in range (1,n):
        u[k+1,i] = u[k,i]+ alpha*(u[k,i+1]-2*u[k,i] + u[k,i-1])
    
    
    Nplot=1000
    if k % Nplot ==0:
        plot(x,u[k,:])
    if k%(Nskip*Nplot)==0:
        
        text(x[-1],u[k][-1],f"{Nplot*(Nskip-1):.1f}",
             fontsize=8,
             horizontalalignment="center",
             verticalalignment="center",
             ).set_bbox(dict(facecolor="white", alpha=0.4, edgecolor="black",boxstyle="round"))   
        Nskip+=5
title("k = {} t = {} s".format(k,k*dt))

title("k = {}   t = {} s".format(k,k*dt))
xlabel("Distancia, $x$ (m)")
ylabel("Temperatura, $T$ (°C)")

show()