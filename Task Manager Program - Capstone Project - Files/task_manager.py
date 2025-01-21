print("TASK MANAGER PROGRAM\n")

"""
A program that is used to do the following:

1. Login users from user.txt.
2. Add new users (admin only).
3. View all tasks from tasks.txt.
4. View tasks for the user from tasks.txt.
5. Displays statistics (admin only).
"""
# Imports.
import datetime
import sys

# Username validation when adding new username.
def get_valid_username():
    while True:
        # Requests user input and removes leading/trailing spaces.
        valid_username = input("Enter a new username: ").strip()
        # Checks if user has not input anything.
        if not valid_username:
            print("Error: username cannot be empty. Please try again.")
        # Usernames need to be at least 4 characters long.
        elif len(valid_username) < 4:
            print("Error: username must be at least 4 characters long."
                  " Please try again.")
        # Ensures that no spaces are contained in username.
        elif ' ' in valid_username:
            print("Error: Username cannot contain spaces. Please try again.")
        # Finally get and print the correct result.
        else:
            print(f"Username '{valid_username}' is valid!")
            return valid_username

# The logic of the function above will be used to create more functions.
# These will have similar parameters with different variables.

# Password validation when adding new password.
def get_valid_password():
    while True:
        valid_password = input("Enter a new password: ").strip()
        if not valid_password:
            print("Error: password cannot be empty. Please try again.")
        elif len(valid_password) < 4:
            print("Error: password must be at least 4 characters long."
                  " Please try again.")
        elif ' ' in valid_password:
            print("Error: password cannot contain spaces. Please try again.")
        else:
            print(f"Password '{valid_password}' is valid!")
            return valid_password

# Login functionality.
def login():
    """
    Handles user login by validating the username and password against the 
    'user.txt' file.
    Ensures the file exists and handles incorrect credentials.
    """
    try:
        # Attempt to open the user file.
        with open('user.txt', 'r') as file: # Opens the file for reading.
        # Creates username and password from document user.txt as dictionary.
            users = {line.split(', ')[0]: 
                     line.split(', ')[1].strip() for line in file.readlines()}
    except FileNotFoundError:
        # Handles the case where the file does not exist.
        print("Error: The file 'user.txt' was not found."
              " Please ensure it exists in the program directory.")
        sys.exit()  # Terminates the program immediately.

    while True:
        # Request for user inputs.
        username = input("Enter your username (case sensitive): ").strip()
        password = input("Enter your password (case sensitive): ").strip()

# This statement tries to match user input with the list from the dictionary.
# The username and password must match correctly in order to proceed.  
        if username in users and users[username] == password:
            print("Login successful!")
            return username
        # Statement that provides error message for incorrect credentials.
        else:
            print("Invalid username or password. Please try again.")

# Register User.
def register_user():
    with open('user.txt', 'r') as file:
        users = {line.split(', ')[0]: 
                 line.split(', ')[1].strip() for line in file.readlines()}
    
    # Checks and validates that user has entered a valid username.
    new_username = get_valid_username()
    # Checks to see if username is already in use.
    while new_username in users:
        print("Username already exists. Try another one.")
        new_username = get_valid_username()
    # User will be directed back to get correct username.
    
    # Checks and validates that user has entered a valid passed.
    new_password = get_valid_password()
    # Requests password be re-entered for confirmation.
    confirm_password = input("Confirm your password: ")
    
    # Ensures that passwords entered match in order for user to be added. 
    while new_password != confirm_password:
        # Error message displayed for passwords not matching.
        print("Passwords do not match. Please try again.")
        new_password = get_valid_password()
        confirm_password = input("Confirm your password: ")
    # User will be directed back to get correct password.
    
    with open('user.txt', 'a') as file:
        file.write(f"\n{new_username}, {new_password}")
    print("User registered successfully!")

# This function validates that tasks be assigned to existing users from list.
def valid_assigned_user():
# Load the list of users from user.txt for validation
    with open('user.txt', 'r') as file:
        valid_users = [line.split(', ')[0].
                       strip() for line in file.readlines()]
    
    while True:
        # Request a username input.
        assignee = input("Enter username of the person to assign task to: ")
        # If username does not match provides an error message.
        if assignee not in valid_users:
                    print(f"Error: '{assignee}' is not a valid username."
                          " Please choose from the following users:")
                    # Display a list of valid users.
                    print(", ".join(valid_users))
        else:
            print(f"You have chosen {assignee} for your task.")
            return assignee

