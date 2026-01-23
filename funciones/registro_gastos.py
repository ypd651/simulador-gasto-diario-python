from datetime import datetime# ver la fecha
from .datos import cargar_datos, guardar_gastos
# cuncion registrar_gasto/menu:
def registrar_gasto():
    print("\n=============================================")
    print("            Registrar Nuevo Gasto")
    print("===============================================")
    
    # tomar especificaciones
    monto = input("Monto del gasto: ")
    categoria = input("Categoría alimentos, transporte, entretenimiento, otro..): ").lower()# sin espacios
    descripcion = input("Descripción (opcional): ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    gasto = {# crear diccionario
        "monto": float(monto),
        "categoria": categoria,
        "descripcion": descripcion,
        "fecha": fecha
    }

    datos = cargar_datos()# agrega la fecha a los gastos existentes
    datos.append(gasto)# agrega el ciccionario a los datos
    guardar_gastos(datos)
    print("Gasto registrado exitosamente.")# anuncia el guardado

# funcion listar_datos/menu:
def listar_gastos():
    print("\n=======================================================")
    print("                     Listar Gastos                       ")
    print("=========================================================")
    print("1. Ver todos los gastos")# muestra los gastos juntos
    print("2. Filtrar por categoría")# gastos de cada categoria
    print("3. Filtrar por rango de fechas")# fecha mas reciente primero
    print("4. Regresar al menú principal")# regresar
    print("=========================================================")
    opcion = input("Seleccione una opción: ")

    datos = cargar_datos()# lee los datos

    if opcion == "1":
        for gasto in datos:
            print(gasto)# muestra todos los gastos
    elif opcion == "2":
        categoria = input("Ingrese la categoría: ").lower()# pedir categoria
        for gasto in datos:
            if gasto["categoria"] == categoria:# busca gstos en cada categoria
                print(gasto)
    elif opcion == "3":
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
        for gasto in datos:
            fecha_gasto = datetime.strptime(gasto["fecha"], "%Y-%m-%d %H:%M:%S")
            if fecha_inicio <= fecha_gasto.strftime("%Y-%m-%d") <= fecha_fin:
                print(gasto)
    elif opcion == "4":
        return
    else:
        print("Opción no válida.")