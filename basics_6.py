for durchgang in range(10):
    if durchgang == 7:
        print("Schleifenabbruch wird erzwungen")
        break
    print(durchgang)

print("Nach der Schleife")

for durchgang in range(10):
    if durchgang%2 == 1:
        continue
    print(durchgang)

print("Nach der Schleife")