def mahlapakkide_arv(õunte_kogus):
    vastus = round(õunte_kogus*0.4/3)
    return vastus


mituõ = float(input("Mitu kilgorammi õunu on? "))
print(mahlapakkide_arv(mituõ))
