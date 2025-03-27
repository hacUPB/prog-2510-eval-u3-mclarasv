# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
print("*" * 60)
print("Calculadora")
print("*" * 60)

print("S. Sumar\nR. restar\nM. multiplicar\nD. dividir\nP. potencia\nE. Salir")
opcion = input("Elija la opción: ")

num1 = float(input("Ingrese número 1: "))
num2 = float(input("Ingrese número 2: "))

if opcion.upper() == 'S':
    resultado = num1 + num2
    operador = "+"
elif opcion.upper() == 'R':
    resultado = num1 - num2
    operador = "-"
elif opcion.upper() == 'M':
    resultado = num1 * num2
    operador = "X"
elif opcion.upper() == 'D':
    operador = "/"
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Indeterminado"
        print("Denominador igual a 0")
elif opcion.upper() == 'P':
    resultado = num1 ** num2
    operador = "^"
else:
    print("Opción no válida")

print("f{num1} {operador} {num2} = {resultado}")