def calcular_comision(venta):
    comision_vendedor = venta * 0.05
    return comision_vendedor

calcular_comision_l = lambda venta: venta * 0.05

print(f"Comision calculada con def: {calcular_comision(1000)}")
print(f"Calcular comision con lambda: {calcular_comision_l(1000)}")

sumar = lambda a,b : a + b
print(f"La funcion sumar: {sumar(10,4)}")

cuadrado = lambda x: x**2
print(f"Funcion al cuadrado: {cuadrado(127)}")

promedio_f = lambda a,b,c: (a+b+c) / 3
print(f"Promedio fijo es: {promedio_f(8,4,9)}")

area_triangul = lambda base,altura: (base*altura) / 2
print(f"Area de triangulo es: {area_triangul(10,17)}")

saludar = lambda nombre: f"Hola, {nombre}!"
print(saludar("John"))

extraer_3 = lambda texto: texto[:4] + saludar("John")
print(extraer_3("Legend of Zelda"))

repetir_te = lambda texto,n: texto*n
print(repetir_te("*", 40))

es_minuscula = lambda texto: texto==texto.lower()
print(es_minuscula("Hola"))
print(es_minuscula("hola"))

mayor =  lambda a,b: a if a>b else b
print(mayor(40,8))

par = lambda x: "Par" if x%2 == 0 else "Impar"
print(par(12))

signo = lambda x: 'Positivo' if x > 0 else ("Negativo" if x < 0 else "Cero")
print(signo(8))
print(signo(-9))
print(signo(0.0))

mayor_19 = lambda edad: True if int(edad) >= 18 else False
print(mayor_19(90))

cuadrado = lambda: [x**2 for x in range(0,100)]


par = lambda: ["Par" if x%2 == 0 else "Impar" for x in range(0,100)]
print(cuadrado())

ultimo = lambda lista:lista[-1]

print(ultimo([10,20,30]))

lista_vacia = lambda lista: len(lista) == 0
print(lista_vacia([]))

obtener_edad = lambda persona: persona.get('edad', 'no especificada')
print(obtener_edad({"nombre":"Luis"}))
