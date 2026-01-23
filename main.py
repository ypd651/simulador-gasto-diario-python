from funciones.registro_gastos import registrar_gasto, listar_gastos
from funciones.operaciones import calcular_total
from funciones.ver_reportes import generar_reporte

def menu():# menu principal
    while True:# bucle
        print("\n================================================================")
        print("                    Simulador de Gasto Diario                  ")
        print("==================================================================")
        print("seleccione una opcion")
        print()
        print("1. Registrar nuevo gasto")# agrega nuevo gasto
        print("2. Listar gastos")# revisar gastos
        print("3. Calcular total de gastos")# ver total(diario,semanal,mensual)
        print("4. Generar reporte de gastos")# hacer nuevo reporte
        print("5. Salir")# terminado
        print("==================================================================")

        opcion = input("Seleccione una opción: ")# eleccion

        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            listar_gastos()
        elif opcion == "3":
            calcular_total()
        elif opcion == "4":
            generar_reporte()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()# llamar al menu