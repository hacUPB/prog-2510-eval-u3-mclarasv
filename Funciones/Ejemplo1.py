#Espacio para función de usuario
def mcd(num, den):
    if num <= den:
        menor = num
    else:
        menor = den

    for divisor in range(menor, 0, -1):
        if num % divisor == 0 and den % divisor == 0:
            max_com_div = divisor
            break
    return max_com_div
#---------------------------------------------------------
def imprime_fraccion(num, den, maximo):
    print(f"{num}\t=\t {den/maximo}")
    print("___\t \t___")
    print(f"{den}\t=\t{int(den/maximo)}")
#---------------------------------------------------------
#Funcion principal
def main():
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    maximo = mcd(numerador, denominador)
    print(f"M.C.D= {maximo}")

#---------------------------------------------------------
#Punto de entrada del programa
if __name__ == "__main__":
    main()