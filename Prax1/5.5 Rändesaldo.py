fail = open("sisseränne.txt", encoding="UTF-8")
sränneteloend = []
for ränne in fail:
    sränneteloend.append(ränne)
fail.close()
fail = open("väljaränne.txt", encoding="UTF-8")
vränneteloend = []
for ränne in fail:
    vränneteloend.append(ränne)
fail.close()
rändesaldo = []
i = 0
while i <10:
    rändesaldo.append(int(sränneteloend[i]) - int(vränneteloend[i]))
    i +=1
print(rändesaldo)
if max(rändesaldo) > 0:
    print("Suurim rändesaldo oli " + str(i) + ". aastal")
else:
    print("Positiivse rändesaldoga aastaid ei ole.")