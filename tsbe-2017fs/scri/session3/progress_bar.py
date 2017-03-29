import time

total = 10000

for i in range(total + 1):
    if i % 100 == 0:
        progress = i * 60 // total
        print('\r[' + '\u2588' * progress + ' ' * (60 - progress) + ']',
              f"{i * 100 // total:>4}%", end='')

    time.sleep(0.001)

print()
