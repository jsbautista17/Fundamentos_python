# match: dias de la semana

#dias = int(input("ingrese el numero del dia de la semana: "))
"""
match dias:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3:
        print("miercoles")
    case 4:
        print("jueves")
    case 5:
        print("viernes")
    case 6:
        print("sabado")
    case 7:
        print("domingo")
    case _:
        print("el numero ingresado no corresponde a ningun dia de la semana")
"""
# ejercicio: faltas de asistencia

falta_aprendiz = input("ingrese la falta del aprendiz: ").lower() # convertir a minusculas
match falta_aprendiz:
    case "comer":
        print("llamdo de atencion por comer en formacion")
    case "impunctualidad":
        print("llamado de atencion por legar tarde")
    case "uniforme":
        print("llamdo de atencion por no portar el unifornme")
    case "jugar":
        print("llamado de atencion por jugar en formacion")
    case _:
        print("aprendiz sin faltas")


