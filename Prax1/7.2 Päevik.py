from datetime import datetime
kuupäev_kellaaeg = datetime.today()

fail = open("paevik.txt", "a")

fail.write(str(kuupäev_kellaaeg))
fail.write("\n")
fail.write(str(input("Sisesta sissekande tekst: ")))
fail.write("\n\n")

fail.close()