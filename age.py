age = int(input("whta's your age? "))
if(age >= 1) and (age <= 18):
    print("your birthday is important")
elif(age == 21) or ( age == 50):
    print("important")
elif not (age < 65):
    print("important")
else:
    print("unimportant")
