täisarv = int(input("Sisestage täisarv: "))
i = 1
nisuteri = 0
if täisarv == 0:
    print("Nisuteri " + str(täisarv) + ".ruudu eest: " + str (nisuteri))
else:
    nisuteri = 1
    while i < täisarv:
        i += 1
        nisuteri *= 2
    print("Nisuteri " + str(täisarv) + ".ruudu 2eest: " + str (nisuteri))