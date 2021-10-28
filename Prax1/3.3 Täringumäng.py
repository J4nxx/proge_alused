täringud = int(input("Täringute arv: "))
from random import randint
a = 0
while a < täringud:
    r = randint(1,6)
    a += 1
    print(str(r))