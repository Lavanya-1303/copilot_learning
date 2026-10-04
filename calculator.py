from finance_data import (
    calculate_annual_savings,
    calculate_monthly_savings,
    calculate_savings_percentage,
)


def calculate(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "**":
        return first_number ** second_number
    if operator == "%":
        return first_number % second_number
    if operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    raise ValueError("Unsupported operation.")


def main():
    choice = input("Choose a tool (1: Calculator, 2: Personal finance): ").strip()

    if choice == "1":
        try:
            first_number = float(input("Enter the first number: "))
            operator = input("Choose an operation (+, -, *, /, %, **): ").strip()
            second_number = float(input("Enter the second number: "))
            result = calculate(first_number, operator, second_number)
            print(f"Result: {result}")
        except ValueError as error:
            print(f"Invalid input: {error}")
        except ZeroDivisionError as error:
            print(error)
    elif choice == "2":
        try:
            monthly_income = float(input("Enter your monthly income: "))
            monthly_expenses = float(input("Enter your monthly expenses: "))
            monthly_savings = calculate_monthly_savings(
                monthly_income, monthly_expenses
            )
            annual_savings = calculate_annual_savings(
                monthly_income, monthly_expenses
            )
            savings_percentage = calculate_savings_percentage(
                monthly_income, monthly_expenses
            )
            print(f"Monthly savings: {monthly_savings:.2f}")
            print(f"Annual savings: {annual_savings:.2f}")
            print(f"Savings percentage: {savings_percentage:.2f}%")
        except ValueError as error:
            print(f"Invalid input: {error}")
    else:
        print("Invalid choice. Choose 1 or 2.")


if __name__ == "__main__":
    main()