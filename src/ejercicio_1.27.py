"""Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre
por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales."""

producto =input("Indique un producto: ")
precio = float (input("Indique su precio: "))
ud = int (input("Indique el stock de ese producto: "))
total = precio * ud
print(f"El nombre del producto es: {producto}. \n El precio del producto es: {precio:06.2f}€. \n El stock es: {ud:03.0f} unidades. \n El coste total es: {total:08.2f}€")
