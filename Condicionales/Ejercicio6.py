peso_kg = float(input("Ingrese el peso del paquete en kg: "))
zona = int(input("Ingrese la zona de destino (1 - América del Norte, 2 - América Central, 3 - América del Sur, 4 - Europa, 5 - Asia): "))
if peso_kg > 5:
    print("El paquete no puede ser transportado debido a que excede el límite de peso de 5 kg.")
else:
    peso_gramos = peso_kg * 1000
    if zona == 1:
        costo = peso_gramos * 11
        zona_nombre = "América del Norte"
    elif zona == 2:
        costo = peso_gramos * 10
        zona_nombre = "América Central"
    elif zona == 3:
        costo = peso_gramos * 12
        zona_nombre = "América del Sur"
    elif zona == 4:
        costo = peso_gramos * 24
        zona_nombre = "Europa"
    elif zona == 5:
        costo = peso_gramos * 27
        zona_nombre = "Asia"
    else:
        print("Zona no válida.")
        costo = 0
    if costo > 0:
        print(f"El costo de enviar el paquete a {zona_nombre} es: ${costo:.2f}")
