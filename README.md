# Simulador de Gasto Diario en Python

Aplicación de consola en Python para registrar, listar, calcular y generar reportes de gastos diarios, semanales y mensuales. Los datos se guardan en un archivo JSON.

> Proyecto académico de nivel introductorio. Código organizado por funciones para practicar modularización.

## Funcionalidades

- Registrar nuevo gasto con monto, categoría, descripción y fecha
- Listar gastos: ver todos, filtrar por categoría o por rango de fechas
- Calcular total de gastos diario, semanal y mensual
- Generar reporte diario, semanal o mensual y opción de guardarlo en `reporte.json`
- Persistencia de datos en `gastos.json`

## Estructura del proyecto

```text  
/  
├── main.py  
├── funciones/  
│   ├── datos.py            # Cargar y guardar datos en JSON  
│   ├── registro_gastos.py  # Registrar y listar gastos  
│   ├── operaciones.py      # Calcular totales  
│   └── ver_reportes.py     # Generar reportes  
├── gastos.json             # Se crea automáticamente  
└── README.md  
