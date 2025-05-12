import random 

print("---- Welcome The Game ----")
while True:
    user_input = input("Choosh One (Y/N)...").lower()
    if user_input == "y":
        number1 = random.randint(1, 20)
        number2 = random.randint(30, 50)
        print(number1, number2)
    elif user_input == "n":
        print("Thank You...!")
        break
    else:
        print("Invalid Choice")
