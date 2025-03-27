secreto = 15
Intento = 1             #Cambio el numero de 0 a 1 para que cuente el primer intento
print("Bienvenido al juego: 'Adivina el número'!")
print("Tienes que adivinar un número entre 1 y 10")
num = int(input("Ingrese el número: "))
while num != secreto:
    if num > secreto:
        print("El número es menor. Intentelo de nuevo")
        num = int(input("Ingrese el número: "))
    elif num < secreto:
        print("El número es mayor. Intentelo de nuevo")
        num = int(input("Ingrese el número: "))
    else:                   #Se corrige que el else no lleva condición 
        print("El número es correcto")
    Intento = (Intento + 1)                     #Le quito las comillas a la variable intento 
print(f"¡Felicidades! Has adivinado el número en {Intento} intentos")