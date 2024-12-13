#documentar los metodos
#hacer el README explicando toda la funcionalidad
#modularizar el codigo
#usar colorama (para darle color a la terminal)

from funciones import *

menu_principal = ['\nBienvenido! Elija la opcion en la cual quiera operar:\n1.Autos', '2.Repuestos', '3.Salir']
menu_autos = ['1.Agregar un auto', '2.Modificar un auto', '3.Eliminar un auto', '4.Mostrar un auto', '5.Mostrar todos los autos', '6.Salir']
menu_repuestos = ['1.Agregar un repuesto', '2.Modificar un repuesto', '3.Eliminar un repuesto', '4.Mostrar un repuesto', 
                '5.Mostrar todos los repuestos', '6.Consultar stock bajo', '7.Salir']

lista_autos = traer_autos()
lista_repuestos = traer_repuestos()

while True:
    respuesta = manejar_menu(menu_principal)
    match respuesta:
        case 1:
            while True:
                respuesta = manejar_menu(menu_autos)
                match respuesta:
                    case 1:
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
                    case 2:
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
                    case 3:
                        auto = pedir_patente(False)
                        if auto:
                            auto = Auto(auto[0], auto[1], auto[2], auto[3], auto[4], auto[5], auto[6])
                            auto.eliminar()
                            eliminar_auto(lista_autos, auto)
                            print('Eliminacion exitosa!')
                        else:
                            print('Error! Patente inexistente.')
                    case 4:
                        auto = pedir_patente(False)
                        if auto:
                            auto = Auto(auto[0], auto[1], auto[2], auto[3], auto[4], auto[5], auto[6])
                            auto.mostrar()
                        else:
                            print('Error! Patente inexistente.')
                    case 5:
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
                        nombre = pedir_nombre()
                        descripcion = pedir_descripcion()
                        cantidad = pedir_cantidad()
                        precio = pedir_precio()
                        categoria = pedir_categoria()
                        
                        repuesto = Repuesto(0, nombre, descripcion, cantidad, precio, categoria)
                        repuesto.agregar()
                        lista_repuestos.append(repuesto)
                        print('Repuesto agregado exitosamente!')
                    case 2:
                        repuesto = pedir_repuesto()

                        if repuesto:
                            nombre = pedir_nombre()
                            descripcion = pedir_descripcion()
                            cantidad = pedir_cantidad()
                            precio = pedir_precio()
                            categoria = pedir_categoria()

                            repuesto = Repuesto(repuesto[0], repuesto[1], repuesto[2], repuesto[3], repuesto[4], repuesto[5])
                            repuesto.modificar(nombre, descripcion, cantidad, precio, categoria)
                            modificar_repuesto(lista_repuestos, repuesto.id, repuesto)
                            print('Modificacion exitosa!')
                        else:
                            print('Error! Repuesto inexistente.')
                    case 3:
                        repuesto = pedir_repuesto()

                        if repuesto:
                            repuesto = Repuesto(repuesto[0], repuesto[1], repuesto[2], repuesto[3], repuesto[4], repuesto[5])
                            repuesto.eliminar()
                            eliminar_repuesto(lista_repuestos, repuesto)
                            print('Eliminacion exitosa!')
                        else:
                            print('Error! Repuesto inexistente.')
                    case 4:
                        repuesto = pedir_repuesto()

                        if repuesto:
                            repuesto = Repuesto(repuesto[0], repuesto[1], repuesto[2], repuesto[3], repuesto[4], repuesto[5])
                            repuesto.mostrar()
                        else:
                            print('Error! Repuesto inexistente.')
                    case 5:
                        lista_repuestos.clear()
                        lista_repuestos = traer_repuestos()
                        mostrar_repuestos(lista_repuestos)
                    case 6:
                        print('Los siguientes repuestos estan bajos de stock (menor a 20):')
                        lista_repuestos_bajo_stock = reporte_bajo_stock()
                        mostrar_repuestos(lista_repuestos_bajo_stock)
                    case 7:
                        break
        case 3:
            break