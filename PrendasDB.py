import sqlite3
import random
import pandas as pd 

def conexionDB():
    # Establecer la conexión a la base de datos
    return sqlite3.connect("PrendasDB.db")  # Cambia el nombre de la base de datos según tu preferencia

def crearDB():
    conexion = conexionDB()
    cursor = conexion.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS StockPrendas (
        id_prenda INTEGER PRIMARY KEY AUTOINCREMENT,
        prenda VARCHAR(100),
        talla VARCHAR(10),
        color VARCHAR(20))""")

    # Confirmar cambios y cerrar conexión
    conexion.commit()
    conexion.close()

def crear_prendas():
    prendas = [
        ("Camiseta", "S", "Rojo"),
        ("Camiseta", "M", "Azul"),
        ("Pantalón", "L", "Negro"),
        ("Pantalón", "S", "Blanco"),
        ("Camisa", "M", "Verde"),
        ("Chaqueta", "L", "Gris"),
        ("Falda", "S", "Azul"),
        ("Vestido", "M", "Rojo"),
        ("Sudadera", "L", "Negro"),
        ("Jersey", "S", "Blanco"),
        ("Abrigo", "M", "Gris"),
        ("Shorts", "L", "Azul"),
        ("Bufanda", "S", "Verde"),
        ("Gorro", "M", "Rojo"),
        ("Chaleco", "L", "Negro"),
        ("Traje", "S", "Blanco"),
        ("Blusa", "M", "Azul"),
        ("Poncho", "L", "Verde"),
        ("Cinturón", "S", "Negro"),
        ("Calcetines", "M", "Rojo")
    ]
    conexion = conexionDB()
    cursor = conexion.cursor()
    for prenda in prendas:
        insert_query = "INSERT INTO StockPrendas (prenda, talla, color) VALUES (?, ?, ?)"
        cursor.execute(insert_query, prenda)
    conexion.commit()
    conexion.close()

def leer_prendas():
    conexion = conexionDB()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM StockPrendas")
    datos_prendas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos_prendas

def actualizar_prenda(id_prenda, nueva_prenda):
    conexion = conexionDB()
    cursor = conexion.cursor()
    update_query = "UPDATE StockPrendas SET prenda = ? WHERE id_prenda = ?"
    cursor.execute(update_query, (nueva_prenda, id_prenda))
    conexion.commit()
    cursor.close()
    conexion.close()

def borrar_prenda(id_prenda):
    conexion = conexionDB()
    cursor = conexion.cursor()
    delete_query = "DELETE FROM StockPrendas WHERE id_prenda = ?"
    cursor.execute(delete_query, (id_prenda,))
    conexion.commit()
    cursor.close()
    conexion.close()

    # Con esta función leemos los datos y lo pasamos a un DataFrame de Pandas
def sql_query(query):
    # Conectamos con la base de datos chinook.db
    connection = sqlite3.connect("PrendasDB.db")

    # Obtenemos un cursor que utilizaremos para hacer las queries
    cursor = connection.cursor()

    # Ejecuta la query
    cursor.execute(query)

    # Almacena los datos de la query 
    ans =  cursor.fetchall()

    # Obtenemos los nombres de las columnas de la tabla
    names = [description[0] for description in cursor.description]

    return pd.DataFrame(ans,columns=names)
