from tkinter import *
 
raam = Tk()
raam.title("Kaarma valla lipp")
# loome tahvli laiusega 1760px ja kõrgusega 1120px
tahvel = Canvas(raam, width=1760, height = 1120)


tahvel.create_rectangle(0, 0, 1760, 1120, fill="white", outline="white")

tahvel.create_rectangle(0,480, 1760, 640, fill="blue", outline="light blue")
    




tahvel.pack()
raam.mainloop()