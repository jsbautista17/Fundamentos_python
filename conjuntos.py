# estructura de un conjunto -----------------
"""
conjunto = {"python", "java", "c#", "js"}
print(conjunto)
print(type(conjunto))

conjunto_2 = set() # se declara el conjunto vacio y luego se llena
print(conjunto_2)
print(type(conjunto_2))
"""
# creaccion de un conjunto -------------------
"""
lenguajes = {"python", "java", "c#", "js", "python"} # no permite duplicados
print(lenguajes)
print(type(lenguajes))
"""
# metodos de los conjuntos ------------------

frutas = {"mango", "guayaba", "mora", "manzana", "mandarina"}

# agregar un nuevo elemento ------------
"""
frutas.add("fresas")
print(frutas) #{'guayaba', 'mangos', 'fresas', 'mora'}

frutas.add("mora")
print(frutas)
"""
# eliminar un elemento .remove()------------
"""
frutas.remove("mango")
print(frutas)

frutas.remove("pera")
print(frutas)
"""

# metodo .discard() ------------------ recomendable
"""
frutas.discard("mora")
print(frutas)

frutas.discard("pera")
print(frutas)
"""
# metodo .pop(), eliminacion aleatoria ---------------
"""
elemento = frutas.pop()
print(elemento)
print(frutas)
"""

# metodo .clear() limpia todos los elementos --------------
"""
frutas.clear()
print(frutas)
"""

# eliminar todo el conjunto "del" ---------------------
"""
del frutas
print(frutas)
"""

# verificar la pertenencia de un elemento en un conjunto: busqueda --------------
"""
anime = {"dragon_ball", "naruto", "solo_leveling"}
print("naruto" in anime)#true
print("one_punch" in anime)#true
"""
# operaciones de la teoria de conjuntos ----------------------

aprendices_formacion = {"yenifer", "liz", "diana", "alejandra", "adriana"}
aprendices_apoyo = {"diana", "adriana", "luis", "sebitas", "oscar"}

# union de conjuntos .union() -------------------

union = aprendices_formacion | aprendices_apoyo
print(union)

union_2 = aprendices_formacion.union(aprendices_apoyo)
print(union_2)

#{'adriana', 'yenifer', 'luis', 'sebitas', 'liz', 'oscar', 'alejandra', 'diana'}

# interseccion, extrae los elementos que se repiten en los conjuntos

# operador interseccion "&"

interseccion_aprendices = aprendices_formacion & aprendices_apoyo
print(interseccion_aprendices) #{'diana', 'adriana'}

# metodo .interseccion()

interseccion_aprendices_2 = aprendices_formacion.intersection(aprendices_apoyo)
print(interseccion_aprendices_2) #{'diana', 'adriana'}

# diferencia, extrae los elementos que no se repiten en los dos conjuntos

diferencia_aprendices = aprendices_formacion - aprendices_apoyo
print(diferencia_aprendices) # {'alejandra', 'liz', 'yenifer'}

# metodo .diferencia()

diferencia_aprendices_2 = aprendices_formacion.difference(aprendices_apoyo)
print(diferencia_aprendices_2) # {'alejandra', 'liz', 'yenifer'}

# diferencia simetrica, extrae los elementos que no se repiten en los dos conjuntos

diferencia_simetrica = aprendices_formacion ^ aprendices_apoyo
print(diferencia_simetrica) # {'oscar', 'alejandra', 'liz', 'sebitas', 'luis', 'yenifer'}

# metodo diferencia .simetrica()

diferencia_simetrica_2 = aprendices_formacion.symmetric_difference(aprendices_apoyo)
print(diferencia_simetrica_2) # {'oscar', 'alejandra', 'liz', 'sebitas', 'luis', 'yenifer'}