while True:
    try:
        number = int(input("Please enter a number: "))
        break

    except ValueError:
        print("You didn't enter a number")

    except:
        print("An unknown Error")
print("thank you for entering a number")
