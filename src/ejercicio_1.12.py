"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase
Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales."""

weight = float (input("Introduzca su peso en kg:"))
height = float (input("Introduzca su altura en m:"))

imc = weight/(height)**2

print("Su IMC es", '{: .2f}'.format(imc))
