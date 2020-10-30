# Entrega 3

## Parte 1

Replicando los resultados de la sección 4.5 de la `memoria de Contreras`, se utilizan las siguientres condiciones de borde:


![ecuaci0ones](https://user-images.githubusercontent.com/43649125/97651562-2a4cc900-1a3b-11eb-993c-1c14ee2a9e04.png)

La solucion analitica se obtiene con una serie de Fourier, la cual converge a un resultado utilizando la siguiente formula:

![ecuacion 2](https://user-images.githubusercontent.com/43649125/97651560-291b9c00-1a3b-11eb-8a3d-71f3735aad56.png)

Con lo anterior se obtienen los siguientes graficos:

* Posición `x = 0.104 [m]`
![image](https://user-images.githubusercontent.com/43451947/97652014-3a18dd00-1a3c-11eb-9f23-31c030c6aaaa.png)

* Posición `x = 0.208 [m]`
![image](https://user-images.githubusercontent.com/43451947/97652024-3f762780-1a3c-11eb-9a92-794fc8ded9d4.png)

* Posición `x = 0.416 [m]`
![image](https://user-images.githubusercontent.com/43451947/97652027-4309ae80-1a3c-11eb-844c-f21a53dcd1e6.png)

Graficos siguientes:

![image](https://user-images.githubusercontent.com/43451947/97655186-418fb480-1a43-11eb-97f3-a106bf453523.png)
![image](https://user-images.githubusercontent.com/43451947/97655191-46546880-1a43-11eb-9835-9c247c8f3140.png)
![image](https://user-images.githubusercontent.com/43451947/97655205-4e140d00-1a43-11eb-9bef-9bd7a2cdd63b.png)

## Parte 2

En el codigo se observan los pasos que se tuvieron que agregar al codigo de la entrega anterior para poder expresar la evolucion de la temperatura con una condicion de borde unica inicial. Se observa que la solucion converge al valor de temperatura `t = 15°C` tanto para los 1000 pasos como para los 50000 pasos.


![image](https://user-images.githubusercontent.com/43451947/97653371-67b35580-1a3f-11eb-9bfa-ec742b210f8f.png)
 
