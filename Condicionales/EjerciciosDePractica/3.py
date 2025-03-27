distancia_km = float(input("Ingrese la distancia del vuelo en kilómetros: "))
consumo_por_km = float(input("Ingrese el consumo de combustible por kilómetro (en litros): "))
carga_combustible = distancia_km * consumo_por_km
if distancia_km <= 1000:
    carga_combustible *= 1.10
else:
    carga_combustible *= 1.15
print(f"La carga de combustible requerida es: {carga_combustible:.2f} litros")
