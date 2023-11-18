# guess = int(input("Guess a number between 1 and 10: "))


# while  guess <= 10:
#     print("you gussed it ")
#     break

secret_num = 7

while True:
    guess = int(input("Guess two numbers between 1 and 10: "))

    if guess == secret_num:
        print("you gussed right")
        break