# Function that gets a valid title for task.
def get_valid_title():
    while True:
        valid_title = input("Enter the title of the task: ").strip()
        if not valid_title:
            print("Error: task title cannot be empty. Please try again.")
        elif len(valid_title) < 5:
            print("Error: task title must be at least 5 characters long."
                  " Please try again.")
        elif ',' in valid_title:
            print("Error: description cannot contain commas."
                  " Please try again.")
        else:
            print(f"Task title '{valid_title}' is valid!")
            return valid_title

# Function that gets a valid description for task.
def get_valid_description():
    while True:
        valid_description = input("Enter the description of task: ").strip()
        if not valid_description:
            print("Error: description cannot be empty. Please try again.")
        elif len(valid_description) < 5:
            print("Error: description must be at least 5 characters long."
                  " Please try again.")
        elif ',' in valid_description:
            print("Error: description cannot contain commas."
                  " Please try again.")
        else:
            print(f"Task title '{valid_description}' is valid!")
            return valid_description

# This function validates user input for task due date.
def get_valid_date():
    while True:
        # Request user input for date in specified format.
        input_date = input("Enter a due date for the task"
                           " (eg. 21 Nov 2024): ").strip()
        
        # Ensures that input is not empty.
        if not input_date:
            # Will only proceed with a valid input.
            print("Input cannot be empty. Please enter a valid date.")
            continue
        try:
            # Tries to convert the input to a date object.
            valid_date = datetime.datetime.strptime(input_date, "%d %b %Y")
            # If successful, returns the formatted date.
            return valid_date.strftime("%d %b %Y")
        except ValueError:
            print("Invalid date format."
                  " Please use the format DD MMM YYYY (e.g., 21 Nov 2024).")

# Add task function.
def add_task():
    """
    Reads tasks from the 'tasks.txt' file and displays them in a user-friendly 
    format.
    Skips empty or invalid lines to avoid errors.
    """
    try:
        # File opened for writing, file created if it does not exist.
        with open('tasks.txt', 'a') as file:
            # Gets valid assigned user for task.
            assigned_user = valid_assigned_user()
            # Gets valid title for task.
            title = get_valid_title()
            # Gets valid description for task.
            description = get_valid_description()
            # Gets valid due date for task.
            due_date = get_valid_date()
            # Task assigned date becomes the current date at present.
            assigned_date = datetime.datetime.now().strftime("%d %b %Y")
            # Successful task creation defaults completion as "No".
            completed = "No"

            # Writes the information obtained above to tasks.txt file. 
            file.write(f"\n{assigned_user}, {title}, {description},"
                       f" {assigned_date}, {due_date}, {completed}")
            # Message created confirming task has been created.
            print("Task added successfully!")

    # Error message displayed if file cannot be found.
    except FileNotFoundError:
        print("Error: The file 'tasks.txt' was not found."
              " Please ensure it exists in the program directory.")

# View all tasks function.
def view_all_tasks():
    """
    Reads tasks from the 'tasks.txt' file and displays them in a user-friendly 
    format.
    Skips empty or invalid lines to avoid errors.
    """
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()    # Read all lines into a list.

        # Iterate through each line in the file.
        for i, task in enumerate(tasks, 1):
        # Skip empty lines or lines with insufficient data.
        # Strip whitespace and split the line by ", " to extract task details.
            task_data = task.strip().split(", ")

            # Check if the line has enough data, in this case 6 fields.
            if len(task_data) < 6:
            # Display error message and skip invalid or incomplete lines.
                print(f"Skipping invalid task data on line {i}: {task}")
                continue

            # Access and display each part of the task data.
            print(f"***Task {i}***")    # Task number in list.
            print(f"Title:          {task_data[1]}")    # Title of the task.
            print(f"Assigned to:    {task_data[0]}")    # Assigned username.
            print(f"Assigned Date:  {task_data[3]}")    # Task Assigned date.
            print(f"Due Date:       {task_data[4]}")    # Task due date.
            print(f"Completed:      {task_data[5]}")    # Completion status.
            print(f"Description:    {task_data[2]}")    # Task description.
            print()

    except FileNotFoundError:
        print("Error: The file 'tasks.txt' was not found."
              " Please ensure it exists in the program directory.")

