autos = {
    'ABC123': ['Toyota', 2020, 'Gasolina', '1.6L'],
    'DEF456': ['Chevrolet', 2019, 'Diesel', '2.0L'],
    'GHI789': ['Hyundai', 2021, 'Eléctrico', '0.0L'],
    'JKL321': ['Mazda', 2022, 'Gasolina', '2.5L']
}

stock = {
    'ABC123': [14, 12500000],
    'DEF456': [0, 10400000],
    'GHI789': [4, 17900000],
    'JKL321': [6, 15500000],
    'ZZZ000': [2, 8900000]  # No está en autos
}

def mostrar_stock():
    print("\nMODELO | CANTIDAD | PRECIO")
    for modelo, datos in stock.items():
        cantidad, precio = datos
        nombre = autos.get(modelo, ["(No registrado)"])[0]
        print(f"{modelo} | {cantidad} unidades | ${precio:,} ({nombre})")

def precio_mas_alto():
    max_precio = -1
    modelo_max = ""
    for modelo, datos in stock.items():
        if datos[1] > max_precio:
            max_precio = datos[1]
            modelo_max = modelo
    if modelo_max in autos:
        marca = autos[modelo_max][0]
        print(f"\nEl auto más caro es el {marca} ({modelo_max}) con precio ${max_precio:,}")
    else:
        print(f"\nEl modelo más caro es {modelo_max}, pero no está registrado en 'autos'.")

def actualizar_stock():
    modelo = input("Ingrese modelo a actualizar stock: ").upper()
    if modelo in stock:
        try:
            nueva_cantidad = int(input("Ingrese nueva cantidad en stock: "))
            stock[modelo][0] = nueva_cantidad
            print("Stock actualizado.")
        except:
            print("Debe ingresar un número.")
    else:
        print("Modelo no encontrado.")

def borrar_modelo():
    modelo = input("Ingrese modelo a borrar: ").upper()
    if modelo in autos:
        del autos[modelo]
        print("Auto eliminado del diccionario 'autos'.")
    else:
        print("Ese modelo no estaba en 'autos'.")
    if modelo in stock:
        del stock[modelo]
        print("Modelo eliminado de 'stock'.")
    else:
        print("Ese modelo no estaba en 'stock'.")

def actualizar_datos_vehiculo():
    modelo = input("Ingrese modelo a actualizar: ").upper()
    if modelo in autos:
        print("Datos actuales:", autos[modelo])
        nueva_marca = input("Nueva marca: ")
        nuevo_anio = int(input("Nuevo año: "))
        nuevo_tipo = input("Nuevo tipo de combustible: ")
        nuevo_motor = input("Nuevo tamaño de motor: ")
        autos[modelo] = [nueva_marca, nuevo_anio, nuevo_tipo, nuevo_motor]
        print("Datos del vehículo actualizados.")
    else:
        print("Modelo no encontrado en 'autos'.")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar stock de cada uno")
        print("2. Buscar precio más alto")
        print("3. Actualizar stock")
        print("4. Borrar un modelo (incluye stock)")
        print("5. Actualizar datos del vehículo")
        print("6. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            mostrar_stock()
        elif opcion == "2":
            precio_mas_alto()
        elif opcion == "3":
            actualizar_stock()
        elif opcion == "4":
            borrar_modelo()
        elif opcion == "5":
            actualizar_datos_vehiculo()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

menu()
