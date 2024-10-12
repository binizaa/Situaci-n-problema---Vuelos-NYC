from necesidadCliente import mes_nombre
from main import datos_completos

# Funciones que solicitan los datos

def solicitarOrigen():
    return input("Ingresa origen: ").capitalize()  

def solicitarDestino():
    return input("Ingresa destino: ").capitalize() 

def solicitarFecha():
    fecha = input("Ingresa la fecha (dd/mm/aaaa): ").strip()
    try:
        dia, mes, anio = fecha.split('/')
        dia, mes, anio = int(dia), int(mes), int(anio)
        return [dia, mes_nombre(mes).capitalize(), anio]  
    except ValueError:
        print("Error: La fecha ingresada no tiene el formato correcto (dd/mm/aaaa).")
        return solicitarFecha()  # Volver a solicitar la fecha si no es válida

def solicitarVariable(): #PENDIENTE CORREGIR
    variable = input("Introduce variable: ")
    if variable not in datos_completos.columns:
        print(f"Error: La variable {variable} no es válida.")
        return solicitarVariable()  # Volver a solicitar la variable si no es válida
    return variable

def solicitarCriterio():
    print("Menú de criterios:")
    print("1. Tiempo en horas")
    print("2. Distancia en kilómetros")
    try:
        opcion = int(input("Elige una opción (1-2): "))
        if opcion == 1:
            return "Tiempo_hr"  # Convertido a formato deseado
        elif opcion == 2:
            return "Distancia_km"  # Convertido a formato deseado
        else:
            print("Opción no válida, por favor elige entre 1 y 2.")
            return solicitarCriterio()  # Volver a solicitar el criterio si no es válido
    except ValueError:
        print("Error: Debes ingresar un número.")
        return solicitarCriterio()  # Volver a solicitar si no es un número

def solicitarTailum(): #CHECAR LO DE LA MAYUSCULA
    return input("Ingresa el número de cola del avión: ").upper()

def solicitarEstadoVuelo():
    print("Menú de estado del vuelo:")
    print("1. Vuelo anticipado")
    print("2. Vuelo retrasado")
    print("3. Vuelo a tiempo")
    try:
        opcion = int(input("Elige una opción (1-3): ").strip())
        if opcion == 1:
            return "Vuelo anticipado"
        elif opcion == 2:
            return "Vuelo retrasado"
        elif opcion == 3:
            return "Vuelo a tiempo"
        else:
            print("Opción no válida, por favor elige entre 1 y 3.")
            return solicitarEstadoVuelo()  # Volver a solicitar si no es válido
    except ValueError:
        print("Error: Debes ingresar un número.")
        return solicitarEstadoVuelo()  # Volver a solicitar si no es un número
