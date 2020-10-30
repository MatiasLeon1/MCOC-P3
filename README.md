# Entrega 3

## Parte 1

Replicando los resultados de la sección 4.5 de la `memoria de Contreras`, se utilizan las siguientres condiciones de borde:


![ecuaci0ones](https://user-images.githubusercontent.com/43649125/97651562-2a4cc900-1a3b-11eb-993c-1c14ee2a9e04.png)

La solucion analitica se obtiene con una serie de Fourier, la cual converge a un resultado utilizando la siguiente formula:

![ecuacion 2](https://user-images.githubusercontent.com/43649125/97651560-291b9c00-1a3b-11eb-8a3d-71f3735aad56.png)

Con lo anterior se obtienen los soguientew graficos

## Parte 2

En el codigo se observan los pasos que se tuvieron que agregar al codigo de la entrega anterior para poder expresar la evolucion de la temperatura con una condicion de borde unica inicial. Se observa que la solucion converge al valor de temperatura `t = 15°C` tanto para los 1000 pasos como para los 50000 pasos.
