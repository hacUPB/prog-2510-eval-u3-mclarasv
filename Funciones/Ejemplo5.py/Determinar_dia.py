def dia_semana(numero:int):
    if numero < 1 or numero > 7:
        print("Dia no valido.")
    elif numero == 1:
        dia = "Lunes"
    elif numero == 2:
        dia = "Martes"
    elif numero == 3:
        dia = "Miercoles"
    elif numero == 4:
        dia = "Jueves"
    elif numero == 5:
        dia = "Viernes"
    elif numero == 6:
        dia = "Sabado"
    else:
        dia = "domingo"
    return dia



def main():
    numero = int(input("Ingrese el número del día de la semana: "))
    dia = dia_semana()
    print(f"dia {numero} equivale al {dia}")

if __name__ == "__main__":
    main()