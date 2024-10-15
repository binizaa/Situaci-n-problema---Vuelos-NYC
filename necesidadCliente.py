import pandas as pd

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

def datos():
    JFK = pd.read_csv("./baseDeDatos/JFK.csv")
    EWR = pd.read_csv("./baseDeDatos/EWR.csv")
    LGA = pd.read_csv("./baseDeDatos/LGA.csv")
    
    return pd.concat([JFK, EWR, LGA], axis = 0, ignore_index = True) 

def getLugar(lugar):
    return lugarMap[lugar].capitalize() 

def mes_nombre(mes):
    return meses[mes].capitalize() 

def estatus_retraso(estatus):
    if estatus < 0:
        return "Vuelo anticipado"
    elif estatus > 0:
        return "Vuelo retrasado"
    else:
        return "Vuelo a tiempo"
