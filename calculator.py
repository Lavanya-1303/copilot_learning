def calculate(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    raise ValueError("Unsupported operation.")


def main():
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ").strip()
        second_number = float(input("Enter the second number: "))
        result = calculate(first_number, operator, second_number)
        print(f"Result: {result}")
    except ValueError as error:
        print(f"Invalid input: {error}")
    except ZeroDivisionError as error:
        print(error)


if __name__ == "__main__":
    main()