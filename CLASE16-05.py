# Diccionario de productos
productos = {
    1: ("Jamon", 2500),
    2: ("Queso", 3000),
    3: ("Osobuco", 5500),
    4: ("Limon", 1500)
}

# Variables
carrito = []
nombre = ""

while True:
    try:
        op = int(input('''
Seleccione una opción:
1.- Ingrese su nombre
2.- Comprar
3.- Boleta
4.- Salir
> '''))
        
        match op:
            case 1:
                nombre = input("Ingrese su nombre: ")
                print(f"\nHola {nombre}, bienvenido al carrito de compras.")

            case 2:
                while True:
                    print("\nSeleccione un producto para comprar:")
                    print("1.- Jamon $2500")
                    print("2.- Queso $3000")
                    print("3.- Osobuco $5500")
                    print("4.- Limon $1500")
                    print("5.- Volver al menú principal")
                    
                    prod = int(input("> "))
                    if prod == 5:
                        break
                    elif prod == 1:
                        carrito.append(("Jamon", 2500))
                        print("Jamon agregado al carrito.")
                    elif prod == 2:
                        carrito.append(("Queso", 3000))
                        print("Queso agregado al carrito.")
                    elif prod == 3:
                        carrito.append(("Osobuco", 5500))
                        print("Osobuco agregado al carrito.")
                    elif prod == 4:
                        carrito.append(("Limon", 1500))
                        print("Limon agregado al carrito.")
                    else:
                        print("Opción inválida. Intente nuevamente.")

            case 3:
                
