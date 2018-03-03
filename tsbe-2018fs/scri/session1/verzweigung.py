
alter = int(input("Dein Alter: "))

if alter < 18:
    print("Noch nicht alt genug")
    print(f"Du must noch {18-alter} Jahre warten")
elif alter > 65:
    print("Gratulation")
else:
    # Einrücken!
    print("An die Arbeit")
    # Ausrücken!

print("Ende")
