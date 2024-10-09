from usuario import Usuario
from baseDeDatos import BaseDeDatos
import pandas as pd


def autenticar(nombre, contrasena):
    global BDUsuario  
    for i in range(len(BDUsuario)):
        if BDUsuario["Usuario"].iloc[i] == nombre and BDUsuario["Contraseña"].iloc[i] == contrasena:
            return True
    return False

def iniciar_sesion():
    global usuario_actual
    intentoLogin = 3

    while intentoLogin > 0:
        print("\n---------------Iniciar sesión---------------")
        
        intentoLogin -= 1

        nombre_usuario = input("Ingresa tu nombre de usuario: ")
        contrasena = input("Ingresa tu contraseña: ")

        if autenticar(nombre_usuario, contrasena):
            usuario_actual = Usuario(nombre_usuario, contrasena)
            print(f"Bienvenido {usuario_actual}, has iniciado sesión correctamente.\n")
            return usuario_actual
        else:
            print(f"Contraseña o usuario incorrecto. Te quedan {intentoLogin} intentos")
    
    print("Se han agotado los intentos de inicio de sesión.\nPrograma Terminado")
    exit()

# Función para crear cuenta
def crear_cuenta():
    print("\n---------------Crear cuenta---------------")
    global usuario_actual
    nombre_usuario = input("Elige un nombre de usuario: ")
    contrasena = input("Elige una contraseña: ")
    
    usuario_actual = Usuario(nombre_usuario, contrasena)

    # Guardamos la nueva cuenta en el archivo CSV
    usuario_actual.agregarRegistro("datosUsuarios.csv") 

    print(f"Cuenta creada exitosamente para {usuario_actual}.")

    return usuario_actual
    
# Función principal de login
def login():
    global BDUsuario 
    BDU = BaseDeDatos("datosUsuarios.csv")
    BDUsuario = BDU.read()  # Cargamos los datos de los usuarios

    while True:
        print("\nBienvenido al sistema. ¿Qué te gustaría hacer?")
        print("1. Iniciar sesión")
        print("2. Crear cuenta (Aun no lo corras, tiene un error, trabajanding -Bini)")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == '1':
            return iniciar_sesion()
        elif opcion == '2':
            return crear_cuenta()
        elif opcion == '3':
            print("Saliendo del sistema. ¡Hasta luego!")
            exit()
        else:
            print("Opción no válida. Intenta de nuevo.")
