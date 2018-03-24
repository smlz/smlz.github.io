
for zeile in open('emails.csv'):
    vorname, name, email = zeile.strip().split(';')
    print(f'"{vorname} {name}" <{email}>; ', end="")
print()
