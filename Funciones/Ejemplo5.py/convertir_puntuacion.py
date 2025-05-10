def convertir_puntuacion(puntaje:int):
    if puntaje < 0 or puntaje > 100:
        print("Puntuación inválida")
    elif puntaje >= 90:
        nota = "A"
    elif puntaje >= 80:
        nota = "B"
    elif puntaje >= 70:
        nota = "C"
    elif puntaje >= 60:
        nota = "D"
    else:
        nota = "F"
    return nota
    


def main():
    puntaje = int(input("Igrese el puntaje: "))
    nota = convertir_puntuacion(67)
    print(f"{puntaje} puntos, equivale a {nota}")

if __name__ == "__main__":
    main()