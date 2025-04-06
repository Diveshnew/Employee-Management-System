import pymysql
from tkinter import messagebox

def connect_database():
    """
    Connect to MySQL, create the employee_data database and data table if they don't exist.
    Uses global variables for connection and cursor.
    """
    global conn, mycursor
    try:
        conn = pymysql.connect(host='localhost', user='root', password='YourPassword')
        mycursor = conn.cursor()
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Something went wrong: {e}\nPlease open MySQL app before running again.')
        return

    # Create database and table if not exists
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            Id VARCHAR(20),
            Name VARCHAR(50),
            Phone VARCHAR(15),
            Role VARCHAR(50),
            Gender VARCHAR(20),
            Salary DECIMAL(10,2)
        )
    ''')
    conn.commit()

def insert(id, name, phone, role, gender, salary):
    """Insert a new employee record into the data table."""
    mycursor.execute(
        'INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s)',
        (id, name, phone, role, gender, salary)
    )
    conn.commit()

def id_exists(id):
    """Check if an employee with the given id already exists."""
    # Passing parameters as a tuple (even for single parameters)
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id = %s', (id,))
    result = mycursor.fetchone()
    return result[0] > 0

def fetch_employees():
    """Fetch all employee records from the data table."""
    mycursor.execute('SELECT * FROM data')
    result = mycursor.fetchall()
    return result

def update(id, new_name, new_phone, new_role, new_gender, new_salary):
    """Update an existing employee record with new values."""
    mycursor.execute(
        'UPDATE data SET name = %s, phone = %s, role = %s, gender = %s, salary = %s WHERE id = %s',
        (new_name, new_phone, new_role, new_gender, new_salary, id)
    )
    conn.commit()

def delete(id):
    """Delete an employee record based on the provided id."""
    mycursor.execute('DELETE FROM data WHERE id = %s', (id,))
    conn.commit()

def search(option, value):
    """
    Search for employee records based on a specified column and value.
    Ensure that `option` is one of the allowed column names to prevent SQL injection.
    """
    allowed_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
    if option not in allowed_options:
        raise ValueError("Invalid search option")
    # Note: Only 'value' is parameterized; 'option' must be validated
    mycursor.execute(f'SELECT * FROM data WHERE {option} = %s', (value,))
    result = mycursor.fetchall()
    return result

def deleteall_records():
    """Delete all employee records from the data table."""
    mycursor.execute('TRUNCATE TABLE data')
    conn.commit()

# Connect to the database when the module is imported.
connect_database()
