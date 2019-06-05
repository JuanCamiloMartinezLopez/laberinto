# LABERINTO
<hr>
Gabriel Esteban Castillo Ramírez - 20171020021
Juan Camilo Martínez López - 20171020074
Omar Alejandro Espitia Sánchez - 20171020094
<hr>
mediante la creacion de un arbol n-ario de los posibles posiciones dentro de un laberinto, se determina si tiene o no solucion este.

## Arbol n-ário

defenido atravez de la clase nodo, donde se modela cada uno de los componentes de este arbol(nodos).

![Class nodo](https://github.com/JuanCamiloMartinezLopez/laberinto/blob/master/images/ClassNodo.jpg)

## Funciones de busqueda por posicion y valor

para la generacion y prueba del arbol se hace uso de funciones que permiten comprobar los valores y estados de los nodos dentro de nuestro arbol.

![Funciones de busqueda](https://github.com/JuanCamiloMartinezLopez/laberinto/blob/master/images/FuntionsOfSearch.png)

## Funciones de insercion al arbol

mediante recursividad se parte de la posicion de "x" para recorrer los posibles caminos y agregarlos al arbol sin repetir( haciendo uso de las funciones de busqueda por posicion). asi se logra construir el arbol que luego sera usado por las funciones de busqueda por valor para determinar si hay solucion

![funciones de insercion](https://github.com/JuanCamiloMartinezLopez/laberinto/blob/master/images/insertNodo.jpg)

<hr>
#prueba

 el programa puede recibir cualquier laberinto de mxn conformado por 0 y 1, donde el cero es camino y el uno un muro, asi tambien se denota "x" el inicio y "y"  el final o meta
 
![laberinto](https://github.com/JuanCamiloMartinezLopez/laberinto/blob/master/images/Laberint.jpg)

asi en este caso el programa responde, si hay camino, caso contrario, no hay camino.

