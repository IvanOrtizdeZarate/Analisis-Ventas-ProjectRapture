import pandas
import matplotlib.pyplot
from pathlib import Path

# Utilizamos rutas relativas para que funcione en Colab sin rutas absolutas
RUTA_DATOS = Path("datos/ventas.csv")
RUTA_RESULTADOS = Path("resultados")
RUTA_RESULTADOS.mkdir(exist_ok=True)

# Leemos el CSV creado con ventas por producto
dataframe_ventas = pandas.read_csv(RUTA_DATOS)
dataframe_ventas["fecha_venta"] = pandas.to_datetime(dataframe_ventas["fecha_venta"])

# Calculamos el monto de cada venta: cantidad * precio unitario
dataframe_ventas["monto_venta"] = dataframe_ventas["cantidad"] * dataframe_ventas["precio"]

# --- Indicadores ---
ventas_totales = dataframe_ventas["monto_venta"].sum()

# Producto más vendido según cantidad total vendida
cantidad_por_producto = dataframe_ventas.groupby("producto")["cantidad"].sum()
producto_mas_vendido = cantidad_por_producto.idxmax()
cantidad_producto_mas_vendido = cantidad_por_producto.max()

# Agrupamos por mes para visualizar la evolución temporal del negocio
dataframe_ventas["mes"] = dataframe_ventas["fecha_venta"].dt.to_period("M")
ventas_por_mes = dataframe_ventas.groupby("mes")["monto_venta"].sum()

print("Ventas totales: $" + f"{ventas_totales:,.0f}")
print("Producto más vendido: " + str(producto_mas_vendido) + " (" + str(cantidad_producto_mas_vendido) + " unidades)")
print("\nVentas por mes:")
print(ventas_por_mes)

# --- Gráfico: evolución mensual de ventas ---
ventas_mensuales = ventas_por_mes.copy()
ventas_mensuales.index = ventas_mensuales.index.astype(str)

matplotlib.pyplot.figure(figsize=(12, 5))
matplotlib.pyplot.bar(ventas_mensuales.index, ventas_mensuales.values)
matplotlib.pyplot.title("Evolución de ventas por mes - Project Rapture")
matplotlib.pyplot.xlabel("Mes")
matplotlib.pyplot.ylabel("Monto de ventas")
matplotlib.pyplot.xticks(rotation=45)
matplotlib.pyplot.grid(True, alpha=0.3, axis="y")
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.savefig(RUTA_RESULTADOS / "evolucion_ventas.png")
matplotlib.pyplot.show()

# Guardamos un resumen en texto para /resultados
with open(RUTA_RESULTADOS / "resumen_analisis.txt", "w", encoding="utf-8") as archivo_resumen:
    archivo_resumen.write("Ventas totales: " + str(ventas_totales) + "\n\n")
    archivo_resumen.write("Producto más vendido: " + str(producto_mas_vendido) + " (" + str(cantidad_producto_mas_vendido) + " unidades)\n\n")
    archivo_resumen.write("Ventas por mes:\n")
    archivo_resumen.write(ventas_por_mes.to_string())
    archivo_resumen.write("\n")

print("\nArchivos guardados en /resultados")
