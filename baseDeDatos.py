import pandas as pd

class BaseDeDatos:

    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
    
    def read(self):
        return pd.read_csv(self.nombreArchivo)