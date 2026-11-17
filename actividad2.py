#1. Crea actividad2.py y solicita al usuario que ingrese tres calificaciones parciales usando input() (recuerda convertirlas a float con float()).
#2. Calcula el promedio de las tres notas.
#4. Determina si el estudiante aprueba (promedio >= 3.0) usando un operador de comparación e imprime el resultado.
#5. Muestra todos los resultados con formato legible. Investiga el método round() para redondear el promedio a dos decimales.


cal_1=float(input ("ingresa la calificacion 1:  "))
cal_2=float(input ("ingresa la calificacion 2:  "))
cal_3=float(input ("ingresa la calificacion 3:  "))
suma= (cal_1 + cal_2 + cal_3)

promedio=(suma/3)

print(f"la suma de sus nota es {suma} y su promedio es igual {round(promedio,3)}")


#3. Calcula cuántos puntos le faltan al estudiante para alcanzar la nota máxima (5.0) usando operadores aritméticos.

puntos_faltantes= (5.0 - promedio)

print(f"te faltan:  {round(puntos_faltantes,3)} para la nota maxima ")