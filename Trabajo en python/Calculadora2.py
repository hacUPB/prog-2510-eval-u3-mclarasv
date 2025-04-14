# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 14:50:35 2025

@author: B09S202est
"""

print("*" * 60)
print("Calculadora")
print("*" * 60)

resultado = "No calculado"
operador = "?"
opcion = 'S'

while opcion != "E":
    print("S. Sumar\nR. restar\nM. multiplicar\nD. dividir\nP. potencia\nE. Salir")
    opcion = input("Elija la opción: ").upper()
    
    num1 = float(input("Ingrese número 1: "))
    num2 = float(input("Ingrese número 2: "))
    
    match opcion:
        case 'S':
            resultado = num1 + num2
            operador = "+"
        case 'R':
            resultado = num1 - num2
            operador = "-"
        case 'M':
            resultado = num1 * num2
            operador = "X"
        case 'D':
            operador = "/"
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Indeterminado"
                print("Denominador igual a 0")
        case 'P':
            resultado = num1 ** num2
            operador = "^"
        case _:
            print("Opción no válida")
    
    print("f{num1} {operador} {num2} = {resultado}")
    
    print("S. Sumar\nR. restar\nM. multiplicar\nD. dividir\nP. potencia\nE. Salir")
    opcion = input("Elija la opción: ").upper()