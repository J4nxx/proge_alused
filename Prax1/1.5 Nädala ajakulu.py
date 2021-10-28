ainepunktide_arv = int(input("Sisestage oma ainepunktide arv: "))

nädalate_arv = int(input("Sisestage oma nädalate arv: "))

ajakulu = ainepunktide_arv * 26

nädala_kulu = round(ajakulu / nädalate_arv)

print("Teie ajakulu nädalas on " + str(nädala_kulu))