def ausgabe():
    print("Ausgabe von Text aus einer Funktion")

ausgabe()
print("Programm abgelaufen")

def ausgabe():
    print("Ausgabe von Text aus einer Funktion")

ausgabe()
ausgabe()
print("Programm abgelaufen")

def ausgabe(wert1):
    print("Ausgabe von Text aus einer Funktion")
    print(wert1)

ausgabe(5)

def ausgabe( *mehrereParameter ):
    for einzelwert in mehrereParameter:
        print(einzelwert)

ausgabe("Hallo", "Welt", "guten", "Morgen")

variablenWert = "außerhalb der Funktion"
print("Variablenwert vor Funktion:", variablenWert)
def bspfunktion():
    variablenWert = "IN der Funktion"
    print("Variablenwert in Funktion:", variablenWert)

bspfunktion()
print("Variablenwert nach Funktion:", variablenWert)


variablenWert = "außerhalb der Funktion"
print("Variablenwert vor Funktion:", variablenWert)
def bspfunktion():
    global variablenWert
    variablenWert = "IN der Funktion"
    print("Variablenwert in Funktion:", variablenWert)

bspfunktion()
print("Variablenwert nach Funktion:", variablenWert)

def bspfunktionfuerrueckgabe(eingabewert):
    rueckgabewert = eingabewert * 2
    return rueckgabewert

def uebergeben(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

uebergeben(vorname="Axel")