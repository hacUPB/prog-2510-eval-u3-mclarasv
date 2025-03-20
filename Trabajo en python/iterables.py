#Agregar elementos a una lista

'''
#ejemplo
frutas = ["Manzana", "Banana", "Cereza"]

# Agregar un elemento al final de la lista
frutas.append("Damasco")

# Insertar un elemento en una posición específica
frutas.insert(1, "Naranja")

# Extender la lista con otra lista
frutas.extend(["Pera", "Kiwi"])

print(frutas)
'''

animales = ["Kohala", "Elefante", "Gato", "Tiburón"]
print(animales)
animales.append("Conejo")
print(animales)
animales.insert(2, "Pez")
print(animales)
animales.extend(["Kiwi","Morza"])
print(animales)


#Eliminar elementos de una lista

'''
numeros = [1, 2, 3, 4, 5]

# Eliminar un elemento por valor
numeros.remove(3)

# Eliminar un elemento por índice y obtener su valor
valor_eliminado = numeros.pop(1)

# Eliminar todos los elementos de la lista
numeros.clear()

print(numeros)
print("Valor Eliminado:", valor_eliminado)
'''
animales = ["Kohala", "Elefante", "Gato", "Tiburón"]
animales.remove("Elefante")
print(animales)
valor_eliminado = animales.pop(3)
print(animales)
animales.clear()
print(animales)
print("Valor Eliminado:", valor_eliminado)

#Ordenar y revertir una lista

'''
nombres = ["Ana", "Carlos", "Eva", "David"]

# Ordenar la lista alfabéticamente (ascendente)
nombres.sort()

# Ordenar la lista alfabéticamente en orden descendente
nombres.sort(reverse=True)

# Revertir el orden de la lista
nombres.reverse()

print(nombres)
'''
animales = ["Kohala", "Elefante", "Gato", "Tiburón"]
print(animales)
animales.sort(reverse=true)
print(animales)
animales.reverse()
print(animales)

#Contar y encontrar elementos en una lista

'''
colores = ["Rojo", "Azul", "Verde", "Rojo", "Amarillo"]

# Contar la cantidad de veces que aparece un elemento
cantidad_rojo = colores.count("Rojo")

# Encontrar el índice de un elemento
indice_azul = colores.index("Azul")

print("Cantidad de Rojo:", cantidad_rojo)
print("Índice de Azul:", indice_azul)
'''
animales = ["Kohala", "Elefante", "Gato", "Tiburón", "Gato"]
cantidad_Gato = animales.count("Gato")
indice_Kohala = animales.index("Kohala")
print("Cantidad de Gatos:", cantidad_Gato)
print("Indice Kohala:", indice_Kohala)

#Metodos de cadenas de caracteres

##upper
'''
texto = "hola, mundo!"
en_mayusculas = texto.upper()
print(en_mayusculas)  # Salida: "HOLA, MUNDO!"
'''
texto = "me gustan las salchipapas"
en_mayusculas = texto.upper()
print(en_mayusculas)

##lower
'''
texto = "Hola, Mundo!"
en_minusculas = texto.lower()
print(en_minusculas)  # Salida: "hola, mundo!"
'''
texto = "Me gustan las salchipapas"
en_minusculas = texto.lower()
print(en_minusculas)

##capitalize
'''
texto = "hola, mundo!"
capitalizado = texto.capitalize()
print(capitalizado)  # Salida: "Hola, mundo!"
'''
texto = "me gustan las salchipapas"
capitalizado = texto.capitalize()
print(capitalizado)

##replace
'''
texto = "Python es genial"
reemplazado = texto.replace("genial", "increíble")
print(reemplazado)  # Salida: "Python es increíble"
'''
texto = "me gustan las salchipapas"
reemplazado = texto.replace("salchipapas", "fresas")
print(reemplazado)

##split
'''
frase = "Hola, cómo estás?"
palabras = frase.split(" ")
print(palabras)  # Salida: ['Hola,', 'cómo', 'estás?']
'''
frase = "me gustan las salchipapas"
palabras = frase.split(" ")
print(palabras)

##strip
'''
texto = "    Hola, mundo!   "
limpio = texto.strip()
print(limpio)  # Salida: "Hola, mundo!"
'''
texto = "       Me gustan las salchipapas           "
limpio = texto.strip()
print(limpio)


#Ejerciocio
frase = 