vornamen = ['Axel', 'Elke', 'Martin']
for einzelwert in vornamen:
    print(einzelwert)
print("nach der for-Schleife")

vornamen = ['Axel', 'Elke', 'Martin']
for einzelwert in vornamen:
    if einzelwert == "Axel":
        print("Ich")
    else:
        print(einzelwert)
print("nach der for-Schleife")

vornamen = ['Axel', 'Elke', 'Martin']

# aufwendige Konstruktion
nummer = 0
for einzelwert in vornamen:
    print(nummer, einzelwert)
    nummer += 1

vornamen = ['Axel', 'Elke', 'Martin']
for nr, einzelwert in enumerate(vornamen):
    print(nr, einzelwert)