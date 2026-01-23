from datetime import datetime, timedelta# da la fecha
from .datos import cargar_datos# añade funcion cargar datos
import json # usar json

# funcion guardar_reporte/menu:
def generar_reporte():
    print("\n====================================================================")
    print("                 Generar Reporte de Gastos                            ")
    print("======================================================================")
    print("1. Reporte diario")# dar reporte del dia
    print("2. Reporte semanal")# dar reporte de la semana
    print("3. Reporte mensual")# dar reporte del mes
    print("4. Regresar al menú principal")# regresar
    print("======================================================================")
    opcion = input("Seleccione una opción: ")

    datos = cargar_datos()# lee los datos
    reporte = []# crea lista vacia

    if opcion == "1":
        hoy = datetime.now().strftime("%Y-%m-%d")# fecha actual
        reporte = [gasto for gasto in datos if gasto["fecha"].startswith(hoy)]# reporte dado hoy
    elif opcion == "2":
        hace_7_dias = datetime.now() - timedelta(days=7)# dar reporte(ultimos 7 dias)
        reporte = [
            gasto
            for gasto in datos
            if datetime.strptime(gasto["fecha"], "%Y-%m-%d") >= hace_7_dias
        ]
    elif opcion == "3":
        mes_actual = datetime.now().strftime("%Y-%m")# fechas de el ultimo mes
        reporte = [gasto for gasto in datos if gasto["fecha"].startswith(mes_actual)]# da reportes(ultimo mes)
    elif opcion == "4":
        return# volver
    else:
        print("Opción no válida.")
        return

    print("Reporte generado:")# confirmar guardado
    for gasto in reporte:
        print(gasto)

    guardar = input("¿Desea guardar el reporte en un archivo JSON? (S/N): ").lower()# desicion
    if guardar == "s":
        with open("reporte.json", "a", encoding="utf-8") as archivo:
            json.dump(reporte, archivo, indent=4)
        print("Reporte guardado como 'reporte.json'.")