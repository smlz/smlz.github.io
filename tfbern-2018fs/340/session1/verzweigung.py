name = input("Wie heisst du? ")
alter = input("Wie alt bist du? ")


if int(alter) >= 18:
    print("Du musst das Absenzenheft nicht mehr zuhause unterschreiben lassen")
    print("Du darfst wählen und abstimmen")
    print("Du musst Steuern bezahlen")
    print("Du darfst in den Ausgang")
elif int(alter) >= 16:
    print("Du darfst Bier trinken")
else:
    print("Du darfst sehr oft kindisch sein")
print("Du darfst singen")
