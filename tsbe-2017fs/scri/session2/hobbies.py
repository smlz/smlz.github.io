name = input("Hallo, wie heisst du? ")

hobbies = input("Was sind deine Hobbies (mit Komma getrennt)? ")

hobbies = hobbies.split(',')

anzahl_hobbies = 0

gueltige_hobbies = []   # Eine neue leere Liste erstellen

print("Deine Hobbies sind:")
for hobby in hobbies:
    hobby = hobby.strip().capitalize()
    if hobby != '':
        if hobby not in gueltige_hobbies:
            anzahl_hobbies = anzahl_hobbies + 1
            gueltige_hobbies.append(hobby)
            print(" *", hobby)
print()

if gueltige_hobbies == []:
    print("Du bist leider hobbylos")
elif anzahl_hobbies < 3:
    print("Gut")
else:
    print("Arbeitest du überhaupt?")
