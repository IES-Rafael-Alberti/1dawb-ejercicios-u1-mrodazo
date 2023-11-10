"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
Después el programa debe mostrar el precio habitual de una barra de pan
(establecido en el programa como una constante), el descuento que se le hace por no ser fresca
y el coste final total de todas las barras no frescas."""

vendidas = int (input("Indique el nº de barras no frescas vendidas: "))

PRECIO = 3.49
final = vendidas * PRECIO * 0.4

print (f"El precio de una barra del día es {PRECIO}€, por no ser fresca se hace un 60% de descuento.\
        Así que el coste final de todas estas barras no frescas es: {final :.2f}€.")