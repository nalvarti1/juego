import random
#El no uso de las tildes es una convencion para evitar que puedan ocurrir errores al entender el texto mostrado finalmente.
class Entidad:
    def __init__(self, nombre, salud, energia, ataque_basico):
        self.nombre = nombre
        self.salud = salud
        self.salud_maxima = salud
        self.energia = energia
        self.energia_maxima = energia
        self.ataque_basico = ataque_basico
        self.probabilidad_critico = 0.1  #10% por defecto
        self.nivel = 1
        self.experiencia = 0
        self.inventario = []

    def atacar(self, objetivo):
        if random.random() < self.probabilidad_critico:
            dano = self.ataque_basico*2  #Ataque crítico
            
        else:
            dano = self.ataque_basico
        objetivo.recibir_dano(dano)

    def recibir_dano(self, dano):
        self.salud = self.salud - dano
        if self.salud <= 0:
            self.morir()    #Al llegar a 0 la vida del personaje se mostrara un mensaje diciendo que este murio

    def morir(self):
        print(f"{self.nombre} murio.")

    def descansar(self):
        if self.salud <= 0:
            print(f"{self.nombre} no puede descansar, está muerto.")
            
        else:
            incremento_salud = self.salud_maxima * 0.15  #En caso delpersonaje su salud maxima es 100, el incremento seria de 15 puntos a su salud actual.
            incremento_energia = self.energia_maxima * 0.15
    
            self.salud += incremento_salud
            self.energia += incremento_energia
            
            if self.salud > self.salud_maxima:
                self.salud = self.salud_maxima
            if self.energia > self.energia_maxima:
                self.energia = self.energia_maxima

    def subir_nivel(self):
        if self.experiencia >= self.nivel * 100:
            self.nivel += 1
            self.ataque_basico += 5
            self.salud_maxima += 20
            self.energia_maxima += 10
            print(f"{self.nombre} subio de nivel {self.nivel}!")

    def agregar_objeto(self, objeto):
        if len(self.inventario) < 10:
            self.inventario.append(objeto)
            print(f"{self.nombre} agrego {objeto.nombre} al inventario.")
            
        else:
            print(f"{self.nombre} no puede llevar más objetos, el inventario esta lleno.")

    def eliminar_objeto(self, objeto):
        if objeto in self.inventario:
            self.inventario.remove(objeto)
            print(f"{self.nombre} elimino {objeto.nombre} del inventario.")
            
        else:
            print(f"{self.nombre} no tiene {objeto.nombre} en el inventario.")
            
class Habilidad:
    def __init__(self, nombre, ataque, energia_requerida):
        self.nombre = nombre
        self.ataque = ataque
        self.energia_requerida = energia_requerida

class Objeto:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

class Pocion(Objeto):
    def __init__(self, nombre, descripcion, tipo, nivel):
        super().__init__(nombre, descripcion)
        self.tipo = tipo  #"salud" o "energia"
        self.nivel = nivel  #De 1 hasta 3

class Tienda:
    def __init__(self):
        self.inventario_objetos = []
        self.inventario_pociones = []

class Personaje(Entidad):
    def __init__(self, nombre, salud, energia, ataque_basico):
        super().__init__(nombre, salud, energia, ataque_basico)
        self.habilidades = []

    def aprender_habilidad(self, habilidad):
        if len(self.habilidades)<3:
            self.habilidades.append(habilidad)
            print(f"{self.nombre} aprendio la habilidad {habilidad.nombre}.")
            
        else:
            print("No puedes aprender mas habilidades.")

    def olvidar_habilidad(self, habilidad):
        if habilidad in self.habilidades:
            self.habilidades.remove(habilidad)
            print(f"{self.nombre} olvido la habilidad {habilidad.nombre}.")
            
        else:
            print(f"{self.nombre} no conoce la habilidad {habilidad.nombre}.")

    def usar_pocion(self, pocion):
        if pocion in self.inventario:
            if pocion.tipo == "salud":
                self.salud += pocion.nivel * 20
                if self.salud > self.salud_maxima:
                    self.salud=self.salud_maxima
                print(f"{self.nombre} uso {pocion.nombre} y recupero su salud.")
                
            elif pocion.tipo == "energia":
                self.energia += pocion.nivel * 10
                if self.energia > self.energia_maxima:
                    self.energia=self.energia_maxima
                print(f"{self.nombre} uso {pocion.nombre} y recupero su energia.")
            
            self.inventario.remove(pocion)
            
        else:
            print(f"{self.nombre} no tiene {pocion.nombre} en el inventario.")

class Enemigo(Entidad):
    def __init__(self, nombre, salud, energia, ataque_basico, experiencia):
        super().__init__(nombre, salud, energia, ataque_basico)
        self.experiencia=experiencia

    def usar_habilidad(self, habilidad, objetivo):
        if self.puede_usar_habilidad(habilidad):
            self.atacar_con_habilidad(habilidad, objetivo)
        else:
            self.mostrar_falta_energia(habilidad)

    def puede_usar_habilidad(self, habilidad):
        return self.energia >= habilidad.energia_requerida

    def atacar_con_habilidad(self, habilidad, objetivo):
        objetivo.recibir_dano(habilidad.ataque)
        self.energia -= habilidad.energia_requerida
        print(f"{self.nombre} usó {habilidad.nombre} contra {objetivo.nombre}.")

    def falta_energia(self, habilidad):
        print(f"{self.nombre} no tiene suficiente energía para usar {habilidad.nombre}.")
      
