class Csapat:
    lista = []
    def __init__(self, sorzsam, csapat, helyezes, ev, vbhely):
        self.sorszam = sorzsam
        self.csapat = csapat
        self.helyezes = helyezes
        self.ev = ev
        self.vbhely = vbhely
        Csapat.lista.append(self)

with open("input.txt", "r", encoding="utf8") as f:
    for sor in f:
        s = sor.strip().split("\t")
        t = Csapat(int(s[0]), s[1], int(s[2]), int(s[3]), s[4])
