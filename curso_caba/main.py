#documentar los metodos
#hacer el README.txt explicando toda la funcionalidad
#modularizar el codigo

#Requerimientos#


#permitir actualizar por el id (en caso de los repuestos, y por patente en caso de los autos)
#permitir elimimar por el id (en caso de los repuestos, y por patente en caso de los autos)
#permitir buscar por el id (en caso de los repuestos, y por patente en caso de los autos) y mostrar todos los datos del objeto
#consultar reporte de bajo stock (para los repuestos, todos los q tengan menos de 20 de cantidad)

#Librerias#

#colorama (para darle color a la terminal)

from funciones import *

menu_principal = ['\nBienvenido! Elija la opcion en la cual quiera operar:\n1.Autos', '2.Repuestos', '3.Salir']
menu_autos = ['1.Agregar un auto', '2.Modificar un auto', '3.Eliminar un auto', '4.Mostrar un auto', '5.Mostrar todos los autos', '6.Salir']
menu_repuestos = ['1.Agregar un repuesto', '2.Modificar un repuesto', '3.Eliminar un repuesto', '4.Mostrar un repuesto', 
                '5.Mostrar todos los repuestos', '6.Consultar stock bajo', '7.Salir']

lista_autos = traer_autos()
lista_repuestos = []

while True:
    respuesta = manejar_menu(menu_principal)
    match respuesta:
        case 1: #listo
            while True:
                respuesta = manejar_menu(menu_autos)
                match respuesta:
                    case 1: #agregar (listo)
                        patente = pedir_patente(True)
                        marca = pedir_marca()
                        modelo = pedir_modelo()
                        anio = pedir_anio()
                        chasis = pedir_chasis()
                        cantidad_puertas = pedir_cantidad_puertas()

                        auto = Auto(0, patente, marca, modelo, anio, chasis, cantidad_puertas)
                        auto.agregar()
                        lista_autos.append(auto)
                        print('Auto agregado exitosamente!')
                    case 2: #modificar (listo)
                        auto = pedir_patente(False)
                        if auto:
                            marca = pedir_marca()
                            modelo = pedir_modelo()
                            anio = pedir_anio()
                            chasis = pedir_chasis()
                            cantidad_puertas = pedir_cantidad_puertas()

                            auto = Auto(auto[0], auto[1], auto[2], auto[3], auto[4], auto[5], auto[6])
                            auto.modificar(marca, modelo, anio, chasis, cantidad_puertas)
                            modificar_auto(lista_autos, auto.patente, auto)
                            print('Modificacion exitosa!')
                        else:
                            print('Error! Patente inexistente.')
                    case 3: #eliminar (listo)
                        auto = pedir_patente(False)
                        if auto:
                            auto = Auto(auto[0], auto[1], auto[2], auto[3], auto[4], auto[5], auto[6])
                            auto.eliminar()
                            eliminar_auto(lista_autos, auto)
                            print('Eliminacion exitosa!')
                        else:
                            print('Error! Patente inexistente.')
                    case 4: #mostrar uno (listo)
                        auto = pedir_patente(False)
                        if auto:
                            auto = Auto(auto[0], auto[1], auto[2], auto[3], auto[4], auto[5], auto[6])
                            auto.mostrar()
                        else:
                            print('Error! Patente inexistente.')
                    case 5: #mostrar todos (listo)
                        lista_autos.clear()
                        lista_autos = traer_autos()
                        mostrar_autos(lista_autos)
                    case 6:
                        break
        case 2:
            while True:
                respuesta = manejar_menu(menu_repuestos)
                match respuesta:
                    case 1:
                        pass #agregar
                    case 2:
                        pass #modificar
                    case 3:
                        pass #eliminar
                    case 4:
                        pass #mostrar uno
                    case 5:
                        pass #mostrar todos
                    case 6:
                        pass #consultar bajo stock
                    case 7:
                        break
        case 3:
            break