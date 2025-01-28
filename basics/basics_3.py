durchgang = 1
while durchgang < 11:
    print(durchgang)
    durchgang = durchgang + 1
print("nach der Schleife")

durchgang = 0
while durchgang < 7:
    print(durchgang)
    durchgang = durchgang + 1
    if (durchgang == 3):
        break
print("nach der Schleife")

durchgang = 0
aktiv = True
while aktiv:
    print(durchgang)
    durchgang = durchgang + 1
    if (durchgang == 3):
        aktiv = False
print("nach der Schleife")


#durchgang = 0
#aktiv = True
#while aktiv:
#    print(durchgang)
#    durchgang = durchgang + 1
#    print("tippe ende für ende")
#    benutzereingabe = input("Bitte Zahl eingeben: ")
#    if (benutzereingabe == "ende"):
#        aktiv = False
#print("nach der Schleife")


import random

myRandNumber = random.randint(0,20)
aktiv = True

count = 0

while aktiv:
    count = count + 1
    print("Errate die Zahl.")
    benutzereingabe = int(input("Bitte Zahl eingeben: "))
    if benutzereingabe == myRandNumber:
        print("Eingegeben Zahl ist erraten: " + str(myRandNumber))
        aktiv = False
        break
    elif benutzereingabe < myRandNumber:
        print("Eingegeben Zahl ist kleiner.")
    else:
        print("Eingegeben Zahl ist größer.")

    if count == 7:
        print("Alle Versuche erreicht. Die Zahl war: " + str(myRandNumber))
        nextGame = input("Nochmal spielen = j ")
        if nextGame == 'j':
            count = 0
            myRandNumber = random.randint(0,20)


print("Ende")
