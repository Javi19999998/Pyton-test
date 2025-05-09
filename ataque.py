import random
import time

def mostrar_barra(hp):
    total_barras = 20
    barras_actuales = int(hp / 2.5)
    return "[" * barras_actuales + " " * (total_barras - barras_actuales) + "]"

# Paso 1: Nombres
peleador1 = input("Ingresa el nombre del primer peleador: ")
peleador2 = input("Ingresa el nombre del segundo peleador: ")

# Paso 2: HP inicial
hp1 = 50
hp2 = 50

# Paso 3: Pelea por turnos
turno = 1
while hp1 > 0 and hp2 > 0:
    print(f"\n--- Turno {turno} ---")
    
    if turno % 2 != 0:
        atacante = peleador1
        defensor = peleador2
        hp_defensor = hp2
    else:
        atacante = peleador2
        defensor = peleador1
        hp_defensor = hp1

    # Paso 4: Ataque
    ataque = random.randint(3, 15)
    critico = random.random() < 0.2
    if critico:
        ataque *= 2
        print(f"¡ATAQUE CRÍTICO de {atacante}!")

    print(f"{atacante} ataca a {defensor} causando {ataque} de daño.")

    # Paso 5: Restar daño
    if turno % 2 != 0:
        hp2 -= ataque
        if hp2 < 0:
            hp2 = 0
    else:
        hp1 -= ataque
        if hp1 < 0:
            hp1 = 0

    # Paso 6: Mostrar barra de energía
    print(f"{peleador1} HP: {hp1} {mostrar_barra(hp1)}")
    print(f"{peleador2} HP: {hp2} {mostrar_barra(hp2)}")

    time.sleep(1)
    turno += 1

# Paso 7: Anunciar ganador
print("\n--- FIN DE LA PELEA ---")
if hp1 <= 0:
    print(f"¡{peleador2} gana la pelea!")
else:
    print(f"¡{peleador1} gana la pelea!")
