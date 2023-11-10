"""Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta."""

listaCompra = input("Indique al lista de la compra, por ejemplo: tomate, lechuga, huevos...: ")
listaCompra = listaCompra.replace(" ", "").replace(',','\n')
print (listaCompra)