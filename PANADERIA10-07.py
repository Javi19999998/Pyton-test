productos = {
    "P001": ["Leche", "Lácteos", "Colun"],
    "P002": ["Pan", "Panadería", "BredenMaster"],
    "P003": ["Queso", "Lácteos", "Soprole"],
    "P004": ["Aceite", "Despensa", "Ideal"]
}

inventario = {
    "P001": [25, 950],
    "P002": [15, 500],
    "P003": [10, 1850],
    "P004": [8, 2200]
}

def op():
    while True:
        try:
            op=int(input(''' 
                1.- Mostrar productos
                2.- Buscar producto mas caro
                3.- Actualizar stock
                4.- Eliminar producto
                5.- Cambiar datos del producto
                6.- Salir 
             '''))
            if op == 1:
                mostrar_productos()
            elif op == 2:
                producto_caro()
            elif op == 3:
                actualizar_stock()
            elif op == 4:
                eliminar_productos()
            elif op == 5:
                cambiar_datosp()
            elif op == 6:
                print("Saliendo...")
                break
            else:
                print("Debe ingresar una opcion entre la 1 y la 6")
        except Exception:
            print("Opcion invalida, intente nuevamente")
    

def mostrar_productos():
    print("LISTA DE PRODUCTOS")
    #codigo = ID del producto (ej: "P001") datos = lista con nombre, categoría, proveedor (ej: ["Leche", "Lácteos", "Colun"])
    for codigo, datos in productos.items(): 
        nombre = datos[0]
        categoria = datos [1]
        proveedor = datos [2]
        if codigo in inventario:
            stock= inventario[codigo][0]
            precio= inventario[codigo][1]
            print("ID:", codigo, "| Nombre:", nombre, "| Categoría:", categoria ,"| Proveedor:", proveedor, "| Stock:" , stock, "| Precio: $",precio )
        else:
            print("ID:", codigo, "| Nombre:", nombre ,"(sin stock registrado)")
 
def producto_caro():
    mayor = 0
    codigo_mayor = ""
    for codigo, datos in inventario.items():
        if datos[1] > mayor:
            mayor = datos[1]
            codigo_mayor = codigo
    if codigo_mayor:
        nombre = productos[codigo_mayor][0]
        print("El producto más caro es:", nombre, "con un precio de", mayor)
    else:
        print("No hay productos en inventario.")
        
def actualizar_stock():
    codigo=input("Ingrese codigo del producto: ").upper()
    if codigo in inventario:
        nuevo_stock = int(input("Ingrese nueva cantidad: "))
        inventario[codigo][0] = nuevo_stock
        print("El inventario se actualizó correctamente.")
    else:
        print("El codigo es invalido")

def eliminar_productos():
    codigo = input("Ingrese código del producto a eliminar: ").upper()
    if codigo in productos and codigo in inventario:
        productos.pop(codigo)
        inventario.pop(codigo)
        print("El producto fue eliminado correctamente")
    else:
        print("No se logró eliminar producto, intente nuevamente")


def cambiar_datosp():
    codigo = input("Ingrese código del producto a modificar: ").upper()
    if codigo in productos:
        nuevo_nombre = input("Ingrese nuevo nombre: ")
        nueva_categoria = input("Ingrese nueva categoría: ")
        nuevo_proveedor = input("Ingrese nuevo proveedor: ")
        nuevo_valor= int(input("Ingrese nuevo valor: "))
        nuevo_stock=int(input("Ingrese nuevo stock: "))
        productos[codigo] = [nuevo_nombre, nueva_categoria, nuevo_proveedor]
        inventario[codigo][0] = nuevo_stock
        inventario[codigo][1]=nuevo_valor
        print("Datos actualizados correctamente.")
    else:
        print("El producto no existe.")

op()




