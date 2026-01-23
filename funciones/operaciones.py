from datetime import datetime, timedelta# agrega la fecha
from .datos import cargar_datos# agrega la funcion de cargar_datos

# funcion calcular_total/menu:
def calcular_total():
    print("\n================================================================")
    print("                     Calcular Total de Gastos                     ")
    print("==================================================================")
    print("1. Calcular total diario")
    print("2. Calcular total semanal")
    print("3. Calcular total mensual")
    print("4. Regresar al menú principal")
    print("===================================================================")
    opcion = input("Seleccione una opción: ")

    datos = cargar_datos()# lee los datos
    total = 0

    hoy = datetime.now().date()
    inicio_semana = hoy - timedelta(days=6)

    if opcion == "1":
        hoy = datetime.now().strftime("%Y-%m-%d")# fecha actual
        total = sum(gasto["monto"] for gasto in datos if gasto["fecha"].startswith(hoy))# suma todos los montos
        print(f"Total de gastos del día: {total}")# aumenta segun la cantidad de gastos
    elif opcion == "2":  # semana
        hoy = datetime.now().date()
        inicio_semana = hoy - timedelta(days=6)
    for gasto in datos:
        fecha_gasto = datetime.strptime(
            gasto["fecha"], "%Y-%m-%d %H:%M:%S"
        ).date()
    if inicio_semana <= fecha_gasto <= hoy:
            print(gasto)
    elif opcion == "3":
        hoy = datetime.now().date()

    for gasto in datos:
        fecha_gasto = datetime.strptime(
            gasto["fecha"], "%Y-%m-%d %H:%M:%S"
        ).date()

    if fecha_gasto.year == hoy.year and fecha_gasto.month == hoy.month:
        print(gasto)