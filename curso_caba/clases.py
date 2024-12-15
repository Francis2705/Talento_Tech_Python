import sqlite3

class Auto:
    def __init__(self, id, patente, marca, modelo, anio, chasis, cantidad_puertas):
        """
        Inicializa un objeto Auto.

        Args:
            id (int): ID del auto en la base de datos.
            patente (str): Patente del auto.
            marca (str): Marca del auto.
            modelo (str): Modelo del auto.
            anio (int): Año de fabricación del auto.
            chasis (str): Número de chasis del auto.
            cantidad_puertas (int): Cantidad de puertas del auto.
        """
        self.id = id
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.chasis = chasis
        self.cantidad_puertas = cantidad_puertas
    def mostrar(self):
        """
        Muestra los datos del auto en formato legible para el usuario.
        """
        info_auto = f'''
--------------------------------
    ID: {self.id}
    Patente: {self.patente}
    Marca: {self.marca}
    Modelo: {self.modelo}
    Año: {self.anio}
    Chasis: {self.chasis}
    Cantidad de puertas: {self.cantidad_puertas}
--------------------------------'''
        print(info_auto)
    def agregar(self):
        """
        Agrega el auto a la base de datos.
        """
        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute('''INSERT INTO Autos (patente, marca, modelo, anio, chasis, cantidad_puertas) VALUES (?, ?, ?, ?, ?, ?)''', 
                    (self.patente, self.marca, self.modelo, self.anio, self.chasis, self.cantidad_puertas))

        conexion.commit()

        self.id = cursor.lastrowid #asigno el id creado por la bd

        conexion.close()
    def modificar(self, marca, modelo, anio, chasis, cantidad_puertas):
        """
        Modifica los datos del auto en la base de datos.

        Args:
            marca (str): Nueva marca del auto.
            modelo (str): Nuevo modelo del auto.
            anio (int): Nuevo año de fabricación del auto.
            chasis (str): Nuevo número de chasis del auto.
            cantidad_puertas (int): Nueva cantidad de puertas del auto.
        """
        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute('''UPDATE Autos SET marca = ?, modelo = ?, anio = ?, chasis = ?, cantidad_puertas = ?
                    WHERE patente = ?''', (marca, modelo, anio, chasis, cantidad_puertas, self.patente))

        conexion.commit()

        conexion.close()
    def eliminar(self):
        """
        Elimina el auto de la base de datos.
        """
        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute('''DELETE FROM Autos WHERE patente = ?''', (self.patente,))

        conexion.commit()

        conexion.close()

class Repuesto:
    def __init__(self, id, nombre, descripcion, cantidad, precio, categoria):
        """
        Inicializa un objeto Repuesto.

        Args:
            id (int): ID del repuesto en la base de datos.
            nombre (str): Nombre del repuesto.
            descripcion (str): Descripción del repuesto.
            cantidad (int): Cantidad disponible en stock.
            precio (float): Precio del repuesto.
            categoria (str): Categoría del repuesto ('interior' o 'exterior').
        """
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria
    def mostrar(self):
        """
        Muestra los datos del repuesto en formato legible para el usuario.
        """
        info_repuesto = f'''
--------------------------------
    ID: {self.id}
    Nombre: {self.nombre}
    Descripcion: {self.descripcion}
    Cantidad: {self.cantidad}
    Precio: {self.precio}
    Categoria: {self.categoria}
--------------------------------'''
        print(info_repuesto)
    def agregar(self):
        """
        Agrega el repuesto a la base de datos.
        """
        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute('''INSERT INTO Repuestos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)''', 
                    (self.nombre, self.descripcion, self.cantidad, self.precio, self.categoria))

        conexion.commit()

        self.id = cursor.lastrowid #asigno el id creado por la bd

        conexion.close()
    def modificar(self, nombre, descripcion, cantidad, precio, categoria):
        """
        Modifica los datos del repuesto en la base de datos.

        Args:
            nombre (str): Nuevo nombre del repuesto.
            descripcion (str): Nueva descripción del repuesto.
            cantidad (int): Nueva cantidad en stock.
            precio (float): Nuevo precio del repuesto.
            categoria (str): Nueva categoría del repuesto ('interior' o 'exterior').
        """
        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute('''UPDATE Repuestos SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
                    WHERE id = ?''', (nombre, descripcion, cantidad, precio, categoria, self.id))

        conexion.commit()

        conexion.close()
    def eliminar(self):
        """
        Elimina el repuesto de la base de datos.
        """
        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute('''DELETE FROM Repuestos WHERE id = ?''', (self.id,))

        conexion.commit()

        conexion.close()