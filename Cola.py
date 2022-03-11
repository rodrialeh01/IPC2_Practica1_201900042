from NodoOrden import NodoOrden
from ListaEntregados import ListaEntregados
import os
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
            print('>>Tiempo Total de Preparación: ' + str(actual.pizzas.TiempoTotal()) + ' minutos')
            print('-----------------------------------------------------------')
            actual = actual.siguiente

    def graficar(self):
        contenido = ''
        file = open('Graficas/Orden_No.'+str(self.ultimo.numero)+'.dot','w')
        actual = self.primero
        contenido += '''digraph G {
    rankdir=LR;
    node [shape="record"];\nlabel="Tiempo total de la cola: ''' + str(self.TiempoTotal()) + ' minutos"\n'
        if self.tamanio == 1:
            contenido += str(self.primero.numero) + '''[style="filled", color="black", fillcolor="darkolivegreen1"];'''+ str(self.primero.numero) + '[label="El pedido generado se encuentra en esta posición de la cola\\nSe esta atendiendo actualmente a: \\nNo. Orden '+str(self.primero.numero )+ '\\n Nombre: ' + str(self.primero.nombre) +'\\n Tiempo estimado: '+ str(self.primero.pizzas.TiempoTotal()) +' minutos"]\n'
        else:
            contenido += str(self.ultimo.numero) + '''[style="filled", color="black", fillcolor="skyblue"];'''
            contenido += str(self.primero.numero) + '''[style="filled", color="black", fillcolor="darkolivegreen1"];'''
            while(actual != None):
                contenido += str(actual.numero) + '[label="No. Orden '+str(actual.numero) + '\\n Nombre: ' + str(actual.nombre) +'\\n Tiempo estimado: '+ str(actual.pizzas.TiempoTotal()) + ' minutos"]\n'
                if actual == self.primero:
                    contenido += str(self.primero.numero) + '[label="Se esta atendiendo actualmente a: \\nNo. Orden '+str(self.primero.numero )+ '\\n Nombre: ' + str(self.primero.nombre) +'\\n Tiempo estimado: '+ str(self.primero.pizzas.TiempoTotal()) + ' minutos"]\n'
                    contenido += str(actual.siguiente.numero) + '->' + str(actual.numero) + '\n'
                elif actual.siguiente == None:
                    contenido += str(self.ultimo.numero) + '[label="El pedido generado se encuentra en esta posición de la cola \\nNo. Orden '+str(self.ultimo.numero )+ '\\n Nombre: ' + str(self.ultimo.nombre) +'\\n Tiempo estimado: '+ str(self.ultimo.pizzas.TiempoTotal()) + ' minutos"]\n'
                else:
                    contenido += str(actual.siguiente.numero) + '->' + str(actual.numero) + '\n'
                actual = actual.siguiente
        contenido += '}'
        file.write(contenido)
        file.close()
        os.system('dot -Tpng Graficas/Orden_No.'+str(self.ultimo.numero)+'.dot -o Orden_No.'+str(self.ultimo.numero)+'.png')
        os.startfile('Orden_No.'+str(self.ultimo.numero)+'.png')

    def abrirorden(self):        
        contenido = ''
        file = open('Graficas/OrdenActualizada_No.'+str(self.primero.numero)+'.dot','w')
        actual = self.primero
        contenido += '''digraph G {
    rankdir=LR;
    node [shape="record"];\nlabel="Tiempo total de la cola: ''' + str(self.TiempoTotal()) + ' minutos"\n'
        if self.tamanio == 1:
            contenido += str(self.primero.numero) + '''[style="filled", color="black", fillcolor="darkolivegreen1"];'''+ str(self.primero.numero) + '[label="Ahora se atendera a este pedido:\\nNo. Orden '+str(self.primero.numero )+ '\\n Nombre: ' + str(self.primero.nombre) +'\\n Tiempo estimado: '+ str(self.primero.pizzas.TiempoTotal()) + ' minutos"]\n'
        else:
            contenido += str(self.primero.numero) + '''[style="filled", color="black", fillcolor="darkolivegreen1"];'''
            while(actual != None):
                contenido += str(actual.numero) + '[label="No. Orden '+str(actual.numero) + '\\n Nombre: ' + str(actual.nombre) +'\\n Tiempo estimado: '+ str(actual.pizzas.TiempoTotal()) + ' minutos"]\n'
                if actual == self.primero:
                    contenido += str(self.primero.numero) + '[label="Se esta atendiendo actualmente a: \\nNo. Orden '+str(self.primero.numero )+ '\\n Nombre: ' + str(self.primero.nombre)  +'\\n Tiempo estimado: '+ str(self.primero.pizzas.TiempoTotal()) + ' minutos"]\n'
                    contenido += str(actual.siguiente.numero) + '->' + str(actual.numero) + '\n'
                elif actual.siguiente == None:
                    contenido += str(self.ultimo.numero) + '[label="No. Orden '+str(self.ultimo.numero )+ '\\n Nombre: ' + str(self.ultimo.nombre)  +'\\n Tiempo estimado: '+ str(self.ultimo.pizzas.TiempoTotal()) + ' minutos"]\n'
                else:
                    contenido += str(actual.siguiente.numero) + '->' + str(actual.numero) + '\n'
                actual = actual.siguiente
        contenido += '}'
        file.write(contenido)
        file.close()
        os.system('dot -Tpng Graficas/OrdenActualizada_No.'+str(self.primero.numero)+'.dot -o OrdenActualizada_No.'+str(self.primero.numero)+'.png')
        os.startfile('OrdenActualizada_No.'+str(self.primero.numero)+'.png')

    def graficarlista(self):
        contenido = ''
        file = open('Graficas/Cola.dot','w')
        actual = self.primero
        contenido += '''digraph G {
    rankdir=LR;
    node [shape="record"];\nlabel="Tiempo total de la cola: ''' + str(self.TiempoTotal()) + ' minutos"\n'
        if self.tamanio == 1:
            contenido += str(self.primero.numero) + '''[style="filled", color="black", fillcolor="darkolivegreen1"];'''+ str(self.primero.numero) + '[label="Se esta atendiendo actualmente a: \\nNo. Orden '+str(self.primero.numero )+ '\\n Nombre: ' + str(self.primero.nombre) +'\\n Tiempo estimado: '+ str(self.primero.pizzas.TiempoTotal()) +' minutos"]\n'
        else:
            contenido += str(self.primero.numero) + '''[style="filled", color="black", fillcolor="darkolivegreen1"];'''
            while(actual != None):
                contenido += str(actual.numero) + '[label="No. Orden '+str(actual.numero) + '\\n Nombre: ' + str(actual.nombre) +'\\n Tiempo estimado: '+ str(actual.pizzas.TiempoTotal()) + ' minutos"]\n'
                if actual == self.primero:
                    contenido += str(self.primero.numero) + '[label="Se esta atendiendo actualmente a: \\nNo. Orden '+str(self.primero.numero )+ '\\n Nombre: ' + str(self.primero.nombre) +'\\n Tiempo estimado: '+ str(self.primero.pizzas.TiempoTotal()) + ' minutos"]\n'
                    contenido += str(actual.siguiente.numero) + '->' + str(actual.numero) + '\n'
                elif actual.siguiente == None:
                    contenido += str(self.ultimo.numero) + '[label="No. Orden '+str(self.ultimo.numero )+ '\\n Nombre: ' + str(self.ultimo.nombre) +'\\n Tiempo estimado: '+ str(self.ultimo.pizzas.TiempoTotal()) + ' minutos"]\n'
                else:
                    contenido += str(actual.siguiente.numero) + '->' + str(actual.numero) + '\n'
                actual = actual.siguiente
        contenido += '}'
        file.write(contenido)
        file.close()
        os.system('dot -Tpng Graficas/Cola.dot -o  Cola.png')
        os.startfile('Cola.png')

    def TiempoTotal(self):
        t = 0
        actual = self.primero
        while(actual != None):
            t+= int(actual.pizzas.TiempoTotal())
            actual = actual.siguiente
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