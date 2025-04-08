n = int(input("Ingrese un número entero positivo n: "))
suma = 0
for i in range(2, n+1, 2):
    suma += i
print(f"La suma de los números pares desde 1 hasta {n} es: {suma}")
