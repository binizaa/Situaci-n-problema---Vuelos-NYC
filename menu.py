from necesidadCliente import datos_completos

def contar_vuelos_origen_destino(origen, destino):
    global datos_completos
    
    if origen not in datos_completos["origin"].unique():
        print(f"Error: El origen {origen} no es válido.")
        return
    if destino not in datos_completos["dest"].unique():
        print(f"Error: El destino {destino} no es válido.")
        return
        
    total_vuelos = len(datos_completos.loc[(datos_completos["origin"] == origen) & (datos_completos["dest"] == destino)])
    print(f"Total de vuelos desde {origen} a {destino}: {total_vuelos}")
