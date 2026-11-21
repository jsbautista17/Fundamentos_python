# estructura -----------------------
'''
diccionario = {
    "clave_1": "valor_1",
    "clave_2": "valor_2",
    "clave_3": "valor_3",
}
print(type(diccionario))
print(diccionario)

#diccionario vacio

diccionario_vacio = {}
print(type(diccionario_vacio))
'''

# diccionario con elementos -------------

diccionario_aprendiz = {
    "nombre": "sebas",
    "apellido": "alarcon",
    "ficha": "3233140",
    "edad": 24
}

#print(diccionario_aprendiz)

# obtener un valor ------------------------

#print(diccionario_aprendiz["edad"])
#print(diccionario_aprendiz.get("correo")) # sin error

# obetener solo las claves del diccionario .keys() ------------------
#print(diccionario_aprendiz.keys())

# obetener solo los valores del diccionario .valuese() ------------------
#print(diccionario_aprendiz.values())

# obetener solo los items del diccionario .items() ------------------
#print(diccionario_aprendiz.items())

# agregar un elemento al diccionario -----------------
diccionario_aprendiz["correo"] = "jsbautistaägmail.com"
#print(diccionario_aprendiz)

# MODIFICAR UN ELEMENTO DEL DICCIONARIO -----------------
diccionario_aprendiz["edad"] = 25
#print(diccionario_aprendiz)

# METODO UPDATE() PARA ACTUALIZAR UN VALOR -----------------
diccionario_aprendiz.update({"nombre": "jhon"})
#print(diccionario_aprendiz)

# agregar un nuevo elemento con update() -------------------
diccionario_aprendiz.update({"ciudad": "sogamoso"})
#print(diccionario_aprendiz)

# eliminar un elemento ----------------------------

# eliminar el ultimo elemento con .popitem() ---------------
diccionario_aprendiz.popitem()
#print(diccionario_aprendiz)

# ELIMINAR UN ELEMENTO ESPECIFICO .pop()
diccionario_aprendiz.pop("edad")
#print(diccionario_aprendiz)

# eliminar todos los elementos del diccionario con .clear()
'''
diccionario_aprendiz.clear()
print(diccionario_aprendiz)
'''

# comprobar la pertenencia con in busqueda
'''
print("ficha" in diccionario_aprendiz)
print("cell" in diccionario_aprendiz)

if "edad" in diccionario_aprendiz:
    print("la edad esta dentro del diccionario")
else:
    print("la clave edad no esta en el diccionario")
'''
# recorrer los valores de un diccionario
'''
for clave in diccionario_aprendiz.keys():
    print(clave) # imprime las claves del diccionario

for valor in diccionario_aprendiz.values():
    print(valor) # imprime los valores del diccionario
'''

# recorrer o imprimir las claves y valores ---------------
'''
for clave,valor in diccionario_aprendiz.items():
    print(f"{clave}: {valor}")
'''

# diccionario anidados ---------------------

futbolistas = {
    "nombre_1": {
        "nombre": "james",
        "profesion": "futbolista",
        "posicion": "bolante"
    },
    "nombre_2": {
        "nombre": "messi",
        "profesion": "futbolista",
        "posicion": "media_punta"
    },
    "nombre_3": {
        "nombre": "cr7",
        "profesion": "futbolista",
        "posicion": "delnatero"
    }
}

# acceder a um valor de un diccionario anidado

print(futbolistas["nombre_2"]["nombre"])

# recorrer un diccionario anidado con ciclor for
for futbolista, datos in futbolistas.items():
    print(f"{futbolista}:")
    for clave, valor in  datos.items():
        print(f"{clave}: {valor}")