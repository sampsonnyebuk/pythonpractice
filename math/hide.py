secreatM = input("Enter a secreate message in upper case: ")
secreatD = " "
for char in secreatM:
    secreatD += str(ord(char))


original = ""
for char in range(1, len(secreatD)-1, 2):


print("Your original Message: ", secreatM)
