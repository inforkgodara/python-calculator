"""A keyboard-friendly calculator for four basic arithmetic operations."""


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


def read_number(label):
    """Ask again after invalid input; return None if the user cancels."""
    while True:
        value = input(f"{label} (or n to cancel): ").strip()
        if value.lower() == "n":
            return None
        try:
            return float(value)
        except ValueError:
            print("Please enter a number, or n to cancel this calculation.")


def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
    }

    while True:
        print("\nCalculator")
        print("1. Add   2. Subtract   3. Multiply   4. Divide")
        choice = input("Choose 1-4, or n to exit: ").strip().lower()

        if choice == "n":
            print("Calculator closed.")
            break
        if choice not in operations:
            print("Please choose 1, 2, 3, 4, or n.")
            continue

        first = read_number("First number")
        if first is None:
            print("Calculation canceled. Returning to menu.")
            continue
        second = read_number("Second number")
        if second is None:
            print("Calculation canceled. Returning to menu.")
            continue

        symbol, operation = operations[choice]
        try:
            print(f"Result: {first} {symbol} {second} = {operation(first, second)}")
        except ValueError as error:
            print(f"Cannot calculate: {error}")


if __name__ == "__main__":
    main()
