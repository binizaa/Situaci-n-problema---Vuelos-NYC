from necesidadCliente import mes_nombre

def solicitarOrigen():
    return input("Ingresa origen:")

def solicitarDestino():
    return input("Ingresa destino:")

def solicitarFecha():
    fecha = input("Ingresa la fecha (dd/mm/aaaa): ")
    dia, mes, anio = fecha.split('/')
    return [int(dia), mes_nombre(int(mes)), int(anio)]

def solicitarVariable():
    return input("Introduce variable: ")

def solicitarCriterio():
    print("Menú de criterios:")
    print("1. Tiempo en horas")
    print("2. Distancia en kilómetros")
    opcion = int(input("Elige una opción (1-2): "))
    
    if opcion == 1:
        return "Tiempo_Hr"
    elif opcion == 2:
        return " Distancia_Km"
    else:
        print("Opción no válida, por favor elige entre 1 y 2.")
        return solicitarCriterio() 

def solicitarTailum():
    return input("Ingresa el número de cola del avión: ")

def solicitarEstadoVuelo():
    print("Menú de estado del vuelo:")
    print("1. Vuelo anticipado")
    print("2. Vuelo retrasado")
    print("3. Vuelo a tiempo")
    
    opcion = int(input("Elige una opción (1-3): "))
    
    if opcion == 1:
        return "Vuelo anticipado"
    elif opcion == 2:
        return "Vuelo retrasado"
    elif opcion == 3:
        return "Vuelo a tiempo"
    else:
        print("Opción no válida, por favor elige entre 1 y 3.")
        return solicitarEstadoVuelo() 