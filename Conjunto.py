class Conjunto:
    
    contador:int = 0

    def __init__(self, nombre:str):
        self.__id = Conjunto.contador
        self.elementos:list = []
        self.nombre:str = nombre
        Conjunto.contador = Conjunto.contador+1
        
    
    @property
    def id(self):
        return self.__id
    
    def contiene(self, elemento) -> bool:
        for e in self.elementos:
            if e.nombre == elemento.nombre:
                return True
        return False
    
    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)
    
    def unir(self, otro_conjunto: "Conjunto"):
        for elemento in otro_conjunto.elementos:
            if not self.contiene(elemento):
                self.agregar_elemento(elemento)
    
    def __add__(self, otro_conjunto: "Conjunto"):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto
    
    @classmethod
    def intersectar(cls, conjunto1: "Conjunto", conjunto2: "Conjunto"):
        elementos_interseccion = []
        for elemento in conjunto1.elementos:
            if elemento in conjunto2.elementos:
                elementos_interseccion.append(elemento)
        return print(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}", elementos_interseccion)
    
    def __str__(self) -> str:
        return f"{self.nombre}: ({','.join(elemento.nombre for elemento in self.elementos)})"