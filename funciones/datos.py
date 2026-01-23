# almacena todos los datos
import json# usar json

ARCHIVO = "gastos.json"# locacion de los datos

# funcion cargar_datos:
def cargar_datos():
    try:# prevenir errores
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)# abre el archivo
    except FileNotFoundError:# no carpeta
        return []# lista vacia
    
# funcion guardar_gastos:
def guardar_gastos(gastos):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(gastos, archivo, indent=4)# ordenar todo