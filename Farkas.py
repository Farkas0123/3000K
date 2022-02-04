from asyncore import read
from sunau import AUDIO_FILE_ENCODING_LINEAR_16
from main import Csapat

def feladat1(lista):
    print("1)  Írja ki Magyarország által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.")
    vissza = list(filter(lambda cs: cs.csapat=="Magyarország", lista))
    for sor in vissza:
        print(f"Magyarország a(z) {sor.helyezes}-dik helyen végzett az {sor.ev} évi világbajnokságon, amit {sor.vbhely} szervezett")
    print()

def feladat6(lista):
    print("6)	A program olvasson be egy csapat nevet és írja ki a csapat álta elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.")
    mit = input()
    for sor in lista:
        if sor.csapat == mit:
            print(f"{mit} a(z) {sor.helyezes}-dik helyen végzett az {sor.ev} évi világbajnokságon, amit {sor.vbhely} szervezett")
    print()

def feladat7(lista):
    print("7)	A program írja ki, hogy az '30-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.")
    for sor in lista:
        if sor.ev<1940 and sor.ev>1929 and sor.helyezes == 1:
            print(f"{sor.csapat} {sor.ev}")
    print()

def feladat13(lista):
    print("13)	Írja ki Magyarország hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!")
    print(len(list(filter(lambda cs: cs.csapat=="Magyarország", lista))))
    print()

def feladat19(lista):
    print("19)	Melyik csapat nyert 1930-ban?")
    kinyert = list(filter(lambda cs: cs.ev==1930 and cs.helyezes == 1, lista))
    print(kinyert[0].csapat if len(kinyert) == 1 else "Ekkor nem rendeztek vb-t!")
    print()

def feladat20(lista):
    print("20)	Melyik csapat nyert 1940-ben?")
    kinyert = list(filter(lambda cs: cs.ev==1940 and cs.helyezes == 1, lista))
    print(kinyert[0].csapat if len(kinyert) == 1 else "Ekkor nem rendeztek vb-t!")
    print()

def feladat21(lista):
    print("21)	Melyik csapat nyert 1950-ben?")
    kinyert = list(filter(lambda cs: cs.ev==1950 and cs.helyezes == 1, lista))
    print(kinyert[0].csapat if len(kinyert) == 1 else "Ekkor nem rendeztek vb-t!")
    print()

def feladat22(lista):
    print("22)	Melyik csapat nyert 1960-ban?")
    kinyert = list(filter(lambda cs: cs.ev==1960 and cs.helyezes == 1, lista))
    print(kinyert[0].csapat if len(kinyert) == 1 else "Ekkor nem rendeztek vb-t!")
    print()

def feladat23(lista):
    print("23)	Melyik csapat nyert 1970-ben?")
    kinyert = list(filter(lambda cs: cs.ev==1970 and cs.helyezes == 1, lista))
    print(kinyert[0].csapat if len(kinyert) == 1 else "Ekkor nem rendeztek vb-t!")
    print()

def feladat24(lista):
    print("24)	Hányszor kapott ki a döntőben Magyarország?")
    print(len(list(filter(lambda cs: cs.helyezes == 2 and cs.csapat == "Magyarország", lista))))
    print()

def feladat30(lista):
    print("30)	A programm olvasson be évszámot és írja ki, hogy melyik csapat nyert az adott évben?")
    a = int(input())
    b = list(filter(lambda cs: cs.ev == a and cs.helyezes == 1, lista))
    print(b[0].csapat if len(b) == 1 else "Ebben az évben nem rendeztek vb-t!")

def feladat60(lista):
    print("60)	Melyik csapat(ok) nyert a legtöbbször vb-t? A csapat neve mellett a vb gyözelmmek számát is írja ki! ")
    a  = list(filter(lambda cs: cs.helyezes == 1, lista))
    b = ""
    d = ""
    max = 0
    akt = 0
    i = 0
    for sor in a:
        b = a[0].csapat
        print(b)
        while i < len(a):
            #print(b+"...")
            if a[i].csapat == b:
                a.remove(a[i])
                akt += 1
            i += 1
        
        if akt > max:
            d = b + " " + str(akt)
            max = akt
        elif akt == max:
            d += ", " + b + " " + str(akt)
        akt = 0
        b = ""
        i = 0
    print(d)
    print()





feladat1(Csapat.lista)
#feladat6(Csapat.lista)
feladat7(Csapat.lista)
feladat13(Csapat.lista)
feladat19(Csapat.lista)
feladat20(Csapat.lista)
feladat21(Csapat.lista)
feladat22(Csapat.lista)
feladat23(Csapat.lista)
feladat24(Csapat.lista)
#feladat30(Csapat.lista)
feladat60(Csapat.lista)