from ListaPizza import ListaPizza
class NodoOrden():
    def __init__(self, numero, nombre):
        self.numero = numero
        self.nombre = nombre
        self.pizzas = ListaPizza()
        self.siguiente = None