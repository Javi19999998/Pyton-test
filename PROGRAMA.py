# Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
# En un delivery de Sushi vende 4 tipos de Sushi:
# 1. Pikachu Roll $4500
# 2. Otaku Roll $5000
# 3. Pulpo Venenoso Roll $5200
# 4. Anguila Eléctrica Roll $4800
# La empresa le ha solicitado a usted, que genere una pequeña aplicación en Python para tomar el pedido de un
# cliente el cuál puede ir agregando Rolls a través de un menú uno por uno con solo seleccionar la opción (1 a 4)
# La aplicación debe mostrar en un menú los Rolls que agregará el usuario, esto se debe repetir hasta que el usuario
# decida que su pedido está completo.
# Luego de ello, debe preguntar al usuario si posee un código de descuento. En caso de que posea el código, deberá
# ingresarlo. Si el código ingresado es “soyotaku”, debe realizar un 10% de descuento al total del pedido, en caso
# contrario enviar el mensaje “código no válido” y dar al usuario la opción de reingresar el código o volver al menú
# tecleando “X”
# Una vez realizado los pasos anteriores, debe mostrar el detalle del pedido contabilizando el total de productos y la
# cantidad de cada uno de ellos y si aplica o no el descuento
# Una vez que haya visualizado el detalle, debe preguntar al usuario si desea realizar otro pedido o salir del programa.
# Para finalizar suba el programa a un repositorio Github como respaldo y el link del repositorio a AVA en la actividad
# formativa 2 para aplicar la pauta de evaluación.
# total=0
# productos = {
#     1: ("Pikachu Roll", 4500),
#     2: ("Otaku Roll", 5000),
#     3: ("Pulpo Venenoso Roll", 5200),
#     4: ("Anguila Electrica Roll", 4800)
# }



print("Bienvenido a SushiOtaku")

total=0
carrito = {1: 0, 2: 0, 3: 0, 4: 0}
while True:
    op=int(input('''
                 Seleccione una opcion: 
                 1.- Pikachu Roll $4500
                 2.- Otaku Roll $5000
                 3.- Pulpo Venenoso Roll $5200
                 4.- Anguila Electrica Roll $4800
                 5.- Salir
                 '''))
    match op:
        case 1:
            total+=4500
        case 2:
            total+=5000
        case 3:
            total+=5200
        case 4:
            total+=4800
        case 5:
            print('''Tiene un codigo de descuento?
                  1.- Si
                  2.- No''')
            desc=int(input())
            if desc==1:
                print("Ingrese codigo de descuento")
            else:
                desc==2
            break
        case _:
            print("Opción invalida")
    print("Su total es: ", total)




codDescuento = input()
if codDescuento == "soyotaku":
    print("Aplica el Descuento")
    desc=total*0.1
    total=total-desc
    print("Su descuento es ", desc)
else:
    print("No aplica descuento")

print("Su total es: ", total)