class Tanulo:
    lista = []
    def __init__(self, sorzsam, csapat, helyezes, ev, vbhely):
        self.sorszam = sorzsam
        self.csapat = csapat
        self.helyezes = helyezes
        self.ev = ev
        self.vbhely = vbhely
        Tanulo.lista.append(self)

with open("J.txt", "r", encoding="utf8") as f:
    for sor in f:
        s = sor.strip().split(";")
        t = Tanulo(int(s[0]), s[1], int(s[2]), int(s[3]), s[4])
