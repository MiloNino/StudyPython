# import LIBRERIA PARA NUMEROS RANDOM
import random
print("\nBienvenido al juego de Piedra, Papel o Tijeras contra el Gato")


def juego_jugador():
    eleccion =input("Elige entre Piedra, Papel o Tijeras \n").lower()
    if eleccion == "piedra" :
        
        print( """"tu elijes: Piedra \n
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    \n""")
    elif eleccion == "papel":
        print( """"tu elijes: Papel \n
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    \n""")
    elif  eleccion == "tijeras":
        print( """"tu elijes: Tijeras \n
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    \n""")
        
    else:
        print("selecion invalida")
        juego_jugador()
        
# parte random
    random_eleccion = random.randint(0,2)
    if random_eleccion == 2:
        random_eleccion ="piedra"
        print( """"el Gato elije: Piedra \n
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    \n""")
    if random_eleccion ==1:
        random_eleccion="papel"
        print( """"el Gato elije: Papel \n
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    \n""")
    if random_eleccion ==0:
        random_eleccion="tijeras"
        print( """"el Gato elije: Tijeras \n
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    \n""")
        
    if (eleccion == "piedra" and random_eleccion == "tijeras") or (eleccion =="tijeras" and random_eleccion == "papel") or (eleccion =="papel" and random_eleccion == "piedra"):
        print("Ganaste, ahora hay un gato triste (T.T).\n")
    elif eleccion == random_eleccion:
        print("Empate.Esto es un duelo de titanes 0.0/.\n")
        juego_jugador()
        
    else:
        print("Perdiste, el gato es el mejor (-.-).\n")  
juego_jugador()