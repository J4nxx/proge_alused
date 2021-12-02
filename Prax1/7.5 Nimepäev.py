import requests

kuu = str(input("Sisestage kuu: "))
päev = int(input("Sisestage päev: "))

url = 'http://kodu.ut.ee/~eno/mooc/' + str(kuu)
output = requests.get(url).text
data = output.splitlines()

a = 0

for line in data:
    a += 1
    if a == päev:
        print("Kuupäeval " + str(päev) + ". " + str(kuu) + " on nimepäevad järgmiste nimedega inimestel:")
        print(line)