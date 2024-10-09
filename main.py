from usuario import Usuario
import pandas as pd
from autenticacion import login

def contar_vuelos_origen_destino():
    print("Contabilizando la cantidad de vuelos según su origen y destino...")

def contar_vuelos_origen_fecha():
    print("Contabilizando el total de vuelos según su origen y una determinada fecha...")

def resumen_estadistico_vuelos_origen_variable():
    print("Realizando resumen estadístico de los vuelos según el aeropuerto de origen y la variable seleccionada...")

def resumen_retrasos_vuelos_origen():
    print("Realizando resumen de retrasos de los vuelos según el aeropuerto de origen...")

def resumen_criterio_fecha():
    print("Realizando resumen según el criterio seleccionado y una fecha...")

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

usuario_actual = login()

print(f"Usuario actual: {usuario_actual}")
