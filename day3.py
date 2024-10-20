# print("\n App to identify the even or odd status of a number \n")
# number= int(input("enter the number you want \n"))
# if (number % 2) == 0 :
#     print("your number is an even number")
# else:
#     print("your number is an odd number")

# weight = 85
# height =  1.85

# bmi = (weight/height**2)

# if bmi <18.5:
#     print("underweight")
# elif bmi <24.9:
#     print("normal")
# else:
#     print("overweight")

# print("\nWelcome to the Pizzeria\n")
# bill = 0
# size = input("What size pizza would you like? (s/m/l): ").lower() 
# extra_1 = input("Would you like extra pepperoni? (Y/N): ").lower()  
# extra_2 = input("Would you like extra cheese? (Y/N): ").lower()  

# # Setting prices based on size
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25
# else:
#     print("Invalid choice, please try again.")

# # Adding pepperoni
# if size == "s" and extra_1 == "y":
#     bill += 2
# elif extra_1 == "y" and (size == "m" or size == "l"):
#     bill += 3

# # Adding cheese
# if extra_2 == "y":
#     bill += 1

# # Final bill message
# print(f"The total bill for a {size} pizza is ${bill}")

print("\nBienvenido al juego de Moka, prueba tu conocimiento sobre el perro más loco.")
contador = 0
pregunta_1 = input("Primer nivel --> ¿Qué prefiere comer Moka?:\n a) Pan.\n b) Manzana.\n").lower()
if pregunta_1 == "a":
    contador += 1
    print(f"\n¡Correcto! Sí conoces a Moka. Vas {contador}/3 preguntas.\n")
    
    pregunta_2 = input("Segundo nivel --> ¿Cómo es la mirada de Moka?:\n a) Loca.\n b) Juzgadora.\n").lower()
    if pregunta_2 == "b":
        contador += 1
        print(f"\n¡Correcto! Sí conoces a Moka. Vas {contador}/3 preguntas.\n")
        
        pregunta_3 = input("Tercer nivel --> Moka es un perro:\n a) Loco.\n b) Express.\n c) Lindo.\n").lower()
        if pregunta_3 == "b":
            print(f"\n¡Felicidades! Conoces a Moka, eres el Fan #1 de Moka.")
        else:
            print("\nLo siento, perdiste. ¡Inténtalo de nuevo!")
    else:
        print("\nLo siento, perdiste. ¡Inténtalo de nuevo!")
else:
    print("\nLo siento, perdiste. ¡Inténtalo de nuevo!")