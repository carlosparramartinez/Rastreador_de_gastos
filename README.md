# Rastreador de Gastos en Línea de Comandos

Una aplicación simple de línea de comandos para gestionar tus gastos personales, desarrollada en Python. Permite agregar, listar, eliminar, actualizar y generar resúmenes de gastos, almacenando los datos en un archivo JSON local.

## Requisitos

- Python 3.7 o superior
- [tabulate](https://pypi.org/project/tabulate/) para mostrar tablas en la consola

### Instalar dependencias

```bash
pip install tabulate
###  Cómo usar

##Agregar un gasto
python expense_tracker.py add --description "Almuerzo" --amount 25

### Eliminar un gasto por ID
bash
python expense_tracker.py delete --id 1

### Listar todos los gastos
bash
python expense_tracker.py list
###Resumen total de gastos
bash
python expense_tracker.py summary

###Resumen de gastos por mes (por número: enero = 1, febrero = 2, etc.)
bash
python expense_tracker.py summary --month 5

###Actualizar un gasto existente
bash
python expense_tracker.py update --id 1 --description "Cena" --amount 30

###Funcionalidades
 Añadir nuevos gastos

 Eliminar gastos por ID

 Listar gastos en formato tabla

 Mostrar resumen general o mensual

 Actualizar gastos existentes