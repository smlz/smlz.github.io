i = 0

zahlen = "eins zwei drei vier fünf sechs sieben acht neun".split()

while i < len(zahlen):
    print(f"{i + 1}: {zahlen[i]}")
    i = i + 1


for i in range(10):
    print(i)

print("=" * 20)

for i, zahl in enumerate(zahlen, 1):
    print(i, zahl)

# for (int i=0; i<10; i++) { System.out.println(i); }
