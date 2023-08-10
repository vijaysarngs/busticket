import pyqrcode
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
def perform_operations():

    def cancel_operation():
        pass

    def generate_qr_code():
        pass

    def display_ticket():
        pass

    def ticket_calculator():
        pass

    root = tk.Tk()
def insert_passenger_data():
    def submit():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if password != confirm_password:
            error_label.config(text="Passwords do not match!")
            return


        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kutta@123",
            database="vijay"
        )


        cursor = conn.cursor()


        create_table_query = """
        CREATE TABLE IF NOT EXISTS passenger1 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            password VARCHAR(255)
        )
        """
        cursor.execute(create_table_query)


        insert_query = """
        INSERT INTO passenger2 (first_name, last_name, password)
        VALUES (%s, %s, %s)
        """
        data = (first_name, last_name, password)
        cursor.execute(insert_query, data)


        conn.commit()
        conn.close()


        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        confirm_password_entry.delete(0, tk.END)

        error_label.config(text="Data saved successfully!")

        login_choice = tk.messagebox.askyesno("Login", "Do you want to login?")
        if login_choice:
            login()

    def cancel_operation():
        def submit():
            entered_first_name = first_name_entry.get()
            entered_password = password_entry.get()


            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Kutta@123",
                database="vijay"
            )

            cursor = conn.cursor()


            select_query = """
            SELECT * FROM passenger2
            WHERE first_name = %s AND password = %s
            """
            data = (entered_first_name, entered_password)
            cursor.execute(select_query, data)
            result = cursor.fetchone()

            if result:

                delete_query = """
                DELETE FROM passenger2
                WHERE first_name = %s
                """
                cursor.execute(delete_query, (entered_first_name,))
                conn.commit()
                messagebox.showinfo("Cancel", "Operation Cancelled Successfully")
            else:
                messagebox.showinfo("Cancel", "Invalid Credentials")


            conn.close()


        window = tk.Tk()
        window.title("Cancel Operation")
        window.geometry("300x200")


        tk.Label(window, text="First Name:").pack()
        first_name_entry = tk.Entry(window)
        first_name_entry.pack()

        tk.Label(window, text="Password:").pack()
        password_entry = tk.Entry(window, show="*")
        password_entry.pack()

        submit_button = tk.Button(window, text="Submit", command=submit)
        submit_button.pack()

        window.mainloop()


    def generate_qr_code():
        def open_image():
            image.show()

        def generate():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()


            data = f"First Name: {first_name}\nLast Name: {last_name}"

            qr = pyqrcode.create(data)


            qr_path = "qr_code.png"
            qr.png(qr_path, scale=10)


            global photo
            global image
            image = Image.open(qr_path)
            photo = ImageTk.PhotoImage(image)

            qr_label.configure(image=photo)
            qr_label.image = photo


            messagebox.showinfo("Success", "QR code generated successfully!")


        window = tk.Tk()
        window.title("Generate QR Code")


        tk.Label(window, text="First Name:").pack()
        first_name_entry = tk.Entry(window)
        first_name_entry.pack()

        tk.Label(window, text="Last Name:").pack()
        last_name_entry = tk.Entry(window)
        last_name_entry.pack()


        generate_button = tk.Button(window, text="Generate QR Code", command=generate)
        generate_button.pack()


        qr_label = tk.Label(window)
        qr_label.pack()


        open_button = tk.Button(window, text="Open Image", command=open_image)
        open_button.pack()


        window.mainloop()

    generate_qr_code()
    def display_ticket():
        print("Display Ticket operation selected")
    def ticket_calculator():
        def calculate_cost():
            num_tickets = int(num_tickets_entry.get())
            tier = tier_var.get()

            if tier == "Tier 1":
                cost = 100 * num_tickets
            elif tier == "Tier 2":
                cost = 75 * num_tickets
            elif tier == "Tier 3":
                cost = 50 * num_tickets
            else:
                cost = 0

            messagebox.showinfo("Ticket Cost", f"The total cost is: {cost}")

        window = tk.Toplevel()
        window.title("Ticket Generator")

        tk.Label(window, text="Number of Tickets:").pack()
        num_tickets_entry = tk.Entry(window)
        num_tickets_entry.pack()

        tk.Label(window, text="Tier:").pack()
        tier_var = tk.StringVar()
        tier_var.set("Tier 1")
        tier_options = ["Tier 1", "Tier 2", "Tier 3"]
        tier_dropdown = tk.OptionMenu(window, tier_var, *tier_options)
        tier_dropdown.pack()

        calculate_button = tk.Button(window, text="Calculate Cost", command=calculate_cost)
        calculate_button.pack()

    def perform_operations():
        root = tk.Tk()

        def on_button_click(operation):
            root.destroy()
            operation()

        label = tk.Label(root, text="Available Operations:")
        label.pack()

        cancel_button = tk.Button(root, text="Cancel", command=lambda: on_button_click(cancel_operation))
        cancel_button.pack()

        qr_button = tk.Button(root, text="Generate QR Code", command=lambda: on_button_click(generate_qr_code))
        qr_button.pack()

        ticket_button = tk.Button(root, text="Display Ticket", command=lambda: on_button_click(display_ticket))
        ticket_button.pack()

        ticket_generator_button = tk.Button(root, text="Ticket Generator",command=lambda: on_button_click(ticket_calculator))
        ticket_generator_button.pack()
        root.mainloop()
    def login():
        def submit():
            entered_first_name = first_name_entry.get()
            entered_last_name = last_name_entry.get()
            entered_password = password_entry.get()

            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Kutta@123",
                database="vijay"
            )


            cursor = conn.cursor()


            select_query = """
            SELECT * FROM passenger2
            WHERE first_name = %s AND last_name = %s AND password = %s
            """
            data = (entered_first_name, entered_last_name, entered_password)
            cursor.execute(select_query, data)
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Login", "Login Successful")
                perform_operations()
            else:
                messagebox.showinfo("Login", "Login Unsuccessful")


            conn.close()


        window = tk.Tk()
        window.title("Login")
        window.geometry("300x200")

        tk.Label(window, text="First Name:").pack()
        first_name_entry = tk.Entry(window)
        first_name_entry.pack()

        tk.Label(window, text="Last Name:").pack()
        last_name_entry = tk.Entry(window)
        last_name_entry.pack()


        tk.Label(window, text="Password:").pack()
        password_entry = tk.Entry(window, show="*")
        password_entry.pack()

        submit_button = tk.Button(window, text="Submit", command=submit)
        submit_button.pack()


        window.mainloop()


    window = tk.Tk()
    window.title("Passenger Details")
    window.geometry("300x250")


    tk.Label(window, text="First Name:").pack()
    first_name_entry = tk.Entry(window)
    first_name_entry.pack()

    tk.Label(window, text="Last Name:").pack()
    last_name_entry = tk.Entry(window)
    last_name_entry.pack()

    tk.Label(window, text="Password:").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    tk.Label(window, text="Confirm Password:").pack()
    confirm_password_entry = tk.Entry(window, show="*")
    confirm_password_entry.pack()

    # Create the submit button
    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

    # Create error label
    error_label = tk.Label(window, text="")
    error_label.pack()

    # Run the Tkinter event loop
    window.mainloop()


insert_passenger_data()
