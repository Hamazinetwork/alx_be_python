
def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and non-numeric input.
    Returns a string with the result or an appropriate error message.
    """
    try:
        # Convert inputs to float (can raise ValueError if invalid)
        num = float(numerator)
        den = float(denominator)

        # Perform division (can raise ZeroDivisionError)
        result = num / den
        return f"The result of dividing {num} by {den} is {result:.2f}"

    except ValueError:
        return "Error: Both inputs must be numeric values."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
