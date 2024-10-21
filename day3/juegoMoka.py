

print("Bienvenido a la juego de Moka, prueba tu concimiento del pero mas loco")
contador= 0
pregunta_1=input("primer nivel --> Moka que prefier comer: \n a) pan.\n b)manzana.\n")
if pregunta_1=="a":
    contador +=1
    print(f"\n correcto, si conoces a Moka, vas {contador}/3 preguntas\n")
    pregunta_2=input("segundo nivel --> Moka que tiene una mirada: \n a) loca.\n b)jusgadora.\n")
    if pregunta_2=="b":
        contador +=1
        print(f"\n correcto, si conoces a Moka, vas {contador}/3 preguntas\n")
        pregunta_3=input("tercer nivel --> Moka es un perro:\n a) loco. \n b)express.\n C) lindo.\n")
        if pregunta_3=="b":
            print(f"\n felicidades, si conoces a Moka, eres el Fan #1 de Moka")
    else:
        print("\n lo seinto perdiste intentalo de nuevo")
else:
    print("\n lo seinto perdiste intentalo de nuevo")