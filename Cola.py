from NodoOrden import NodoOrden
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
            return aux
        elif self.tamanio == 2:
            aux = self.primero
            self.primero = self.ultimo
            self.primero.siguiente = None
            self.tamanio -= 1
            return aux
        else:
            aux = self.primero
            self.primero = self.primero.siguiente
            self.tamanio -= 1
            return aux

    def MostrarCola(self):
        actual = self.primero
        while actual != None:
            print('ID: ' + str(actual.numero))
            actual = actual.siguiente

    def __len__(self):
        return self.tamanio

'''

PRUEBAS CON LA COLA
C = Cola()
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
#C.MostrarCola()
print('Tamaño de la Cola: ' + str(len(C)))
print('DESENCOLANDO')
print('Salió: ' + str(C.Desencolar().numero))
print('Tamaño de la Cola: ' + str(len(C)))
print('----------------------------------')
print('Salió: ' + str(C.Desencolar().numero))
print('Tamaño de la Cola: ' + str(len(C)))
print('----------------------------------')
print('Salió: ' + str(C.Desencolar().numero))
print('Tamaño de la Cola: ' + str(len(C)))

'''
