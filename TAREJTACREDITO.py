# Descripción de la Actividad:
# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.
# Las opciones disponibles deben estar construidas de la siguiente forma:
# 1. Pago de Tarjeta de Crédito:
# a. El usuario comienza con una deuda de $100.000
# b. El usuario puede ingresar un monto para realizar un pago en la
# tarjeta de crédito.
# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# la tarjeta.
# e. Al pagar el sistema debe descontar de la deuda total
# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# saldo de la tarjeta.
# 2. Simulación de Compras:
# a. El usuario puede simular realizar un número ilimitado de compras.
# b. Para cada compra, se solicita al usuario ingresar el monto de la
# compra. El programa suma los montos de cada compra.
# c. Se verifica que el monto de la compra sea mayor o igual a cero.
# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# iteración del bucle for.
# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# A considerar:
# 1. Manejo de Errores:
# a. Se utilizan bloques try y except para manejar posibles errores al
# ingresar datos, validar valores no numéricos y errores inesperados.
# b. Se debe programar mensajes de error específicos para guiar al
# usuario sobre posibles problemas

# op=int(input(''' Ingrese una opción:
#              1.- Pago de Tarjeta de Crédito
#              2.- Simulación de Compras
#              3.- Salir'''))
# while True:
#     match op:
#         case 1:
#             print("Usted tiene una deuda de $100.000")
#             deuda=100000
#             print("Que sea hacer: 1. pagar, 2. salir: ")
#             op=int(input())
#             if op==1:
#                 while True:
#                     try:
#                         pago=int(input("Ingrese el monto a pagar: "))
#                         if pago<0:
#                             print("Debe ingresar un monto mayor a 0")
#                         if pago>deuda:
#                             print("El monto a pagar no puede ser mayor a la deuda")
#                         deuda-=pago
#                         print("Su deuda es de: ", deuda)
#                         break
# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.
# Las opciones disponibles deben estar construidas de la siguiente forma:
# 1. Pago de Tarjeta de Crédito:
# a. El usuario comienza con una deuda de $100.000
# b. El usuario puede ingresar un monto para realizar un pago en la
# tarjeta de crédito.
# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# la tarjeta.
# e. Al pagar el sistema debe descontar de la deuda total
# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# saldo de la tarjeta.
# 2. Simulación de Compras:
# a. El usuario puede simular realizar un número ilimitado de compras.
# b. Para cada compra, se solicita al usuario ingresar el monto de la
# compra. El programa suma los montos de cada compra.
# c. Se verifica que el monto de la compra sea mayor o igual a cero.
# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# iteración del bucle for.
# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# A considerar:
# 1. Manejo de Errores:
# a. Se utilizan bloques try y except para manejar posibles errores al
# ingresar datos, validar valores no numéricos y errores inesperados.
# 2
# b. Se debe programar mensajes de error específicos para guiar al
# usuario sobre posibles problemas.
# Instrucciones para el envío de la actividad
deuda=100000
saldo=500000
while True:
    try:
        opc=int(input("""Menu
            1.- Pago de Credito
            2.- Simulacion de compras
            3.- Consulta de Saldo
            4.- Salir
            """))
        match opc:
            case 1:
                print("Usted tiene una deuda de $ ",deuda)
                while True:
                    try:
                        op2=int(input("""Desea pagar o volver al menu
                              1.- Pagar
                              2.- Volver al menu
                              """))
                        break
                    except Exception:
                        print("Ingrese valores numericos")
                        if op2==1:
                            while True:
                                try:
                                    pago_credito=int(input("Ingrese el monto que va a pagar : "))
                                    break
                                except Exception:
                                    while pago_credito<0 and pago_credito<=deuda:
                                        while True:
                                            try:
                                                print("Ingrese un monto valido")
                        pago_credito=int(input("""Ingrese 1 para salir
                        Ingrese el monto que va a pagar : """))
                        if pago_credito==1:
                            print("No quiere pagar nada")
                            break    
                    deuda=deuda-pago_credito
                    saldo=saldo+pago_credito
                    print("Su saldo es $ ", saldo)
                    print("Su deuda es $ ", deuda)
                if op2==2:
                    print("")
            case 2:
                while True:
                    try:
                        compra=int(input("Ingrese el monto a pagar"))
                        if compra<=saldo:
                            print("Pago realizado con exito")
                            saldo=saldo-compra
                            deuda=deuda+compra
                        else:
                            print("Su saldo no es suficiente")
            case 3:
                print("Su saldo es $ ", saldo)
            case 4:
                print("Saliendo...")
                break
            case _ :
                print("Opcion invalida")
    except:
        print("Ingrese un valor valido")

