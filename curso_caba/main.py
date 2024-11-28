#pasar todo a clases
#hacer todo con modelos de autos
#hacer que tenga id, pero que cuando busque el auto, busque por patente
#un crud de autos y otro crud de repuestos de autos
#documentar los metodos
#la bd se va a llamar "taller_fmb.db"
#hacer el README.txt explicando toda la funcionalidad

#Atributos del auto#

#id (primary key, autoincremental)
#patente (string, unic, not null) #validar que sean 6 o 7 caracteres alfanumericos
#marca (string, not null)
#modelo (string, not null)
#chasis (string, not null)
#cantidad_puertas (int, not null)

#Atributos de los repuestos#

#id (primary key, autoincremental)
#nombre (string, unic, not null)
#descripcion (string, not null)
#cantidad (int, not null)
#precio (float, not null)
#categoria \interior o exterior del auto/ (string, not null) 

#Requerimientos#

#permitir actualizar por el id (en caso de los repuestos, y por patente en caso de los autos)
#permitir elimimar por el id (en caso de los repuestos, y por patente en caso de los autos)
#permitir buscar por el id (en caso de los repuestos, y por patente en caso de los autos) y mostrar todos los datos del objeto
#consultar reporte de bajo stock (para los repuestos, todos los q tengan menos de 20 de cantidad)

#Librerias#

#colorama (para darle color a la terminal)
#sqlite3 (para la bd)
#regex (para cualquier posible validacion)

from funciones import *

menu = ['1.Agregar un producto', '2.Modificar un producto', 
        '3.Eliminar un producto', '4.Mostrar un producto', '5.Mostrar todos los productos', '6.Salir']
lista_productos = []

while True:
    respuesta = manejar_menu(menu)
    match respuesta:
        case 1:
            nombre = pedir_nombre("Ingrese el nombre del producto: ")
            cantidad = pedir_cantidad("Ingrese la cantidad del producto: ")
            producto = crear_producto(nombre, cantidad)

            if agregar_producto(lista_productos, producto):
                print("Producto agregado con exito!")
            else:
                print("Error! Producto repetido!")
        case 2:
            if len(lista_productos) == 0:
                print("Error, no hay productos en la lista para modificar")
            else:
                nombre_viejo = pedir_nombre("Ingrese el nombre del producto a modificar: ")
                nombre_nuevo = pedir_nombre("Ingrese el nuevo nombre del producto: ")
                cantidad_nueva = pedir_cantidad("Ingrese la nueva cantidad del producto: ")
                nuevo_producto = crear_producto(nombre_nuevo, cantidad_nueva)

                if modificar_producto(lista_productos, nombre_viejo, nuevo_producto):
                    print("Producto modificado con exito!")
                else:
                    print("Error! Producto inexistente!")
        case 3:
            if len(lista_productos) == 0:
                print("Error, no hay productos en la lista para eliminar")
            else:
                nombre_eliminado = pedir_nombre("Ingrese el nombre del producto a eliminar: ")

                if eliminar_producto(lista_productos, nombre_eliminado):
                    print("Producto eliminado con exito!")
                else:
                    print("Error! Producto inexistente!")
        case 4:
            if len(lista_productos) == 0:
                print("Error, no hay productos en la lista para mostrar")
            else:
                nombre_buscado = pedir_nombre("Ingrese el nombre del producto a mostrar: ")
                flag_existe, descripcion = mostrar_producto(lista_productos, nombre_buscado)
                if flag_existe:
                    print(descripcion)
                else:
                    print("Error! Producto inexistente!")
        case 5:
            if len(lista_productos) == 0:
                print("Error, no hay productos en la lista para mostrar")
            else:
                mostrar_productos(lista_productos)
        case 6:
            break