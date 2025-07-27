# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date,
    and prints it in 'YYYY-MM-DD' format.
    """
    try:
        num_days_input = input("Enter the number of days to add to the current date: ")
        num_days = int(num_days_input)

        current_date_for_future = datetime.now()
        future_date = current_date_for_future + timedelta(days=num_days)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to run the datetime operations.
    """
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
    