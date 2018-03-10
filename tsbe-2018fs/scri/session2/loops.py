
wort = "Hexagon"

for buchstabe in wort:
    print(buchstabe)

print("*******")

liste = [1, 2, 3, 4]

quadratzahlen = []

for zahl in liste:
    quadratzahl = zahl * zahl
    quadratzahlen.append(quadratzahl)

# Enumerate: Listen durchnummerieren
for i, x in enumerate(quadratzahlen):  # Start bei 0 per default
    print(f"{i}: {x}")

print("********")

for i, x in enumerate("Cup-Final", 1):
    print(f"Buchstabe {i} ist '{x}'")


print("**********")
zahlen = [1,2,3,4,5,6,7,8,9]
gerade_zahlen = []
ungerade_zahlen = []
for a in zahlen:
     if a % 2 == 0:  # a ist eine gerade Zahl!
        gerade_zahlen.append(a)
     else:           # a ist eine UNgerade Zahl!
        ungerade_zahlen.append(a)
