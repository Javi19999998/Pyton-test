# Paso 1: Solicitar datos
ingresos = int(input("Ingrese su ingreso mensual: "))
educacion = input("Ingrese su nivel educacional (Basico, Medio, Superior): ").capitalize()
nacionalidad = input("Ingrese su nacionalidad (Chilena o Extranjero): ").capitalize()

# Paso 2: Puntaje base por ingresos
if 500000 <= ingresos <= 1000000:
    base = 300000
elif 1000001 <= ingresos <= 1500000:
    base = 650000
elif ingresos > 1500000:
    base = 1000000
else:
    base = 0  # Si gana menos de 500 mil, no califica

# Paso 3: Multiplicador por educación
mult_educacion = {
    "Basico": 1,
    "Medio": 1.3,
    "Superior": 1.5
}.get(educacion, 1)  # Valor por defecto 1 si el ingreso es inválido

# Paso 4: Bono por nacionalidad
bono_nacionalidad = 300000 if nacionalidad == "Chilena" else 0

# Paso 5: Calcular puntaje total
puntaje_total = base * mult_educacion + bono_nacionalidad

# Paso 6: Mostrar resultado
print("\n=== RESULTADO DE EVALUACIÓN ===")
print(f"Ingreso base considerado: ${base:,}")
print(f"Multiplicador por educación ({educacion}): x{mult_educacion}")
print(f"Bono por nacionalidad ({nacionalidad}): ${bono_nacionalidad:,}")
print(f"👉 Puntaje total de crédito: ${puntaje_total:,.0f}")
