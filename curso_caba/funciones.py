import re
from clases import *
from colorama import *

#Funciones varias
def manejar_menu(menu: list):
    """
    Muestra un menú y solicita al usuario que seleccione una opción válida.

    Args:
        menu (list): Lista de opciones del menú.

    Returns:
        int: Opción seleccionada por el usuario.
    """
    contador = 0
    for opcion in menu:
        print(opcion)
        contador = contador + 1
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            while respuesta > contador or respuesta <= 0:
                respuesta = int(input(Fore.RED + f"Error. Ingrese un numero del 1 al {contador}: " + Style.RESET_ALL))
            return int(respuesta)
        except ValueError:
            print(Fore.RED + "Error, ingrese un numero valido!" + Style.RESET_ALL)
def traer_autos():
    """
    Obtiene la lista de autos desde la base de datos.

    Returns:
        list: Lista de objetos Auto.
    """
    lista_autos = []
    conexion = sqlite3.connect('curso_caba/taller_fmb.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Autos")
    registros = cursor.fetchall()

    for a in registros:
        auto = Auto(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
        lista_autos.append(auto)

    return lista_autos
def traer_repuestos():
    """
    Obtiene la lista de repuestos desde la base de datos.

    Returns:
        list: Lista de objetos Repuesto.
    """
    lista_repuestos = []
    conexion = sqlite3.connect('curso_caba/taller_fmb.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Repuestos")
    registros = cursor.fetchall()

    for r in registros:
        repuesto = Repuesto(r[0], r[1], r[2], r[3], r[4], r[5])
        lista_repuestos.append(repuesto)

    return lista_repuestos

#Pedido de datos (auto)
def pedir_patente(agregar: bool):
    """
    Solicita una patente de auto al usuario y valida su formato.

    Args:
        agregar (bool): Indica si se está agregando un nuevo auto.

    Returns:
        str or bool: La patente del auto (si es válida) o False si no se encuentra el auto.
    """
    if agregar:
        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute("SELECT patente FROM Autos") #obtener todas las patentes existentes en la tabla Autos
        patentes_existentes = {row[0] for row in cursor.fetchall()}

        while True:
            patente = input("Ingrese la patente del auto: ").strip().upper().replace(" ", "")

            if re.fullmatch(r"[A-Z]{3}\d{3}", patente): #validar formato de 6 caracteres (AAA000)
                if patente in patentes_existentes:
                    print(Fore.RED + "Error. La patente ya existe en la base de datos. Intente nuevamente.\n" + Style.RESET_ALL)
                    continue
                conexion.close()
                return patente

            if re.fullmatch(r"[A-Z]{2}\s?\d{3}\s?[A-Z]{2}", patente): #validar formato de 7 caracteres (AA000AA)
                if patente in patentes_existentes:
                    print(Fore.RED + "Error. La patente ya existe en la base de datos. Intente nuevamente.\n" + Style.RESET_ALL)
                    continue
                conexion.close()
                return patente

            print(Fore.RED + "Error. Formato inválido. Intente nuevamente.\n" + Style.RESET_ALL)
    else:
        while True:
            patente = input("Ingrese la patente del auto: ").strip().upper().replace(" ", "")

            if re.fullmatch(r"[A-Z]{3}\d{3}", patente): #validar formato de 6 caracteres (AAA000)
                break

            if re.fullmatch(r"[A-Z]{2}\s?\d{3}\s?[A-Z]{2}", patente): #validar formato de 7 caracteres (AA000AA)
                break

            print(Fore.RED + "Error. Formato inválido. Intente nuevamente.\n" + Style.RESET_ALL)

        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM Autos")
        registros = cursor.fetchall()
        conexion.close()

        for a in registros:
            if patente == a[1]:
                return a
        return False
def pedir_marca():
    """
    Solicita la marca del auto al usuario.

    Returns:
        str: Marca del auto.
    """
    return input('Ingrese la marca: ').strip()
def pedir_modelo():
    """
    Solicita el modelo del auto al usuario.

    Returns:
        str: Modelo del auto.
    """
    return input('Ingrese el modelo: ').strip()
def pedir_anio():
    """
    Solicita y valida el año de fabricación del auto.

    Returns:
        str: Año del auto.
    """
    anio = input('Ingrese el año: ').strip()

    while True:
        if len(anio) == 4 and anio.isdigit() and int(anio) >= 1970 and int(anio) <= 2024:
            return anio
        else:
            anio = input(Fore.RED + 'Error. Ingrese un año valido: ' + Style.RESET_ALL).strip()
def pedir_chasis():
    """
    Solicita y valida el número de chasis del auto.

    Returns:
        str: Número de chasis.
    """
    chasis = input('Ingrese el chasis: ').strip()

    while True:
        if any(c.isalpha() for c in chasis) and any(c.isdigit() for c in chasis):
            return chasis
        else:
            chasis = input(Fore.RED + 'Error. Ingrese un chasis valido, tiene que ser alfanumerico: ' + Style.RESET_ALL).strip()
def pedir_cantidad_puertas():
    """
    Solicita y valida la cantidad de puertas del auto.

    Returns:
        int: Cantidad de puertas.
    """
    while True:
        try:
            cantidad_puertas = int(input("Ingrese la cantidad de puertas: "))
            while cantidad_puertas <= 1 or cantidad_puertas >= 10:
                cantidad_puertas = int(input(Fore.RED + "Error. Ingrese un numero del 2 al 9: " + Style.RESET_ALL))
            return int(cantidad_puertas)
        except ValueError:
            print(Fore.RED + "Error, ingrese un numero valido!" + Style.RESET_ALL)

#CRUD AUTO
def modificar_auto(lista_autos: list, patente: str, auto: Auto):
    """
    Modifica un auto en la lista basado en su patente.

    Args:
        lista_autos (list): Lista de autos.
        patente (str): Patente del auto a modificar.
        auto (Auto): Objeto Auto con los nuevos datos.
    """
    for i, a in enumerate(lista_autos): #i = indice, a = Auto
        if a.patente == patente:
            lista_autos[i] = auto
def eliminar_auto(lista_autos: list, auto: Auto):
    """
    Elimina un auto de la lista basado en su patente.

    Args:
        lista_autos (list): Lista de autos.
        auto (Auto): Objeto Auto a eliminar.
    """
    for a in lista_autos:
        if a.patente == auto.patente:
            lista_autos.remove(a)
def mostrar_autos(lista_autos: list):
    """
    Muestra la información de todos los autos en la lista.

    Args:
        lista_autos (list): Lista de autos.
    """
    for a in lista_autos:
        a.mostrar()

#Pedido de datos (repuesto)
def pedir_nombre():
    """
    Solicita el nombre del repuesto al usuario.

    Returns:
        str: Nombre del repuesto.
    """
    return input('Ingrese el nombre: ').strip().lower()
def pedir_descripcion():
    """
    Solicita la descripción del repuesto al usuario.

    Returns:
        str: Descripción del repuesto.
    """
    return input('Ingrese la descripcion: ').strip().lower()
def pedir_cantidad():
    """
    Solicita y valida la cantidad de un repuesto.

    Returns:
        int: Cantidad del repuesto.
    """
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            while cantidad <= 0:
                cantidad = int(input(Fore.RED + "Error. Ingrese un numero mayor que 0: " + Style.RESET_ALL))
            return int(cantidad)
        except ValueError:
            print(Fore.RED + "Error, ingrese un numero valido!" + Style.RESET_ALL)
def pedir_precio():
    """
    Solicita y valida el precio de un repuesto.

    Returns:
        float: Precio del repuesto.
    """
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            while precio <= 0:
                precio = float(input(Fore.RED + "Error. Ingrese un numero mayor que 0: " + Style.RESET_ALL))
            return float(precio)
        except ValueError:
            print(Fore.RED + "Error, ingrese un numero valido!" + Style.RESET_ALL)
def pedir_categoria():
    """
    Solicita y valida la categoría del repuesto.

    Returns:
        str: Categoría del repuesto ('interior' o 'exterior').
    """
    categoria = input("Ingrese la categoria (interior o exterior): ").lower().strip()
    while categoria != 'interior' and categoria != 'exterior':
        categoria = input(Fore.RED + "Error! Ingrese una categoria valida (interior o exterior): " + Style.RESET_ALL).lower().strip()
    return categoria
def pedir_repuesto():
    """
    Solicita un ID de repuesto al usuario y valida si existe en la base de datos.

    Returns:
        tuple or bool: Tupla con los datos del repuesto si existe, o False si no se encuentra.
    """
    while True:
        try:
            id = int(input("Ingrese el id del repuesto: "))
            while id <= 0:
                id = int(input(Fore.RED + "Error. Ingrese un numero mayor que 0: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Error, ingrese un numero valido!" + Style.RESET_ALL)
            continue

        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM Repuestos")
        registros = cursor.fetchall()
        conexion.close()

        for r in registros:
            if id == r[0]:
                return r
        return False

#CRUD REPUESTO
def modificar_repuesto(lista_repuestos: list, id: int, repuesto: Repuesto):
    """
    Modifica un repuesto en la lista basado en su ID.

    Args:
        lista_repuestos (list): Lista de repuestos.
        id (int): ID del repuesto a modificar.
        repuesto (Repuesto): Objeto Repuesto con los nuevos datos.
    """
    for i, r in enumerate(lista_repuestos): #i = indice, r = Repuesto
        if r.id == id:
            lista_repuestos[i] = repuesto
def eliminar_repuesto(lista_repuestos: list, repuesto: Repuesto):
    """
    Elimina un repuesto de la lista basado en su ID.

    Args:
        lista_repuestos (list): Lista de repuestos.
        repuesto (Repuesto): Objeto Repuesto a eliminar.
    """
    for r in lista_repuestos:
        if r.id == repuesto.id:
            lista_repuestos.remove(r)
def mostrar_repuestos(lista_repuesto: list):
    """
    Muestra la información de todos los repuestos en la lista.

    Args:
        lista_repuesto (list): Lista de repuestos.
    """
    for r in lista_repuesto:
        r.mostrar()
def reporte_bajo_stock():
    """
    Genera un reporte de repuestos con stock bajo (menos de 20 unidades).

    Returns:
        list: Lista de objetos Repuesto con stock bajo.
    """
    lista_repuestos_bajo_stock = []
    conexion = sqlite3.connect('curso_caba/taller_fmb.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Repuestos WHERE cantidad < 20")
    registros = cursor.fetchall()

    for r in registros:
        repuesto = Repuesto(r[0], r[1], r[2], r[3], r[4], r[5])
        lista_repuestos_bajo_stock.append(repuesto)

    return lista_repuestos_bajo_stock