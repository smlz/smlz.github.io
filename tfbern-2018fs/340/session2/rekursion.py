
import time

def countdown(x):
    if x == 0:
        print("Lift Off")
    else:
        print(x)
        #time.sleep(1)
        countdown(x - 1)


countdown(10)


def quicksort(l):
    if len(l) <= 1:
        return l
    smaller, larger = [], []
    p = l[0]
    for el in l[1:]:
        if el < p:
            smaller.append(el)
        else:
            larger.append(el)
    return quicksort(smaller) + [p] + quicksort(larger)
