'''PYCODE'''

# ? 1. Simple Calculator
# ? Features: Perform basic arithmetic operations.

# * Source Code
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = input("Operation (+, -, * /, **): ")

match c:
    case '+':
        print(a + b)
        
    case '-':
        print(a - b)
        
    case '*':
        print(a * b)
        
    case '/':
        print(a / b)
        
    case '**':
        print(a ** b)
