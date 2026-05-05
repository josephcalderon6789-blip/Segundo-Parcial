#JOSEPH CALDERON
#PROGRAMACIÓN 2 “A”
#22/04/2026

cantidad = int(input("Cantidad de llantas: "))

if cantidad < 5:
    precio = 300
elif cantidad <= 10:
    precio = 250
else:
    precio = 200

total = cantidad * precio

print("Precio por llanta:", precio)
print("Total a pagar:", total)
