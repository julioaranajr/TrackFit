"""
TrackFit is a simple app that helps users track their fitness progress.
The app has the following features:
- Register users
- Authenticate users
- Generate workout plans
- Calculate calories burned
- Log activities
"""

import json
from datetime import datetime
from stringcolor import cs


def load_users() -> list:
    """Load the user data from a JSON file.

    Returns:
        list: A list of user data.
    """
    with open('users.json', mode="r", encoding="utf-8") as f: # r is read mode
        data = json.load(f) # we are converting the data from json => dict
    return data['users']

def save_users(users: list) -> None:
    """Save the users to a JSON file.

    Args:
        users (list): A list of user objects to be saved.
    """
    with open('users.json', mode="w", encoding="utf-8") as file: # w is write mode
        json.dump({"users": users}, file, indent=4) # indent=4 is for pretty print

def load_logs() -> list:
    """Loads the authentication logs from a JSON file.

    Returns:
        dict: A dictionary containing the authentication logs.
    """
    with open('auth_logs.json', mode="r", encoding="utf-8") as f:
        data = json.load(f)
    return data['auth_logs']

def save_logs(auth_logs: list) -> None:
    """
    Save authentication logs to a JSON file.

    Args:
        auth_logs (list): A list of authentication logs.

    Returns:
        None
    """
    with open('auth_logs.json', mode="w", encoding="utf-8") as file:
        json.dump({"auth_logs": auth_logs}, file, indent=4)


def load_activity() -> list:
    """Loads the activity log from a JSON file and returns the activity data.

    Returns:
        list: A list containing the activity data.
    """
    with open('activity_log.json', mode="r", encoding="utf-8") as f:
        data = json.load(f)
    return data['activity']

def save_activity(activity: list) -> None:
    """Saves the activity log to a JSON file.

    Args:
        activity (list): A list of activity data.

    Returns:
        None
    """
    with open('activity_log.json', mode="w", encoding="utf-8") as file:
        json.dump({"activity": activity}, file, indent=4)

#<-------------------------USER  AUTHENTICATION MODULE------------------------>


def register_user():
    """Register a new user.

    Returns:
        Appends the new user to the users list.
    """
    print("Register a new user:")
    username = input("please give your username : ")
    password = input("please give your password : ")
    users = load_users()
    # Check if the users list is empty
    if users == []:
        # Add the first user
        users.append({"username":username,"password":password})
        save_users(users)
        print(cs("User registered successfully!","green"))
        # Exit the function
    # Check if the username already exists
    elif any(user['username'] == username for user in users):
        print(cs("Username already exists, Please, Try again:","red"))
        return register_user()
    # Add the new user
    else:
        users.append({"username":username,"password":password})
        save_users(users)
        print(cs("User registered successfully!","green"))


# test register_user
# register_user()

def authenticate_user() -> bool:
    """Authenticate the user.

    Returns:
        bool: True if the user is authenticated, False otherwise.
    """
    print("Authenticating user...")
    username = input("please give your username : ")
    password = input("please give your password : ")
    login = load_logs()
    users = load_users()
    # Check if the user is in the users list
    if any(user['username'] == username and user['password'] == password for user in users):
        print(cs("User authenticated successfully!","green"))
        # Log the user's authentication
        login.append({"username":username,"status":"Authenticated","time":str(datetime.now())})
        save_logs(login)
        return True
    # Check if the user is not in the users list
    else:
        print(cs("Invalid credentials, Please, Try again:","red"))
        # Log the user's failed authentication
        login.append({"username":username,"status":"Not Authenticated","time":str(datetime.now())})
        save_logs(login)
        return authenticate_user()

# test authenticate_user
# authenticate_user()

#<-------------------AUTHENTICATION MODULE------------------------>

#<-----------------------WORKOUT MODULE--------------------------->

def load_workouts() -> list:
    """Load the workouts from a JSON file.

    Returns:
        list: A list of workout data.
    """
    with open('workouts.json', mode="r", encoding="utf-8") as f:
        data = json.load(f)
    return data['workouts']

def save_workouts(workouts: list) -> None:
    """Save the workouts to a JSON file.

    Args:
        workouts (list): A list of workout data.
    """
    with open('workouts.json', mode="w", encoding="utf-8") as file:
        json.dump({"workouts": workouts}, file, indent=4)

def get_workouts(workouts,workout_id) -> dict:
    """Get the workout data from the workout list.
    
    Args:
        workouts (list): A list of workout data.
        workout_id (int): The workout ID.
        
    Returns:
        dict: The workout data.
    """
    # Loop through the workouts list
    for workout in workouts:
        # Check if the workout ID matches
        if workout['id'] == workout_id:
            return workout
    return None

def add_workout(workouts,workout_id,workout_name,calorie_chart) -> None:
    """Add a new workout to the workout list.
    
    Args:
        workouts (list): A list of workout data.
        workout_id (int): The workout ID.
        workout_name (str): The workout name.
        calorie_chart (int): The calorie chart.
        
    Returns:
        None
    """
    # Check if the workouts list is empty
    if workouts == []:
        # Add the first workout
        workout_id = 1

    # Check if the workouts list is not empty
    else:
        workout_id = workouts[-1]['id'] + 1
    # Add the new workout
    workouts.append({"id":workout_id,"workout_name":workout_name,"calorie_chart":calorie_chart})
    save_workouts(workouts)
    print(cs("Workout added successfully!","green"))

