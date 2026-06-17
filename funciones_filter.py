# numeros = [1, 2, 3, 4, 5, 6]
# pares = list(filter(lambda x: x % 2 == 0, numeros))
# # pares = filter(lambda x: x % 2 == 0, numeros)
# impares = list(filter(lambda x: x % 2 != 0, numeros))

# print(pares)
# print(impares)

# numeros = [-10, 5, -3, 8, 0]
# positivos = list(filter(lambda x: x > 0, numeros))
# print(positivos)

# edades = [5, 12, 25, 45, 60, 8]
# rango = list(filter(lambda x: 10 <= x <= 50, edades))
# print(rango)

# numeros = [10, 12, 15, 22, 25]
# multiplos = list(filter(lambda x: x % 5 == 0, numeros))
# print(multiplos)

# # Filtrar palabras largas (más de 5 letras):
# palabras = ["sol", "murcielago", "luz", "elefante"]
# largas = list(filter(lambda x: len(x) > 5, palabras))
# print(largas)
# # Encontrar palabras que empiecen con una letra específica (A)
# nombres = ["Ana", "Carlos", "Alberto", "Beto"]
# con_a = list(filter(lambda x: x.startswith("A"), nombres))
# print(con_a)
# # Filtrar palabras que contengan una subcadena (ej. "pro"):
# terminos = ["programa", "casa", "proyecto", "arbol"]
# tienen_pro = list(filter(lambda x: "pro" in x, terminos))
# # Identificar palíndromos (se leen igual al revés): -> 
# palabras = ["radar", "python", "oso", "java"]
# palindromos = list(filter(lambda x: x == x[::-1], palabras))
# print(palindromos)
# # Conservar solo las palabras que estén completamente en mayúsculas:
# codigos = ["MX", "es", "USA", "fr"]
# mayusculas = list(filter(lambda x: x.isupper(), codigos))

# datos = [1, 0, "h", "", None, False, 5,(None),[2],-1,()]
# limpios = list(filter(None,datos))
# print(limpios)

# sin_none = list(filter(lambda x: x is not None, datos))
# print(sin_none)

# mezcla = [1, "dos", 3.5, 4, "cinco"]
# enteros = list(filter(lambda x: isinstance(x, int), mezcla))
# print(enteros)

# usuarios = [{'nombre': 'Luis', 'edad': 16}, {'nombre': 'Ana', 'edad': 22}]
# mayores = list(filter(lambda u: u['edad'] >= 18, usuarios))
# print(mayores)
# cuentas = [{'user': 'admin', 'activo': True}, {'user': 'invitado', 'activo': False}]
# activos = list(filter(lambda c: c['activo'], cuentas))
# print(activos)
# productos = [("Mouse", 25), ("Monitor", 150), ("Teclado", 45)]
# baratos = list(filter(lambda p: p[1] < 50, productos))
# print(baratos)
# inventario = [{'item': 'A', 'stock': 0}, {'item': 'B', 'stock': 10}]
# disponibles = list(filter(lambda i: i['stock'] > 0, inventario))
# # disponibles = list(filter(lambda i: i['stock'] > 0, inventario))
# print(disponibles)

lista_a = [1,2,3,4,5,6]
lista_b = [4,5,6,7,8,9]
comunes = list(filter(lambda x: x in lista_b, lista_a))
print(comunes)

texto = "murcielago"
sin_vocales = "".join(filter(lambda letra: letra.lower() not in 'aeiou', texto))
print(sin_vocales)

logs_servidor = [
    {"ip": "192.168.1.10", "endpoint": "/home", "status": 200, "user_agent": "Chrome"},
    {"ip": "45.33.22.11", "endpoint": "/wp-admin.php", "status": 403, "user_agent": "Python-urllib"},
    {"ip": "10.0.0.5", "endpoint": "/api/v1/users", "status": 200, "user_agent": "Safari"},
    {"ip": "88.15.44.3", "endpoint": "/.env", "status": 404, "user_agent": "Curl/7.68.0"},
    {"ip": "192.168.1.12", "endpoint": "/dashboard", "status": 200, "user_agent": "Firefox"}
]

def es_amenza(log:dict) -> bool:
    endpoints_peligroso = ['.env', 'wp-admin', 'config.php']

    if any(peligro in log['endpoint'] for peligro in endpoints_peligroso):
        return True
    
    if log['status'] == 403 and log['user_agent'] not in ['Chrome', 'Firefox', 'Safari', 'Edge', 'Brave']:
        return True
    
    return False

ataques_detectados = list(filter(es_amenza, logs_servidor))
print(ataques_detectados)
