from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkImage, CTkFrame
from PIL import Image
from tkinter import messagebox

class LoginApp:
    """
    A login application using customtkinter that splits the window into a login form (left)
    and an image display (right) for a modern and responsive layout.
    """
    def __init__(self, master):
        self.master = master
        self.master.title("Login Page")
        self.master.geometry("1000x478")
        self.master.resizable(0, 0)
        
        # Create a main container frame with some padding.
        self.container = CTkFrame(self.master)
        self.container.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Setup the left and right frames.
        self.setup_frames()

    def setup_frames(self):
        """Create and place left (login form) and right (image) frames in the container."""
        # Left frame for the login form.
        self.left_frame = CTkFrame(self.container, width=350, corner_radius=10)
        self.left_frame.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="nsew")
        
        # Right frame for displaying the image.
        self.right_frame = CTkFrame(self.container, width=550, corner_radius=10)
        self.right_frame.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="nsew")
        
        # Configure grid weights to ensure the frames resize properly.
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        
        # Setup the login form and image within their frames.
        self.setup_login_form()
        self.setup_image()

    def setup_login_form(self):
        """Setup the login form with a heading, username & password fields, and a login button."""
        # Heading label for the login form.
        self.heading_label = CTkLabel(
            self.left_frame,
            text="Employee Management System",
            font=("Helvetica Neue", 20, "bold"),
            text_color="#6665F1"
        )
        self.heading_label.pack(pady=(100, 20))
        
        # Username entry field.
        self.username_entry = CTkEntry(
            self.left_frame,
            placeholder_text="Enter Your Username",
            width=300
        )
        self.username_entry.pack(pady=5)
        
        # Password entry field with masked input.
        self.password_entry = CTkEntry(
            self.left_frame,
            placeholder_text="Enter Your Password",
            width=300,
            show="*"
        )
        self.password_entry.pack(pady=5)
        
        # Login button that calls the login method.
        self.login_button = CTkButton(
            self.left_frame,
            text="Login",
            cursor="hand2",
            command=self.login,
            width=300,
            fg_color="#6665F1"
        )
        self.login_button.pack(pady=10)

    def setup_image(self):
        """Load and display the image in the right frame."""
        try:
            # Open and resize the image using PIL and CTkImage.
            self.image = CTkImage(Image.open("cover.png"), size=(550, 430))
        except Exception as e:
            messagebox.showerror("Error", f"Image failed to load: {e}")
            self.master.destroy()
            return
        
        # Label to hold and display the image.
        self.image_label = CTkLabel(self.right_frame, image=self.image, text="")
        self.image_label.pack(expand=True, fill="both", padx=10, pady=10)

    def login(self):
        """
        Check the provided credentials.
        In a real-world application, validate against a secure database or service.
        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if both fields are filled.
        if not username or not password:
            messagebox.showerror("Error", "All fields are required.")
            return

        # Simple hardcoded check for demonstration purposes.
        if username == "divesh" and password == "1234":
            messagebox.showinfo("Success", "Login is successful")
            self.master.destroy()  # Close the login window.
            try:
                import ems  # Import the employee management system module.
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load the EMS module: {e}")
        else:
            messagebox.showerror("Error", "Wrong Credentials")

if __name__ == "__main__":
    # Create the main window and start the login application.
    root = CTk()
    app = LoginApp(root)
    root.mainloop()
