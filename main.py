def AgregarOrden():
    pass

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

def menu():
    opcion = 0
    while(int(opcion) != 4):
        print('===========================================================')
        print('==             SISTEMA DE CONTROL DE PIZZAS              ==')
        print('===========================================================')
        print('===========================================================')
        print('== 1. Agregar una orden.                                 ==')
        print('== 2. Mostrar las ordenes.                               ==')
        print('== 3. Creditos del sistema.                              ==')
        print('== 4. Salir del programa.                                ==')
        print('===========================================================')
        try:
            opcion = int(input('== Elija una opción:                                     ==\n>'))
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                creditos()
            elif opcion == 4:
                print('== Adios, Vuelve Pronto c:                               ==')
                break
            else:
                print('\n== OPCION INVALIDA :c                                    ==')
        except:
            print('\n== OPCION INVALIDA :c                                    ==')

menu()