
for i in range(10):
    print(i)

for c in "Hallo":
    print(c)

for line in open("lyrics.txt"):
    print(line.strip())

for zahl in [1, 2, 3, 4, 5]:
    print(zahl)

for index, wort in enumerate(['Habe', 'nun', 'ach'], 1):
    print(f"Das {index}. Wort ist { wort }.")