# test add_workout
# workouts = load_workouts()
# add_workout(workouts,1,"Running",600)
# add_workout(workouts,2,"Cycling",500)
# add_workout(workouts,3,"Swimming",700)
# add_workout(workouts,4,"Yoga",300)
# add_workout(workouts,5,"Push-ups",300)
# add_workout(workouts,6,"Sit-ups",500)
# add_workout(workouts,7,"Squats",300)
# add_workout(workouts,8,"Jumping Jacks",700)

def create_workout_plan() -> None:
    """Create a workout plan for the user.
    
    Returns:
        None
    """
    print("Create a workout plan:")
    username = input("please give your username : ")
    workouts = load_workouts()
    print("Available workouts:")
    # Loop through the workouts list
    for workout in workouts:
        print(f"{workout['id']}: {workout['workout_name']}")
    # Create a list of workout names
    workout_names = []
    # Loop through the workouts list
    for workout in workouts:
        workout_names.append(workout['workout_name'])
    # Create a list of workout plan
    plan = []
    # Loop indefinitely
    while True:
        workout_name = input("Enter workout Name (x to finish): ")
        # Check if the user wants to finish
        if workout_name == 'x':
            break
        # Check if the workout name is not in the workout names
        elif workout_name not in workout_names:
            print(cs("Invalid workout Name, please try again.","red"))
        # Add the workout name to the plan
        else:
            plan.append(workout_name)
    # Save the workout plan
    users = load_users()
    # Loop through the users list
    for user in users:
        # Check if the username matches
        if user['username'] == username:
            user['workout_plan'] = plan
            save_users(users)
            print(cs("Workout plan created and saved successfully!","green"))
            return
    print(cs("User not found, please try again.","red"))

# test create_workout_plan
# create_workout_plan()

#<-----------------------WORKOUT MODULE--------------------------->

#<-----------------------CALORIES MODULE-------------------------->

def get_duration_in_minutes(start_time, end_time) -> int:
    """Get the duration in minutes between two times.
    
    Args:
        start_time (str): The start time.
        end_time (str): The end time.
        
    Returns:
        int: The duration in minutes
    """
    # Define the time format
    fmt = "%H:%M"
    # Convert the start and end times to datetime objects
    start = datetime.strptime(start_time, fmt)
    end = datetime.strptime(end_time, fmt)
    # Calculate the duration
    delta  = end - start
    # Calculate the duration in minutes
    duration_minutes = delta.total_seconds() / 60
    return int(duration_minutes)

def calculate_calories_burned() -> None:
    """Calculate the calories burned by the user.
    
    Returns:
        None
    """
    print("Calculate calories burned:")
    username = input("Please enter your username: ")
    workout_name = input("Please enter the workout name: ")
    start_time = input("Please enter the start time (HH:MM): ")
    end_time = input("Please enter the end time (HH:MM): ")
    # Load the workouts
    workouts = load_workouts()
    # Loop through the workouts
    calorie_chart = None
    for workout in workouts:
        if workout['workout_name'] == workout_name:
            calorie_chart = workout['calorie_chart']
            break
    # Check if the workout is not found
    if calorie_chart is None:
        print(cs("Workout not found, please try again.", "red"))
        return
    # Calculate the calories burned
    duration_minutes = get_duration_in_minutes(start_time, end_time)
    calories_burned = calorie_chart * duration_minutes // 60
    print(f"Calories burned: {calories_burned}")
    # Log the activity
    activity = load_activity()
    # Append the new activity
    activity.append({
        "username": username,
        "workout_name": workout_name,
        "start_time": start_time,
        "end_time": end_time,
        "calories_burned": calories_burned,
        "timestamp": str(datetime.now())
    })
    save_activity(activity)
    # Update the user's calories burned
    users = load_users()
    # Loop through the users
    for user in users:
        # Check if the username matches
        if user['username'] == username:
            # Add the workout name to the user
            user['workout_name'] = workout_name
            # Add the calories burned to the user
            user['calories_burned'] = user.get('calories_burned', 0) + calories_burned
            save_users(users)
            break
    print(cs("Calories burned calculated and logged successfully!", "green"))

# test calculate_calories_burned
# calculate_calories_burned()

#<-----------------------CALORIES MODULE-------------------------->

#<-----------------------PROGRESS MODULE-------------------------->

def get_user_progress() -> None:
    """Get the user's progress.
    
    Returns:
        None
    """
    print("Get user's progress:")
    username = input("Please enter the username: ")
    # Load the activity
    activity = load_activity()
    # Create a list of progress
    progress = []
    # Loop through the activity
    for entry in activity:
        # Check if the username matches
        if entry['username'] == username:
            # Add the workout name and calories burned to the progress
            workout_name = entry['workout_name']
            calories_burned = entry['calories_burned']
            progress.append((workout_name, calories_burned))
    # Check if the progress is empty
    if len(progress) == 0:
        print(cs("No progress found for the user.", "red"))
    # if the progress is not empty
    else:
        print("User's progress:")
        for workout_name, calories_burned in progress:
            print(f"Workout: {workout_name}, Calories Burned: {calories_burned}")

# test get_user_progress
# get_user_progress()

#<-----------------------PROGRESS MODULE-------------------------->

#<-------------------------LOGS MODULE---------------------------->

# Print authentication logs

def print_auth_logs() -> None:
    """Print the authentication logs.
    
    Returns:
        If there are logs, print the logs.
    """
    logs = load_logs()
    print("Authentication logs:")
    for log in logs:
        print(f"Username: {log['username']}, Status: {log['status']}, Time: {log['time']}")
    print(cs("Authentication logs printed successfully!","green"))
# test print_logs
# print_logs()

#<-------------------------LOGS MODULE---------------------------->
