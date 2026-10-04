from math import isfinite


def _validate_amounts(monthly_income, monthly_expenses):
    if not isfinite(monthly_income) or not isfinite(monthly_expenses):
        raise ValueError("Income and expenses must be finite numbers.")
    if monthly_income < 0 or monthly_expenses < 0:
        raise ValueError("Income and expenses cannot be negative.")


def calculate_monthly_savings(monthly_income, monthly_expenses):
    _validate_amounts(monthly_income, monthly_expenses)
    return monthly_income - monthly_expenses


def calculate_annual_savings(monthly_income, monthly_expenses):
    return calculate_monthly_savings(monthly_income, monthly_expenses) * 12


def calculate_savings_percentage(monthly_income, monthly_expenses):
    monthly_savings = calculate_monthly_savings(monthly_income, monthly_expenses)
    if monthly_income == 0:
        raise ValueError("Savings percentage is undefined when income is zero.")
    return monthly_savings / monthly_income * 100