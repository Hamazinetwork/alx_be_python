def self_divide(numerator, denominator):
    try: 
        num = float(numerator)
        den = float(denominator)
        result = num / den 
        return f"{num} by {den} is {result:.2f}"
    except ValueError:
        return "Error: both inputs must be numeric values"
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
