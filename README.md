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
Previamente se estaba por utilizar un DataSet de un repositorio de GitHub, sugerido por el documento adjunto del TP,
pero debido a que este no contenía una columna producto, decidí optar por crear un CSV propio con datos aleatorios con ayuda de la IA.

Columnas:
- `id`: identificador de la venta
- `fecha_venta`: fecha de la operación
- `producto`: nombre del producto
- `cantidad`: unidades vendidas
- `precio`: precio unitario en pesos

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
