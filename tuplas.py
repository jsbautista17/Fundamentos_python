 # estructura de las tuplas -----------

tupla = ("elemento_1","elemento_2","elemento_3")
#print(type(tupla))

tupla_2 = "a", "b", "c"
#print(type(tupla_2))

tupla_3 = ("hola",) # la coma hace que sea una tupla
#print(type(tupla_3))

tupla_4 = tuple("hola") # convertir en tupla
#print(tupla_4)
#print(type(tupla_4))

tupla_mixta = ("hola", 123, 13.1416, True,[1,2,3])
#print(tupla_mixta)


 # ejemplo de uso ------------------------------

aprendices = ("dayana", "luis", "john", "oscar", "john")
#print(aprendices)

 # acceder a un elemento de la tupla -----------------
#print(aprendices[0])  # acceder al primer elemento
#print(aprendices[1])  # acceder al segundo elemento
#print(aprendices[2])  # acceder al tercer elemento
#print(aprendices[3])  # acceder al cuarto elemento

 # modificar un elemento de la tupla -----------------
#aprendices[0] = "diana"
#print(aprendices) genera un error porque las tuplas son inmutables


 # consultar rangos de elementos -------------
#print(aprendices[0:2])


 # concatenar dos tuplas -----------
tupla_uno = (1,2,3)
tupla_dos = (4,5,6)

tupla_suma = tupla_uno + tupla_dos
#print(tupla_suma)

 # multiplicar una tupla -------------
tupla_multi = tupla_uno * 3
#print(tupla_multi)

 # metodos de las tuplas -----------------
 # medir la longitud de una tupla .len() --------
 
#print(len(aprendices))

 # contar los elementos repetidos ----------
#print(aprendices.count("john"))

 # obtener el indice de un elemento .index() -----------
#print(aprendices.index("luis")) # devuelve la posicion del primer elemento que encuentra

 # modificar una tupla conviertiendola en lista -----------
lenguajes = ("html", "css", "js", "py")
"""print(lenguajes)
print(type(lenguajes))

lenguajes_lista = list(lenguajes)
print(lenguajes_lista)
print(type(lenguajes_lista))

lenguajes_lista.append("dgango")
print(lenguajes_lista)

lenguajes = tuple(lenguajes_lista)
print(lenguajes)"""

 # comprobacion de pertenencia con "in" busqueda
""" 
print("py" in lenguajes) #true
print("c#" in lenguajes) #false

if "html" in lenguajes:
    print("fue encontrado en la tupla")
else:
    print("no fue encontrado en la tupla")
"""
 # empaquetar y desempaquetar tuplas -----------------
"""
programa_1 = "adso"
programa_2 = "sst"
programa_3 = "topografia"

tupla_programas = (programa_1, programa_2, programa_3)
print(tupla_programas)
print(type(tupla_programas))
"""

 # desempaquetar tuplas -----------------
tupla_ciudades = ("sogamoso", "duitama", "tunja")

ciudad_1, ciudad_2, ciudad_3 = tupla_ciudades # desempaquetar
#print(ciudad_1)
#print(ciudad_2)
#print(ciudad_3)

# iterar o recorrer una tupla "for"

for ciudad in tupla_ciudades:
    print(ciudad)