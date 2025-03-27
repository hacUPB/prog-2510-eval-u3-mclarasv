
compra = float(input("Ingrese el valor de la compra: $"))
costo_envio = 9000
if compra > 100000:
    total_a_pagar = compra 
else:
    total_a_pagar = compra + costo_envio 
print(f"El valor total a pagar es: ${total_a_pagar}")
