pöialpoisid = int(input("Mitu põialpoissi tahab õunu? "))
if pöialpoisid > 7:
    print("Meil on ainult seitse põialpossi.")
else:
    from random import randint
    a = 0
    õun = 14
    while a < pöialpoisid:
        a += 1
        r = randint(1,2)
        õun = õun - r
        print(str(r))
    print("Lumivalgekesele jäi " + str(õun))