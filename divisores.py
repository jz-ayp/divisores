"""
Dados dos números, determinar si uno es divisor del otro
"""

# Entradas
numero1 = eval(input("Introduzca el primer número: "))
numero2 = eval(input("Introduzca el segundo número: "))

# Proceso
if numero2 !=0 and numero1 % numero2 == 0:
	resultado = f"El número {numero1} es múltiplo del {numero2}."
elif numero1 !=0 and numero2 % numero1 == 0:
    resultado = f"El número {numero2} es múltiplo del {numero1}."
else:
	resultado = "Ninguno de los números es múltiplo del otro."

# Salidas
print(resultado)
