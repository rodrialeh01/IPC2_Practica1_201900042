from NodoOrden import NodoOrden
from ListaEntregados import ListaEntregados
class Cola():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def Vacio(self):
        return self.primero == self.ultimo == None

    def Encolar(self, numero, nombre):
        nuevo = NodoOrden(numero, nombre)
        if self.Vacio():
            self.primero = self.ultimo = nuevo
        elif self.primero == self.ultimo:
            self.ultimo = nuevo
            self.primero.siguiente = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        print('Entró: ' + str(nuevo.numero))
        self.tamanio += 1

    def Desencolar(self):
        if self.tamanio == 0:
            return None
        elif self.tamanio == 1:
            aux = self.primero
            self.primero = self.ultimo = None
            self.tamanio -= 1
            aux.siguiente = None
            return aux
        elif self.tamanio == 2:
            aux = self.primero
            self.primero = self.ultimo
            self.primero.siguiente = None
            self.tamanio -= 1
            aux.siguiente = None
            return aux
        else:
            aux = self.primero
            self.primero = self.primero.siguiente
            self.tamanio -= 1
            aux.siguiente = None
            return aux

    def MostrarCola(self):
        actual = self.primero
        print('===========================================================')
        print('==                LISTA DE PEDIDOS EN COLA               ==')
        print('===========================================================')
        while actual != None:
            print('Orden No.: ' + str(actual.numero))
            print('Nombre del Cliente: ' + str(actual.nombre))
            actual.pizzas.MostrarPizzas()
            print('Tiempo Total de Preparación: ' + str(actual.pizzas.TiempoTotal()) + ' minutos')
            print('-----------------------------------------------------------')
            actual = actual.siguiente

    def TiempoTotal(self):
        t = 0
        actual = self.primero
        while(actual != None):
            t+= int(actual.pizzas.TiempoTotal())
        return t

    def __len__(self):
        return self.tamanio


'''
#PRUEBAS CON LA COLA
C = Cola()
L = ListaEntregados()
print('ENCOLANDO')
print('----------------------------------')
C.Encolar(1,'Rodri')
#C.MostrarCola()
print('Tamaño de la Cola: ' + str(len(C)))
print('----------------------------------')
C.Encolar(2,'Alejandro')
#C.MostrarCola()
print('Tamaño de la Cola: ' + str(len(C)))
print('----------------------------------')
C.Encolar(3,'Diego')
print('Tamaño de la Cola: ' + str(len(C)))
C.Encolar(4,'Felix')
#C.MostrarCola()
print('Tamaño de la Cola: ' + str(len(C)))
print('DESENCOLANDO')
L.AgregarEntregados(C.Desencolar())
L.AgregarEntregados(C.Desencolar())
L.AgregarEntregados(C.Desencolar())
L.AgregarEntregados(C.Desencolar())
L.MostrarEntregados()
'''