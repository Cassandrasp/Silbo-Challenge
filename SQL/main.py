import crud

if __name__ == "__main__":
    crud.crearDB()

    # Crear 50 empresas
    for i in range(1, 51):
        crud.crear_empresa(f"Empresa {i}", f"Dirección {i}", f"12345678{i}", f"empresa{i}@example.com")

    # Crear 50 clientes
    for i in range(1, 51):
        crud.crear_cliente(1, f"Cliente {i}", f"Apellido {i}", f"Dirección {i}", f"12345678{i}", f"cliente{i}@example.com")

    # Crear 50 camisetas
    for i in range(1, 51):
        crud.crear_camiseta(1, 1, f"Camiseta {i}", "M", "Blanco", "Manga corta", i, i * 10)

    # Imprimir el contenido de las tablas
    print("Empresas:")
    empresas = crud.leer_empresas()
    for empresa in empresas:
        print(empresa)

    print("\nClientes:")
    clientes = crud.leer_clientes()
    for cliente in clientes:
        print(cliente)

    print("\nCamisetas:")
    camisetas = crud.leer_camisetas()
    for camiseta in camisetas:
        print(camiseta)




