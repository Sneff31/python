print ("Hallo Welt")
print ("!")

def quadrieren(zahl):
    print(zahl*zahl)

print( 'Ausgabe Kurve ohne Grafik' );

print( 3 * '*' );
print( 5 * '*' );
print( 8 * '*' );
print( 9 * '*' );
print( 10 * '*' );
print( 9 * '*' );
print( 8 * '*' );
print( 5 * '*' );
print( 3 * '*' );

import math as m
print(m.sqrt(25))

print(7%2)

print(2**3)

zahl3 = 1_000_000
zahl4 = 100_000_000
print(zahl3 + zahl4)

zahl3 = 1_000_000
print(type(zahl3))

vornamen = ['Axel', 'Elke', 'Martin']
print(vornamen[1])

vornamen = ['Axel', 'Elke', 'Martin']
print(vornamen[-2])

vornamen = ['Axel', 'Elke', 'Martin']
vornamen.append('Rolf')
print(vornamen)

vornamen = ['Heike', 'Sabine']
del(vornamen)[0]
print(vornamen)

buchstaben = ['a', 'b', 'c']
print(buchstaben)
buchstaben.remove('b')
print(buchstaben)

buchstaben = ['a', 'c', 'b']
print(buchstaben)

buchstaben_sortiert = sorted(buchstaben)
print(buchstaben_sortiert)

buchstaben_sortiert_absteigend = sorted(buchstaben, reverse=True)
print(buchstaben_sortiert_absteigend)

variableA = 'Ich bin eine Variable'
print( variableA[0:5] )

variableA = 'Ich bin eine Variable'
print( variableA[7:] )

variableA = 'Ich bin eine Variable'
print( variableA[-4:] )

variableA = 'Ich bin eine Variable'
print( len (variableA) )


deutschenglisch = {}
deutschenglisch['null'] = 'zero'
deutschenglisch['eins'] = 'one'
deutschenglisch['zwei'] = 'two'
deutschenglisch['drei'] = 'three'
copydeutschenglisch = deutschenglisch.copy()

print(deutschenglisch)

print(deutschenglisch.values())
print(deutschenglisch.keys())
print(deutschenglisch.items())
print(deutschenglisch.clear())
print(copydeutschenglisch)

print(copydeutschenglisch.setdefault('zwei'))
print(copydeutschenglisch.setdefault('acht'))
copydeutschenglisch.update({'zwei':"sieben"})
print(copydeutschenglisch)

inhaltA = ('wert1',)
inhaltB = ('wert2')
print(type(inhaltA))
print(type(inhaltB))

tupel = ('wert1', 'wert2', 'wert3', 'wert4', 'wert5')
print (tupel[0])

tupel = ('wert1', 'wert2', 'wert3', 'wert4', 'wert5')
print (tupel[2:4])

vornamen =  ( "Hans","Peter","Elke","Peter","Sabine","Elke")
print(vornamen)

# Wie oft kommt bestimmter Vornamen im Tuple vor
print (vornamen.count("Peter"))

print (vornamen.index("Peter"))

werte_als_tupel = (1,1,1,3,5,3,4,5,3)
werte_als_set   = set(werte_als_tupel)
print(werte_als_set)

set_a = { 1, 2, 3, 'A', 'B', 'C' }
set_b = { 2, 3, 'B', 'D' }
print("Set Beispiel")
print(set_a)
print(set_b)

print("Schnittmenge über &")
print( set_a & set_b )
print("Vereinigungsmenge über |")
print( set_a | set_b )
print("Differenzmenge über - ")
print( set_a - set_b )
print("Symmmetrische Differnz (entweder-oder) über ^")
print( set_a ^ set_b )
print("Obermenge von  > ")
print( set_a > set_b )
print("Obermenge von  < ")
print( set_a < set_b )
print("Obermenge von  > von b")
print( set_b > set_a )
print("Obermenge von  < von b")
print( set_b < set_a )


set_a = { 1, 2, 3, 'A', 'B', 'C' }
set_c = frozenset(set_a)

print(set_c)
print(type(set_c))

inhalt = "anzahl"

# doppelte Buchstaben entfernen
buchstaben = set(inhalt)
print(buchstaben)

# zum Sortieren aus dem SET eine Liste machen
buchstabenliste = list(buchstaben)
print(buchstabenliste)

# sortieren
buchstabensortiert = sorted(buchstabenliste)
print(buchstabensortiert)

# der Reihen nach durchlaufen und Anzahl zählen
# die for-Schleife kommt in einem späteren Kapitel

for einzelbuchstabe in buchstabensortiert:
    print(einzelbuchstabe ,": Anzahl ", inhalt.count(einzelbuchstabe))

inhalt = "Buchstaben zählen"
for einzelbuchstabe in sorted(list(set(inhalt))):
    print(einzelbuchstabe ,": Anzahl ", inhalt.count(einzelbuchstabe))

benutzereingabe = input("Bitte Zahl eingeben")
print(benutzereingabe)


inhalt = "   https://www.py thon-le rnen.de  "
ausgabe = inhalt.strip()
print(ausgabe)

exit()