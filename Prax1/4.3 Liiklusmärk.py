from tkinter import *
 
raam = Tk()
raam.title("parkimiskeelumärk")
tahvel = Canvas(raam, width=300, height = 300)

tahvel.create_rectangle(0, 0, 300, 300, fill="white", outline="white")

tahvel.create_oval(10, 10, 290, 290, fill="red", width=2.5, outline="black")

tahvel.create_oval(30, 30, 270, 270, fill="light blue", width=2.5, outline="black")

tahvel.create_polygon(75, 55, 230, 250, width=14, fill="red", outline="red")

tahvel.create_polygon(50, 230, 250, 70, width=14, fill="red", outline="red")

tahvel.pack()
raam.mainloop()