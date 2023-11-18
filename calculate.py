num1, num2, operator = input("Enter numbers and operator ").split()
num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
defference = num1 - num2
quotient = num1 / num2
remender = num1 % num2
product = num1*num2

if operator == '+':
    print('{} = {} + {}'.format(sum, num1, num2))
elif operator == '-':
    print('{} = {} - {}'.format(defference, num1, num2))
elif operator == '/':
    print('{} = {} / {}'.format(quotient, num1, num2))
elif operator == '%':
    print('{} = {} % {}'.format(remender, num1, num2))
elif operator == '*':
    print('{} = {} * {}'.format(product, num1, num2))
