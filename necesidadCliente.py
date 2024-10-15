import pandas as pd

# Mapeo de códigos de aeropuerto a nombres de aeropuertos
lugarMap = {
    "JFK": "Jhon F.Kennedy",
    "EWR": "Newark",
    "LGA": "LaGuardia",
    "ABQ": "Albuquerque",
    "ACK": "Nantucket",
    "ALB": "Albany",
    "ANC": "Anchorage",
    "ATL": "Atlanta", 
    "AUS": "Austin",
    "AVL": "Asheville",
    "BDL": "Bradley",
    "BGR": "Bangor",
    "BHM": "Birmingham",
    "BNA": "Nashville",
    "BOS": "Boston", 
    "BTV": "Burlington",
    "BUF": "Buffalo",
    "BUR": "Burbank",
    "BWI": "Baltimore",
    "BZN": "Bozeman",
    "CAK": "Akron-Canton",
    "CAE": "Columbia",
    "CHAR": "Charlottesville",
    "CHO": "Charlottesville",
    "CHS": "Charleston",
    "CLE": "Cleveland",
    "CLT": "Charlotte",
    "CMH": "Columbus",
    "CRW": "Charleston (West Virginia)",
    "CVG": "Cincinnati",
    "DAY": "Dayton",
    "DCA": "Washington D.C.",
    "DEN": "Denver",
    "DFW": "Dallas/Fort Worth",
    "DSM": "Des Moines",
    "DTW": "Detroit",
    "EGE": "Eagle",
    "EYW": "Key West",
    "FLL": "Fort Lauderdale",
    "GRR": "Grand Rapids",
    "GSO": "Greensboro",
    "GSP": "Greenville",
    "HDN": "Hayden",
    "HNL": "Honolulu",
    "HOU": "Houston",
    "IAD": "Washington Dulles",
    "IAH": "Houston Intercontinental",
    "ILM": "Wilmington",
    "IND": "Indianapolis",
    "JAC": "Jackson Hole",
    "JAX": "Jacksonville",
    "LAX": "Los Ángeles",
    "LEX": "Lexington",
    "LGA": "LaGuardia",
    "LGB": "Long Beach",
    "LAS": "Las Vegas",
    "MCI": "Kansas City",
    "MCO": "Orlando",
    "MDW": "Chicago Midway",
    "MEM": "Memphis",
    "MHT": "Manchester",
    "MIA": "Miami",
    "MKE": "Milwaukee",
    "MSN": "Madison",
    "MSP": "Minneapolis",
    "MSY": "Nueva Orleans",
    "MTJ": "Montrose",
    "MVY": "Martha's Vineyard",
    "MYR": "Myrtle Beach",
    "NASH": "Nashville",
    "OAK": "Oakland",
    "OKC": "Oklahoma City",
    "OMA": "Omaha",
    "ORD": "Chicago O'Hare",
    "ORF": "Norfolk",
    "PBI": "Palm Beach",
    "PDX": "Portland",
    "PHL": "Philadelphia",
    "PHX": "Phoenix",
    "PIT": "Pittsburgh",
    "PSE": "Ponce",
    "PSP": "Palm Springs",
    "PVD": "Providence",
    "PWM": "Portland (Maine)",
    "RDU": "Raleigh-Durham",
    "RIC": "Richmond",
    "ROC": "Rochester",
    "RSW": "Fort Myers",
    "SAN": "San Diego",
    "SAT": "San Antonio",
    "SAV": "Savannah",
    "SBN": "South Bend",
    "SDF": "Louisville",
    "SEA": "Seattle",
    "SFO": "San Francisco",
    "SJC": "San José (California)",
    "SJU": "San Juan",
    "SLC": "Salt Lake City",
    "SMF": "Sacramento",
    "SNA": "Santa Ana",
    "SRQ": "Sarasota",
    "STL": "St. Louis",
    "STT": "St. Thomas",
    "SYR": "Syracuse",
    "TUL": "Tulsa",
    "TPA": "Tampa",
    "TVC": "Traverse City",
    "TYS": "Knoxville",
    "XNA": "Northwest Arkansas",
    "BQN": "Aguadilla"
}

# Mapeo de números de meses a nombres de meses en español
meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

# Función 'datos'
# Esta función carga los datos de tres aeropuertos (JFK, EWR, LGA) desde archivos CSV y los combina en un solo DataFrame.
# Retorna un DataFrame que contiene los datos consolidados de los tres aeropuertos.
def datos():
   JFK = pd.read_csv("./baseDeDatos/JFK.csv")
   EWR = pd.read_csv("./baseDeDatos/EWR.csv")
   LGA = pd.read_csv("./baseDeDatos/LGA.csv")

    # La siguiente sección es un comentario de una fuente de datos alternativa
   '''
   JFK = pd.read_csv("https://raw.githubusercontent.com/Alejandro-FB/Bases-Datos/main/2013%20-%20JFK.csv")
   EWR = pd.read_csv("https://raw.githubusercontent.com/Alejandro-FB/Bases-Datos/main/2013%20-%20EWR.csv")
   LGA = pd.read_csv("https://raw.githubusercontent.com/Alejandro-FB/Bases-Datos/main/2013%20-%20LGA.csv")
   '''
   
   return pd.concat([JFK, EWR, LGA], axis = 0, ignore_index = True) 

# Función 'getLugar'
# Recibe un código de aeropuerto (e.g., 'JFK') y retorna el nombre completo del aeropuerto.
# Usa el diccionario 'lugarMap' para hacer la conversión de código a nombre.
def getLugar(lugar):
    return lugarMap[lugar].capitalize() 

# Función 'mes_nombre'
# Recibe un número de mes (e.g., 1 para enero) y retorna el nombre del mes en español.
# Usa el diccionario 'meses' para realizar la conversión de número a nombre.
def mes_nombre(mes):
    return meses[mes].capitalize() 

# Función 'estatus_retraso'
# Evalúa el estado de retraso de un vuelo basado en el tiempo de retraso (en minutos).
# - Si el tiempo es negativo (< 0), se considera que el vuelo fue anticipado.
# - Si el tiempo es positivo (> 0), se considera que el vuelo fue retrasado.
# - Si el tiempo es exactamente 0, se considera que el vuelo fue a tiempo.
def estatus_retraso(estatus):
    if estatus < 0:
        return "Vuelo anticipado"
    elif estatus > 0:
        return "Vuelo retrasado"
    else:
        return "Vuelo a tiempo"
