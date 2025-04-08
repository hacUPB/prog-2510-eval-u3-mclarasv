titulo = int(input("¿Es usted señor o señora?: "))
nombre = int(input("Introduce tu nombre:"))
apellido = int(input("Introduce tu apellido: "))
print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!")
ciudades_disponibles = ["Medellín", "Bogotá", "Cartagena"]
origen = int(input("¿cuál es su lugar de origen?: ")).capitalize()
while origen not in ciudades_disponibles:
     print("Ciudad no válida. Inténtelo de nuevo.")
     origen = input("Ingrese la ciudad de origen: ")
destino = input("Ingrese la ciudad de destino: ").capitalize()
while destino not in ciudades_disponibles or destino == origen:
    print("Ciudad no válida o igual a la de origen. Inténtelo de nuevo.")
    destino = input("Ingrese la ciudad de destino: ")
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dia_viaje = input("Ingrese el día de la semana en que desea viajar: ").capitalize()
while dia_viaje not in dias:
    print("Día inválido. Inténtelo de nuevo.")
    dia_viaje = input("Ingrese el día de la semana en que desea viajar: ").capitalize()
dia_mes = input("Ingrese el día del mes (1-30): ")
distancia = {("Medellín", "Bogotá"): 240,("Medellín", "Cartagena"): 461,("Bogotá", "Cartagena"): 657}