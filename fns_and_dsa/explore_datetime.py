# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add: "))
        future_date = datetime.now() + timedelta(days=days)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print("Future Date after", days, "days will be:", formatted_future)
    except ValueError:
        print("Invalid input. Please enter an integer value.")

def main():
    print("\n--- Part 1: Display Current Date and Time ---")
    display_current_datetime()

    print("\n--- Part 2: Calculate a Future Date ---")
    calculate_future_date()

if __name__ == "__main__":
    main()
