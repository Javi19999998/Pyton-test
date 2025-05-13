# uso y explicacion de match( enfrenta opciones PARECIDO AL IF)
#FUNCIONES: SE DEFINE LA FUNCION, NOMBRE DE LA OPCION, 

def suma():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese un numero: "))
    print("El resultado de la suma es: ", n1+n2)
# suma()
# suma() ESTO SIRVE PARA QUE SE EJECUTE CADA CODIGO

def resta():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese un numero: "))
    print("El resultado de la resta es: ", n1-n2)
# resta()

def multi():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese un numero: "))
    print("El resultado de la multiplicacion es: ", n1*n2)
# multi

def division():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese un numero: "))
    print("El resultado de la multiplicacion es: ", n1/n2)



def calcu():
    while True:
        op=int(input(""" Ingrese una operacion
             1.- Suma 
             2.- Resta 
             3.- Multiplicacion
             4.- Division
             5.- Salir
            """))
        match op:
            case 1:
                print("Suma")
                suma()
            case 2:
                print("Resta")
                resta()
            case 3:
                print("Multiplicacion")
                multi()
            case 4:
                print("Division")
                division()
            case 5:
                print("Saliendo...")
                break 
            case _:
                print("Opcion invalida")
calcu()
    


