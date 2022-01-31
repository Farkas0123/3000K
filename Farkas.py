from main import Csapat

def feladat1(lista):
    print("1)  Írja ki Magyarország által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.")
    vissza = list(filter(lambda cs: cs.csapat=="Magyarország", lista))
    for sor in vissza:
        print(f"Magyarország a(z) {sor.helyezes}-dik helyen végzett az {sor.ev} évi világbajnokságon, amit {sor.vbhely} szervezett")
    print()




feladat1(Csapat.lista)