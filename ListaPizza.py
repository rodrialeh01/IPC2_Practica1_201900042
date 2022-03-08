from NodoPizza import NodoPizza
class ListaPizza():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def Vacio(self):
        return self.primero == self.ultimo == None

    def InsertarPizza(self,numero, ingrediente, tiempo):
        nuevo = NodoPizza(numero,ingrediente, tiempo)
        if self.Vacio():
            self.primero = self.ultimo = nuevo
        elif self.primero == self.ultimo:
            self.ultimo = nuevo
            self.primero.siguiente = self.ultimo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.tamanio += 1

    def MostrarPizzas(self):
        actual = self.primero
        while(actual != None):
            print('==           PIZZA No.' + str(actual.numero) + '          ==')
            print('== Ingrediente: ' + str(actual.ingrediente))
            print('== Tiempo: ' + str(actual.tiempo))
    
    def __len__(self):
        return self.tamanio