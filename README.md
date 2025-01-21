📝 Task Manager Application

A Python-based Task Manager designed to help small businesses manage tasks efficiently. The application supports user authentication, task assignment, task viewing, and basic statistics tracking.

🚀 Features
- User Authentication: Secure login system for multiple users with stored credentials.
- Task Assignment: Assign tasks to team members with a title, description, due date, and completion status.
- View Tasks:
  - View all tasks in the system.
  - View tasks assigned to the logged-in user.
- Statistics: Admin users can view the total number of tasks and registered users.
- User Management: Admin users can register new users.
- Data Validation:
  - Ensures tasks.txt and user.txt files have the correct structure.
  - Skips and reports invalid entries.

🛠️ Technologies Used
- Python: Core programming language.
- File Handling: Uses .txt files (tasks.txt and user.txt) for data storage.
- Datetime Module: For handling task due dates and assignment dates.

🖥️ How to Use
Login
- Upon starting the program, you'll be prompted to log in using your username and password stored in user.txt.

Admin Features
- The admin user (admin) has additional privileges:
  - Register new users.
  - View system statistics (total users and tasks).

Task Management
- Add a new task by specifying the assignee, title, description, and due date.
- View all tasks or only tasks assigned to you.
- Update a task's completion status (e.g., from No to Yes).

🛡️ Error Handling
- Ensures user.txt and tasks.txt files are present. If missing, the program exits with an error message.
- Skips invalid lines in tasks.txt or user.txt and provides warnings for debugging.
