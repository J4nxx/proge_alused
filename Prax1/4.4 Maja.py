from tkinter import *
 
raam = Tk()
raam.title("Maja")
tahvel = Canvas(raam, width=500, height = 500)



#taevas
tahvel.create_rectangle(0, 0, 500, 230, fill="blue", outline="blue")
#muru
tahvel.create_rectangle(0, 500, 500, 230, fill="green", outline="green")
#korsten
tahvel.create_rectangle(260, 75, 290, 150, fill="light gray", width=3, outline="black")
#maja
tahvel.create_rectangle(150, 170, 340, 280, fill="yellow", width=3, outline="black")
#majakatus
tahvel.create_polygon(150, 170, 245, 85, 340, 170, fill="red", width=3, outline="black")
#uks
#korsten
tahvel.create_rectangle(227.5, 220, 265, 280, fill="brown", width=2, outline="black")
#ukse käepide
tahvel.create_oval(240, 245, 230, 255, fill="gray", outline="black")


tahvel.pack()
raam.mainloop()