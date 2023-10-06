"""
Dados dos números, determinar si uno es divisor del otro
"""

# Entradas
numero1 = eval(input("Introduzca el primer número: "))
numero2 = eval(input("Introduzca el segundo número: "))

# Proceso
if numero1 % numero2 == 0:
	resultado = "El número " + str(numero2) + " es divisor del número " \
        + str(numero1) + "."
elif numero2 % numero1 == 0:
    resultado = "El número " + str(numero1) + " es divisor del número " \
        + str(numero2) + "."
else:
	resultado = "Ninguno de los números es divisor del otro."

# Salidas
print(resultado)
