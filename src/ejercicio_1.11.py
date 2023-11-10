"""Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla
 la suma de todos los enteros desde 1 hasta n
 
 """

n = int (input ("Introduzca un número: "))

suma = (n*(n+1))/2

print ("La suma de los números del 1 al ", n, " es ", suma)