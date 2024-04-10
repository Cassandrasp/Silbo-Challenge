import sqlite3
import pandas as pd 
from itertools import product

#Conectar una DB
def conexionDB():
    return sqlite3.connect("PrendasDB.db")

# Crear una nueva DB
def crearDB():
    conexion = conexionDB()
    cursor = conexion.cursor()

    # Crear tabla de CaracteristicasPrendas
    cursor.execute("""CREATE TABLE IF NOT EXISTS CaracteristicasPrendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prenda TEXT NOT NULL,
        caracteristicas TEXT NOT NULL)""")

    # Crear tabla de StockPrendas
    cursor.execute("""CREATE TABLE IF NOT EXISTS StockPrendas (
        id_prenda INTEGER PRIMARY KEY AUTOINCREMENT,
        prenda VARCHAR(100),
        talla VARCHAR(10),
        color VARCHAR(20))""")

    # Confirmar cambios y cerrar conexión
    conexion.commit()
    conexion.close()

# Método CRUD: Crear una nueva prenda
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
    
    # Ampliar las combinaciones
    combinaciones_ampliadas = []

    for prenda, talla, color in prendas:
        for nueva_talla, nuevo_color in product(["XS", "S", "M", "L", "XL", "XXL"], ["Rojo", "Azul", "Negro", "Blanco", "Verde", "Gris", "Morado"]):
            combinaciones_ampliadas.append((prenda, nueva_talla, nuevo_color))

    # Eliminar duplicados
    combinaciones_ampliadas = list(set(combinaciones_ampliadas))

    # Conexión a la base de datos
    conexion = conexionDB()
    cursor = conexion.cursor()

    # Insertar las prendas originales
    for prenda in prendas:
        insert_query = "INSERT INTO StockPrendas (prenda, talla, color) VALUES (?, ?, ?)"
        cursor.execute(insert_query, prenda)

    # Insertar las prendas ampliadas
    for prenda_ampliada in combinaciones_ampliadas:
        insert_query = "INSERT INTO StockPrendas (prenda, talla, color) VALUES (?, ?, ?)"
        cursor.execute(insert_query, prenda_ampliada)

    conexion.commit()
    conexion.close()

# Método CRUD: Crear una nueva prenda
def leer_prendas():
    conexion = conexionDB()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM StockPrendas")
    datos_prendas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos_prendas

# Método CRUD: Actualizar una nueva prenda
def actualizar_prenda(id_prenda, nueva_prenda):
    conexion = conexionDB()
    cursor = conexion.cursor()
    update_query = "UPDATE StockPrendas SET prenda = ? WHERE id_prenda = ?"
    cursor.execute(update_query, (nueva_prenda, id_prenda))
    conexion.commit()
    cursor.close()
    conexion.close()

# Método CRUD: Borrar una nueva prenda
def borrar_prenda(id_prenda):
    conexion = conexionDB()
    cursor = conexion.cursor()
    delete_query = "DELETE FROM StockPrendas WHERE id_prenda = ?"
    cursor.execute(delete_query, (id_prenda,))
    conexion.commit()
    cursor.close()
    conexion.close()

