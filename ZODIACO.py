import random

# -------- PARTE 1: Signo Zodiacal --------
dia = int(input("Ingrese su día de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento (número): "))

# Determinar el signo zodiacal
def obtener_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricornio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"
    else:
        return "Fecha inválida"

signo = obtener_signo(dia, mes)
print(f"\nTu signo zodiacal es: {signo}")

# -------- PARTE 2: Número aleatorio y símbolo ▄ --------
while True:
    n1 = int(input("\nIngresa un primer número (entre 1 y 98): "))
    n2 = int(input("Ingresa un segundo número mayor que el primero: "))
    if n1 < n2:
        break
    else:
        print("❌ El segundo número debe ser mayor que el primero. Intenta de nuevo.")

# Número aleatorio entre n1 y n2
aleatorio = random.randint(n1, n2)
print(f"\nNúmero aleatorio generado: {aleatorio}")
print("Símbolo ▄ impreso", aleatorio, "veces:\n")

# Imprimir símbolo ▄
print("▄" * aleatorio)
