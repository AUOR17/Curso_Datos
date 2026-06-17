class Personaje:

    def __init__(self, nombre, salud_maxima):
        self.nombre = nombre
        self._salud = salud_maxima # principio de encapsulamiento. 
        self.salud_maxima = salud_maxima
        self.inventario = ['Pocion chica', 'Pan seco']

    @property
    def salud(self):
        return self._salud
    
    @salud.setter
    def salud(self,nueva_salud):
        if  nueva_salud <= 0:
            self._salud = 0
            print(f"El personaje {self.nombre} ha muerto")

        elif nueva_salud > self.salud_maxima:
            self._salud = self.salud_maxima

        else:
            self._salud = nueva_salud
            print(f"Salud de {self.nombre} actulizada a: {self._salud}/{self.salud_maxima}")

    #del salud
    @salud.deleter
    def salud(self):
        print(f"Alerta, el hacker intenta borrar el atributo salud de {self.nombre}")

    def _efecto_sonido_curacion(self):
        print(F"Realizando efecto de sonido de curación, ")

    def tomar_pocion(self, cantidad_curacion):
        print(f"{self.nombre} intenta tomar una pocion de +{cantidad_curacion}")

        self._efecto_sonido_curacion()
        self.salud = self.salud + cantidad_curacion

    # Metodos magicos 

    def __str__(self):
        '''Se activa cuando se usa print(objeto) o str(objeto)'''
        return f"Personaje: {self.nombre} | HP: {self.salud} / {self.salud_maxima}"

    def __repr__(self):
        '''Este metodo es para debug y funcionada al inspeccionar un objeto en consola
        o usar repr()'''
        return f"Personaje('{self.nombre}', {self.salud_maxima})"
    
    def __gt__(self,otro_personaje):
        '''Este metodo se activa al usar el operado ( > )'''
        return self.salud_maxima > otro_personaje.salud_maxima

    def __add__(self,otro_personaje):
        '''Se activa al usar el simobolo de suma (+)'''
        print(f"Fusion iniciada entre {self.nombre} y {otro_personaje.nombre}")

        nuevo_nombre = f"{self.nombre[:3]}{otro_personaje.nombre[3:]}"
        nueva_salud = self.salud_maxima + otro_personaje.salud_maxima

        return Personaje(nuevo_nombre, nueva_salud)        
    
    def __len__(self):
        '''Se activa al usar la funcion len(objeto)'''
        return len(self.inventario)
    
    @classmethod
    def crear_npc_basico(cls):
        '''Crea un personaje generico sin pedir datos manuales'''
        print("Generando NPC basico de la clase Personaje")
        return cls(nombre='Aldeano Generico', salud_maxima=10)

    @staticmethod
    def mostrar_manual_juego():
        '''Utilidad: Funciona sin necesidad de crear un personaje ni usar la clase'''
        print("\n --- MANUAL DEL JUEGO ---")
        print("1. La salud máxima no puede superarse.")
        print("2. Si la salud llega a 0, el personaje muere.")
        print("3. Usa pociones con sabiduría.")
        print("---------------------------\n")
    

class Guerrero(Personaje):

    def __init__(self, nombre, salud_maxima, puntos_armadura):
        super().__init__(nombre, salud_maxima)
        self.puntos_armadura = puntos_armadura

    def recibir_dano(self,dano_enemigo):
        print(f"Un enemigo ataca a {self.nombre} con {dano_enemigo} de daño")

        dano_real = dano_enemigo - self.puntos_armadura
        if dano_real < 0:
            dano_real = 0

        print(f"La armadura bloquea {self.puntos_armadura} puntos. Daño real: {dano_real}")

        self.salud = self.salud - dano_real

    def __str__(self):
        ficha_base = super().__str__() 
        return f"{ficha_base} | Armadura: {self.puntos_armadura}"
    
    @classmethod
    def crear_guerrero_elite(cls):
        print("Entrenando a un espartano de elite")
        return cls(nombre="Espartano", salud_maxima=200, puntos_armadura=50)

class Mago(Personaje):

    def __init__(self, nombre, salud_maxima, puntos_mana):
        super().__init__(nombre, salud_maxima)
        self.puntos_mana = puntos_mana

    def __eq__(self, objeto):
        if self.salud_maxima == objeto.salud_maxima:
            return True
        else:
            return False
        
    def __lt__(self, objeto: Mago) -> str:
        if self.puntos_mana < objeto.puntos_mana:
            return f"{self.nombre} tiene mas mana que {objeto.nombre}"
        
if __name__=='__main__':
    ilze = Personaje('Ilze',10)
    Mustafa = Guerrero('Mustafa', 20, 80)
    print(ilze)
    print(Mustafa)  
    