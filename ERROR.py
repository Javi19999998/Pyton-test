import random, time
while True:
    try:
        perros=int(input("Indique la cantidad de perros que participaran: "))
        cuota=random.randint(2,7)
        cumple=0
        # no_cumple=0
        print("La cuota minima de conejos es", cuota)

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
    except Exception:
        print("Solo debe poner numeros enteros")
        