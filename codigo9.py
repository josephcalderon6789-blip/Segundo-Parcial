#JOSEPH CALDERON 
#PROGRAMACIÓN 2 “A”
22/04/2026

n = int(input("Número de vendedores: "))
i = 1

while i <= n:
    sueldo = float(input("Sueldo base: "))

    v1 = float(input("Venta 1: "))
    v2 = float(input("Venta 2: "))
    v3 = float(input("Venta 3: "))

    total_ventas = v1 + v2 + v3
    comision = total_ventas * 0.10
    total = sueldo + comision

    print("Comisión:", comision)
    print("Pago total:", total)

    i += 1

