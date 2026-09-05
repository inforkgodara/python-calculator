# Program makes a basic calculator
# Original author: @inforkgodara


def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        raise ValueError("Division by zero is not allowed.")

    return first_number / second_number


def main():
    print("Select an option.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input(
            "Enter choice (1/2/3/4 or n to cancel): "
        ).strip().lower()

        if choice in ("1", "2", "3", "4"):
            try:
                first_number = float(
                    input("Enter first number: ")
                )
                second_number = float(
                    input("Enter second number: ")
                )
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == "1":
                result = add(first_number, second_number)
                print(first_number, "+", second_number, "=", result)

            elif choice == "2":
                result = subtract(first_number, second_number)
                print(first_number, "-", second_number, "=", result)

            elif choice == "3":
                result = multiply(first_number, second_number)
                print(first_number, "*", second_number, "=", result)

            elif choice == "4":
                try:
                    result = divide(first_number, second_number)
                    print(first_number, "/", second_number, "=", result)
                except ValueError as error:
                    print(f"Error: {error}")

        elif choice == "n":
            print("You have successfully exited the calculator!")
            break

        else:
            print("Please enter a valid choice: 1, 2, 3, 4, or n.")


if __name__ == "__main__":
    main()