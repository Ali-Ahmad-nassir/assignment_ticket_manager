import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from CoreService import CoreService
from User import User
from picke_data import *
import random
import string
from datetime import datetime


# A mock service for testing (uses CoreService later)
mock_service = CoreService()


class TicketBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adventure Land Theme Park Ticket Booking")
        self.root.geometry("800x600")

        # Main frame to switch between scenes
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        # Header and footer
        self.create_header()

        # Initialize the first scene (login/registration)
        self.show_login_scene()

        self.create_footer()

        self.logged_user = None

    def isSuper(self):
        if self.logged_user.get_username() == "superuser":
            return True
        return False

    def create_footer(self):
        """Creates the footer at the top of the window."""
        footer_frame = tk.Frame(self.root, bg="gray", bd=2, relief="ridge")
        footer_frame.pack(side="bottom", fill="x")

        footer = tk.Label(footer_frame, text="© 2024 Adventure Land. All rights reserved.",
                        bg="gray", fg="white", font=("Arial", 10), pady=5)
        footer.pack()


    def create_header(self):
        """Creates the header at the top of the main frame."""
        # Ensure the header is placed at the top of the main_frame
        header_frame = tk.Frame(self.main_frame, bg="blue", bd=2, relief="ridge")
        header_frame.pack(side="top", fill="x", pady=10)  # Add padding to create space between content

        header = tk.Label(header_frame, text="Adventure Land Theme Park", bg="blue", fg="white",
                        font=("Arial", 26, "bold"), pady=10)
        header.pack()



    def show_login_scene(self):
        # Clear current frame
        
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.create_header()
        # Create a styled frame for the form
        form_frame = tk.Frame(self.main_frame, bd=2, relief="ridge", padx=20, pady=20, bg="#f2f2f2")
        form_frame.pack(side="top",pady=20, padx=20)

        # Login Title
        tk.Label(form_frame, text="Login", font=("Arial", 20, "bold"), bg="#f2f2f2").grid(row=0, column=0, columnspan=2, pady=10)

        # Username
        tk.Label(form_frame, text="Username:", font=("Arial", 12), bg="#f2f2f2").grid(row=1, column=0, sticky="e", pady=5)
        username_entry = tk.Entry(form_frame, width=30, relief="sunken", bd=2)
        username_entry.grid(row=1, column=1, pady=5)

        # Password
        tk.Label(form_frame, text="Password:", font=("Arial", 12), bg="#f2f2f2").grid(row=2, column=0, sticky="e", pady=5)
        password_entry = tk.Entry(form_frame, show="*", width=30, relief="sunken", bd=2)
        password_entry.grid(row=2, column=1, pady=5)

        # Login Button
        login_btn = tk.Button(form_frame, text="Login", font=("Arial", 12), bg="#007BFF", fg="white", relief="raised",
                            command=lambda: self.handle_login(username_entry.get(), password_entry.get()))
        login_btn.grid(row=3, column=0, columnspan=2, pady=15, ipadx=10)

        # Register Button
        register_btn = tk.Button(form_frame, text="Register", font=("Arial", 10), bg="#CCCCCC", fg="black",
                                command=self.show_registration_scene)
        register_btn.grid(row=4, column=0, columnspan=2, pady=5)

       

   
    def show_registration_scene(self):
        # Clear current frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.create_header()

        # Create a styled frame for the form
        form_frame = tk.Frame(self.main_frame, bd=2, relief="ridge", padx=20, pady=20, bg="#f2f2f2")
        form_frame.pack(pady=20, padx=20)

        # Registration Title
        tk.Label(form_frame, text="Register", font=("Arial", 20, "bold"), bg="#f2f2f2").grid(row=0, column=0, columnspan=2, pady=10)

        # Username
        tk.Label(form_frame, text="Username:", font=("Arial", 12), bg="#f2f2f2").grid(row=1, column=0, sticky="e", pady=5)
        username_entry = tk.Entry(form_frame, width=30, relief="sunken", bd=2)
        username_entry.grid(row=1, column=1, pady=5)

        # Password
        tk.Label(form_frame, text="Password:", font=("Arial", 12), bg="#f2f2f2").grid(row=2, column=0, sticky="e", pady=5)
        password_entry = tk.Entry(form_frame, show="*", width=30, relief="sunken", bd=2)
        password_entry.grid(row=2, column=1, pady=5)

        # Email
        tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#f2f2f2").grid(row=3, column=0, sticky="e", pady=5)
        email_entry = tk.Entry(form_frame, width=30, relief="sunken", bd=2)
        email_entry.grid(row=3, column=1, pady=5)

        # Phone Number
        tk.Label(form_frame, text="Phone Number:", font=("Arial", 12), bg="#f2f2f2").grid(row=4, column=0, sticky="e", pady=5)
        phone_entry = tk.Entry(form_frame, width=30, relief="sunken", bd=2)
        phone_entry.grid(row=4, column=1, pady=5)

        # Register Button
        register_btn = tk.Button(form_frame, text="Register", font=("Arial", 12), bg="#007BFF", fg="white",
                                relief="raised", command=lambda: self.handle_registration(
                                    username_entry.get(), password_entry.get(), email_entry.get(), phone_entry.get()))
        register_btn.grid(row=5, column=0, columnspan=2, pady=15, ipadx=10)

        # Back to Login Button
        back_btn = tk.Button(form_frame, text="Back to Login", font=("Arial", 10), bg="#CCCCCC", fg="black",
                            command=self.show_login_scene)
        back_btn.grid(row=6, column=0, columnspan=2, pady=5)


    def handle_login(self, username, password):
        # Simulate a login check (replace with CoreService logic)
        user = mock_service.find_user(username)
        if user and user.get_password() == password:
            messagebox.showinfo("Login Successful", f"Welcome back, {username}!")
            self.logged_user = user
            self.show_user_dashboard(user)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def handle_registration(self, username, password, email, phone_number):
        # Simulate user registration (replace with CoreService logic)
        if mock_service.find_user(username):
            messagebox.showerror("Registration Failed", "Username already exists.")
        else:
            new_user = User(username, password, email, phone_number)
            mock_service.add_user(new_user)
            messagebox.showinfo("Registration Successful", "Account created successfully!")
            self.show_login_scene()

    def show_user_dashboard(self, user=None):
        # Clear current frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.create_header()

        # Logged-in user
        user = self.logged_user

        # Centered Frame
        dashboard_frame = tk.Frame(self.main_frame, bd=2, relief="solid", padx=20, pady=20, bg="#f4f4f4")
        dashboard_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center in the main frame

        # Welcome Message
        tk.Label(
            dashboard_frame,
            text=f"Welcome, {user.get_username()}!",
            font=("Arial", 18, "bold"),
            bg="#f4f4f4",
            fg="#333333"
        ).pack(pady=(0, 20))  # Extra top padding

        # Styled Buttons
        button_style = {
            "font": ("Arial", 12, "bold"),
            "relief": "raised",
            "bd": 3,
            "bg": "#007BFF",  # Blue
            "fg": "white",
            "activebackground": "#0056b3",  # Darker blue
            "activeforeground": "white",
            "width": 20,
            "height": 2,
        }
        if self.isSuper():
            # Purchase Tickets Button
            tk.Button(
                dashboard_frame,
                text="View Clients Tickets",
                command=self.show_ticket_purchase_scene,
                **button_style
            ).pack(pady=10)

            # View Purchase History Button
            tk.Button(
                dashboard_frame,
                text="View Our Clients",
                command=self.show_user_management_scene,
                **button_style
            ).pack(pady=10)

            # Logout Button
            tk.Button(
                dashboard_frame,
                text="Logout",
                command=self.show_login_scene,
                **button_style
            ).pack(pady=10)
        else:
            # Purchase Tickets Button
            tk.Button(
                dashboard_frame,
                text="Purchase Tickets",
                command=self.show_ticket_purchase_scene,
                **button_style
            ).pack(pady=10)

            # View Purchase History Button
            tk.Button(
                dashboard_frame,
                text="View Purchase History",
                command=self.show_purchase_history_scene,
                **button_style
            ).pack(pady=10)

            # Logout Button
            tk.Button(
                dashboard_frame,
                text="Logout",
                command=self.show_login_scene,
                **button_style
            ).pack(pady=10)



    def show_ticket_purchase_scene(self):
        # Clear current frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.create_header()

        # Ticket Purchase Scene Title
        tk.Label(self.main_frame, text="Available Tickets", font=("Arial", 18)).pack(pady=20)

        # Create Treeview
        self.tree = ttk.Treeview(self.main_frame, columns=("Ticket ID", "Type", "Price", "Validity", "Discount", "Limitations", "Action"), show="headings")
        
        # Define column headings
        self.tree.heading("Ticket ID", text="Ticket ID")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Price", text="Price (DHS)")
        self.tree.heading("Validity", text="Validity")
        self.tree.heading("Discount", text="Discount (%)")
        self.tree.heading("Limitations", text="Limitations")
        self.tree.heading("Action", text="Action")

        # Set column widths for better readability
        self.tree.column("Ticket ID", width=100)
        self.tree.column("Type", width=150)
        self.tree.column("Price", width=100)
        self.tree.column("Validity", width=100)
        self.tree.column("Discount", width=100)
        self.tree.column("Limitations", width=200)
        self.tree.column("Action", width=100)

        # Add tickets to the treeview
        for ticket in mock_service.tickets:
            self.tree.insert("", "end", values=(ticket.get_ticket_id(), ticket.get_ticket_type(), f"{ticket.get_price()} DHS", ticket.get_validity(), f"{ticket.get_discount()}%", ticket.get_limitations(), "Purchase"))

        # Create Purchase Button
        self.tree.bind("<Double-1>", self.on_ticket_purchase)

        # Pack the treeview to fill the window
        self.tree.pack(fill="both", expand=True, pady=10)

        # Back to Dashboard Button
        tk.Button(self.main_frame, text="Back to Dashboard", command=self.show_user_dashboard).pack(pady=20)

    def generate_random_order_id(self):
        # Generate a random number (e.g., between 100 and 999 for the numeric part)
        numeric_part = random.randint(100, 999)
        
        # Generate a random 4-letter uppercase string (alphabetic part)
        alphabetic_part = ''.join(random.choices(string.ascii_uppercase, k=4))
        
        # Combine both parts to create the order ID (e.g., R175TRETE)
        order_id = f"R{numeric_part}{alphabetic_part}"
    
        return order_id
    
    def show_purchase_history_scene(self):
        # Clear current frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.create_header()

        # Purchase History Scene Title
        tk.Label(self.main_frame, text="Purchase History", font=("Arial", 18)).pack(pady=20)

        # Create Treeview
        self.history_tree = ttk.Treeview(self.main_frame, columns=("Order ID", "Ticket Type", "Quantity", "Total Price", "Purchase Date"), show="headings")
        
        # Define column headings
        self.history_tree.heading("Order ID", text="Order ID")
        self.history_tree.heading("Ticket Type", text="Ticket Type")
        self.history_tree.heading("Quantity", text="Quantity")
        self.history_tree.heading("Total Price", text="Total Price (DHS)")
        self.history_tree.heading("Purchase Date", text="Purchase Date")

        # Set column widths for better readability
        self.history_tree.column("Order ID", width=100)
        self.history_tree.column("Ticket Type", width=150)
        self.history_tree.column("Quantity", width=100)
        self.history_tree.column("Total Price", width=150)
        self.history_tree.column("Purchase Date", width=200)

        # Add purchase history data to the treeview
        for purchase in mock_service.purchase_orders:
            if self.isSuper():
                
                self.history_tree.insert(
                    "", "end",
                    values=(
                        purchase.get_order_id(),
                        purchase.get_ticket().get_ticket_type(),
                        purchase.get_quantity(),
                        f"{purchase.get_total_price():.2f} DHS",
                        purchase.get_purchase_date().strftime("%Y-%m-%d %H:%M:%S"),
                    )
                )

            else:
                if purchase.get_user() == self.logged_user:  # Filter by logged-in user
                    self.history_tree.insert(
                        "", "end",
                        values=(
                            purchase.get_order_id(),
                            purchase.get_ticket().get_ticket_type(),
                            purchase.get_quantity(),
                            f"{purchase.get_total_price():.2f} DHS",
                            purchase.get_purchase_date().strftime("%Y-%m-%d %H:%M:%S"),
                        )
                    )


        # Bind a click event to the Treeview
        self.history_tree.bind("<Double-1>", self.on_purchase_delete)

        # Pack the treeview to fill the window
        self.history_tree.pack(fill="both", expand=True, pady=10)

        # Back to Dashboard Button
        tk.Button(self.main_frame, text="Back to Dashboard", command=self.show_user_dashboard).pack(pady=20)

    def on_purchase_delete(self, event):
        # Get selected item
        selected_item = self.history_tree.selection()

        if not selected_item:
            return

        # Get Order ID of the selected item
        order_id = self.history_tree.item(selected_item, "values")[0]

        # Confirm Deletion
        confirm = tk.messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete Purchase Order {order_id}?")
        if not confirm:
            return

        # Find and remove the PurchaseOrder object from the service
        for purchase in mock_service.purchase_orders:
            if purchase.get_order_id() == order_id:
                mock_service.purchase_orders.remove(purchase)
                break

        # Remove item from Treeview
        self.history_tree.delete(selected_item)

        
    def on_ticket_purchase(self, event):
        # Get the selected item in the treeview
        item = self.tree.selection()[0]
        ticket_id = self.tree.item(item, "values")[0]  # Get the ticket ID from the selected row

    
        
        # Create a modal window
        def ask_ticket_quantity():
            # Create a new top-level window (modal)
            modal = tk.Toplevel(self.root)
            modal.title("Enter Ticket Quantity")
            
            # Label to ask for the quantity
            tk.Label(modal, text=f"Enter the number of tickets for {ticket_id}").pack(pady=10)

            ticket = mock_service.find_ticket(ticket_id)
            
            # Entry widget for the user to input the number of tickets
            quantity_entry = tk.Entry(modal)
            quantity_entry.pack(pady=10)
            
            # Function to handle the purchase action
            def purchase_tickets():
                try:
                    quantity = int(quantity_entry.get())  # Convert the entry value to an integer
                    if quantity <= 0:
                        raise ValueError("Please enter a positive number")
                    print(f"Purchasing {quantity} tickets for Ticket ID: {ticket_id}")

                    OI = self.generate_random_order_id()
                    po = PurchaseOrder(OI, self.logged_user, ticket, datetime.now() , 5)
                    mock_service.add_purchase_order(po)
                    messagebox.showinfo("Purchase of ticket "+str(ticket_id)+" Successful", "Process Completed you can View History!")
                    modal.destroy()  # Close the modal after purchase
                except ValueError as e:
                    tk.Label(modal, text=f"Error: {e}", fg="red").pack()  # Show an error message if invalid input

            # Button to confirm the purchase
            tk.Button(modal, text="Confirm Purchase", command=purchase_tickets).pack(pady=10)
            
            # Button to cancel and close the modal
            tk.Button(modal, text="Cancel", command=modal.destroy).pack(pady=5)

        ask_ticket_quantity()  # Open the modal for ticket quantity input


    def show_user_management_scene(self):
        # Clear current frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.create_header()

        # User Management Scene Title
        tk.Label(self.main_frame, text="User Management", font=("Arial", 18)).pack(pady=20)

        # Create Treeview
        self.user_tree = ttk.Treeview(
            self.main_frame,
            columns=("Username", "Email", "Phone Number", "Action"),
            show="headings"
        )

        # Define column headings
        self.user_tree.heading("Username", text="Username")
        self.user_tree.heading("Email", text="Email")
        self.user_tree.heading("Phone Number", text="Phone Number")
        self.user_tree.heading("Action", text="Action")

        # Set column widths for better readability
        self.user_tree.column("Username", width=150)
        self.user_tree.column("Email", width=200)
        self.user_tree.column("Phone Number", width=150)
        self.user_tree.column("Action", width=100)

        # Add users to the treeview
        for user in mock_service.users:
            self.user_tree.insert(
                "", "end",
                values=(user.get_username(), user.get_email(), user.get_phone_number(), "Delete")
            )

        # Bind a delete action to the rows
        self.user_tree.bind("<Double-1>", self.on_user_delete)

        # Pack the treeview to fill the window
        self.user_tree.pack(fill="both", expand=True, pady=10)

        # Back to Dashboard Button
        tk.Button(
            self.main_frame,
            text="Back to Dashboard",
            command=self.show_user_dashboard,
            font=("Arial", 12, "bold"),
            relief="raised",
            bd=2,
            bg="#007BFF",
            fg="white",
            activebackground="#0056b3",
            activeforeground="white"
        ).pack(pady=20)

    def on_user_delete(self, event):
        # Get the selected item
        selected_item = self.user_tree.selection()[0]  # Get selected row ID
        username = self.user_tree.item(selected_item)["values"][0]  # Extract username

        # Confirmation dialog
        confirm = tk.messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete user '{username}'?"
        )

        if confirm:
            if mock_service.delete_user(username):  # Delete user from the service
                self.user_tree.delete(selected_item)  # Remove row from Treeview
                tk.messagebox.showinfo("Success", f"User '{username}' has been deleted.")
            else:
                tk.messagebox.showerror("Error", f"User '{username}' could not be deleted.")



# Run the application
root = tk.Tk()
initialize_mock_service(mock_service)
mock_service.print_data()
app = TicketBookingApp(root)
root.mainloop()
