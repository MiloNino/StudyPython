# fruits = ["manzana","pera","naranja"]

# for fruit in fruits:
#     print (fruit)
#     print(fruits)
    
    
# for fruit in fruits:
#     print (fruit)
# print(fruits)



mascotas=["Moka","Lana","Poposo","Lulu","Dacota"]
print(mascotas)
puesto=0

for perro in mascotas:
    print(f"el for esta ubicado en el puesto # {puesto}")
    puesto += 1
    print(perro)
    
    
# comando "range" genera numeros en el intervalo dado             A<= X <B
for i in range(1,10):
    print(i)
# comando "range" genera numeros en el intervalo dado peor definiendo la forama en que aumenta       A<= X <B  ++3
for i in range(1,10,3):
    print(i)
    