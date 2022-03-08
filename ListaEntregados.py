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
            self.ultimo = pedido
            self.primero.siguiente = self.ultimo
        else:
            self.ultimo.siguiente = pedido
            self.ultimo = pedido
        self.tamanio += 1

    def MostrarEntregados(self):
        actual = self.primero
        print('=======================================')
        print('==           ENTREGADOS:             ==')
        while(actual != None):
            print('Id: ' + str(actual.numero))
            actual = actual.siguiente

    def __len__(self):
        return self.tamanio