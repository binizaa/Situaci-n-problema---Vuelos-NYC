from necesidadCliente import datos, mes_nombre, getLugar, estatus_retraso
from solicitudes import *

datos_completos = datos()  # 4

datos_completos["Meses"] = datos_completos["month"].apply(mes_nombre)  # 5
datos_completos["Distancia_Km"] = datos_completos["distance"] * 1.60934  # 6
datos_completos["Tiempo_Hr"] = datos_completos["air_time"] / 60  # 7
datos_completos["Velocidad_promedio"] = (datos_completos["Distancia_Km"] / datos_completos["Tiempo_Hr"]).round(2)  # 8
datos_completos["Origen"] = datos_completos["origin"].apply(getLugar)  # 9
datos_completos["Destino"] = datos_completos["dest"].apply(getLugar)
datos_completos["Status_atraso"] = datos_completos["dep_delay"].apply(estatus_retraso)  # 10


#---------------Opcion A---------------
def contar_vuelos_origen_destino():

    print("\n---------------Opcion A---------------")
    origen = solicitarOrigen()
    destino = solicitarDestino()

    if origen not in datos_completos["Origen"].unique():
        print(f"Error: No hay vuelos en ese {origen}.")
        return
    if destino not in datos_completos["Destino"].unique():
        print(f"Error: No hay vuelos en ese {destino}.")
        return

    total_vuelos = len(datos_completos[(datos_completos["Origen"] == origen) & (datos_completos["Destino"] == destino)])

    print(f"Total de vuelos desde {origen} a {destino}: {total_vuelos}")

#---------------Opcion  B---------------
def contar_vuelos_origen_fecha(): 
    print("\n---------------Opcion B---------------")

    origen = solicitarOrigen()
    fecha = solicitarFecha()

    total_vuelos = datos_completos[
        (datos_completos["day"] == fecha[0]) & 
        (datos_completos["Meses"] == fecha[1]) & 
        (datos_completos["year"] == fecha[2]) & 
        (datos_completos["Origen"] == origen)
    ]

    fecha_formateada = f"{fecha[0]}/{fecha[1]}/{fecha[2]}"

    print(f"Total de vuelos desde {origen} en la fecha {fecha_formateada}: {len(total_vuelos)}")

#---------------Opcion  C---------------
def resumen_estadistico_vuelos_origen_variable():
    print("\n---------------Opcion C---------------")

    origen = solicitarOrigen()
    variable = solicitarVariable()

    if origen not in datos_completos["Origen"].unique():
        print(f"Error: No hay vuelos en ese {origen}.")
        return

    datos = datos_completos.loc[datos_completos["Origen"] == origen, variable]

    valor_minimo = datos.min()
    valor_maximo = datos.max()
    media = datos.mean()
    desviacion_estandar = datos.std()
    print(f"\nEl valor mínimo registrado para la variable {variable} es de: {valor_minimo:.2f} ")
    print(f"El valor máximo registrado para la variable {variable} es de: {valor_maximo:.2f} ")
    print(f"El valor promedio registrado para la variable {variable} es de: {media:.2f} ")
    print(f"El valor de la desviación estándar para la variable {variable} es de: {desviacion_estandar:.2f} ")

#---------------Opcion  D---------------
#Checar array delay
def resumen_retrasos_vuelos_origen():
    print("\n---------------Opcion D---------------")

    origen = solicitarOrigen()
    opcion = solicitarEstadoVuelo()  

    salida = datos_completos[(datos_completos["Origen"] == origen) & 
                            (datos_completos["dep_delay"]) & 
                            (datos_completos["Status_atraso"] == opcion)]
    salidan = len(salida)
    llegada = datos_completos[(datos_completos["Origen"] == origen) & 
                                (datos_completos["arr_delay"]) & 
                                (datos_completos["Status_atraso"] == opcion)]
    llegadan = len(llegada)
    todos = datos_completos[(datos_completos["Origen"] == origen) & 
                            (datos_completos["Status_atraso"] == opcion)]
    todosn = len(todos)
    
    print(f"Resumen de vuelos {opcion} en el aeropuerto {origen}: ")
    print(f"Salida: Hubo {salidan} vuelos")
    print(f"Llegada: Hubo {llegadan} vuelos")
    print(f"Todos: Hubo {todosn} vuelos")

