# Project Rapture – Análisis de Ventas

## Integrantes
- Iván Ortiz de Zárate (trabajo individual)

## Roles creados dentro del space de Jira
1. Líder y Organizador
2. Desarrollador Técnico
3. Revisor y QA

## Escenario
Escenario B – Análisis de ventas de una pequeña empresa.

## Dataset
Archivo `datos/ventas.csv` generado aleatoriamente para este proyecto (200 registros simulados).

Columnas:
- `id`: identificador de la venta
- `fecha_venta`: fecha de la operación
- `producto`: nombre del producto
- `cantidad`: unidades vendidas
- `precio`: precio unitario en pesos

El dataset fue creado con Python en Google Colab para cumplir con el Escenario B, ya que el dataset sugerido en la consigna (https://gist.github.com/khanusama20/ee33c2869dd5cf3cebdf020be1ca43f6) solo incluía fecha y monto diario, sin columna de producto.

## Estructura
- `datos/` – datos de entrada
- `scripts/` – código de análisis en Python
- `resultados/` – gráficos y salidas

## Ejecución en Colab
1. Configurar el usuario para commits
2. Clonar el repositorio
3. Crear o verificar el dataset en `datos/ventas.csv`
4. Ejecutar el script en `scripts/analisis_ventas.py`
5. Revisar salidas en `resultados/`

## Trazabilidad Jira
- PROYECT-1: Crear roles para los miembros del equipo
- PROYECT-2: Inicialización del repositorio
- PROYECT-3: Desarrollo del script
- PROYECT-4: Revisión y Pull Request
