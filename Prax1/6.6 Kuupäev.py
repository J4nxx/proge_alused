def kuu_nimi(järjekord):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[int(järjekord) - 1]
def kuupäev_sõ(kuupäev):
    kuupäevad = kuupäev.split(".")
    kuupäev = kuupäevad[0] + "." + kuu_nimi(kuupäevad[1]) + " " + kuupäevad[2] + ". a"
    return kuupäev
kuupäev = input("Sisesta kuupäev kujul DD.MM.YYYY: ")

print(str(kuupäev_sõ(kuupäev)))