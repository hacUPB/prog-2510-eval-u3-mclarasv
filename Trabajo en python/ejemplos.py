'''
envio = 0
compra = input("Ingrese el valor de la compra: ")
compra = int(compra)
if compra < 100000:
    envio = 9000
total = compra + envio
print(f"El valor a pagar es: {total}")
'''

'''
numero = input("Ingrese el número telefonico: ")
cont = 1
for digito in numero: 
    #print(digito)
    cont = cont + 1
print(cont)
if cont != 10:
    print("¡Número no valido...!")
print(numero)
''' 

'''
cuenta = float(input("Ingrese la cuenta a pagar: "))
sexo = input("Ingrese el sexo del niño: Masculino o Femenino")
M = Masculino
F = Femenino
if sexo == F:
    precio = precio - 50
elif sexo == M:
    precio = precio - 30
else:
    print("Ingresó in valor no valido")
print(precio)
'''
print("S. Suma\nR. Resta\nD, División\nM. Multiplicación")
opcion = int(input("Elija una opcion: "))

if opcion == "S":
    prinyt("Sumar")
    
