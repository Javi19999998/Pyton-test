while True:
    try:
        int(input("Ingrese un numero: "))
        break
    except Exception:
        print("Es solo numeros")