# crear programa de manejo de notas 
# 1-.- Ingresar Nota 
# 2.- Borrar Nota 
# 3.- Mostrar Notas
# 4.- Sacar Promedio, nota mayor y nota menor
# 5.- Limpiar todas las notas 
# 6.- Salir

notas=[]
while True:
    menu=int(input('''
                 1.- Ingresar Nota
                 2.- Borrar Nota
                 3.- Mostrar Notas
                 4.- Sacar Promedio, nota mayor y nota menor
                 5.- Limpiar todas las notas
                 6.- Salir
                 Seleccione una opcion: '''))
    match menu:
        case 1:
            nota=float(input('Ingrese la nota: '))
            notas.append(nota)
            print(f'Nota {nota} ingresada correctamente.')
        case 2:
            if notas:
                nota_borrar=float(input('Ingrese la nota a borrar: '))
                if nota_borrar in notas:
                    notas.remove(nota_borrar)
                    print(f'Nota {nota_borrar} borrada correctamente.')
                else:
                    print('Nota no encontrada.')
            else:
                print('No hay notas para borrar.')
        case 3:
            if notas:
                print('Notas:', notas)
            else:
                print('No hay notas para mostrar.')
        case 4:
            if notas:
                promedio = sum(notas) / len(notas)
                mayor = max(notas)
                menor = min(notas)
                print(f'Promedio: {promedio}, Nota Mayor: {mayor}, Nota Menor: {menor}')
            else:
                print('No hay notas para calcular.')
        case 5:
            notas.clear()
            print('Todas las notas han sido limpiadas.')
        case 6:
            print('Saliendo del programa...')
            break
        case _:
            print('Opción no válida, intente nuevamente.')

