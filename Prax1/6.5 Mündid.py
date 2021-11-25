def pronksikarva_summa(raha):
    summa = 0
    for mündid in raha:
        if int(mündid) <= 5:
            summa += int(mündid)
    return summa
fail = open(input("Sisestage failinimi: "), encoding="UTF-8")
print("Hoiupõrsasse läheb", pronksikarva_summa(fail),"senti")
fail.close()        