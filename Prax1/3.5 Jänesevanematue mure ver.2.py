ringide_arv = int(input("Sisestage ringide arv: "))
ring = 1
pndid = 0
while ring <= ringide_arv:
    pp = 0
    p = 1
    while p <= ring:
        pp = pp + p
        p = p + 1
    print(str(ring) + ". ringiga sai " + str(pp))
    pndid = pndid + pp
    ring = ring + 1
print(pndid)