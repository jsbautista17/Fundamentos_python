#operadores aritmeticos

a= 10
b= 3

'''
suma = a + b
print(f"la suma es: {suma}")

resta = a - b
print(f"la resta es: {resta}")

multiplicacion = a * b
print(f"la multiplicacion es: {multiplicacion}")

division = a / b
print(f"la division es: {division}")

exponente = a ** b
print(f"el exponente es: {exponente}")

residuo = a % b
print(f"el residuo es: {residuo}")

raiz = a ** (1/2)
print(f"la raiz es: {raiz}")

division_entera = a // b
print(f"la division entera es: {division_entera}")

modulo = a % b
print(f"el modulo es: {modulo}")
'''

# presedencia de operadores

resultado = a + b * 2
print(f"el resultado es: {resultado}")

resultado_2 = (a + b) * 2
print(f"el resultado_2 es: {resultado_2}")

resultado_3 = a * b // 3
print(f"el resultado_3 es: {resultado_3}")

ejercicio = ((a + b) * (a - b) / (a * b)) - ((a ** b) % 3)
print(f"el ejercicio es: {ejercicio}")


# librerias en python

import math 

print(f"el valor de pi es: {math.pi}")
print(f"el valor de e es: {math.e}")
print(f"el valor de la raiz cuadrada de 16 es: {math.sqrt(16)}")
raiz = 16 ** (1/2)
print(f"la raiz es: {raiz}")

import random
print(f"el numero aleatorio entre 1 y 10 es: {random.randint(1, 10)}")