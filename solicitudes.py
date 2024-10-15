from necesidadCliente import mes_nombre

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
        return [dia, mes_nombre(mes).capitalize() , anio]  
    except ValueError:
        print("Error: La fecha ingresada no tiene el formato correcto (dd/mm/aaaa).")
        return solicitarFecha() 

def solicitarCriterio():
    print("Menú de criterios:")
    print("1. Tiempo en horas")
    print("2. Distancia en kilómetros")
    try:
        opcion = int(input("Elige una opción (1-2): "))
        if opcion == 1:
            return "Tiempo_Hr" 
        elif opcion == 2:
            return "Distancia_Km"  
        else:
            print("Opción no válida, por favor elige entre 1 y 2.")
            return solicitarCriterio()  
    except ValueError:
        print("Error: Debes ingresar un número.")
        return solicitarCriterio() 

def solicitarTailum():
    return input("Ingresa el número de cola del avión: ").upper()

def solicitarEstadoVuelo():
    print("\n---------------Menú de estado del vuelo:---------------")
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


def solicitarVariable():
    variables_map = {
        "dep_time": "Hora de salida real.",
        "sched_dep_time": "Hora programada de salida.",
        "dep_delay": "Retraso en la salida (en minutos).",
        "arr_time": "Hora de llegada real.",
        "sched_arr_time": "Hora programada de llegada.",
        "arr_delay": "Retraso en la llegada (en minutos).",
        "flight": "Número del vuelo.",
        "air_time": "Tiempo de vuelo (en minutos).",
        "distance": "Distancia recorrida (en millas).",
        "hour": "Hora de salida programada (hora).",
        "minute": "Minuto de salida programada."
    }

    print("\n---------------Seleccione una variable---------------")

    keys = list(variables_map.keys())

    for i, key in enumerate(keys, 1):
        print(f"{i}. {variables_map[key]}")

    try:
        seleccion = int(input("\nIngrese el número de la variable: ")) - 1

        if 0 <= seleccion < len(keys):
            return keys[seleccion]  
        else:
            print("Selección inválida.")
            exit()
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        exit()

def solicitarAeropuerto():
    aeropuertos = {
        1: "Jhon F. Kennedy",
        2: "Newark",
        3: "LaGuardia",
        4: "Todas",
        5: "Salir"
    }

    print("\n---------------Menú de Aeropuertos---------------")
    for key, value in aeropuertos.items():
        print(f"{key}. {value}")

    try:
        opcion = int(input("Seleccione un número (1-5): "))

        if opcion == 5:
            print("Saliendo del programa...")
            exit()
        elif opcion in aeropuertos:
            return aeropuertos[opcion].capitalize() 
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")
            return solicitarAeropuerto()  
    except ValueError:
        print("Error: Ingrese un número válido.")
        return solicitarAeropuerto() 