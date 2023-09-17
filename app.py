from Conjunto import Conjunto
from Elemento import Elemento

conjunto_A = Conjunto("Conjunto A")

conjunto_A.agregar_elemento(Elemento("Juan"))
conjunto_A.agregar_elemento(Elemento("Ximena"))
conjunto_A.agregar_elemento(Elemento("Thomas"))
print(conjunto_A)

conjunto_B = Conjunto("Conjunto B")
conjunto_B.agregar_elemento(Elemento("Ximena"))
conjunto_B.agregar_elemento(Elemento("Pablo"))
conjunto_B.agregar_elemento(Elemento("Valentina"))
print(conjunto_B)

conjunto_unido = conjunto_A + conjunto_B
print(conjunto_unido)

conjunto_interseccion = Conjunto.intersectar(conjunto_A, conjunto_B)
print(conjunto_interseccion)