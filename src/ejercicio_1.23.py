"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre
por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es."""

mail = input ("Indique su correo electrónico: ")
sindom = mail.find("@")
print(mail[: sindom]+ "@ceu.es")

#print(mail[: mail.find("@")]+ "@ceu.es") otra forma

"""Otra forma:

division = mail.split('@')
print (division[0] + '@ceu.es')

"""