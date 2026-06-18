import numpy as np

lista_cantidades = [5,77,10,50,48]
lista_precios = [6.95, 6.75, 6.75, 2.10, 1.25]
# print(f"Lista normal de precios: {lista_precios}")

array_cantidades = np.array(lista_cantidades)
array_precios = np.array(lista_precios)

# print(f"Tipo de dato del objeto numpy: {type(array_cantidades)}")
# print(f"Array de precios: {array_precios}")

# subtotales_lista = lista_cantidades * lista_precios
subtotal = array_cantidades * array_precios
# print(subtotal)

ingreso_total = np.sum(subtotal)
venta_maxima = np.max(subtotal)
venta_promedio = np.mean(subtotal)
venta_mediana = np.median(subtotal)

# print("\n=== REPORTE ESTADÍSTICO INSTANTÁNEO ===")
# print(f" El arreglo de las ventas    : {subtotal}")
# print(f" Ingreso Total de la factura : ${ingreso_total:.2f}")
# print(f" Venta más alta registrada   : ${venta_maxima:.2f}")
# print(f" Promedio de venta por item  : ${venta_promedio:.2f}")
# print(f" Mediana de la venta         : ${venta_mediana:.2f}")
# print("=="*30)

ventas = np.array([15.50, 85.00, 5.00, 120.00, 8.95, 50.0])

etiquetas = np.where(ventas > 50.00, "Venta Alta", "Venta Baja")
# np.where(condicion, valor si es verdad, valor si es falso)

# print("[*] Análisis de Ventas con np.where:")
# print(f"Ventas crudas : {ventas}")
# print(f"Clasificación : {etiquetas}\n")

tabla_transacciones = np.array([
    [10, 2.50],
    [5,  1.25],
    [24, 7.00],
    [1,  0.99]
])

dimensiones = tabla_transacciones.shape
# print(f"Elemento 1: {tabla_transacciones[0]}")

# print("[*] Escáner de Dimensiones (.shape):")
# print(f"La matriz es:\n{tabla_transacciones}")
# print(f"\nReporte de anatomía: {dimensiones}")
# print(f"-> Tenemos {dimensiones[0]} filas (transacciones).")
# print(f"-> Tenemos {dimensiones[1]} columnas (variables).\n")

ids_clientes = np.arange(0, -10, -2) 
# print(f"IDs generados con arange:\n {ids_clientes}")
# print(type(ids_clientes))

puntos_grafica = np.linspace(0, 10, 9) 
# print(f"Puntos generados con linspace: {puntos_grafica}")

# inventario_vacio = np.zeros((3,3)) 
# inventario_vacio = np.zeros(5)
# inventario_vacio = np.ones(8)
inventario_vacio = np.ones((3,3))
print(inventario_vacio)

# Instrucciones para los alumnos:
# Completa los TODO en el siguiente script de Python utilizando únicamente las 
# herramientas de NumPy que vimos en clase 
# (np.array, *, np.sum, np.mean, np.where, .shape, np.arange, np.zeros).