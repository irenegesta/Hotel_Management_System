from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("700x500+400+150")

        # Registration frame
        frame = Frame(self.root, bg="white")
        frame.place(x=20, y=20, width=650, height=450)

        # Title
        title = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="lightsteelblue", bg="white")
        title.place(x=20, y=20)

        # Username
        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="black")
        username_lbl.place(x=20, y=80)
        self.txt_username = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_username.place(x=20, y=110, width=250)

        # Email
        email_lbl = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email_lbl.place(x=320, y=80)
        self.txt_email = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_email.place(x=320, y=110, width=250)

        # Password
        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        password_lbl.place(x=20, y=160)
        self.txt_password = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txt_password.place(x=20, y=190, width=250)

        # Confirm Password
        confirm_password_lbl = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_password_lbl.place(x=320, y=160)
        self.txt_confirm_password = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txt_confirm_password.place(x=320, y=190, width=250)

        # Security Question
        security_Q_lbl = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q_lbl.place(x=20, y=240)
        self.combo_security_Q = ttk.Combobox(frame, font=("times new roman", 15), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Pet Name")
        self.combo_security_Q.place(x=20, y=270, width=250)
        self.combo_security_Q.current(0)

        # Security Answer
        security_A_lbl = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A_lbl.place(x=320, y=240)
        self.txt_security_A = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_security_A.place(x=320, y=270, width=250)

        # Register Button
        btn_register = Button(frame, text="Register", command=self.register_data, font=("times new roman", 15, "bold"), bg="red", fg="white")
        btn_register.place(x=250, y=320, width=150)

    def register_data(self):
        if self.txt_username.get() == "" or self.txt_email.get() == "" or self.txt_password.get() == "" or self.txt_confirm_password.get() == "" or self.combo_security_Q.get() == "Select" or self.txt_security_A.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_password.get() != self.txt_confirm_password.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sir_Levi@7", database="management")
                my_cursor = conn.cursor()
                query = "INSERT INTO register (username, email, password, securityQ, securityA) VALUES (%s, %s, %s, %s, %s)"
                value = (self.txt_username.get(), self.txt_email.get(), self.txt_password.get(), self.combo_security_Q.get(), self.txt_security_A.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                self.root.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error due to: {str(err)}", parent=self.root)
   
