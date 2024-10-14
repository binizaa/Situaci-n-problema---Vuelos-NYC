from menu import solicitarEstadoVuelo, solicitarFecha, solicitarOrigen
from usuario import Usuario
import pandas as pd
from autenticacion import login
from menu import *
from necesidadCliente import datos_completos, mes_nombre, getLugar, mes_nombre, estatus_retraso

#Necesidades del cliente
datos_completos = datos_completos() #4

datos_completos["Meses"] = datos_completos["month"].apply(mes_nombre) #5

datos_completos["Distancia_Km"] = datos_completos["distance"] * 1.60934 #6

datos_completos["Tiempo_Hr"] = datos_completos["air_time"]/60 #7

datos_completos["Velocidad_promedio"] = (datos_completos["Distancia_Km"]/ datos_completos["Tiempo_Hr"]).round(2) #8

datos_completos["Origen"] = datos_completos["origin"].apply(getLugar) #9

datos_completos["Destino"] = datos_completos["dest"].apply(getLugar)

datos_completos["Status_atraso"] = datos_completos["dep_delay"].apply(estatus_retraso) #10

#Menu funciones
def contar_vuelos_origen_destino(origen, destino):
    if origen not in datos_completos["origin"].unique():
        print(f"Error: El origen {origen} no es válido.")
        return
    if destino not in datos_completos["dest"].unique():
        print(f"Error: El destino {destino} no es válido.")
        return
        
    total_vuelos = len(datos_completos.loc[(datos_completos["origin"] == origen) & (datos_completos["dest"] == destino)])
    print(f"Total de vuelos desde {origen} a {destino}: {total_vuelos}")

def contar_vuelos_origen_fecha(): #FALTAA
    lugar = input("Ingresa el origen: ")
    fecha = input("Ingresa la fecha: ")

    #print(datos_completos[datos["origin"]==])

def resumen_estadistico_vuelos_origen_variable(origen, variable):
    if origen not in datos_completos["origin"].unique():
        print(f"Error: El origen {origen} no es válido.")
        return
    if variable not in datos_completos.columns:
        print(f"Error: La variable {variable} no existe en los datos.")

    datos = datos_completos.loc[datos_completos["origin"] == origen, variable]

    if datos.empty:
        print(f"No se encontraron datos para el origen {origen} y la variable {variable}.")
        return
    
    valor_minimo = datos.min()
    valor_maximo = datos.max()
    media = datos.mean()
    desviacion_estandar = datos.std()
    print(f"El valor mínimo registrado para la variable {variable} es de: {valor_minimo} ")
    print(f"El valor máximo registrado para la variable {variable} es de: {valor_maximo} ")
    print(f"El valor promedio registrado para la variable {variable} es de: {media} ")
    print(f"El valor de la desviación estándar para la variable {variable} es de: {desviacion_estandar} ")


def resumen_retrasos_vuelos_origen():
    print("Realizando resumen de retrasos de los vuelos según el aeropuerto de origen...")

def resumen_criterio_fecha(criterio, mes, dia):
    dias_meses = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31,
    }

    if mes <1 or mes >12:
        print("El valor del mes es inválido.")
        return
    
    if dia <1 or dia > dias_meses[mes]:
        print(f"El valor del día es inválido para el mes {mes}.")
        return
    
    datos = datos_completos[(datos_completos["month"] == mes) & (datos_completos["day"] == dia)]

    if criterio == "Tiempo_Hr":
        tiempo = datos["Tiempo_Hr"].sum()
        print(f"El total de horas de todos los vuelos realizados el {dia} de {mes} es de: {tiempo}.")
    
    elif criterio == "Distancia_Km":
        distancia = datos["Distancia_Km"].sum()
        print(f"El total de kilómetros de todos los vuelos realizados el {dia} de {mes} es de {distancia}.")
    else:
       print(f"El criterio debe ser 'Distancia_Km' o 'Tiempo_Hr'.")
       return 

def contar_aviones_aeropuerto_vuelos():
    print("Realizando conteo de aviones según el aeropuerto y el número de vuelos realizados...")

def funcionalidad_personalizada():
    print("Ejecutando funcionalidad personalizada...")

def finalizar_programa():
    print("Finalizando el programa...")
    exit()

def mostrar_menu():
    opcValida = False
    while opcValida == False:
        
        print("\nMenú:")
        print("a. Cantidad de vuelos según su origen y destino.")
        print("b. Total de vuelos según su origen y una determinada fecha.")
        print("c. Resumen estadístico de los vuelos según el aeropuerto de origen y la variable seleccionada.")
        print("d. Resumen de retrasos de los vuelos según el aeropuerto de origen.")
        print("e. Resumen según el criterio seleccionado y una fecha.")
        print("f. Conteo de aviones según el aeropuerto y el número de vuelos realizados.")
        print("g. Funcionalidad personalizada.")
        print("x. Finalizar el programa.")
        
        opcion = input("Ingrese una opción: ").lower()

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


#usuario_actual = login()
#print(f"Usuario actual: {usuario_actual}")

