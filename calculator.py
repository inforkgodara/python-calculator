# Program make a basic calculator
# Author @inforkgodara

# Function adds two numbers
def add(first_number, second_number):
    return first_number + second_number


# Function subtracts two numbers
def subtract(first_number, second_number):
    return first_number - second_number


# Function multiplies two numbers
def multiply(first_number, second_number):
    return first_number * second_number


# Function divides two numbers
def divide(first_number, second_number):
    return first_number / second_number


print('Select options.')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

while True:
    # Take input from the console
    choice = input('Enter choice(1/2/3/4 or n to cancel): ')
    # Check if choice is one of the five options
    if choice in ('1', '2', '3', '4'):
        first_number = float(input('Enter first number: '))
        second_number = float(input('Enter second number: '))

        if choice == '1':
            print(first_number, '+', second_number, '=', add(first_number, second_number))

        elif choice == '2':
            print(first_number, '-', second_number, '=', subtract(first_number, second_number))

        elif choice == '3':
            print(first_number, '*', second_number, '=', multiply(first_number, second_number))

        elif choice == '4':
            print(first_number, '/', second_number, '=', divide(first_number, second_number))
    elif choice == 'n':
        print('Your are successfully logged out!')
        break
    else:
        print('Please enter correct input among these 1/2/3/4/n')
