import random
woerter = ['Baum', 'Hose', 'Affe']
print("hangman in Python")
guessingWort = random.choice(woerter)
foundLetters = {}
wordNotFound = True
myGuessingWordArray = {}
wrongLetter = []
guessingWort = guessingWort.lower()
for letter in guessingWort:
    if myGuessingWordArray.get(letter) == None:
        myGuessingWordArray[letter] = False
while wordNotFound:
    myLetter = input("Rate einen buchstaben!")
    foundLetter = False
    for letter in guessingWort:
        if letter == myLetter:
            if myGuessingWordArray.get(letter) == True:
                print("Buchstabe wurde schon gefunden!")
                foundLetter = True
                break
            elif myGuessingWordArray.get(letter) == False:
                print("Buchstabe gefunden!")
                myGuessingWordArray[letter] = True
                foundLetter = True
                break
    if foundLetter == False:
        print("Buchstabe nicht im Wort!")
        wrongLetter.insert(1,myLetter)
        print("Lister falsche Buchstaben: " + str(wrongLetter))
    foundAllLetter = False
    count = 1
    for letter in guessingWort:
        if myGuessingWordArray.get(letter) == True:
            count = count + 1
            print(letter)
        elif len(guessingWort) == count:
            print("Alle Buchstaben gefunden!")
            print(guessingWort)
            foundAllLetter = True
        else:
            print("_")
    if foundAllLetter:
        break

