cadenas = ['1','2','3']
enteros = list(map(int, cadenas))
print(enteros)
print(type(enteros[0]))

precios =[100,200,50]
con_iva = list(map(lambda x: x*1.16, precios))
print(con_iva)

celsiuas = [0,20,30,10,-100,60,50]
fahrenheit = list(map(lambda c: (c*9/5)+32, celsiuas))
print(fahrenheit)

# 1 De una lista en mayusculas, convertir a minusculas
palabras_mayu = ['ILZE', 'MUSTAFA', 'MUNDIAL', 'SILLA']
# ilze = list(map(str.lower, palabras_mayu))
minuw = list(map(lambda x: x.lower(), palabras_mayu))
print(minuw)

# 2 Aplicar el metodo capitalize a una lista de texto
texto = ['hola mundo', 'mundial fifa', 'tr net', 'sat me cae mal']
capital = list(map(lambda x: x.capitalize(), texto))
titulo = list(map(lambda x: x.title(), texto))
print(capital)
print(titulo)
# 3 Quitar espacios en blanco a una lista de correos
coreeos = ['    must@gmail.com  ', '   elon@fifa.org        ']
limpios = list(map(str.strip, coreeos))
print(limpios)
# 4 Aplicar una funcion lambda a una liste de dias,tal que, solo obtengo la primera letra de cada dia. 

dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
iniciales = list(map(lambda d: d[0], dias))
print(iniciales)

usuarios = ['Mustafa', 'lucia']
usernames = list(map(lambda u: f"@{u}", usuarios))
print(usernames)

lista_1 = [1,2,3]
lista_2 = [10,20,30]
suma = list(map(lambda x,y: x+y, lista_1, lista_2))
print(suma)

bases = [2,3,4,5,6,7,8,9]
exponentes = [10,2,4,7,10,4,5,8]
potenicas = list(map(pow, bases, exponentes))
print(potenicas)

lista_a = [10, 50, 30]
lista_b = [20, 40, 40]
mayores = list(map(max, lista_a, lista_b))
print(mayores)

coordenadas = [(10,20), (5,8), (3,1)]
ejey_y = list(map(lambda t: t[1], coordenadas))
print(ejey_y)

empleados = [{'id':1,'nombre':"Hugo"},{'id':2,'nombre':"Ilze"}]
nombres = list(map(lambda e: e['nombre'], empleados))
print(nombres)

inventario_crudo = [
    {"sku": "A1", "producto": "LAPTOP gamer", "precio_str": "$1200.50", "moneda": "USD"},
    {"sku": "B2", "producto": "ratón Inalámbrico", "precio_str": "€45.00", "moneda": "EUR"},
    {"sku": "C3", "producto": "TECLADO MECÁNICO", "precio_str": "$85.99", "moneda": "USD"}
]

TASA_EURO_A_USD = 1.08

def normalizar_producto(item: dict) -> dict:
    precio_limpio = float(item['precio_str'].replace("$", "").replace("€", ""))

    if item['moneda'] == "EUR":
        precio_limpio = round(precio_limpio*TASA_EURO_A_USD, 2)

    return{
        "sku": item["sku"],
        "producto": item["producto"].title(),
        "precio_usd": precio_limpio
    }

inventario_limpio = list(map(normalizar_producto, inventario_crudo))
print(inventario_limpio)