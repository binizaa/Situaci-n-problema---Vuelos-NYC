import csv

class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

    def __str__(self):
        return f"Usuario: {self.nombre}"

    def agregarRegistro(self, archivoRegistros):
        with open(archivoRegistros, mode='a', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow([self.nombre, self.contrasena])
