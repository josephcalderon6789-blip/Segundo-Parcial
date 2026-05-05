#JOSEPH CALDERON
#PROGRAMACIÓN 2”A”
#22/04/2026

cantidad = int(input("Cantidad de computadoras: "))
precio = 11000
total = cantidad * precio

if cantidad < 5:
    descuento = total * 0.10
elif cantidad < 10:
    descuento = total * 0.20
else:
    descuento = total * 0.40

pagar = total - descuento

print("Total:", total)
print("Descuento:", descuento)
print("Pago final:", pagar)

