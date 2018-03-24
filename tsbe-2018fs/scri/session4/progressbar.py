
import time

r = range(10001)

b = '\u2588'

for i in r:
    if i % 100 == 0:
        prozent = (i + 1) * 100 // len(r)

        print(f"[{b * (prozent // 2) }{' ' * (50 - prozent // 2)}] {prozent}%",
              end="\r")
    time.sleep(0.0001)
print()
