# Paso 1: Lista de productos (nombre, categoría, precio base)
productos = [
    {"nombre": "Lápiz", "categoria": 1, "precio": 700},
    {"nombre": "Cuaderno", "categoria": 1, "precio": 900},
    {"nombre": "Regla", "categoria": 1, "precio": 600},
    
    {"nombre": "Mochila", "categoria": 2, "precio": 3200},
    {"nombre": "Cartuchera", "categoria": 2, "precio": 1500},
    {"nombre": "Libro", "categoria": 2, "precio": 4000},
    
    {"nombre": "Laptop", "categoria": 3, "precio": 15000},
    {"nombre": "Tablet", "categoria": 3, "precio": 8000},
    {"nombre": "Proyector", "categoria": 3, "precio": 12000}
]

# Paso 2: Impuestos por categoría
impuestos = {
    1: 200,
    2: 400,
    3: 600
}

# Paso 3: Calcular total con impuesto
total_boleta = 0
print("=== DETALLE DE PRODUCTOS ===")
for producto in productos:
    impuesto = impuestos[producto["categoria"]]
    precio_con_impuesto = producto["precio"] + impuesto
    total_boleta += precio_con_impuesto
    print(f"{producto['nombre']} (Cat {producto['categoria']}): ${producto['precio']} + Impuesto ${impuesto} = ${precio_con_impuesto}")

# Paso 4: Determinar descuento por total
if total_boleta <= 1000:
    descuento = 0.03
elif 1001 <= total_boleta <= 5000:
    descuento = 0.05
else:
    descuento = 0.06

monto_descuento = total_boleta * descuento
total_final = total_boleta - monto_descuento

# Paso 5: Mostrar resumen final
print("\n=== RESUMEN DE BOLETA ===")
print(f"Total con impuestos: ${total_boleta:,.0f}")
print(f"Descuento aplicado: {descuento*100}% = ${monto_descuento:,.0f}")
print(f"Total final a pagar: ${total_final:,.0f}")
