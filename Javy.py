# # VOTATOON
# # Designe 2 cantdidatos. Pregunte cuanto votantes son
# # por cada votante , debe peguntar por quin votrá
# # cuente la cantidad de votos y muestre los resultados
# # definir quien ganó la votacion. Considere empate

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
    voto=int(input("Ingrese su voto"))
    print("por quien votara?" \
    "1- kast" \
    "2- kayser")
    if voto==1:
        kast=kast+1
        print("votaste por kast")
    if voto==2:
        kayser=kayser+1
        print("votaste por kayser")
    else:
        print("Voto nulo")
if kast>kayser:
    print("Gano Kast con ", kast, "votos")
if kayser>kast:
    print ("Gano Kayser" , kayser,"votos")
else:
    print("Hubo empate")




