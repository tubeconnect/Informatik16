# -*- coding:utf-8 -*-
#Wer wird Milliardär von Jan Moritz
#Version 1.0

import random
import time
import math

name = None

qualifragen = ["Wann wurde die Berliner Mauer niedergerissen","1989","1979","1999","1972","A"],["Wann wurde die Berliner Mauer niedergerissen","A - 1989","B - 1979","C - 1999","D - 1972","A"],["Welches Wahrzeichen ist in Paris zu bewundern?","A - Der Berliner Fernsehturm","B - Der Eifelturm","C - Der schiefe Turm von Pisa","D - Charlies Schokoladenfabrik","B"]

def verify():
    global name
    global age
    
    print("Herzlich Willkommen bei 'Wer wird Millionär...'")
    time.sleep(0.5)
    name = input("Wie heißen Sie?")
    time.sleep(0.2)
    age = input("Hallo " + name +"! Du hast echt einen tollen Namen! Wie alt bist du?")
    time.sleep(0.2)
    print("Alles klar. Haben Sie einen kleinen Augenblick Geduld, die Teilnehmer werden ausgelost...")
    time.sleep(random.randint(0,3))
def qualify():
    frageandanswer = qualifragen[0]
    frage = frageandanswer[0]
    rightanswer = frageandanswer[5]
    antworta = frageandanswer[1]
    antwortb = frageandanswer[2]
    antwortc = frageandanswer[3]
    antwortd = frageandanswer[4]
    print("Die erste Frage lautet:")
    print(frage)
    print(antworta)
    print(antwortb)
    print(antwortc)
    print(antwortd)
def maingame():
    print("Frage " + questionnumbber)
verify()
qualify()
