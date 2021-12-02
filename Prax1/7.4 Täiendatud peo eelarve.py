def eelarve(külalised):
    ruumirent = 55
    summa = külalised * 10 + ruumirent
    return summa
kindlad_tulijad = 0
vb_tulijad = 0

fail = open(input("Sisestage failinimi: "), "r")

for line in fail:
    for char in line:
        if char == "+":
            kindlad_tulijad += 1
        elif char == "?":
            vb_tulijad += 1

inim_kokku = kindlad_tulijad + vb_tulijad

print("Kutsutud on", inim_kokku, "inimest")
print(kindlad_tulijad, "inimest tuleb")
print("Maksimaalne eelarve:", eelarve(inim_kokku), "eurot")
print("Minimaalne eelarve:", eelarve(kindlad_tulijad), "eurot")