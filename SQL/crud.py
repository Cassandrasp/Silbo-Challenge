import sqlite3

def conexionDB():
    # Establecer la conexión a la base de datos
    return sqlite3.connect("SilboDB.db")  # Cambia el nombre de la base de datos según tu preferencia

def crearDB():
    conexion = conexionDB()
    cursor = conexion.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS DatosEmpresa (
        id_empresa INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_empresa VARCHAR(100),
        direccion_empresa VARCHAR(255),
        telefono_empresa VARCHAR(15),
        email_empresa VARCHAR(100))""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS DatosCliente (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        id_empresa INT,
        nombre VARCHAR(100),
        apellido VARCHAR(100),
        direccion VARCHAR(255),
        telefono VARCHAR(15),
        email VARCHAR(100),
        FOREIGN KEY (id_empresa) REFERENCES DatosEmpresa(id_empresa))""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS StockCamisetas (
        id_camiseta INTEGER PRIMARY KEY AUTOINCREMENT,
        id_empresa INT,
        id_cliente INT,
        nombre VARCHAR(100),
        talla VARCHAR(10),
        color VARCHAR(20),
        tiro VARCHAR(20),
        cantidad INT,
        precio DECIMAL(10, 2),
        FOREIGN KEY (id_empresa) REFERENCES DatosEmpresa(id_empresa),
        FOREIGN KEY (id_cliente) REFERENCES DatosCliente(id_cliente))""")

    # Confirmar cambios y cerrar conexión
    conexion.commit()
    conexion.close()

def crear_empresa(nombre, direccion, telefono, email):
    conexion = conexionDB()
    cursor = conexion.cursor()
    insert_query = "INSERT INTO DatosEmpresa (nombre_empresa, direccion_empresa, telefono_empresa, email_empresa) VALUES (?, ?, ?, ?)"
    datos_empresa = (nombre, direccion, telefono, email)
    cursor.execute(insert_query, datos_empresa)
    conexion.commit()
    cursor.close()
    conexion.close()

def leer_empresas():
    conexion = conexionDB()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM DatosEmpresa")
    datos_empresas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos_empresas

def actualizar_empresa(id_empresa, nueva_direccion):
    conexion = conexionDB()
    cursor = conexion.cursor()
    update_query = "UPDATE DatosEmpresa SET direccion_empresa = ? WHERE id_empresa = ?"
    cursor.execute(update_query, (nueva_direccion, id_empresa))
    conexion.commit()
    cursor.close()
    conexion.close()

def borrar_empresa(id_empresa):
    conexion = conexionDB()
    cursor = conexion.cursor()
    delete_query = "DELETE FROM DatosEmpresa WHERE id_empresa = ?"
    cursor.execute(delete_query, (id_empresa,))
    conexion.commit()
    cursor.close()
    conexion.close()

def crear_cliente(id_empresa, nombre, apellido, direccion, telefono, email):
    conexion = conexionDB()
    cursor = conexion.cursor()
    insert_query = "INSERT INTO DatosCliente (id_empresa, nombre, apellido, direccion, telefono, email) VALUES (?, ?, ?, ?, ?, ?)"
    datos_cliente = (id_empresa, nombre, apellido, direccion, telefono, email)
    cursor.execute(insert_query, datos_cliente)
    conexion.commit()
    cursor.close()
    conexion.close()

def leer_clientes():
    conexion = conexionDB()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM DatosCliente")
    datos_clientes = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos_clientes

def actualizar_cliente(id_cliente, nueva_direccion):
    conexion = conexionDB()
    cursor = conexion.cursor()
    update_query = "UPDATE DatosCliente SET direccion = ? WHERE id_cliente = ?"
    cursor.execute(update_query, (nueva_direccion, id_cliente))
    conexion.commit()
    cursor.close()
    conexion.close()

def borrar_cliente(id_cliente):
    conexion = conexionDB()
    cursor = conexion.cursor()
    delete_query = "DELETE FROM DatosCliente WHERE id_cliente = ?"
    cursor.execute(delete_query, (id_cliente,))
    conexion.commit()
    cursor.close()
    conexion.close()

def crear_camiseta(id_empresa, id_cliente, nombre, talla, color, tiro, cantidad, precio):
    conexion = conexionDB()
    cursor = conexion.cursor()
    insert_query = "INSERT INTO StockCamisetas (id_empresa, id_cliente, nombre, talla, color, tiro, cantidad, precio) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    datos_camiseta = (id_empresa, id_cliente, nombre, talla, color, tiro, cantidad, precio)
    cursor.execute(insert_query, datos_camiseta)
    conexion.commit()
    cursor.close()
    conexion.close()

def leer_camisetas():
    conexion = conexionDB()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM StockCamisetas")
    datos_camisetas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos_camisetas

def actualizar_camiseta(id_camiseta, nueva_cantidad):
    conexion = conexionDB()
    cursor = conexion.cursor()
    update_query = "UPDATE StockCamisetas SET cantidad = ? WHERE id_camiseta = ?"
    cursor.execute(update_query, (nueva_cantidad, id_camiseta))
    conexion.commit()
    cursor.close()
    conexion.close()

def borrar_camiseta(id_camiseta):
    conexion = conexionDB()
    cursor = conexion.cursor()
    delete_query = "DELETE FROM StockCamisetas WHERE id_camiseta = ?"
    cursor.execute(delete_query, (id_camiseta,))
    conexion.commit()
    cursor.close()
    conexion.close()