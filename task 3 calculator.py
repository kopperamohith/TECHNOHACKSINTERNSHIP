operation = input('''
enter the operation to be performed
+ for add
- for sub
* for mul
/ for div
''')

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if operation == '+':
    print(num1 + num2)

elif operation == '-':
    print(num1 - num2)

elif operation == '*':
    print(num1 * num2)

elif operation == '/':
    print(num1 / num2)

else:
    print('invalid operator.')
