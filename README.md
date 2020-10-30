# Entrega 3

## Parte 1

Replicando los resultados de la sección 4.5 de la `memoria de Contreras`, se utilizan las siguientres condiciones de borde:


![ecuaci0ones](https://user-images.githubusercontent.com/43649125/97651562-2a4cc900-1a3b-11eb-993c-1c14ee2a9e04.png)

La solucion analitica se obtiene con una serie de Fourier, la cual converge a un resultado utilizando la siguiente formula:

![ecuacion 2](https://user-images.githubusercontent.com/43649125/97651560-291b9c00-1a3b-11eb-8a3d-71f3735aad56.png)

Con lo anterior se obtienen los siguientes graficos
![image](https://user-images.githubusercontent.com/43451947/97652014-3a18dd00-1a3c-11eb-9f23-31c030c6aaaa.png)
![image](https://user-images.githubusercontent.com/43451947/97652024-3f762780-1a3c-11eb-9a92-794fc8ded9d4.png)
![image](https://user-images.githubusercontent.com/43451947/97652027-4309ae80-1a3c-11eb-844c-f21a53dcd1e6.png)

## Parte 2

En el codigo se observan los pasos que se tuvieron que agregar al codigo de la entrega anterior para poder expresar la evolucion de la temperatura con una condicion de borde unica inicial. Se observa que la solucion converge al valor de temperatura `t = 15°C` tanto para los 1000 pasos como para los 50000 pasos.
