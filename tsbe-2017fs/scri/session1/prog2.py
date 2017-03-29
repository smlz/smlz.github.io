studierende = 25
dozenten = 1
schulzimmer = 2
schulleitung = 3

print("Es befinden sich", studierende, "Studierende", end=" ")
print("und", dozenten, "Dozenten in", schulzimmer, end=" ")
print("Schulzimmern.")

print('Die Schulleitung besteht aus', schulleitung, "Personen")

personen_pro_raum = (studierende + dozenten) / schulzimmer

print("Es befinden sich durchschnittlich", personen_pro_raum,
      "Personen im Raum.")
