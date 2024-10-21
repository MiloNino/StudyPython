
height = 1.65 
weight = 84
bmi=weight/height**2
print(bmi)

print("\n Hola, Bienvenidos a tu calculadora de cuentas de comida morbida.   /(0.0)/ \n")
cuenta= int(input("Cuanto te costo esa comida gigante??.   [-_-] \n"))
personas= int(input("Cuantas personas comieron comida morbida hoy??.    _(0.0)_ \n"))
porcentajePropina= 1 + int(input("Cuanta porcentaje de propina quieren dar??. \n"))/100

pago=round(cuenta* porcentajePropina /personas,2)
print( f"Cada Mechas debe pagar: $ {pago}  pesos.    (T.T)   \n MECHAS CHINCHOSOOOOOO")