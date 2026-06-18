from functools import reduce

numeros = [10,-2,3,-4,5]
# reduce(funcion, iterable, [valor_inicial])
suma = reduce(lambda actual,acumulador: acumulador + actual, numeros)
print(suma)

numeros = [2, 3, 4]
producto = reduce(lambda acc, x: acc * x, numeros)

numeros = [100, 2, 5, 4]
division = reduce(lambda acc, x: acc / x, numeros)

numeros = [2, 3, 4]
suma_cuadrados = reduce(lambda acc, x: acc + (x ** 2), numeros, 0)

numeros = [15, 8, 42, 4, 23]
mayor = reduce(lambda acc, x: acc if acc > x else x, numeros)

valores = [True, True, False, True]
todos_verdaderos = reduce(lambda acc, x: acc and x, valores)

valores = [True, True, False, True]
todos_verdaderos = reduce(lambda acc, x: acc or x, valores)

palabras = ["Python", "es", "muy", "poderoso"]
frase = reduce(lambda acc, x: acc + " " + x, palabras)

letras = ["a", "b", "a", "c", "a"]
conteo = reduce(lambda acc, x: acc + 1 if x == "a" else acc, letras, 0)

texto = "hola"
invertido = reduce(lambda acc, x: x + acc, texto)

listas = [[1, 2], [3, 4], [5, 6]]
aplanada = reduce(lambda acc, x: acc + x, listas)

conjuntos = [{1, 2, 3}, {2, 3, 4}, {3, 5}]
comunes = reduce(lambda acc, x: acc & x, conjuntos)

elementos = ['manzana', 'pera', 'manzana', 'uva', 'pera']
frecuencias = reduce(lambda acc, x: {**acc, x: acc.get(x, 0) + 1}, elementos, {})
print(frecuencias)

numeros = [1, 2, 3, 4, 5, 6]
agrupados = reduce(
    lambda acc, x: {**acc, 'pares': acc['pares'] + [x]} if x % 2 == 0 else {**acc, 'impares': acc['impares'] + [x]}, 
    numeros, 
    {'pares': [], 'impares': []}
)

print(agrupados)

ventas_sucursales = [
    {"Laptops": 5000, "Smartphones": 3000, "Accesorios": 500},
    {"Laptops": 2000, "Smartphones": 4500, "Accesorios": 1200},
    {"Laptops": 8000, "Smartphones": 1500, "Accesorios": 300},
    {"Monitores": 4000, "Accesorios": 800} 
]

def consolidar_reportes(acumulador: dict, reporte_actual: dict) -> dict:
    """
    Toma el reporte maestro acumulado y le suma las ventas de la siguiente sucursal.
    Si la categoría no existe en el maestro, la crea.
    """
    nuevo_maestro = acumulador.copy()

    for categoria, monto in reporte_actual.items():

        if categoria in nuevo_maestro:
            nuevo_maestro[categoria] += monto
        else:
            nuevo_maestro[categoria] = monto

    return nuevo_maestro

reporte = reduce(consolidar_reportes, ventas_sucursales,{})

print(reporte)