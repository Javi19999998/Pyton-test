#perro de caza
#pida al usuario la cantidad de perros
#muestre cual es la cuota minima de conejos 
#luego consulte cuantos conejos trajo
#si el perro trajo la cantidad minima
#cumplio la cuota, si no, se queda sin filete
#mostrar resumen de perros de cumplieron y los que no.
import random, time
perros=int(input("Indique la cantidad de perros que participaran: "))
cuota=random.randint(2,7)
cumple=0
# no_cumple=0
print("La cuota minima de conejos es", cuota)

#OPCION 1
# for i in range(1, perros+1):
#     conejos=int(input("Cuantos conejos trajo el perro: "))
#     if conejos>=cuota:
#         cumple+=1
#     else:
#         no_cumple+=1
# print("Los perros que cumplieron la cuota son", cumple)
# print("Los perros que no cumplieron la cuota son", no_cumple)


#OPCION 2
for p in range(perros):
    conejos=random.randint(0,8)
    time.sleep(1)
    if conejos>=cuota:
        print(f"El perro {p+1} trajo {conejos} conejos, cumplio la cuota")
        cumple+=1
    else:
        print(f"El perro {p+1} trajo {conejos} conejos, se quedo sin filete")
print("El total de perros que cumple la cuota fue", cumple)
print("El total de perros que cumple la cuota fue", perros-cumple)