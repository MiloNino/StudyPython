# print("\n App to identify the even or odd status of a number \n")
# number= int(input("enter the number you want \n"))
# if (number % 2) == 0 :
#     print("your number is an even number")
# else:
#     print("your number is an odd number")


weight = 85
height =  1.85

bmi = (weight/height**2)

if bmi <18.5:
    print("underweight")
elif bmi <24.9:
    print("normal")
else:
    print("overweight")
