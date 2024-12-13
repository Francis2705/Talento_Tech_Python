import sqlite3

class Auto:
    def __init__(self, id, patente, marca, modelo, anio, chasis, cantidad_puertas):
        self.id = id
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.chasis = chasis
        self.cantidad_puertas = cantidad_puertas
    def mostrar(self): #listo
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
    def agregar(self): #listo
        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute('''INSERT INTO Autos (patente, marca, modelo, anio, chasis, cantidad_puertas) VALUES (?, ?, ?, ?, ?, ?)''', 
                    (self.patente, self.marca, self.modelo, self.anio, self.chasis, self.cantidad_puertas))

        conexion.commit()

        self.id = cursor.lastrowid #asigno el id creado por la bd

        conexion.close()
    def modificar(self, marca, modelo, anio, chasis, cantidad_puertas): #listo
        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute('''UPDATE Autos SET marca = ?, modelo = ?, anio = ?, chasis = ?, cantidad_puertas = ?
                    WHERE patente = ?''', (marca, modelo, anio, chasis, cantidad_puertas, self.patente))

        conexion.commit()

        conexion.close()
    def eliminar(self): #listo
        conexion = sqlite3.connect('curso_caba/taller_fmb.db')
        cursor = conexion.cursor()

        cursor.execute('''DELETE FROM Autos WHERE patente = ?''', (self.patente,))

        conexion.commit()

        conexion.close()

#id (primary key, autoincremental)
#nombre (string, unic, not null)
#descripcion (string, not null)
#cantidad (int, not null)
#precio (float, not null)
#categoria \interior o exterior del auto/ (string, not null)

class Repuesto:
    def __init__(self, id, nombre, descripcion, cantidad, precio, categoria):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria
    def mostrar_repuesto(self):
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