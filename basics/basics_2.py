wert = 3
if wert < 5:
    print('Wert ist kleiner als 5')
    print('Ich gehöre auch noch zu der Bedingung')
    
print('und hier geht es nach der if-Abfrage weiter')

if True:
    print('if-Bedingung ist wahr')

wahroderfalsch = True
if wahroderfalsch:
    print('if-Bedingung ist wahr')

wert = 11
if wert != 5: 
    print('Es ist nicht 12 Uhr')

wert = 11
if wert == 11: 
    print('Es ist 11 Uhr')

wert = 9
if wert < 5:
    print('Wert ist kleiner als 5')
    
if wert > 4:
    print('Wert ist größer als 4')

import random
print(help(random.random))
help(random.random)

print(random.random())

def zufallszahl():
    return random.random() * 9 + 1
print (zufallszahl())

help(random.uniform)
print(random.uniform(5,8))

print(random.normalvariate(5, 0.1))
print(random.randint(1,6))

for i in range(15):
    print("Würfel: " + str(i+1))
    print(random.randint(1,6))


handgeste = ['Schere', 'Stein', 'Papier']
print(random.choice(handgeste))

print(dir(random))

nomen = ['Freund','Kumpel','Bruder']
adjectiv = ['coolste','beste','erste']

print("Du bist der " + random.choice(adjectiv) + " " + random.choice(nomen))