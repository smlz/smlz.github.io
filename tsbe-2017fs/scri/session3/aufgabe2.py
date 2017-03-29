for i in range(5):
    print(i)
print('-' * 5)

for i in range(1, 5):
    print(i)
print('-' * 5)

for i in range(1, 5, 2):
    print(i)
print('-' * 5)

liste = 'schwimmen,velofahren,schach'.split(',')

for i, hobby in enumerate(liste):
    print(f"{i}. {hobby}")
