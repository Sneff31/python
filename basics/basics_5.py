werte = list(range(3))
print(werte)

for durchgang in range(3):
    print(durchgang)

werte = list(range(2,8))
print(werte)

werte = list(range(2,8,2))
print(werte)

werte = list(range(12,8,-1))
print(werte)

import random

lottozahlen_alle = []
lottozahlen_alle = range(1,50)

lottozahlen_gewinner = random.sample(lottozahlen_alle, 6)
lottozahlen_gewinner.sort()
print("Lottezahlen: ")
print(lottozahlen_gewinner)
print(random.choices(lottozahlen_alle, k=6))