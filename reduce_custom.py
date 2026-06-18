from functools import reduce

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
            # nuevo_maestro[categoria] = nuevo_maestro[categoria] + monto
        else:
            nuevo_maestro[categoria] = monto

    return nuevo_maestro

reporte = reduce(consolidar_reportes, ventas_sucursales,{})

print(reporte)