altitud_actual = float(input("Ingrese la altitud inicial del satélite (km): "))
coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (ej: 0.01): "))
altitud_minima_seguridad = float(input("Ingrese la altitud mínima de seguridad (km): "))

orbita = 0
sat_estabilizado = False

while altitud_actual > altitud_minima_seguridad:
    orbita += 1

    altitud_perdida = coeficiente_arrastre * altitud_actual
    altitud_actual -= altitud_perdida

    coeficiente_arrastre += 0.0001

    if altitud_perdida < 0.01:  
        sat_estabilizado = True
        break

print("\n--- Resultado de la Simulación ---")
if sat_estabilizado:
    print(f"El satélite se estabilizó en una órbita baja.")
    print(f"Altitud final: {altitud_actual:.2f} km")
    print(f"Órbitas completadas: {orbita}")
else:
    print(f"El satélite ha reingresado en la atmósfera terrestre.")
    print(f"Altitud final: {altitud_actual:.2f} km")
    print(f"Órbitas completadas: {orbita}")
