class Proyecto2:

    ERROR_USO = 1

    def __init__(self, args):
        self.aplicacion = Aplicacion(args)

    def ejecuta(self):
        try:
            self.aplicacion.ejecuta()
        except ValueError as e:  
            print(str(e))
            exit(self.ERROR_USO)


class Aplicacion:
    
    def __init__(self, args):
        # Inicializa con los argumentos
        self.args = args

    def ejecuta(self):
        print("HELLO")
        pass


if __name__ == "__main__":
    import sys
    proyecto = Proyecto2(sys.argv[1:])
    proyecto.ejecuta()
