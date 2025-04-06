from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkImage, CTkFrame, CTkComboBox
from PIL import Image
from tkinter import ttk, messagebox
import database

class EmployeeManagementSystem:
    """
    A class that encapsulates the UI and functionality for the Employee Management System.
    """

    def __init__(self, master):
        self.master = master
        self.master.geometry('1000x580+100+100')
        self.master.resizable(False, False)
        self.master.title('Employee Management System')
        self.master.configure(fg_color='#161C30')
        self.setup_ui()

    def setup_ui(self):
        """Set up the GUI elements."""
        # Logo setup
        self.logo = CTkImage(Image.open('bg.jpg'), size=(1000, 158))
        self.logo_label = CTkLabel(self.master, image=self.logo, text="")
        self.logo_label.grid(row=0, column=0, columnspan=2)

        # Left frame (data input)
        self.left_frame = CTkFrame(self.master, fg_color='#161C30')
        self.left_frame.grid(row=1, column=0)
        self.create_left_widgets()

        # Right frame (search and table)
        self.right_frame = CTkFrame(self.master)
        self.right_frame.grid(row=1, column=1)
        self.create_right_widgets()

        # Buttons frame
        self.button_frame = CTkFrame(self.master, fg_color='#161C30')
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        self.create_button_widgets()

        # Load initial data into the treeview
        self.treeview_data()

        # Bind selection event for treeview
        self.master.bind("<ButtonRelease>", self.selection)

    def create_left_widgets(self):
        """Create widgets for the left frame."""
        # Id Field
        self.id_label = CTkLabel(self.left_frame, text='Id', font=('arial', 18, 'bold'), text_color='white')
        self.id_label.grid(row=0, column=0, padx=20, pady=15, sticky='w')
        self.id_entry = CTkEntry(self.left_frame, font=('arial', 15, 'bold'), width=180)
        self.id_entry.grid(row=0, column=1)

        # Name Field
        self.name_label = CTkLabel(self.left_frame, text='Name', font=('arial', 18, 'bold'), text_color='white')
        self.name_label.grid(row=1, column=0, padx=20, pady=15, sticky='w')
        self.name_entry = CTkEntry(self.left_frame, font=('arial', 15, 'bold'), width=180)
        self.name_entry.grid(row=1, column=1)

        # Phone Field
        self.phone_label = CTkLabel(self.left_frame, text='Phone', font=('arial', 18, 'bold'), text_color='white')
        self.phone_label.grid(row=2, column=0, padx=20, pady=15, sticky='w')
        self.phone_entry = CTkEntry(self.left_frame, font=('arial', 15, 'bold'), width=180)
        self.phone_entry.grid(row=2, column=1)

        # Role Field
        self.role_label = CTkLabel(self.left_frame, text='Role', font=('arial', 18, 'bold'), text_color='white')
        self.role_label.grid(row=3, column=0, padx=20, pady=15, sticky='w')
        role_options = ['Web Developer', 'Cloud Architect', 'Technical Writer', 'Network Engineer',
                        'DevOps Engineer', 'Data Scientist', 'Business Analyst', 'IT Consultant', 'UX/UI Designer']
        self.role_box = CTkComboBox(self.left_frame, values=role_options, width=180,
                                    font=('arial', 15, 'bold'), state='readonly')
        self.role_box.grid(row=3, column=1)
        self.role_box.set(role_options[0])

        # Gender Field
        self.gender_label = CTkLabel(self.left_frame, text='Gender', font=('arial', 18, 'bold'), text_color='white')
        self.gender_label.grid(row=4, column=0, padx=20, pady=15, sticky='w')
        gender_options = ['Male', 'Female']
        self.gender_box = CTkComboBox(self.left_frame, values=gender_options, width=180,
                                      font=('arial', 15, 'bold'), state='readonly')
        self.gender_box.grid(row=4, column=1)
        self.gender_box.set('Male')

        # Salary Field
        self.salary_label = CTkLabel(self.left_frame, text='Salary', font=('arial', 18, 'bold'), text_color='white')
        self.salary_label.grid(row=5, column=0, padx=20, pady=15, sticky='w')
        self.salary_entry = CTkEntry(self.left_frame, font=('arial', 15, 'bold'), width=180)
        self.salary_entry.grid(row=5, column=1)

    def create_right_widgets(self):
        """Create widgets for the right frame."""
        search_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
        self.search_box = CTkComboBox(self.right_frame, values=search_options, state='readonly')
        self.search_box.grid(row=0, column=0)
        self.search_box.set('Search By')

        self.search_entry = CTkEntry(self.right_frame)
        self.search_entry.grid(row=0, column=1)

        self.search_button = CTkButton(self.right_frame, text='Search', width=100, command=self.search_employee)
        self.search_button.grid(row=0, column=2)

        self.showall_button = CTkButton(self.right_frame, text='Show All', width=100, command=self.show_all)
        self.showall_button.grid(row=0, column=3, pady=5)

        self.tree = ttk.Treeview(self.right_frame, height=13)
        self.tree.grid(row=1, column=0, columnspan=4)
        self.tree['columns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')

        for col in ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.config(show='headings')
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('arial', 16, 'bold'))
        style.configure('Treeview', font=('arial', 10, 'bold'), rowheight=20, background='#161C30', foreground='white')

        self.scrollbar = ttk.Scrollbar(self.right_frame, orient='vertical', command=self.tree.yview)
        self.scrollbar.grid(row=1, column=4, sticky='ns')
        self.tree.config(yscrollcommand=self.scrollbar.set)

    def create_button_widgets(self):
        """Create action buttons in the bottom frame."""
        self.new_button = CTkButton(self.button_frame, text='New Employee', font=('arial', 15, 'bold'),
                                    width=160, corner_radius=15, command=lambda: self.clear(True))
        self.new_button.grid(row=0, column=0, pady=5)

        self.add_button = CTkButton(self.button_frame, text='Add Employee', font=('arial', 15, 'bold'),
                                    width=160, corner_radius=15, command=self.add_employee)
        self.add_button.grid(row=0, column=1, pady=5, padx=5)

        self.update_button = CTkButton(self.button_frame, text='Update Employee', font=('arial', 15, 'bold'),
                                       width=160, corner_radius=15, command=self.update_employee)
        self.update_button.grid(row=0, column=2, pady=5, padx=5)

        self.delete_button = CTkButton(self.button_frame, text='Delete Employee', font=('arial', 15, 'bold'),
                                       width=160, corner_radius=15, command=self.delete_employee)
        self.delete_button.grid(row=0, column=3, pady=5, padx=5)

        self.deleteall_button = CTkButton(self.button_frame, text='Delete All', font=('arial', 15, 'bold'),
                                          width=160, corner_radius=15, command=self.delete_all)
        self.deleteall_button.grid(row=0, column=4, pady=5, padx=5)

    # --- Functionality Methods ---

    def delete_all(self):
        """Delete all records after user confirmation."""
        result = messagebox.askyesno('Confirm', 'Do you really want to delete all the records?')
        if result:
            database.deleteall_records()
            self.treeview_data()

    def show_all(self):
        """Show all employee records and reset search fields."""
        self.treeview_data()
        self.search_entry.delete(0, 'end')
        self.search_box.set('Search By')

    def search_employee(self):
        """Search for employees based on the selected criteria and search input."""
        if self.search_entry.get() == '':
            messagebox.showerror('Error', 'Enter value to search')
        elif self.search_box.get() == 'Search By':
            messagebox.showerror('Error', 'Please select an option')
        else:
            searched_data = database.search(self.search_box.get(), self.search_entry.get())
            self.tree.delete(*self.tree.get_children())
            for employee in searched_data:
                self.tree.insert('', 'end', values=employee)

    def delete_employee(self):
        """Delete the selected employee record."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror('Error', 'Select data to delete')
        else:
            database.delete(self.id_entry.get())
            self.treeview_data()
            self.clear()
            messagebox.showinfo('Success', 'Data is deleted')

    def update_employee(self):
        """Update the selected employee record with new values."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror('Error', 'Select data to update')
        else:
            database.update(self.id_entry.get(), self.name_entry.get(), self.phone_entry.get(),
                            self.role_box.get(), self.gender_box.get(), self.salary_entry.get())
            self.treeview_data()
            self.clear()
            messagebox.showinfo('Success', 'Data is updated')

    def selection(self, event):
        """Populate form fields when a row in the treeview is selected."""
        selected_item = self.tree.selection()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear()
            self.id_entry.insert(0, row[0])
            self.name_entry.insert(0, row[1])
            self.phone_entry.insert(0, row[2])
            self.role_box.set(row[3])
            self.gender_box.set(row[4])
            self.salary_entry.insert(0, row[5])

    def clear(self, value=False):
        """Clear the form fields and optionally remove treeview selection."""
        if value:
            self.tree.selection_remove(self.tree.focus())
        self.id_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.role_box.set('Web Developer')
        self.gender_box.set('Male')
        self.salary_entry.delete(0, 'end')

    def treeview_data(self):
        """Fetch employee data from the database and display it in the treeview."""
        employees = database.fetch_employees()
        self.tree.delete(*self.tree.get_children())
        for employee in employees:
            self.tree.insert('', 'end', values=employee)

    def add_employee(self):
        """Add a new employee record after validation."""
        if (self.id_entry.get() == '' or self.phone_entry.get() == '' or
                self.name_entry.get() == '' or self.salary_entry.get() == ''):
            messagebox.showerror('Error', 'All fields are required')
        elif database.id_exists(self.id_entry.get()):
            messagebox.showerror('Error', 'Id already exists')
        elif not self.id_entry.get().startswith('EMP'):
            messagebox.showerror('Error', 'Invalid ID format. Use "EMP" followed by a number (e.g., "EMP1").')
        else:
            database.insert(self.id_entry.get(), self.name_entry.get(), self.phone_entry.get(),
                            self.role_box.get(), self.gender_box.get(), self.salary_entry.get())
            self.treeview_data()
            self.clear()
            messagebox.showinfo('Success', 'Data is added')

if __name__ == '__main__':
    root = CTk()
    app = EmployeeManagementSystem(root)
    root.mainloop()
