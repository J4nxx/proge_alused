nimi = input("Sisestage oma nimi: ")

a = int(input("Sisestage lubatud kiirus (km/h): "))

b = int(input("Sisestage tegelik kiirus (km/h: "))

if b > a:
    c = b - a
    d = c * 3
else:
    d = 0
   
if d > 190:
    d = 190
print(nimi + ", kiiruse ületamise eest saad trahvi " + str(d) + " eurot.")
    
    