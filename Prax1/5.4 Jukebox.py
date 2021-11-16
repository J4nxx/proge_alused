fail = open(input("Sisestage failinimi: jukebox.txt / 80ndad.txt / eesti_muusika.txt / edm.txt "), encoding="UTF-8")
laul = 1
print("laulu valik: ")
loend = []
for rida in fail:
    print(str(laul) + " " + str(rida[:-1]))
    laul += 1
    loend. append(rida)
lauluvalik = int(input("valige laul (sisestage number): "))
lauluvalik -= 1
print("praegu mängib: " + loend[lauluvalik])
fail.close()