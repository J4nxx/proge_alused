def eelarve(külalised):
    rent = 55
    summa = külalised * 10 + rent
    return summa
kutsutud = int(input("Mitu inimest on kutsutud? "))
tulemas = int(input("Mitu inimest tuleb? "))
print("Maksimaalne eelarve ", eelarve(kutsutud), "eurot")
print("Minimaalne eelarve ", eelarve(tulemas), "eurot")