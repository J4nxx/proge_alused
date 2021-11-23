def tervitus(arv):
    for i in range (1, arv + 1):
        print("Võõrustaja: 'Tere!'")
        print("Täna", str(i)  + ". kord tervitada, mõtiskleb võõrustaja.")
        print("Külaline: 'Tere, suur tänu kutse eest!'")
arv = int(input("Sisestage külaliste arv: "))
tervitus(arv)