#print(datos_completos[1:3])

#Funciones a,c,e,f,x
def contar_vuelos_origen_destino(origen, destino):
    if origen not in datos_completos["origin"].unique():
        print(f"Error: El origen {origen} no es válido.")
        return
    if destino not in datos_completos["dest"].unique():
        print(f"Error: El destino {destino} no es válido.")
        return
        
    total_vuelos = len(datos_completos.loc[(datos_completos["origin"] == origen) & (datos_completos["dest"] == destino)])
    print(f"Total de vuelos desde {origen} a {destino}: {total_vuelos}")

def resumen_estadistico_vuelos_origen_variable(origen, variable):
    if origen not in datos_completos["origin"].unique():
        print(f"Error: El origen {origen} no es válido.")
        return
    if variable not in datos_completos.columns:
        print(f"Error: La variable {variable} no existe en los datos.")

    datos = datos_completos.loc[datos_completos["origin"] == origen, variable]

    if datos.empty:
        print(f"No se encontraron datos para el origen {origen} y la variable {variable}.")
        return
    
    valor_minimo = datos.min()
    valor_maximo = datos.max()
    media = datos.mean()
    desviacion_estandar = datos.std()
    print(f"El valor mínimo registrado para la variable {variable} es de: {valor_minimo} ")
    print(f"El valor máximo registrado para la variable {variable} es de: {valor_maximo} ")
    print(f"El valor promedio registrado para la variable {variable} es de: {media} ")
    print(f"El valor de la desviación estándar para la variable {variable} es de: {desviacion_estandar} ")

def resumen_retrasos_vuelos():
    origen = solicitarOrigen()
    opcion = solicitarEstadoVuelo()  

    if origen in ["JFK", "EWR", "LGA"]:
            salida = datos_completos[(datos_completos["origin"] == origen) & 
                                     (datos_completos["dep_delay"]) & 
                                     (datos_completos["Status_atraso"] == opcion)]
            salidan = len(salida)
            llegada = datos_completos[(datos_completos["origin"] == origen) & 
                                      (datos_completos["arr_delay"]) & 
                                      (datos_completos["Status_atraso"] == opcion)]
            llegadan = len(llegada)
            todos = datos_completos[(datos_completos["origin"] == origen) & 
                                    (datos_completos["Status_atraso"] == opcion)]
            todosn = len(todos)
    print(f"Resumen de vuelos {opcion} en el aeropuerto {origen}: ")
    print(f"Salida: Hubo {salidan} vuelos {opcion}")
    print(f"Llegada: Hubo {llegadan} vuelos {opcion}")
    print(f"Todos: Hubo {todosn} vuelos {opcion}")

#Tienes que ver si hay años bisiestos, y corregir lo de los meses
def resumen_criterio_fecha(criterio, mes, dia):
    dias_meses = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31,
    }

    if mes <1 or mes >12:
        print("El valor del mes es inválido.")
        return
    
    if dia <1 or dia > dias_meses[mes]:
        print(f"El valor del día es inválido para el mes {mes}.")
        return
    
    datos = datos_completos[(datos_completos["month"] == mes) & (datos_completos["day"] == dia)]

    if criterio == "Tiempo_Hr":
        tiempo = datos["Tiempo_Hr"].sum()
        print(f"El total de horas de todos los vuelos realizados el {dia} de {mes} es de: {tiempo}.")
    
    elif criterio == "Distancia_Km":
        distancia = datos["Distancia_Km"].sum()
        print(f"El total de kilómetros de todos los vuelos realizados el {dia} de {mes} es de {distancia}.")
    else:
       print(f"El criterio debe ser 'Distancia_Km' o 'Tiempo_Hr'.")
       return 
    
def funcionalidad_personalizada():
    fecha = solicitarFecha()
    dia,mes,anio = fecha

    print(f"Aeropuertos y ciudades con más vuelos el día {dia}/{mes}/{anio}")
    
    aeropuerto = datos_completos[(datos_completos["day"] == dia) &
                             (datos_completos["month"] == mes) &
                             (datos_completos["year"] == anio)]["origin"].mode()
    
    print("Aeropuertos con más salidas:")
    
    for a in aeropuerto: 
        salida = datos_completos[(datos_completos["day"] == dia) &
                             (datos_completos["month"] == mes) &
                             (datos_completos["year"] == anio) &
                             (datos_completos["origin"] == a)]
        salidan = len(salida)
        print(f"El aeropuerto {a} tuvo {salidan} vuelos")

    ciudad = datos_completos[(datos_completos["day"] == dia) &
                             (datos_completos["month"] == mes) &
                             (datos_completos["year"] == anio) ]["dest"].mode()
    
    print("Ciudades con más llegadas:")
    
    for c in ciudad: 
        llegada = datos_completos[(datos_completos["day"] == dia) &
                             (datos_completos["month"] == mes) &
                             (datos_completos["year"] == anio) &
                             (datos_completos["dest"] == c)]
        llegadan = len(llegada)
        print(f"La ciudad {c} tuvo {llegadan} vuelos")
