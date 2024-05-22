from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from hotel import HotelManagementSystem
from register import Register

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Irene\Desktop\Hotel_Management_System\images\hotel1.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="red")
        frame.place(x=610, y=170, width=340, height=430)

        img1 = Image.open(r"C:\Users\Irene\Desktop\Hotel_Management_System\images\hotel1.jpg")
        img1 = img1.resize((90, 90), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(image=self.photoimage1, bg="red", borderwidth=0)
        lbl_img1.place(x=730, y=170, width=90, height=90)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="red")
        get_str.place(x=95, y=85)

        username_lbl = Label(frame, text="Username", font=("times new roman", 12, "bold"), fg="white", bg="red")
        username_lbl.place(x=70, y=125)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=150, width=270)

        password_lbl = Label(frame, text="Password", font=("times new roman", 12, "bold"), fg="white", bg="red")
        password_lbl.place(x=70, y=195)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=220, width=270)

        btn_login = Button(frame, text="Login", borderwidth=3, relief=RAISED, command=self.login,
                           font=("arial", 12, "bold"), bg="lightsteelblue", fg="red", width=9)
        btn_login.place(x=110, y=270, width=120, height=35)

        register_btn = Button(frame, text="New User Register", command=self.register_window,
                              font=("arial", 12, "bold"))
        register_btn.place(x=15, y=320, width=160)

        forgot_pass_btn = Button(frame, text="Forget Password", command=self.forgot_password_window,
                                 font=("arial", 12, "bold"))
        forgot_pass_btn.place(x=19, y=360, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "admin" and self.txtpass.get() == "admin":
            messagebox.showinfo("Success", "Welcome to Hotel Management System")
            self.open_hotel_management_system()
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sir_Levi@7", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM register WHERE username=%s AND password=%s", (
                    self.txtuser.get(),
                    self.txtpass.get()
                ))
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username & Password")
                else:
                    self.open_hotel_management_system()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error due to: {str(err)}")
            finally:
                if conn.is_connected():
                    conn.close()

    def open_hotel_management_system(self):
        self.new_window = Toplevel(self.root)
        self.app = HotelManagementSystem(self.new_window)

    def forgot_password_window(self):
        if not hasattr(self, 'forgot_window'):
            self.forgot_window = Toplevel(self.root)
            self.forgot_window.title("Forgot Password")
            self.forgot_window.geometry("400x450+400+150")

            lbl_title = Label(self.forgot_window, text="Reset Password", font=("times new roman", 20, "bold"), fg="red")
            lbl_title.pack(side=TOP, fill=X)

            security_Q_lbl = Label(self.forgot_window, text="Select Security Question", font=("times new roman", 15, "bold"))
            security_Q_lbl.place(x=70, y=80)

            self.combo_security_Q = ttk.Combobox(self.forgot_window, font=("times new roman", 15, "bold"), state="readonly")
            self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Pet Name")
            self.combo_security_Q.place(x=70, y=110, width=250)
            self.combo_security_Q.current(0)

            security_A_lbl = Label(self.forgot_window, text="Security Answer", font=("times new roman", 15, "bold"))
            security_A_lbl.place(x=70, y=150)

            self.txt_security = ttk.Entry(self.forgot_window, font=("times new roman", 15, "bold"))
            self.txt_security.place(x=70, y=180, width=250)

            email_lbl = Label(self.forgot_window, text="Email", font=("times new roman", 15, "bold"))
            email_lbl.place(x=70, y=220)

            self.txt_email = ttk.Entry(self.forgot_window, font=("times new roman", 15, "bold"))
            self.txt_email.place(x=70, y=250, width=250)

            new_password_lbl = Label(self.forgot_window, text="New Password", font=("times new roman", 15, "bold"))
            new_password_lbl.place(x=70, y=290)

            self.txt_new_password = ttk.Entry(self.forgot_window, font=("times new roman", 15, "bold"), show="*")
            self.txt_new_password.place(x=70, y=320, width=250)

            reset_btn = Button(self.forgot_window, text="Reset", command=self.reset_pass, font=("times new roman", 15, "bold"), bg="lightsteelblue", fg="red")
            reset_btn.place(x=140, y=360)

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select" or self.txt_security.get() == "" or self.txt_email.get() == "" or self.txt_new_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.forgot_window)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sir_Levi@7", database="management")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
                value = (self.txt_email.get(), self.combo_security_Q.get(), self.txt_security.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please provide correct Security Answer or Email", parent=self.forgot_window)
                else:
                    query = "UPDATE register SET password=%s WHERE email=%s"
                    value = (self.txt_new_password.get(), self.txt_email.get())
                    my_cursor.execute(query, value)
                    conn.commit()
                    messagebox.showinfo("Success", "Your password has been reset successfully", parent=self.forgot_window)
                    self.forgot_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error due to: {str(err)}", parent=self.forgot_window)
            finally:
                if conn.is_connected():
                    conn.close()



if __name__ == "__main__":
    main()
