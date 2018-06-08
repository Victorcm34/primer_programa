
rival = input("¿Contra que Pokemon quieres cambatir? (Squirtle / Charmander / Bulbasur): ").upper()

vida_pikachu = 100
ataque_rival = 0

if rival== "SQUIRTLE":
    vida_rival = 90
    ataque_rival = 8
elif rival == "CHARMANDER":
    vida_rival = 80
    ataque_rival = 7
elif rival == "BULBASUR":
    vida_rival = 100
    ataque_rival = 10

print("Combate contra {}".format(rival))

while vida_pikachu > 0 and vida_rival > 0:
    print("Vida PIKACHU {} - Vida {} {}".format(vida_pikachu, rival, vida_rival))

    ataque = input("¿Que ataque quieres usar? (Impactrueno/Rayo)").upper()

    if ataque == "IMPACTRUENO":
        vida_rival -= 10

    if ataque == "RAYO":
        vida_rival -= 12

    print("PIKACHU usa {} !".format(ataque))

    print("{} ataca y hace {} puntos de daño a PIKACHU!".format(rival, ataque_rival))

    vida_pikachu -= ataque_rival

if vida_pikachu > vida_rival:
    print("Has ganado!")
else:
    print("Has perdido")