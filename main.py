from Cola import Cola

Cola_de_Pedidos = Cola()
def AgregarOrden(c):
    try:
        global Cola_de_Pedidos
        nombre = str(input('== Ingrese el nombre del Cliente:                        ==\n>'))
        cantidad = int(input('== Ingrese la Cantidad de Pizzas que desea comprar       ==\n>'))
        Cola_de_Pedidos.Encolar(c,nombre)
        contador = 1
        while(contador<=cantidad):
            print('==                    INGREDIENTES                       ==')
            print('===========================================================')
            print('== 1. Pepperoni.                                         ==')
            print('== 2. Salchicha.                                         ==')
            print('== 3. Carne.                                             ==')
            print('== 4. Queso.                                             ==')
            print('== 5. Piña.                                              ==')
            ingrediente = int(input('== Seleccione un ingrediente para la Pizza No.'+str(contador)+'          ==\n>'))
            if ingrediente == 1:
                Cola_de_Pedidos.ultimo.pizzas.InsertarPizza(contador,'Pepperoni',3)
                contador += 1
            elif ingrediente == 2:
                Cola_de_Pedidos.ultimo.pizzas.InsertarPizza(contador,'Salchicha',4)
                contador += 1
            elif ingrediente == 3:
                Cola_de_Pedidos.ultimo.pizzas.InsertarPizza(contador,'Carne',10)
                contador += 1
            elif ingrediente == 4:
                Cola_de_Pedidos.ultimo.pizzas.InsertarPizza(contador,'Queso',5)
                contador += 1
            elif ingrediente == 5:
                Cola_de_Pedidos.ultimo.pizzas.InsertarPizza(contador,'Piña',2)
                contador += 1
            else:
                print('\n== OPCION INVALIDA :c                                    ==')
    except:
        print('== HUBO UN ERROR :c                                      ==')


def creditos():
    print('===========================================================')
    print('===========================================================')
    print('== Nombre: Rodrigo Alejandro Hernández de León           ==')
    print('== Carnet: 201900042                                     ==')
    print('== Curso: Introducción a la Programación y Computación 2 ==')
    print('== Carrera: Ingeniería en Ciencias y Sistemas            ==')
    print('== Universidad de San Carlos de Guatemala                ==')
    print('== Hecho en marzo 2022                                   ==')
    print('===========================================================')
    print('===========================================================')
contadororden = 1
def menu():
    global contadororden
    global Cola_de_Pedidos
    opcion = 0
    while(int(opcion) != 5):
        print('===========================================================')
        print('==             SISTEMA DE CONTROL DE PIZZAS              ==')
        print('===========================================================')
        print('===========================================================')
        print('== 1. Agregar una orden.                                 ==')
        print('== 2. Mostrar las ordenes pendientes.                    ==')
        print('== 3. Mostrar las ordenes entregadas.                    ==')
        print('== 4. Creditos del sistema.                              ==')
        print('== 5. Salir del programa.                                ==')
        print('===========================================================')
        try:
            opcion = int(input('== Elija una opción:                                     ==\n>'))
            if opcion == 1:
                AgregarOrden(contadororden)
                contadororden += 1
            elif opcion == 2:
                if len(Cola_de_Pedidos) == 0:
                    print('>>>>>>>>>>No hay Ordenes en Cola<<<<<<<<<<<')
                else:
                    Cola_de_Pedidos.MostrarCola()
            elif opcion == 3:
                pass
            elif opcion == 4:
                creditos()
            elif opcion == 5:
                print('== Adios, Vuelve Pronto c:                               ==')
                break
            else:
                print('\n== OPCION INVALIDA :c                                    ==')
        except:
            print('\n== OPCION INVALIDA :c                                    ==')

menu()