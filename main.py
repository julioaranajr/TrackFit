"""
This script is a command-line program called TrackFit. 
It allows users to register, authenticate, generate workout plans, 
calculate calories burned, track progress, and view authentication logs.

Usage:
    python main.py

Dependencies:
    - stringcolor
    - trackfit

Author:
    Julio Arana, Jr.
"""

import sys
from stringcolor import cs
from trackfit import register_user, authenticate_user
from trackfit import create_workout_plan, calculate_calories_burned
from trackfit import get_user_progress, print_auth_logs

def main() -> None:
    """
    The main function of the TrackFit program.

    Returns:
        the echoing the user's input
    """
    print(cs("Welcome to TrackFit!", "blue"))
    print(cs("Please select an option:", "white"))
    print(cs("1. Register", "green"))
    print(cs("2. Authenticate", "green"))
    print(cs("3. Generate workout plan", "green"))
    print(cs("4. Calculate calories burned", "green"))
    print(cs("5. Track progress", "green"))
    print(cs("6. View Users Auth logs", "green"))
    print(cs("q. Exit\n", "green"))
    option = input("Enter option: ")
    if option == "1":
        register_user()
        print('\n')

    elif option == "2":
        authenticate_user()
        print('\n')

    elif option == "3":
        create_workout_plan()
        print('\n')

    elif option == "4":
        calculate_calories_burned()
        print('\n')

    elif option == "5":
        get_user_progress()
        print('\n')

    elif option == "6":
        print_auth_logs()
        print('\n')

    elif option == "q":
        print(cs("Goodbye!", "blue"))
        sys.exit()
    else:
        print(cs("Invalid option. Please try again.", "red"))
        main()

if __name__ == "__main__": #this is the entry point of the program
    main()
