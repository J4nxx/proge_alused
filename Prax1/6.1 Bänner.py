def banner(mislause):
    return mislause.upper()
mitukord = int(input("Mitu korda soovite reklaamlauset kuvada? "))
mislause = str(input("Sisestage reklaamlause "))
for i in range(0, mitukord):
    print(banner(mislause))






