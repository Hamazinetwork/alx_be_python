# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and non-numeric input.
    Returns a string with the result or an appropriate error message.
    """
    try:
        # Attempt to convert to float (could raise ValueError)
        num = float(numerator)
        den = float(denominator)

        # Attempt division (could raise ZeroDivisionError)
        result = num / den
        return f"The result of the division is {result:.1f}"

    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
