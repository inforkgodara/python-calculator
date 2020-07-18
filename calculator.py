# Program make a basic calculator
# Author @inforkgodara

# Function adds two numbers
def add(firstNumber, secondNumber):
    return firstNumber + secondNumber

# Function subtracts two numbers
def subtract(firstNumber, secondNumber):
    return firstNumber - secondNumber

# Function multiplies two numbers
def multiply(firstNumber, secondNumber):
    return firstNumber * secondNumber

# Function divides two numbers
def divide(firstNumber, secondNumber):
    return firstNumber / secondNumber


print("Select options.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take input from the console
    choice = input("Enter choice(1/2/3/4 or n to cancel): ")
    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        firstNumber = float(input("Enter first number: "))
        secondNumber = float(input("Enter second number: "))

        if choice == '1':
            print(firstNumber, "+", secondNumber, "=", add(firstNumber, secondNumber))

        elif choice == '2':
            print(firstNumber, "-", secondNumber, "=", subtract(firstNumber, secondNumber))

        elif choice == '3':
            print(firstNumber, "*", secondNumber, "=", multiply(firstNumber, secondNumber))

        elif choice == '4':
            print(firstNumber, "/", secondNumber, "=", divide(firstNumber, secondNumber))
    elif choice == 'n':
        print("Your are successfully logged out!")
        break
    else:
        print("Please enter correct input among these 1/2/3/4/n")
