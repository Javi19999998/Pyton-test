# Calcular el araccel a pagar segun grupo familiar y comuna en la que reside
# A continuacion , los descuentos por cumuna:
# La Florida 20%, La pintana 30%, Puente Alto 25%, San Joaquin 15%
# Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas=>4%
# Preguntar al usuario en que comuna vive
# Preguntar al usuario con cuantas personas vive
# El arancel actual es de 200.000 por semestre
# Basados en las respuestas del usuario  y en 
# la informacion dada, calcular su descuento

arancel=200000
desc=0
print("""Cual es su comuna de residencia:" \
"1.- La Florida" 
"2.- La Pintanini" 
"3.- Puente Alto" 
"4.- San Joaquin""")
residencia=int(input("Ingrese su comuna: "))
if residencia==1:
    desc=desc+0.20
    print("Su descuento es del 20%")
elif residencia==2:
    desc=desc+0.30
    print("Su descuento es del 30%")
elif residencia==3:
    desc=desc+0.25
    print("Su descuento es del 25%")
elif residencia==4:
    desc=desc+0.15
    print("Su descuento es del 15%")
else:
    print("La residencia no registra descuento")

# Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas=>4%

print("""Ingrese cuantas personas son en su grupo familiar " 
"1.- 1 = 2%
2.- 2 a 4=3%
3.- 5 o mas=4% """)

gfamiliar=int(input("Ingrese cuantas personas son: "))

if gfamiliar==1:
    desc=desc+0.02
elif gfamiliar>=2 and gfamiliar<=4:
    desc=desc+0.030
elif gfamiliar>=5:
    desc=desc+0.04
else:
    print("Su grupo familiar no tiene descuento")

print(desc)

total=arancel*(1-desc)

print("Su total es ", total)




    


