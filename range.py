square = [x ** 2 for x in range(10)]
print(square)
double = [(x,y) for x in range(10) for y in range(5, 10) if (x + y) % 2 != 0]
print(double)
