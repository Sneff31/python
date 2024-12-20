# -*- coding: utf-8 -*-

print("Willkommen das ist ein simpler Chatbot!")
print("Du kannst die Unterhaltung mit dem Wort 'bye' beenden")

import random

chatbotDictionary = {}
chatbotDictionary['hallo'] = {'antwort': "Hallo!"}
chatbotDictionary['geht'] = {'antwort': "Gut",'gegenfrage': "Und dir?"}
chatbotDictionary['auch'] = {'antwort': "Super! Mir auch"}

randomAnswers = ["Und sonst so?","Das weiß ich nicht","Willst du weiter reden?"]

activ = True

def normalizeString(myString):
    lowerString = myString.lower()
    stringArray = lowerString.split(' ')
    return stringArray

while activ:
    myUserinput = input("Was möchtest du dem Chatbot sagen? ").lower()
    normalizedUserinput = normalizeString(myUserinput)
    for einzelwort in normalizedUserinput:
        if einzelwort == "bye":
            print("Bye!")
            activ = False
            break
        elif einzelwort in chatbotDictionary:
            print(chatbotDictionary[einzelwort]['antwort'])
            if 'gegenfrage' in chatbotDictionary[einzelwort]:
                print(chatbotDictionary[einzelwort]['gegenfrage'])
            else:
                print(random.choice(randomAnswers))