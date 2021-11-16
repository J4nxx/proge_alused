from tkinter import *

raam = Tk()
raam.title("Malelaud")
malelaud = Canvas(raam, width=800, height=800)


#raami vasak ülemine nurk
x1 = 0
y1 = 0
#raami paremal all nurk
x2 = 100
y2 = 100

#i'd on vaja mustade ja valgete kastide vahetamiseks
i = 0

j = 1

while y2 <= 800:
    
    while x2 <= 800:
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            malelaud.create_rectangle(x1, y1, x2, y2, fill="white", outline = "white")
        if i == 1 or i == 3 or i == 5 or i == 7:
            malelaud.create_rectangle(x1, y1, x2, y2, fill="black", outline = "black")
        #muudame värvi
        i += 1
        #teeb uue ruudu täpselt õigesse kohta
        x1 += 100
        x2 += 100
    #teeb uue rea õigesse kohta 
    y1 += 100
    y2 += 100
    #x kordinaadid algusesse tagasi    
    x1 = 0
    x2 = 100
    #arvutab mis värviga järgmine ruut peaks olema    
    if j == 0 or j == 2 or j == 4 or j == 6 or j == 8:
        i = 0
    if j == 1 or j == 3 or j == 5 or j == 7:
        i = 1
    j += 1

#teeb malenuppud (2tk)
malelaud.create_oval(390, 390, 310, 310, fill ="#807a7a", outline="#807a7a")
malelaud.create_oval(490, 490, 410, 410, fill ="#D2B48C", outline="#D2B48C")

malelaud.pack()
raam.mainloop()