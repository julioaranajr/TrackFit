# Functions outputs

## Register a new user

```python
# Register a new user with a function
register_user()
```

```bash
Register a new user:
please give your username : admin
please give your password : password
User registered successfully!
```

## Authenticate user

```python
# Authenticate users with a function
authenticate_user()
```

```bash
# login with a registered user
Authenticating user...
please give your username : admin
please give your password : password
User authenticated successfully!

# another user
Authenticating user...
please give your username : guest
please give your password : 1234
User authenticated successfully!

# another user with wrong credentials
Authenticating user...
please give your username : julio
please give your password : iglesias
Invalid credentials, Please, Try again:

## Add a workout plan

```python
# Add workout to the workout list
add_workout(workouts,workout_id,workout_name,calorie_chart):
```

```bash
# test add_workout
workouts = load_workouts()
add_workout(workouts,1,"Running",600)
add_workout(workouts,2,"Cycling",500)
add_workout(workouts,3,"Swimming",700)
add_workout(workouts,4,"Yoga",300)
add_workout(workouts,5,"Push-ups",300)
add_workout(workouts,6,"Sit-ups",500)
add_workout(workouts,7,"Squats",300)
add_workout(workouts,8,"Jumping Jacks",700)
```

## Create a workout plan

```python
# Create workout plan for the current user
create_workout_plan():
```

```bash
Create a workout plan:
please give your username : guest
Available workouts:
1: Running
2: Cycling
3: Swimming
4: Yoga
5: Push-ups
6: Sit-ups
7: Squats
8: Jumping Jacks
Enter workout Name (x to finish): 1
Invalid workout Name, please try again.
Enter workout Name (x to finish): Yoga
Enter workout Name (x to finish): Squats
Enter workout Name (x to finish): x
Workout plan created and saved successfully!
```

## Calculate calories burned

```python
# Calculate calories burned for the current user
calculate_calories_burned():
```

```bash
Calculate calories burned:
Please enter your username: guest
Please enter the workout name: Yoga
Please enter the start time (HH:MM): 06:00
Please enter the end time (HH:MM): 10:00
Calories burned calculated and logged successfully!
```

## Get user progress

```python
# Get user progress
get_user_progress():
```

```bash
Get user's progress:
Please enter the username: guest
User's progress:
Workout: Cycling, Calories Burned: 500
Workout: Squats, Calories Burned: 300
Workout: Yoga, Calories Burned: 1200
Workout: Sit-ups, Calories Burned: 250
Workout: Jumping Jacks, Calories Burned: 350
Workout: Swimming, Calories Burned: 700
Workout: Swimming, Calories Burned: 700
Workout: Swimming, Calories Burned: 700
Workout: Push-ups, Calories Burned: 150
Workout: Yoga, Calories Burned: 525
Workout: Yoga, Calories Burned: 150
```

## Print log activity

```python
# Print authentication logs
print_auth_logs():
```

```bash
Authentication logs:
Username: admin, Status: Authenticated, Time: 2024-07-23 17:39:19.391214
Username: guest, Status: Authenticated, Time: 2024-07-23 17:39:33.978835
Username: julio, Status: Not Authenticated, Time: 2024-07-23 17:39:51.543183
Username: user, Status: Not Authenticated, Time: 2024-07-24 03:04:20.310658
Username: user, Status: Not Authenticated, Time: 2024-07-24 03:04:29.063723
Username: user, Status: Not Authenticated, Time: 2024-07-24 03:04:42.178019
Username: user, Status: Not Authenticated, Time: 2024-07-24 03:04:49.599046
Username: user, Status: Authenticated, Time: 2024-07-24 15:04:56.978019
```
