#!/usr/bin/python3.6

import atexit
import random
import subprocess
import time

# Grosse Zahl
total = 5 * 10**6

block = '\u2588'

# Teil-Blöcke      0/8       1/8       2/8       3/8
block_fractions = ['',      '\u258F', '\u258E', '\u258D',
                   '\u258C', '\u258B', '\u258A', '\u2589']
#                  4/8       5/8       6/8       7/8

# Drehendes 'Dings'
spinner = ['-', '\\', '|', '/']

# Cursor ein- bzw. ausblenden
atexit.register(subprocess.call, 'setterm -cursor on'.split())
subprocess.call('setterm -cursor off'.split())

try:
    # Finde die Breite des Terminals raus.
    width = int(subprocess.check_output(['tput', 'cols'])) - 6  # Breite des Terminals
except:
    # Falls es nicht funktioniert hat (Windodws), nimm einen Default-Wert
    width = 74

# ============ #
# Progress Bar #
# ============ #
last_time = 0
for i in range(total + 1):
    now = time.time()
    if now - last_time >= 0.04:                  # Update 25 mal in der Sekunde
        last_time = now
        progress = i * width * 8 // total
        print('\r',                                   # zurück zum Zeilenanfang
              f"{i * 100 // total:>3}% ",             # Prozentangabe
              block * (progress // 8),                # ganze Blöcke
              block_fractions[progress % 8],          # Teil-Block
              ' ' * ((width * 8 - progress) // 8),        # Leerzeichen
              spinner[int(8 * now % 4)],              # Drehendes Blöckli
              sep='',
              end='')


# =================== #
# Abschluss-Animation #
# =================== #

# Die voll schwarze Progress Bar (4 = schwarz, 0 = weiss)
bar = [4] * (width + 1)

# Graustufen:  weiss  hellgrau  grau      dunkelgrau  schwarz
chars =       [' ',   '\u2591', '\u2592', '\u2593',   '\u2588']

# k = len(bar) // 16

while any(bar):   # Solange nicht alles weiss ist
    # for i in range(len(bar)):
    #     if bar[i]:
    #         bar[i] -= 1
    #         if bar[i] == 3:
    #             break
    # for i in reversed(range(len(bar))):
    #     if bar[i]:
    #         bar[i] -= 1
    #         if bar[i] == 3:
    #             break
    #     # pos = random.randrange(len(bar))
    #     # if bar[pos]:
    #     #     bar[pos] -= 1
    # k += len(bar) // 16

    # Alle Positionen die noch nicht weiss sind
    non_white = [i for (i, val) in enumerate(bar) if val > 0]

    # Wähle zufällig die Positionen, die um eine Graustufe heller gemacht werden
    minus_one = random.choices(
        # Wähle nur unter den Position, welche noch nicht weiss sind
        non_white,
        # Gewichtung: Je weiter vorne, desto eher werden sie heller gemacht
        #weights=reversed([i**2 for i, _ in enumerate(non_white, 4)]),
        weights=reversed([(i - (len(non_white)//2 + 4))**2 + 1 for i, _ in enumerate(non_white, 4)]),
        # Wähle 25% der Positionen
        k=min(int(width * 0.25), len(non_white))
    )

    # Neue Progress Bar berechnen und ausgeben
    bar = [(num - 1 if i in minus_one else num) for (i, num) in enumerate(bar)]
    print('\r100% ' + ''.join(chars[i] for i in bar), sep='', end='')
    time.sleep(0.04)

# Abschlussmeldung
print('\rDone', end='')
time.sleep(2)
print()
try:
    subprocess.check_call('setterm -cursor on'.split())
except:
    pass
