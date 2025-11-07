"""
==========================================
 CLASE 1 - VARIABLES Y TIPOS DE DATOS
==========================================
Objetivo:
Aprender qué es una variable, cómo se crea y
qué tipos de datos existen en Python.

"""

# -----------------------------
# ¿Qué es una variable?
# -----------------------------
# Una variable es un espacio en memoria donde guardamos un valor.

nombre = "Brandon"      
edad = 21                
estatura = 1.80           
activo = True             

# Mostramos los valores
print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)
print("Activo:", activo)

# Podemos comprobar el tipo de cada variable
print(type(nombre))   # <class 'str'>
print(type(edad))     # <class 'int'>
print(type(estatura)) # <class 'float'>
print(type(activo))   # <class 'bool'>


# -----------------------------
# Asignación múltiple
# -----------------------------
# Se pueden crear varias variables en una sola línea

x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)

# O asignar el mismo valor a varias variables
a = b = c = "Python"
print(a, b, c)



# -----------------------------
# Tipos de datos más comunes
# -----------------------------
# str (cadena de texto)
mensaje = "Hola, Python!"
print(mensaje)

# int (entero)
cantidad = 50
print(cantidad)

# float (decimal)
precio = 19.99
print(precio)

# bool (booleano)
disponible = False
print(disponible)

# list (lista)
colores = ["rojo", "verde", "azul"]
print(colores)

# tuple (tupla)
coordenadas = (10, 20)
print(coordenadas)

# dict (diccionario)
persona = {"nombre": "Ana", "edad": 22}
print(persona)

# set (conjunto)
numeros = {1, 2, 3, 4, 5}
print(numeros)


# -----------------------------
# Conversión de tipos
# -----------------------------
# A veces necesitamos cambiar un tipo de dato por otro

numero = 10
numero_como_texto = str(numero)
print("Tipo convertido:", type(numero_como_texto))

texto = "25"
texto_a_numero = int(texto)
print("Suma:", texto_a_numero + 5)

# Si el texto no es convertible, Python da error:
# int("abc")  # ValueError


# -----------------------------
# Entrada de datos por teclado
# -----------------------------
# input() siempre devuelve un texto (str)

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
print("Hola", nombre, "tienes", edad, "años")

# Para operar con números, debemos convertir el input:
edad = int(input("Ingresa tu edad nuevamente (en número): "))
print("El año que viene tendrás:", edad + 1)


# -----------------------------
# Mini práctica
# -----------------------------
"""
Pide al usuario su nombre, edad y altura
Calcula cuántos años tendrá dentro de 5 años.
Muestra todo en una frase.
"""

nombre = input("Nombre: ")
edad = int(input("Edad: "))
altura = float(input("Altura (en metros): "))

edad_futura = edad + 5

print(f"Hola {nombre}, en 5 años tendrás {edad_futura} años y seguirás midiendo {altura} m.")


# -----------------------------
# Reto final (para practicar)
# -----------------------------
"""
Escribe un programa que:
- Pida al usuario 2 números
- Los convierta a enteros
- Muestre la suma, resta, multiplicación y división
"""

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

print("Suma:", n1 + n2)
print("Resta:", n1 - n2)
print("Multiplicación:", n1 * n2)
print("División:", n1 / n2)

