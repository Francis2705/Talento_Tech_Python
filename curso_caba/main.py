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