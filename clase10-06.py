nombres=[]
apellidos=[]
while True:
    print('''
          1.- Ingresar nombre y apellido
          2.- Buscar nombre
          3.- Mostrar lista
          4.- Salir
          ''')
    op=int(input('Ingrese una opcion: '))
    match op:
        case 1:
            nombre=input('Ingrese un nombre: ')
            nombres.append(nombre)
            print(nombres)
            apellido=input('Ingrese un apellido: ')
            apellidos.append(apellido)
            print(apellidos)
        case 2:
            busca=input("Ingrese el nombe a buscar: ")
            if busca in nombres:
                print("El nombre", busca, "esta e esta lista")
            else:
                print("El nombre", busca, "no esta en la lista")
            if busca in apellidos:
                print("El apellido", busca, "esta en la lista")
            else:
                print("El apellido", busca, "no esta en la lista")
        case 3:
            cont=0
            for n in nombres:
                print(cont+1, ".-", nombres[cont], apellidos[cont])
                cont+=1
            # for i in range(len(nombres)):
            #     print(i+1, ".-", nombres[i], apellidos[i])
        case 4:
            print('Saliendo del programa...')
            break
        case _:
            print('Opcion no valida, intente de nuevo.')


           # for i, nombre in enumerate(nombres, start=1):
            #     print(i, nombre)
            #     print('Lista de nombres:')
            # for i, apellido in enumerate(apellidos, start=1):
            #     print(i, apellido)
            #     print('Lista de apellidos:')