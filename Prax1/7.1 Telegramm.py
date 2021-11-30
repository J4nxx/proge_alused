fail = open(input("Sisestage failinimi: "), encoding ="UTF-8")
sõnum = fail.read().upper().replace("Ä", "AE").replace("Õ", "OE").replace("Ü", "UE").replace("Ö", "OE")
print(sõnum)
fail.close