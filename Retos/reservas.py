
titulo = input("Ingrese su título (Sr. o Sra.): ")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!\n")


ciudades = ["Medellín", "Bogotá", "Cartagena"]
print("Ciudades disponibles:", ", ".join(ciudades))

origen = input("Ciudad de origen: ")
destino = input("Ciudad de destino: ")

while origen == destino:
    print("El origen y el destino no pueden ser iguales. Inténtelo de nuevo.")
    destino = input("Ciudad de destino: ")

dia_semana = input("Ingrese el día de la semana en que desea viajar (ej: lunes): ").lower()
dia_mes = input("Ingrese el día del mes (1 a 30): ")

distancia = 0
if (origen == "Medellín" and destino == "Bogotá") or (origen == "Bogotá" and destino == "Medellín"):
    distancia = 240
elif (origen == "Medellín" and destino == "Cartagena") or (origen == "Cartagena" and destino == "Medellín"):
    distancia = 461
elif (origen == "Bogotá" and destino == "Cartagena") or (origen == "Cartagena" and destino == "Bogotá"):
    distancia = 657

dias_lunes_a_jueves = ["lunes", "martes", "miércoles", "jueves"]
dias_viernes_a_domingo = ["viernes", "sábado", "domingo"]

if distancia < 400:
    if dia_semana in dias_lunes_a_jueves:
        precio = 79900
    else:
        precio = 119900
else:
    if dia_semana in dias_lunes_a_jueves:
        precio = 156900
    else:
        precio = 213000

preferencia = input("¿Prefiere asiento en el pasillo, ventana o sin preferencia?: ").lower()

if preferencia == "pasillo":
    letra_asiento = "C"
elif preferencia == "ventana":
    letra_asiento = "A"
else:
    letra_asiento = "B"

numero_asiento = random.randint(1, 29)
asiento = str(numero_asiento) + letra_asiento

print("\n--- Confirmación de Reserva ---")
print(f"Pasajero: {titulo} {nombre} {apellido}")
print(f"Origen: {origen}")
print(f"Destino: {destino}")
print(f"Fecha de vuelo: {dia_semana.capitalize()} {dia_mes}")
print(f"Precio del boleto: ${precio:,}")
print(f"Asiento asignado: {asiento}")
print("--------------------------------")
