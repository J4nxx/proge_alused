fail = open("rebased.txt", encoding="UTF-8")
aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))
aasta1 = 2011
if aasta <= 2010 or aasta >= 2020:
        print("Kahjuks ei ole meil informatsiooni sellel aastal.")
        
for rida in fail:
    if aasta == aasta1:
        print(aasta1, " aastal oli vastuvõetuid ", rida)
        break
    aasta1 +=1


    
fail.close()