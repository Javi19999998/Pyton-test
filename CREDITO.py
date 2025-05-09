#Calcular el puntaje de credito
#De bede calcular que tanto credito tiene una persona
#en cierta entidad financiera, debera considerar
#cantidad de ingresos, nivel educacional y nacionalidad
#Cantidad de ingresos
#500.000 a 1.000.000 : 300.000
#1.000.001 a 1.500.000: 650.000
#1.500.001 o mas : 1.000.000
#Nivel Educacional
#Basico : x1, medio: x1.3 , superior: x1.5
#Nacionalidad
#Chilena : +300.000, Extranjero: +0

credito=0
ingresos=int(input("Cual es su cantidad de ingresos "))

if ingresos>=500000 and ingresos<=1000000:
    credito=credito+300000
elif ingresos>=1000001 and ingresos<=1500000:
    credito=credito+650000
elif ingresos>=1500001:
    credito=credito+1000000
else:
    print("Su sueldo es insuficiente para sacar un crédito")

print(""" Ingrese su nivel Educacional 
      1.- Basico
      2.- Medio
      3.- Superior """)

neducacion=int(input())

if neducacion==1:
    credito=credito*1
elif neducacion==2:
    credito=credito*1.3
elif neducacion==3:
    credito=credito*1.5
else:
    print("Su nivel de educacion no es valido")


print(""" Ingrese su Nacionalidad
      1.- Chileno
      2.- Veneco
     """)

Nacionalidad=int(input())

if Nacionalidad==1:
    credito=credito+300000
elif Nacionalidad==2:
    credito=credito+0
else:
    print("Su nacionalidad no es valida")

print("El total de su credito es ", credito)
