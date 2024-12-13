import re
from clases import *

#Funciones varias
def manejar_menu(menu: list):
    contador = 0
    for opcion in menu:
        print(opcion)
        contador = contador + 1
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            while respuesta > contador or respuesta <= 0:
                respuesta = int(input(f"Error. Ingrese un numero del 1 al {contador}: "))
            return int(respuesta)
        except ValueError:
            print("Error, ingrese un numero valido!")
def traer_autos():
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
    if agregar:
        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute("SELECT patente FROM Autos") #obtener todas las patentes existentes en la tabla Autos
        patentes_existentes = {row[0] for row in cursor.fetchall()}

        while True:
            patente = input("Ingrese la patente del auto: ").strip().upper().replace(" ", "")

            if re.fullmatch(r"[A-Z]{3}\d{3}", patente): #validar formato de 6 caracteres (AAA000)
                if patente in patentes_existentes:
                    print("Error. La patente ya existe en la base de datos. Intente nuevamente.\n")
                    continue
                conexion.close()
                return patente

            if re.fullmatch(r"[A-Z]{2}\s?\d{3}\s?[A-Z]{2}", patente): #validar formato de 7 caracteres (AA000AA)
                if patente in patentes_existentes:
                    print("Error. La patente ya existe en la base de datos. Intente nuevamente.\n")
                    continue
                conexion.close()
                return patente

            print("Error. Formato inválido. Intente nuevamente.\n")
    else:
        while True:
            patente = input("Ingrese la patente del auto: ").strip().upper().replace(" ", "")

            if re.fullmatch(r"[A-Z]{3}\d{3}", patente): #validar formato de 6 caracteres (AAA000)
                break

            if re.fullmatch(r"[A-Z]{2}\s?\d{3}\s?[A-Z]{2}", patente): #validar formato de 7 caracteres (AA000AA)
                break

            print("Error. Formato inválido. Intente nuevamente.\n")

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
    return input('Ingrese la marca: ').strip()
def pedir_modelo():
    return input('Ingrese el modelo: ').strip()
def pedir_anio():
    anio = input('Ingrese el año: ').strip()

    while True:
        if len(anio) == 4 and anio.isdigit() and int(anio) >= 1970 and int(anio) <= 2024:
            return anio
        else:
            anio = input('Error. Ingrese un año valido: ').strip()
def pedir_chasis():
    chasis = input('Ingrese el chasis: ').strip()

    while True:
        if any(c.isalpha() for c in chasis) and any(c.isdigit() for c in chasis):
            return chasis
        else:
            chasis = input('Error. Ingrese un chasis valido, tiene que ser alfanumerico: ').strip()
def pedir_cantidad_puertas():
    while True:
        try:
            cantidad_puertas = int(input("Ingrese la cantidad de puertas: "))
            while cantidad_puertas <= 1 or cantidad_puertas >= 10:
                cantidad_puertas = int(input(f"Error. Ingrese un numero del 2 al 9: "))
            return int(cantidad_puertas)
        except ValueError:
            print("Error, ingrese un numero valido!")

#CRUD AUTO
def modificar_auto(lista_autos: list, patente: str, auto: Auto):
    for i, a in enumerate(lista_autos): #i = indice, a = Auto
        if a.patente == patente:
            lista_autos[i] = auto
def eliminar_auto(lista_autos: list, auto: Auto):
    for a in lista_autos:
        if a.patente == auto.patente:
            lista_autos.remove(a)
def mostrar_autos(lista_autos: list):
    for a in lista_autos:
        a.mostrar()

#Pedido de datos (repuesto)
def pedir_nombre():
    return input('Ingrese el nombre: ').strip().lower()
def pedir_descripcion():
    return input('Ingrese la descripcion: ').strip().lower()
def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            while cantidad <= 0:
                cantidad = int(input(f"Error. Ingrese un numero mayor que 0: "))
            return int(cantidad)
        except ValueError:
            print("Error, ingrese un numero valido!")
def pedir_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            while precio <= 0:
                precio = float(input(f"Error. Ingrese un numero mayor que 0: "))
            return float(precio)
        except ValueError:
            print("Error, ingrese un numero valido!")
def pedir_categoria():
    categoria = input("Ingrese la categoria (interior o exterior): ").lower().strip()
    while categoria != 'interior' and categoria != 'exterior':
        categoria = input("Error! Ingrese una categoria valida (interior o exterior): ").lower().strip()
    return categoria
def pedir_repuesto():
    while True:
        try:
            id = int(input("Ingrese el id del repuesto: "))
            while id <= 0:
                id = int(input(f"Error. Ingrese un numero mayor que 0: "))
        except ValueError:
            print("Error, ingrese un numero valido!")

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
    for i, r in enumerate(lista_repuestos): #i = indice, r = Repuesto
        if r.id == id:
            lista_repuestos[i] = repuesto
def eliminar_repuesto(lista_repuestos: list, repuesto: Repuesto):
    for r in lista_repuestos:
        if r.id == repuesto.id:
            lista_repuestos.remove(r)
def mostrar_repuestos(lista_repuesto: list):
    for r in lista_repuesto:
        r.mostrar()
def reporte_bajo_stock():
    lista_repuestos_bajo_stock = []
    conexion = sqlite3.connect('curso_caba/taller_fmb.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Repuestos WHERE cantidad < 20")
    registros = cursor.fetchall()

    for r in registros:
        repuesto = Repuesto(r[0], r[1], r[2], r[3], r[4], r[5])
        lista_repuestos_bajo_stock.append(repuesto)

    return lista_repuestos_bajo_stock