# addition
def add(a, b):
    return a + b

# subtraction


def sub(a, b):
    return a - b

# multiplication


def mul(a, b):
    return a * b

# division


def div(a, b):
    try:
        return a / b
    except Exception as e:
        print(e)

# power


def pow(a, b):
    return a ** b

# remainder


def rem(a, b):
    return a % b


while True:
    print('''
  Select operation.
  1. Add       : +
  2. Subtract  : -
  3. Multiply  : *
  4. Divide    : /
  5. Power     : **
  6. Remainder : %
 ''')

    choice = input("Enter choice(+, -, *, /, **, %): ")
    print(choice)

    while True:
        num1 = input("Enter first number: ")
        try:
            num1 = float(num1)
            break
        except:
            print("Enter valid number")
            continue
    while True:
        num2 = input("Enter Second number: ")
        try:
            num2 = float(num2)
            break
        except:
            print("Enter valid number")
            continue
        
    if choice == '+':
        print(num1, '+', num2, '=', add(num1,num2))
    elif choice == '-':
            print(num1, '-', num2, '=', sub(num1,num2))
    elif choice == '*':
            print(num1, '*', num2, '=', mul(num1,num2))
    elif choice == '/':
            print(num1, '/', num2, '=', div(num1,num2))
    elif choice == '**':
            print(num1, '**', num2, '=', pow(num1,num2))
    elif choice == '%':
            print(num1, '%', num2, '=', rem(num1,num2))
    else:
        print("Invalid input")
        continue
    
    ch = input("Do you want to continue? (y/n): ")
    if ch == 'y' or ch == 'Y':
        continue
    else:
         print("Bye")
         exit()
