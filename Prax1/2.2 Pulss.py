#Info treenija kohta:
vanus = int(input("Sisestage enda vanus: "))
sugu = str(input("Sisestage enda sugu m või n: "))
treeningtüüp = int(input("Sisestage treeningu tüüp 1, 2 või 3: "))

# Treeningtüüpid
if (sugu == "m" or "M"):
    tervisetreening = 220 - vanus
elif (sugu == "n" or "N"):
    tervisetreening = 206 - (vanus * 0.88)

# Treeningu arvutus.
if treeningtüüp == 1:
    tervisetreening_min = round(tervisetreening * 0.5)
    tervisetreening_max = round(tervisetreening * 0.7)

elif treeningtüüp == 2:
    tervisetreening_min = round(tervisetreening * 0.7)
    tervisetreening_max = round(tervisetreening * 0.8)

elif treeningtüüp == 3:
    tervisetreening_min = round(tervisetreening * 0.8)
    tervisetreening_max = round(tervisetreening * 0.87)

print("Pulsisagedus peaks olema vahemikus " + str(tervisetreening_min) + " kuni " + str(tervisetreening_max) + ".")
        