#CONDICIONALES IF/ELIF/ELSE

#ESTRUCTURA DEL CONDICIONAL IF:

if True:
    print("se ejecuto la instruccion")
    
#ejemplo if

edad=19
if edad>18:
    print("eres un adulto")
else:
    print("eres joven")
    

#ESTRUCTURA DEL CONDICIONAL ELIF:

if False:
    print("la primera condicion")
elif False:
    print("la segunda condicion")
elif False:
    print("la tercera condicion")
else:
    print("todas las condiciones son falsas")
    
    

#EJERCICIO CLASIFICACION DE EDAD

edad= 30

if edad<18:
    print("eres menor de edad")
elif edad >=18 and edad <65:
    print("eres un adulto ")
else:
    print("eres un adulto mayor")
    
    
#ESTRUCTURA CONDICIONAL ANIDADO

if True:
    if False:
         print("se ejecuta la instruccion")
    elif True:
        print("se ejecuta la instruccion (elif)")
    else:
        print("no se ejecuta la instruccion")
else:
        print("no se ejecuta la instruccion")
        


#EJERCICIO CLASIFICACION DE EDADES

edad=13 
if edad <18:
    if edad >12 and edad <18:
        print ("Adolescente")
    else:
        print("Niño")
else:
    
    if edad>=18 and edad<60:
         print("eres un Adulto")
    else:
        print("Eres un adulto mayor")
        
        
#EJERCICIO MARCADOR PARTIDO 

marcador_Colombia=int(input("Ingresa el marcador de colombia"))
marcador_chile=int(input("ingresa marcador chile"))

if marcador_Colombia > marcador_chile:
    print("ganamos el partido :)")
elif marcador_chile== marcador_Colombia:
    print("quedamos empatados :/")

else:
    print("perdimos el partido :(")
    
    
    
    
    
#OPERADOR TERNARIOOO--------------------------------------------------------

numero=12
if numero%2 ==0:
    print("el numero es par")
    
else:
    print("el numero es impar")
    
print("el numero es par" if numero%2 ==0 else"el numero es impar")
    
