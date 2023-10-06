"""
Dados dos números, determinar si uno es divisor del otro
"""

# Entradas
numero1 = eval(input("Introduzca el primer número: "))
numero2 = eval(input("Introduzca el segundo número: "))

# Proceso
if numero1 % numero2 == 0:
	resultado = f"El número {numero1} es múltiplo del número {numero2}."
elif numero2 % numero1 == 0:
    resultado = f"El número {numero2} es múltiplo del número {numero1}."
else:
	resultado = "Ninguno de los números es divisor del otro."

# Salidas
print(resultado)
