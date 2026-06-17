from Poo import Personaje, Guerrero, Mago

def encapsulamiento():

    arthur = Personaje('Arthur', 80)
    # arthur._salud = "Modo Dios"
    # arthur.salud(500)
    arthur.tomar_pocion(200)
    print(arthur)

def herencia():
    ilze = Personaje('Ilze', 100)
    kratos = Guerrero('Kratos', 100, 80)

    kratos.recibir_dano(25)
    kratos.tomar_pocion(700)
    print(f"Kratos tiene {kratos.puntos_armadura} de armadura")
    print(kratos)

    # ilze.puntos_armadura #_> Error de atributo

def metodo_magico():
    ilze = Personaje('Ilze', 100)
    kratos = Guerrero('Kratos', 100, 80)

    print(ilze) # Convoca al llamado del metodo magico __str__
    print(repr(ilze)) # Convova al llamado del metodo magico __repr__

    #Ejemplo del metodo __gt__

    if kratos>ilze:
        print("Kratos tiene mas vida que Ilze")
    else:
        print(f"La vida de {ilze.nombre} es de: {ilze.salud_maxima}")
        print(f"La vida de {kratos.nombre} es de {kratos.salud_maxima}")

    # ejemplo del metodo (+)
    guerrero_definito = ilze + kratos
    print(guerrero_definito)

    kratos.inventario.append('Espadas del caos')
    print(len(kratos))

def decoradores():
    Personaje.mostrar_manual_juego()

    # Crear personaje generico
    npc= Personaje.crear_npc_basico()
    print(npc)

    extra = Guerrero.crear_guerrero_elite()
    print(extra)

    Guerrero.mostrar_manual_juego()

    try:
        del npc.salud
    except AttributeError:
        pass

def test_mago():
    Merlin = Mago('Merlin', 100, 10000)
    Ganondorf = Mago('Ganondorf', 200, 700)

    if Merlin == Ganondorf:
        print("Pelea Pareja")
    
    if Ganondorf < Merlin:
        print(f"{Ganondorf.nombre} es mas debil que {Merlin.nombre}")

if __name__=='__main__':
    # encapsulamiento()
    # herencia()
    # metodo_magico()
    # decoradores()
    test_mago()
