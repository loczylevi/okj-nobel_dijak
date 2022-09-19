class Nobel_dijak:
    def __init__(self,sor):
        evszam,tipus,kereszt,vezetek = sor.strip().split(";")
        self.evszam = int(evszam)
        self.tipus = tipus
        self.kereszt = kereszt
        self.vezetek = vezetek
        
with open("nobel.csv","r",encoding="utf-8") as f:
    fejlec = f.readline()
    lista = [Nobel_dijak(sor) for sor in f]
    
milyen_tipusu = [print(f"3.feladat: {sor.tipus}") for sor in lista if sor.kereszt == "Arthur B." and sor.vezetek == "McDonald"][0]

irodalmi_2017 = [print(f"4.feladat: {sor.kereszt} {sor.vezetek}") for sor in lista if sor.evszam == 2017 and sor.tipus == "irodalmi"]

print("5.feladat")
szervezetek_beke = [print(f"       {sor.evszam}: {sor.kereszt}") for sor in lista if sor.vezetek == "" and sor.tipus == "béke" and 1990 < sor.evszam]

print("6.feladat:")
curie_nobel = [print(f"       {sor.evszam}: {sor.kereszt} {sor.vezetek}({sor.tipus})") for sor in lista if "Curie" in sor.vezetek or "Curie" in sor.kereszt]

print("7.feladat:")
stat = dict()
for sor in lista:
    stat[sor.tipus] = stat.get(sor.tipus, 0) + 1
    
satisztika = [print(f"       {tipus}           {db} db") for tipus,db in stat.items()]

with open("orvosi.txt","w",encoding="UTF-8") as f2:
    orvosok = [sor for sor in lista if sor.tipus == "orvosi"]
    orvosok.sort(key=lambda x:x.evszam)
    for sor in orvosok:
        f2.write(f"{str(sor.evszam)}:{sor.kereszt} {sor.vezetek}\n")      # ༼ つ ◕_◕ ༽つ

print("8.feladat: orvosi.txt")