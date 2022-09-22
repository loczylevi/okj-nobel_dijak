#év;          típus;          keresztnév;          vezetéknév

# 0              1                 2                    3

with open("nobel.csv","r",encoding="utf-8") as f:
    fejlec = f.readline()
    lista = [sor.strip().split(";") for sor in f]
    
milyen_tipusu = [print(f"3.feladat: {sor[1]}") for sor in lista if sor[2] == "Arthur B." and sor[3] == "McDonald"][0]

irodalmi_2017 = [print(f"4.feladat: {sor[2]} {sor[3]}") for sor in lista if int(sor[0]) == 2017 and sor[1] == "irodalmi"]

print("5.feladat")
szervezetek_beke = [print(f"       {sor[0]}: {sor[2]}") for sor in lista if sor[3] == "" and sor[1] == "béke" and 1990 < int(sor[0])]

print("6.feladat:")
curie_nobel = [print(f"       {sor[0]}: {sor[2]} {sor[3]}({sor[1]})") for sor in lista if "Curie" in sor[3] or "Curie" in sor[2]]

print("7.feladat:")
stat = dict()
for sor in lista:
    stat[sor[1]] = stat.get(sor[1], 0) + 1
    
satisztika = [print(f"       {tipus}           {db} db") for tipus,db in stat.items()]

with open("orvosi.txt","w",encoding="UTF-8") as f2:
    orvosok = [sor for sor in lista if sor[1] == "orvosi"]
    orvosok.sort(key=lambda x:x[0])
    for sor in orvosok:
        f2.write(f"{str(sor[0])}:{sor[2]} {sor[3]}\n")      # ༼ つ ◕_◕ ༽つ

print("8.feladat: orvosi.txt")