# View my tasks function with username as an argument.
def view_my_tasks(username):
    """
    Displays tasks assigned to the current user logged-in.
    Reads tasks from 'tasks.txt' and filters only those assigned to the given 
    username.
    Handles missing or invalid task lines.
    """
    try:
    # Open tasks.txt file in read mode
        with open('tasks.txt', 'r') as file:
            # Read all lines from the file into a list.
            tasks = file.readlines()
        
        # Initialize a list to store tasks for the current user.
        user_tasks = []

        # Iterate through each line in the file.
        for i, task in enumerate(tasks, 1):
            # Split the line into parts and validate the structure.
            task_data = task.strip().split(", ")

            if len(task_data) < 6:
                # Skip and display invalid or incomplete lines.
                print(f"Skipping invalid task on line {i}: {task.strip()}")
                continue

            # Check if the task is assigned to the current user.
            if task_data[0] == username:
                # Add valid tasks to the user's task list.
                user_tasks.append(task_data)

                # Access and display each part of the task data.
                print(f"***Task {i}***")
                print(f"Title:            {task_data[1]}")
                print(f"Assigned to:      {task_data[0]}")
                print(f"Assigned Date:    {task_data[3]}")
                print(f"Due Date:         {task_data[4]}")
                print(f"Completed:        {task_data[5]}")
                print(f"Description:      {task_data[2]}")
                print()
        
        # If no tasks are assigned to the user, print a message.
        if not user_tasks:
            print("No tasks assigned to you.")

    except FileNotFoundError:
        print("Error: The file 'tasks.txt' was not found."
              " Please ensure it exists in the program directory.")

# Display statistics function for admin.
def display_statistics():
    """
    Displays the total number of valid users and valid tasks.
    Validates that:
    - Each line in 'user.txt' contains exactly 2 fields (username, password).
    - Each line in 'tasks.txt' contains exactly 6 fields (task details).
    Handles missing files.
    """
    try:
        # Open user.txt to count the total number of valid users.
        with open('user.txt', 'r') as file:
            lines = file.readlines()   # Read all lines from the file.
            valid_users = 0 # Counter for valid users.

            # Validate each line in the file.
            for i, line in enumerate(lines, 1):
                # Split the line into fields.
                user_data = line.strip().split(", ")
                # Ensure the line has exactly 2 fields.
                if len(user_data) == 2:
                    valid_users += 1    # Count the line if valid.
                else:
                    # Displays message for invalid lines.
                    print(f"Skipping invalid user on line {i}: {line.strip()}")

    except FileNotFoundError:
        # Handle the case where 'user.txt' is missing
        print("Error: 'user.txt' file not found."
              " Unable to display user statistics.")
        return  # Exit the function.

    try:
        # Open tasks.txt to count the total number of valid tasks.
        with open('tasks.txt', 'r') as file:
            lines = file.readlines()   # Read all lines from the file.
            valid_tasks = 0  # Counter for valid tasks

            # Validate each line in the file.
            for i, line in enumerate(lines, 1):
                # Split the line into fields.
                task_data = line.strip().split(", ")
                if len(task_data) == 6: # Ensure the line has exactly 6 fields.
                    valid_tasks += 1    # Count the line if valid.
                else:
                    # Displays message about invalid lines.
                    print(f"Skipping invalid task on line {i}: {line.strip()}")

    except FileNotFoundError:
        # Handle the case where 'tasks.txt' is missing
        print("Error: 'tasks.txt' file not found."
              " Unable to display task statistics.")
        return  # Exit the function.

    # Display the statistics to the admin.
    print("Statistics:")
    # Display the total number of valid users.
    print(f"Total Valid Users: {valid_users}")
    # Display the total number of valid tasks.
    print(f"Total Valid Tasks: {valid_tasks}")

# Main Function
def main():
    # Call function in order to get valid user login.
    username = login()
    while True:
        # Options displayed if user is admin.
        if username == "admin":
            print("\nPlease select an option:")
            print("r - Register a new user (admin only)")
            print("ds - Display statistics (admin only)")
            print("a - Add a task")
            print("va - View all tasks")
            print("vm - View my tasks")
            print("e - Exit")
        # Options displayed if user is not the admin.
        else:
            print("\nPlease select an option:")
            print("a - Add a task")
            print("va - View all tasks")
            print("vm - View my tasks")
            print("e - Exit")
        
        # Requested input converted to lowercase and trailing spaces removed.
        option = input("Enter your choice: ").strip().lower()
        
        # Calls function to register a new user.
        if option == 'r' and username == 'admin':
            register_user()
        # Restricts non-admin user from accessing option.
        elif option == 'r':
            print("Only admin can register new users.")
        # Calls function to add a task.
        elif option == 'a':
            add_task()
        # Calls function to view all tasks.
        elif option == 'va':
            view_all_tasks()
        # Calls function to view the current users tasks. 
        elif option == 'vm':
            view_my_tasks(username)
        # Calls function to display statistics.
        elif option == 'ds' and username == 'admin':
            display_statistics()
        elif option == 'ds':
        # Restricts non-admin user from accessing option.
            print("Only admin can view statistics.")
        # Exits the program.
        elif option == 'e':
            print("Exiting the program. Goodbye!")
            break
        # Error message displayed for invalid option.
        else:
            print("Invalid choice. Please try again.")

# Statement created to always bring user back to the main function.
if __name__ == "__main__":
    main()
