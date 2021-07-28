# -*- coding: utf-8 -*-
import sys

# definimos las funciones a utilizar

def suma(a,b):
	return a+b

def resta(a,b):
	return a-b

def multiplicacion(a,b):
	return a*b

def division(a,b):
	return float(a)/b

def potencia(a,b):
	return a**b


# eliminamos el primer elemento de entrada
entrada = sys.argv[1:]

# convertimos a tipo string
entrada_text = ''.join(str(e) for e in entrada)

# eliminamos los espacios
entrada_text = entrada_text.replace(" ", "")


# para cada posible operación
# comprobamos que existe el operador
# y que los datos de la izda y dcha son números

if "+" in entrada_text:
	numeros = entrada_text.split("+")
	try:
		num1 = float(numeros[0])
		num2 = float(numeros[1])

		print(suma(num1,num2))

	except ValueError:
		print("Los valores numéricos no están bien introducidos")

elif "-" in entrada_text:
	numeros = entrada_text.split("-")
	try:
		num1 = float(numeros[0])
		num2 = float(numeros[1])

		print(resta(num1,num2))

	except ValueError:
		print("Los valores numéricos no están bien introducidos")
	
elif "*" in entrada_text:
	numeros = entrada_text.split("*")
	try:
		num1 = float(numeros[0])
		num2 = float(numeros[1])

		print(multiplicacion(num1,num2))

	except ValueError:
		print("Los valores numéricos no están bien introducidos")

elif "/" in entrada_text:
	numeros = entrada_text.split("/")
	try:
		num1 = float(numeros[0])
		num2 = float(numeros[1])

		print(division(num1,num2))

	except ValueError:
		print("Los valores numéricos no están bien introducidos")
	except ZeroDivisionError:
		print("No se pueden realizar divisiones entre cero")

elif "^" in entrada_text:
	numeros = entrada_text.split("^")
	try:
		num1 = float(numeros[0])
		num2 = float(numeros[1])

		print(potencia(num1,num2))

	except ValueError:
		print("Los valores numéricos no están bien introducidos")


