# TrackFit

TrackFit is a mobile app that allows users register their fitness activities and provide personalized workout plans.

## Features

- Register user (new feature)
- Authenticate user (updated feature)
- Authentication log (new feature)
- Allow user to input the number of activities they want to track to create a workout plan (updated feature)
- Track user progress (updated feature)
- Calculate calories burned
- Log user activities

## Description of the features

- Register user: The user can register in the app by providing a username and password. The user will be added to a json file to store the registered users.
- Authenticate user: The user can authenticate in the app by providing a username and password. The app will check if the credentials are correct. If the credentials are wrong, the app will ask again for a username and password.
- Authentication log: The app will log the authentication attempts in a json file.
- Allow user to input the number of activities they want to track to create a workout plan: The user can input the number of activities they want to track. The app will create a workout plan based on the number of activities. The app will also track the user progress based on the workout plan.
- Track user progress: The app will track the user progress based on the workout plan. The app will also test the function `update_progress()` in `progress` and add additional features if needed.
- Calculate calories burned: The app will calculate the number of calories burned during a workout.
- Log user activities: The app will log the user activities in a json file.

## Modifications

- Unified the current modules into a single one called `trackfit.py`.
- Added a register function.
- Added the users to a json file to store the registered users.
- Added a recursive function to ask again for a username and password if the credentials are wrong.
- Added a log authentication function.
- Added the logs to a json file to store the authentication logs.
- Added a function in `workout` to allow the user to input the number of activities they want to track.
- Fixed the code in `calories` to calculate the number of calories burned correctly.
- Tested the function `update_progress()` in `progress` and added additional features if needed.
- Fixed the error in `log` module.

## User Guide

1.- Clone the repository:

```bash
git clone
```

2.- Run the app:

```bash
python main.py
```

3.- Choose an option from the menu:

```ruby
Welcome to TrackFit!
Please select an option:
1. Register
2. Authenticate
3. Generate workout plan
4. Calculate calories burned
5. Track progress
6. View Users Auth logs
q. Exit

Enter option:
```

4.- Register a user:

```ruby
Enter option: 1
Register a new user:
please give your username : your-name
please give your password : your-password
User registered successfully!
```

or use the admin or guest user:

```json
{
    "users": [
        {
            "username": "admin",
            "password": "password"
        },
        {
            "username": "guest",
            "password": "1234"
        }
    ]
}
```

5.- Enjoy the app!

6.- Follow me and star the repository for more updates.

## Conclusion

By unifying the modules into a single one, we have improved the code organization and made it easier to maintain and debug. We have also added new features to make the app more efficient and user-friendly. The app now allows users to register, authenticate, track progress, calculate calories burned, and log activities. The app is now ready for deployment and use by fitness enthusiasts.
