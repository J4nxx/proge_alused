from datetime import *
list = str(input("Palun sisestage failinimi: "))
fail = open("nimekiri.txt", encoding="UTF-8")
nimed = []
for rida in fail:
    nimed = nimed + [rida.strip("\n")]
fail.close()

print("Vastama tuleb: " + nimed[datetime.now().day - 1])