# Método CRUD: Crear una nueva característica
def crear_caracteristicas():
    conexion = conexionDB()
    cursor = conexion.cursor()

    prendas_caracteristicas = {
        "Camisa": "Camisa de manga larga con cuello italiano y confeccionada en algodón.",
        "Pantalón": "Pantalón slim fit con detalle de bolsillos y cremalleras.",
        "Vestido": "Vestido con corte A y detalle de encaje en el escote.",
        "Chaqueta": "Chaqueta con diseño acolchado y detalles de botones en los puños.",
        "Zapatos": "Zapatos de material de cuero con suela antideslizante y plantilla acolchada.",
        "Falda": "Falda plisada con estampado de lunares y detalle de cinturón.",
        "Bufanda": "Bufanda tejida en lana con diseño de trenzas y borlas en los extremos.",
        "Sombrero": "Sombrero de ala ancha con detalle de lazo en la parte trasera.",
        "Suéter": "Suéter tejido de punto grueso con cuello alto y patrón de ochos.",
        "Gorra": "Gorra deportiva con paneles de malla para mayor ventilación y cierre ajustable.",
        "Abrigo": "Abrigo largo con cuello de solapa y cinturón para ajustar a la cintura.",
        "Pijama": "Pijama conjunto de pantalón y camiseta con estampado de estrellas y ajuste elástico.",
        "Bikini": "Bikini conjunto de top bandeau y braguita de tiro alto con diseño de hojas tropicales.",
        "Corbata": "Corbata clásica con diseño a rayas diagonales y tejido de seda.",
        "Mochila": "Mochila con varios compartimentos y bolsillo lateral para botella de agua.",
        "Guantes": "Guantes tejidos en lana con detalle de botón en la muñeca.",
        "Parka": "Parka con capucha desmontable y forro interior de pelo sintético.",
        "Sudadera": "Sudadera con capucha y detalle de estampado gráfico en la parte delantera.",
        "Medias": "Medias opacas con tejido elástico y refuerzo en la puntera.",
        "Chaleco": "Chaleco acolchado con cierre de cremallera y bolsillos frontales.",
        "Traje": "Traje de dos piezas con diseño entallado y solapa de muesca.",
        "Shorts": "Shorts de algodón con cintura elástica y detalle de cordón ajustable.",
        "Blusa": "Blusa de manga corta con detalle de pliegues en el escote y botones frontales.",
        "Poncho": "Poncho tejido con flecos en el borde y diseño geométrico.",
        "Cinturón": "Cinturón de cuero con hebilla metálica y detalle de pespuntes en los bordes.",
        "Calcetines": "Calcetines deportivos con tecnología de absorción de humedad y acolchado en la planta del pie.",
        "Top": "Top ajustado de tirantes con detalle de encaje en el escote.",
        "Traje de baño": "Traje de baño de una pieza con escote en V y detalle de volantes en la cintura.",
        "Botas": "Botas altas de cuero con tacón grueso y detalle de hebillas en el lateral."
    }

    # Insertar las prendas con sus características en la tabla CaracteristicasPrendas
    for prenda, caracteristicas in prendas_caracteristicas.items():
        cursor.execute("INSERT INTO CaracteristicasPrendas (prenda, caracteristicas) VALUES (?, ?)", (prenda, caracteristicas))
    conexion.commit()
    conexion.close()
    print("Características creadas correctamente.")


# Método CRUD: Leer todas las prendas y sus caracteristicas
def leer_caracteristicas():
    conexion = conexionDB()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM CaracteristicasPrendas")
    prendas = cursor.fetchall()
    for prenda in prendas:
        print(prenda)

# Método CRUD: Leer una prenda con caracteristica por su ID
def leer_caracteristicas_por_id(id):
    conexion = conexionDB()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM CaracteristicasPrendas WHERE id = ?", (id,))
    prenda = cursor.fetchone()
    print(prenda)

# Método CRUD: Actualizar características de una prenda
def actualizar_caracteristicas(id, nuevas_caracteristicas):
    conexion = conexionDB()
    cursor = conexion.cursor()
    cursor.execute("UPDATE CaracteristicasPrendas SET caracteristicas = ? WHERE id = ?", (nuevas_caracteristicas, id))
    conexion.commit()
    print("Características actualizadas correctamente.")

# Método CRUD: Eliminar una prenda con caracteristica por su ID
def eliminar_prenda_caracteristicas(id):
    conexion = conexionDB()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM CaracteristicasPrendas WHERE id = ?", (id,))
    conexion.commit()
    print("Prenda eliminada correctamente.")


#Conversor de SQL a PANDAS
def sql_query(query):
    connection = sqlite3.connect("PrendasDB.db")
    cursor = connection.cursor()
    cursor.execute(query)
    ans = cursor.fetchall()
    names = [description[0] for description in cursor.description]
    return pd.DataFrame(ans,columns=names)
