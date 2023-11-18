amount, interest = map(float, (input("Enter your capital and expected interest ").split()))
year = 10
for i in range(year):
    amount += amount + (interest/100)


print("Compound interest for {} is {:.2f}".format(year, amount))
