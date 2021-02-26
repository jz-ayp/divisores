"""
Inserta el encabezado aquí y escribe tu código abajo


# Declaraciones
CONSTANTE = valor

# Entradas
entrada = input()

# Proceso


# Salidas
print(salida)
"""
# Entradas
numero1 = eval(input("Introduzca el primer número: "))
numero2 = eval(input("Introduzca el segundo número: "))

# Proceso
if numero1 % numero2 == 0:
	resultado = "El número " + str(numero1) + " es múltiplo del número " \
        + str(numero2) + "."
elif numero2 % numero1 == 0:
    resultado = "El número " + str(numero2) + " es múltiplo del número " \
        + str(numero1) + "."
else:
	resultado = "Ninguno de los números es múltiplo del otro."

# Salidas
print(resultado)
