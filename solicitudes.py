from necesidadCliente import mes_nombre

# Funciones que solicitan los datos

# Función 'solicitarOrigen'
# Solicita al usuario que ingrese el origen del vuelo y lo capitaliza (primera letra en mayúscula).
def solicitarOrigen():
    return input("Ingresa origen: ").capitalize() 

# Función 'solicitarDestino'
# Solicita al usuario que ingrese el destino del vuelo y lo capitaliza (primera letra en mayúscula).
def solicitarDestino():
    return input("Ingresa destino: ").capitalize()  

# Función 'solicitarFecha'
# Solicita al usuario una fecha en formato dd/mm/aaaa, valida el formato, y retorna la fecha en una lista [día, mes (en texto), año].
# Si el formato es incorrecto, vuelve a pedir la fecha.
def solicitarFecha():
    fecha = input("Ingresa la fecha (dd/mm/aaaa): ").strip()
    try:
        dia, mes, anio = fecha.split('/')
        dia, mes, anio = int(dia), int(mes), int(anio)
        return [dia, mes_nombre(mes).capitalize() , anio]  
    except ValueError:
        print("Error: La fecha ingresada no tiene el formato correcto (dd/mm/aaaa).")
        return solicitarFecha() 

# Función 'solicitarCriterio'
# Solicita al usuario que seleccione un criterio de análisis (1 para "Tiempo_Hr", 2 para "Distancia_Km").
# Si elige una opción inválida o si no ingresa un número, vuelve a solicitar la entrada.
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

# Función 'solicitarTailum'
# Solicita el número de cola del avión al usuario. Se devuelve en mayúsculas.
def solicitarTailum():
    return input("Ingresa el número de cola del avión: ").upper()

# Función 'solicitarEstadoVuelo'
# Solicita al usuario que seleccione el estado del vuelo: "Vuelo anticipado", "Vuelo retrasado" o "Vuelo a tiempo".
# Si se selecciona una opción inválida o si no se ingresa un número, vuelve a solicitar la entrada.
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

# Función 'solicitarVariable'
# Muestra un menú con las variables de vuelo disponibles, solicita una opción y retorna la clave de la variable seleccionada.
# Si la selección es inválida o no se ingresa un número, el programa sale.
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