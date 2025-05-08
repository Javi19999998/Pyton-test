kast=0
kayser=0 
#print("Cuantas personas votaran?")
#int es PARA DEFINIR COMO ENTERO
#input es para PEDIR ALGO AL USUARIO 
#EL TEXTO DENTRO DEL INPUT ES LO MISMO QUE EL PRINT

cantvotantes=int(input("Cuantas personas votaran? " ))
#FOR I ES LO MISMO QUE EL PARA
#EL RANGO ES LA CANTIDAD DE VECES QUE SE REPETIRA EL PARA
for i in range(cantvotantes):
    print("por quien votara? " \
    "1- kast" \
    "2- kayser")
    voto=int(input("Ingrese su voto "))
    if voto==1:
        kast=kast+1
        print("votaste por kast ")
    elif voto==2:
        kayser=kayser+1
        print("votaste por kayser ")
    else:
        print("Voto nulo")
if kast>kayser:
    print("Gano Kast con ", kast, "votos")
elif kayser>kast:
    print ("Gano Kayser" , kayser,"votos")
else:
    print("Hubo empate")
