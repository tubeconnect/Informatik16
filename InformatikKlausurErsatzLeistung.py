#Wer wird Milliardär von Jan Moritz
#Version 1.0

import random
import time
import math

name = None

qualifragen = ["Wann wurde die Berliner Mauer niedergerissen","1989","1978","1999","1972","A"],["Wann wurde die Berliner Mauer niedergerissen","1989","1979","1999","1972","A"]

def verify():
    global name
    global age
    
    print("Herzlich Willkommen bei 'Wer wird Millionär'")
    time.sleep(0.5)
    name = input("Wie heißen sie")
    time.sleep(0.2)
    age = input("Hallo " + name +" Du hast echt einen tollen Namen. Wie alt bist du?")
    time.sleep(0.2)
    print("Ok haben sie einen kleinen Augenblick gedult, die Teilnehmer werden ausgelost")
    time.sleep(random.randint(0,3))
def qualify():
    frageandanswer = qualifragen[0]
    frage = frageandanswer[0]
    rightanswer = frageandanswer[5]
    antworta = frageandanswer[1]
    antwortb = frageandanswer[2]
    antwortc = frageandanswer[3]
    antwortd = frageandanswer[4]
    rightanswer = frageandanswer[5]
    print("Die erste Frage lautet")
    print(frage)
    print(antworta)
    print(antwortb)
    print(antwortc)
    print(antwortd)
    if(input("Tippen sie A, B, C, oder D\n") == rightanswer.upper()):
        print("YALLAH")
def maingame():
    print("Frage " + questionnumbber)
verify()
if(name.upper() == "UWE"):
        print("Entschuldigung mein Psychater hat gesagt ich darf nicht mit ihnen reden. Bitte verlassen die den Raum - Einbruchsgefahr!!!")
else:
    print("Herzlichen Glückwunsch! Sie sind dabei, in wenigen Sekunden starten die ersten Qualifikationsfragen")
    qualify()
