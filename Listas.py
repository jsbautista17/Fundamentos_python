# listas ---------------------------------

# estructura de una list ----------------

lista = ["dato_!", "dato_2", "dato_3"]
#print(type(lista))

# lista mixta ---------------------------

lista_mixta = ["hola", 123, 3.14, True, ["adso", "sst"]]
#print(lista_mixta)

# lista de aprendices adso 3233140 ----------------

aprendices = ["juan", "pedro", "alexa", "diana", "raul"]
#print(aprendices[4])

# modificar un elemento de la lista ---------------
aprendices[4] = "maria"
#print(aprendices)
#print(aprendices[4])

# consultar rangos de elementos de la lista ----------
#print(aprendices[0:3]) # imprime desde el indice 0 hasta el 2
#print(aprendices[0::2]) # imprime saltandose 1

# concatenar listas -------------------------
programas_tecnicos = ["adsi", "sst", "minas"]
programas_tecnologos = ["adso", "sistemas", "topografia"]

programas = programas_tecnicos + programas_tecnologos
#print(programas)
#print(programas_tecnicos[0:2], programas_tecnologos[0:1])

# extender listas .extend() ----------------
nuevos_programas = ["ia", "agronomia", "adsi"]
programas_tecnicos.extend(nuevos_programas)
#print(programas_tecnicos)

# medir la longitud de una liota .len() -----------------
#print(len(programas_tecnicos))

# contar elementos repetidos en una lista .count() -----------------
#print(programas_tecnicos)
#print(programas_tecnicos.count("adsi")) # cuenta cuantas veces se repite el elemento 

# obtener el indice de un elemento .index() -----------------
#print(programas_tecnicos)
#print(programas_tecnicos.index("ia")) # devuelve el indice del elemento

# copiar una lista nueva .copy() -----------------
nueva_lista_aprendices = aprendices.copy()
#print(nueva_lista_aprendices)

# agregar un elemento a la lista .append() -----------------
nueva_lista_aprendices.append("carlos")
#print(nueva_lista_aprendices)

#add = input("Ingrese un nuevo aprendiz: ")
#nueva_lista_aprendices.append(add)
#print(nueva_lista_aprendices)

# agregar un nuevo elemento en una posicion del indice .insert() -----------------
nueva_lista_aprendices.insert(2, "tata")
#print(nueva_lista_aprendices)

# eliminar un elemento de la lista -------------

# .remove() elimina la primera ocurrencia de la lista ------------
nueva_lista_aprendices.remove("juan")
#print(nueva_lista_aprendices)
 
# .pop() elimina el elemento segun su indice -------------
nueva_lista_aprendices.pop(2)
#print(nueva_lista_aprendices)

# .clear() elimina todos los elementos de la lista -------------
#nueva_lista_aprendices.clear()
#print(nueva_lista_aprendices)

# ordenar la lista: ------------

# ordenar ascendentemente A-Z .sort()
nueva_lista_aprendices.sort()
#print(nueva_lista_aprendices)

# ordenar descendentemente Z-A .reversed()
nueva_lista_aprendices.reverse()
#print(nueva_lista_aprendices)

# buscar un elemento en la lista .in() -------------
if "felipe" in nueva_lista_aprendices:
    print("el aprendiz se encuentra en la lista")
else:
    print("el aprendiz no se encuentra en la lista")
    
    