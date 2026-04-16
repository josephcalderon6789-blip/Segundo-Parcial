#JOSEPH CALDERON
#OBTENR EL SUELDO
#26/03/26

sueldo_base = float(input("ingresa el sueldo base"))
venta_1 = float(input("ingresa la venta_1"))
venta_2 = float(input("ingresa la venta_2"))
venta_3 = float(input("ingresa la venta_3"))
total_ventas = venta_1 + venta_2 + venta_3
com = total_ventas * 0.10
pago_total = sueldo_base + com
print("el resutado del pago es", pago_total)