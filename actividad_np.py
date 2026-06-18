import numpy as np

lista_tazas_vendidas = [18, 45, 30, 12]
lista_precios_mxn = [35.0, 40.0, 65.0, 70.0]

array_tazas = np.array(lista_tazas_vendidas)
array_precios = np.array(lista_precios_mxn)

subtotales_bebidas = array_tazas * array_precios

ingreso_total = np.sum(subtotales_bebidas)
venta_maxima = np.max(subtotales_bebidas)
venta_promedio = np.mean(subtotales_bebidas)
venta_mediana = np.median(subtotales_bebidas)

print("\n--- CORTE DE CAJA ---")
print(f"Ingreso Total del turno : ${ingreso_total:.2f}")
print(f"Producto que más vendió : ${venta_maxima:.2f}")
print(f"Promedio de venta       : ${venta_promedio:.2f}")
print(f"Mediana                 : ${venta_mediana:.2f}")

etiquetas_rendimiento = np.where(subtotales_bebidas > 1000.00, "Top Ventas", "Venta Regular")

print("\n[*] Clasificación de Rendimiento:")
print(etiquetas_rendimiento)


tabla_inventario = np.array([
    [5.5, 12.0],
    [2.0, 18.5],
    [8.2, 5.0]
])

dimensiones_inventario = tabla_inventario.shape
print(f"\n[*] La matriz de inventario tiene {dimensiones_inventario[0]} sucursales y {dimensiones_inventario[1]} insumos.")

ids_baristas = np.arange(1001, 1005, 1)
print(f"[*] IDs de baristas asignados: {ids_baristas}")

matriz_mermas = np.zeros((2, 2))
print("\n[*] Contador de mermas inicializado:")
print(matriz_mermas)   