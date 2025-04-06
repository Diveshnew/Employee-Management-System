# Employee Management System

A desktop-based Employee Management System built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) and MySQL. This project demonstrates a GUI application that provides basic CRUD (Create, Read, Update, Delete) operations along with search functionality. The project is divided into separate modules for the login screen, employee management, and database operations.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Login:**  
  A login screen built with CustomTkinter that verifies credentials before granting access to the system.

- **Employee Management:**  
  Add, update, delete, and search employee records through a user-friendly interface.

- **Database Integration:**  
  Uses MySQL via PyMySQL to store and manage employee data, including automatic creation of the database and table if they do not exist.

- **Responsive GUI:**  
  Modern UI design using CustomTkinter and Tkinter widgets for a smooth user experience.

## Requirements

Before you begin, ensure you have met the following requirements:

- **Python 3.x** installed on your machine.
- **MySQL Server** installed and running.
- A MySQL user with appropriate privileges (the current code uses `root` with a password in `database.py`).
- Required Python packages:
  - `pymysql`
  - `customtkinter`
  - `Pillow`
  
You can install the required packages using pip:

```bash
pip install pymysql customtkinter Pillow
```

## Installation

1. **Clone the Repository:**

   Open your terminal (or command prompt) and run:

   ```bash
   git clone https://github.com/Diveshnew/Employee-Management-System.git
   cd employee-management-system
   ```

2. **Setup MySQL:**

   - Ensure your MySQL server is running.
   - Update the connection parameters in `database.py` if necessary (e.g., host, user, password).

3. **Run the Application:**

   Start by running the login page:

   ```bash
   python login.py
   ```

   After a successful login, the Employee Management System window will open.

## Usage

1. **Login:**
   - Enter the username and password on the login screen. (Note: The current login uses hardcoded credentials ```username:divesh and password:1234``` in `login.py`.)

2. **Employee Management:**
   - **Add Employee:** Fill in the employee details and click **Add Employee**.
   - **Update Employee:** Select an employee from the table, update the details, and click **Update Employee**.
   - **Delete Employee:** Select an employee and click **Delete Employee**.
   - **Delete All:** Click **Delete All** to remove all records (a confirmation prompt will appear).
   - **Search:** Use the search functionality by selecting a field and entering a search term, then click **Search**.
  
3. **Database Setup:**
   - The application automatically creates the `employee_data` database and `data` table when you run it, if they do not exist.
  
4. **Problem You May Face**
   - While running this Code for the first time, You may face an Error. So, to resolve that first Open your ``` MYSQL Command Line Client``` and Put ```Your SQL password``` then again run this code. This Should resolve your issue.

## Project Structure

```
employee-management-system/
│
├── login.py         # Login screen implementation using CustomTkinter.
├── ems.py           # Main Employee Management System GUI with CRUD and search functionality.
├── database.py      # Database connection and CRUD operations using PyMySQL.
├── bg.jpg           # Background image used in the EMS.
├── cover.png        # Image used in the login screen.
├── README.md        # This file.
└── .gitignore       # Git ignore file to exclude unnecessary files.
```

## Contributing

Contributions are welcome! If you have suggestions, bug fixes, or improvements, please fork the repository and create a pull request. Make sure your code follows the project's style guidelines. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).
