def manejar_menu(menu: list):
    for opcion in menu:
        print(opcion)
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            while respuesta >= 7 or respuesta <= 0:
                respuesta = int(input("Error. Ingrese un numero del 1 al 6: "))
            return int(respuesta)
        except ValueError:
            print("Error, ingrese un numero valido!")

def pedir_nombre(mensaje: str):
    nombre = input(mensaje)
    while nombre.isnumeric():
        nombre = input("Error, el nombre no puede ser solo numeros. Ingrese un nombre valido: ")
    return nombre.lower()

def pedir_cantidad(mensaje: str):
    while True:
        try:
            cantidad = int(input(mensaje))
            while cantidad <= 0:
                cantidad = int(input("Error, la cantidad no puede ser igual o menor a cero. Ingrese una cantidad valida: "))
            return cantidad
        except ValueError:
            print("Error, ingrese un numero entero positivo, no un caracter o un numero con coma!")

def crear_producto(nombre: str, cantidad: int):
    producto = {
        "nombre" : nombre,
        "cantidad" : cantidad
    }
    return producto

#CRUD
def agregar_producto(lista_productos: list, producto: dict):
    if len(lista_productos) == 0:
        lista_productos.append(producto)
        return True
    else:
        for p in lista_productos:
            if p['nombre'] == producto['nombre']:
                return False #el producto ya existe
        lista_productos.append(producto)
        return True

def modificar_producto(lista_productos: list, nombre_viejo: str, nuevo_producto: dict):
    for i, p in enumerate(lista_productos): #i = indice, p = diccionario
        if p['nombre'] == nombre_viejo:
            lista_productos[i] = nuevo_producto
            return True
    return False

def eliminar_producto(lista_productos: list, nombre_producto: str):
    for p in lista_productos:
        if p['nombre'] == nombre_producto:
            lista_productos.remove(p)
            return True
    return False

def mostrar_producto(lista_productos: list, nombre_buscado: str):
    for p in lista_productos:
        if p['nombre'] == nombre_buscado:
            descripcion = f"""\n--------------\nNombre: {nombre_buscado.capitalize()}\nCantidad: {p['cantidad']}\n--------------\n"""
            return True, descripcion
    return False, None

def mostrar_productos(lista_productos: list):
    for p in lista_productos:
        print(f"""\n--------------\nNombre: {p['nombre'].capitalize()}\nCantidad: {p['cantidad']}\n--------------\n""")