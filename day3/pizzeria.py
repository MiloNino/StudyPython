
print("\nWelcome to the Pizzeria\n")
bill = 0
size = input("What size pizza would you like? (s/m/l): ").lower() 
extra_1 = input("Would you like extra pepperoni? (Y/N): ").lower()  
extra_2 = input("Would you like extra cheese? (Y/N): ").lower()  

# Setting prices based on size
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid choice, please try again.")

# Adding pepperoni
if size == "s" and extra_1 == "y":
    bill += 2
elif extra_1 == "y" and (size == "m" or size == "l"):
    bill += 3

# Adding cheese
if extra_2 == "y":
    bill += 1

# Final bill message
print(f"The total bill for a {size} pizza is ${bill}")
