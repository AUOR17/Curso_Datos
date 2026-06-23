import numpy as np 
import time

def demo_numpy():

    cantidad_siniestros = 1_000_000
    print(cantidad_siniestros)
    print(type(cantidad_siniestros))

    costos = np.random.randint(2000,350000, size=cantidad_siniestros)

    lista_costo = costos.tolist()

    inicio_python = time.time()
    deducible_py = []
    for costo in lista_costo:
        deducible_py.append(costo*0.10)
    fin_python = time.time()
    tiempo_py = fin_python - inicio_python

    inicio_numpy = time.time()
    deducible_numpy = costos * 0.10
    fin_numpy = time.time()
    tiempo_numpy = fin_numpy - inicio_numpy

    print(f"Tiempo calculano 1 millon de deducibles con un bucle for y listas: {tiempo_py:.5f} segundos")
    print(f"Tiempo calculand 1 millon de deducibles con numpy: {tiempo_numpy:.5f} segundos")
    print(f"Numpy fue {(tiempo_py / tiempo_numpy):.2f} mas rápido. ")


    mascara_casos_graves = costos > 200000
    print(mascara_casos_graves)
    print(type(mascara_casos_graves))
    siniestros_graves = costos[mascara_casos_graves]
    print(siniestros_graves)
    print(type(siniestros_graves))

    print(f"De 1,000,000 de choues, {len(siniestros_graves)} costaron mas de $200,000")
    print(F"Probabilidad de siniestros mayores a $ 200, 000: {(len(siniestros_graves)/len(mascara_casos_graves))*100:.2f}")

    promedio = np.mean(costos)
    costo_mx = np.max(costos)
    desviacion = np.std(costos)

    print(f"Costo promedio por siniestro: ${promedio}")
    print(f"siniestro mas caro: $ {costo_mx}")
    print(f"Desviacion estandar del costo: ${desviacion}")

if __name__ == '__main__':
    demo_numpy()