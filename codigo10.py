#JOSEPH CALDERON
#PROGRAMACIÓN 2 “A”
#22/04/2026

n = int(input("Número de obreros: "))
i = 1

while i <= n:
    horas = int(input("Horas trabajadas: "))

    if horas <= 40:
        salario = horas * 20
    else:
        extras = horas - 40
        salario = (40 * 20) + (extras * 25)

    print("Salario:", salario)

    i += 1
