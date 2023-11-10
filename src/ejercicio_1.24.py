"""Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
y muestre por pantalla el número de euros y el número de céntimos del precio introducido."""


precio = input ("Introduzca un precio en € con 2 decimales: ")
precio2=precio.split(".")
print (precio2[0], "son los € ", precio2[1], "son los céntimos.")