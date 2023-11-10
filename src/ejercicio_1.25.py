""" Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa
y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione
cuando el día o el mes se introduzcan con un solo carácter."""

fecha = input ("Introduzca su fecha de nacimiento de la siguiente forma: dd/mm/aaaa: ")
fecha = fecha.split('/')
print (" El día es: ", fecha[0], " del mes: ", fecha[1], " del año: ", fecha[2]) #Vale tanto para 2 dígitos como para 1