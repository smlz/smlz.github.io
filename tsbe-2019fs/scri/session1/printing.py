import sys

f = open('/tmp/email.csv', 'w')

print("vorname", "name", "email", sep=";", file=f)

# Wo landet diese Zeile
print("Irgendetwas ist schief gelaufen", sep=";", file=sys.stderr)

print("Hans", "Müller", "housi@bluewin.ch", sep=";", file=f)
print("Irmgard", "Hunziker", "irhu@gmx.ch", sep=";", file=f)

f.close()
