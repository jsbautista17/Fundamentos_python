#1. Crea actividad3.py. Solicita al usuario su peso en kg y su estatura en metros.
#2. Calcula el Índice de Masa Corporal con la fórmula: IMC = peso / (estatura ** 2).
#3. Usa if / elif / else para clasificar el resultado:
#• Bajo peso (< 18.5),
#• Normal (18.5–24.9),
#• Sobrepeso (25–29.9),
#• Obesidad (>= 30).
#4. Imprime el valor del IMC y su clasificación correspondiente.
#5. Bonus: Valida que el peso y la estatura sean valores positivos antes de calcular.


peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

if peso <= 0 or altura <= 0:
    print("Error: el peso y la altura deben ser valores positivos.")
else:
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc}")

    if imc >= 30:
        print("Usted es obeso")
    elif imc >= 25 and imc < 30:
        print("Usted está en sobrepeso")
    elif imc >= 18.5 and imc < 25:
        print("Usted está en un rango normal")
    else:
        print("Usted está bajo de peso")