#---------------Opcion  E---------------
def resumen_criterio_fecha():
    print("\n---------------Opcion E---------------")

    criterio = solicitarCriterio()
    fecha = solicitarFecha()

    dia = fecha[0]
    mes = fecha[1]
    
    datos = datos_completos[(datos_completos["Meses"] == mes) & (datos_completos["day"] == dia)]

    if criterio == "Tiempo_Hr":
        tiempo = datos["Tiempo_Hr"].sum()
        print(f"El total de horas de todos los vuelos realizados el {dia} de {mes} es de: {tiempo:.2f}.")
    
    elif criterio == "Distancia_Km":
        distancia = datos["Distancia_Km"].sum()
        print(f"El total de kilómetros de todos los vuelos realizados el {dia} de {mes} es de {distancia:.2f}.")

#---------------Opcion  F---------------
def contar_aviones_aeropuerto_vuelos():
    print("\n---------------Opcion F---------------")

    tailnum = solicitarTailum()  
    aeropuerto = solicitarAeropuerto() 

    if aeropuerto != "todas":
        total_vuelos = datos_completos[(datos_completos["tailnum"] == tailnum) & (datos_completos["Origen"] == aeropuerto)]
        total_vuelos_count = len(total_vuelos)
        print(f"El avión con número de cola {tailnum} ha tenido {total_vuelos_count} vuelos desde el aeropuerto {aeropuerto}.")
    else:
        total_vuelos = datos_completos[(datos_completos["tailnum"] == tailnum)]
        total_vuelos_count = len(total_vuelos)
        print(f"El avión con número de cola {tailnum} ha tenido {total_vuelos_count} vuelos en total desde los 3 aeropuertos.")

#---------------FUNCIÓN PERSONALIZADA---------------
def funcionalidad_personalizada():
    print("\n---------------FUNCIÓN PERSONALIZADA---------------")
    fecha = solicitarFecha()
    dia,mes,anio = fecha

    print(f"Aeropuertos y ciudades con más vuelos el día {dia}/{mes}/{anio}")
    
    aeropuerto = datos_completos[(datos_completos["day"] == dia) &
                             (datos_completos["Meses"] == mes) &
                             (datos_completos["year"] == anio)]["Origen"].mode()
    
    print("Aeropuertos con más salidas:")
    
    for a in aeropuerto: 
        salida = datos_completos[(datos_completos["day"] == dia) &
                             (datos_completos["Meses"] == mes) &
                             (datos_completos["year"] == anio) &
                             (datos_completos["Origen"] == a)]
        salidan = len(salida)
        print(f"El aeropuerto {a} tuvo {salidan} vuelos")

    ciudad = datos_completos[(datos_completos["day"] == dia) &
                             (datos_completos["Meses"] == mes) &
                             (datos_completos["year"] == anio) ]["Destino"].mode()
    
    print("Ciudades con más llegadas:")
    
    for c in ciudad: 
        llegada = datos_completos[(datos_completos["day"] == dia) &
                             (datos_completos["Meses"] == mes) &
                             (datos_completos["year"] == anio) &
                             (datos_completos["Destino"] == c)]
        llegadan = len(llegada)
        print(f"La ciudad {c} tuvo {llegadan} vuelos")


def finalizar_programa():
    print("Finalizando el programa...")
    exit()

def mostrar_menu():
    opcValida = False
    while opcValida == False:
        print("\n---------------Menú:---------------")
        print("a. Cantidad de vuelos según su origen y destino.")
        print("b. Total de vuelos según su origen y una determinada fecha.")
        print("c. Resumen estadístico de los vuelos según el aeropuerto de origen y la variable seleccionada.")
        print("d. Resumen de retrasos de los vuelos según el aeropuerto de origen.")
        print("e. Resumen según el criterio seleccionado y una fecha.")
        print("f. Conteo de aviones según el aeropuerto y el número de vuelos realizados.")
        print("g. Funcionalidad personalizada.")
        print("x. Finalizar el programa.")
        
        opcion = input("\nIngrese una opción: ").lower()

        opcValida = True
        
        if opcion == 'a':
            contar_vuelos_origen_destino()
        elif opcion == 'b':
            contar_vuelos_origen_fecha()
        elif opcion == 'c':
            resumen_estadistico_vuelos_origen_variable()
        elif opcion == 'd':
            resumen_retrasos_vuelos_origen()
        elif opcion == 'e':
            resumen_criterio_fecha()
        elif opcion == 'f':
            contar_aviones_aeropuerto_vuelos()
        elif opcion == 'g':
            funcionalidad_personalizada()
        elif opcion == 'x':
            finalizar_programa()
        else:
            print("Opción no válida, por favor intente de nuevo.")
            opcValida = False


#Main
mostrar_menu()
