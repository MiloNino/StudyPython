# import LIBRERIA PARA NUMEROS RANDOM
import random

mymoneda=input("elige entre Cara o Sello \n").lower()
random_moneda= random.randint(0,1)

if random_moneda == 1:
    random_moneda="cara"
elif random_moneda ==0:
    random_moneda="sello"
else:
    print("selecion invalida")
print(random_moneda)
    
if mymoneda == random_moneda:
    print("Ganaste")
else:
    print("Perdiste")
