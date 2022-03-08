class ListaEntregados():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def Vacio(self):
        return self.primero == self.ultimo == None

    def AgregarEntregados(self, pedido):
        if self.Vacio():
            self.primero = self.ultimo = pedido
        elif self.primero == self.ultimo:
            self.primero = pedido
            self.primero.siguiente = self.ultimo
        else:
            aux = self.primero
            self.primero = pedido
            self.primero.siguiente = aux
            
        self.tamanio += 1

    def MostrarEntregados(self):
        actual = self.primero
        print('=======================================')
        print('==           ENTREGADOS:             ==')
        while(actual != None):
            print('Orden No.' + str(actual.numero))
            print('Nombre del Cliente: ' + str(actual.nombre))
            actual = actual.siguiente

    def __len__(self):
        return self.tamanio