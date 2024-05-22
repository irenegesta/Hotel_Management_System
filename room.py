from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # ============= variables ==================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        self.var_noofperson=StringVar()


        # =============== title ==================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS", font=("times new roman",18, "bold"),bg="lightsteelblue", fg="red",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0, width=1295,height=50)


        # =============== logo ======================
        img2=Image.open(r"C:\Users\Irene\Desktop\Hotel_Management_System\images\logohotel.png")
        img2=img2.resize((100,45),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=45)

        # ================ label Frame ================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room booking Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        

        # =============== labels and entries ===========
        # Customer Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=0,pady=5)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=20)
        enty_contact.grid(row=0,column=1,sticky=W)

        #fetch data button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",9,"bold"),bg="lightsteelblue",fg="red",width=8)
        btnFetchData.place(x=347,y=4)

        #check_in date
        check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check In Date:",padx=0,pady=5)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        #check_out date
        lbl_check_out=Label(labelframeleft,font=("arial",12,"bold"),text="Check Out Date:",padx=0,pady=5)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        txt_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txt_check_out.grid(row=2,column=1)

        #Room Type
        label_RoomType=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=0,pady=5)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Sir_Levi@7",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27, state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Available room
        lbl_RoomAvailable=Label(labelframeleft,font=("arial",12,"bold"),text="Available Room:",padx=0,pady=5)
        lbl_RoomAvailable.grid(row=4,column=0,sticky=W)
        #txt_RoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        #txt_RoomAvailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="Sir_Levi@7",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27, state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)


        #Meal type
        lbl_Meal=Label(labelframeleft,font=("arial",12,"bold"),text="Meal",padx=0,pady=5)
        lbl_Meal.grid(row=5,column=0,sticky=W)

        combo_MealType=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12,"bold"),width=27, state="readonly")
        combo_MealType["value"]=("Breakfast","Lunch","Dinner")
        combo_MealType.current(0)
        combo_MealType.grid(row=5,column=1)

        #Number of Days
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="No of Days:",padx=0,pady=5)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        #Paid Tax
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="Paid Tax:",padx=0,pady=5)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=7,column=1)

        #Sub Total
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="Sub Total:",padx=0,pady=5)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=8,column=1)

        #Total cost
        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Total Cost:",padx=0,pady=5)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        #No. of Person
        lblNoOfPerson=Label(labelframeleft,font=("arial",12,"bold"),text="No. of Person:",padx=0,pady=5)
        lblNoOfPerson.grid(row=10,column=0,sticky=W)
        txtNoOfPerson=ttk.Entry(labelframeleft,textvariable=self.var_noofperson,font=("arial",13,"bold"),width=29)
        txtNoOfPerson.grid(row=10,column=1)

        #=============== Bill button ===============
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="lightsteelblue",fg="red",width=10)
        btnBill.grid(row=11,column=0,padx=2,sticky=W)

        # =================== buttons =================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="lightsteelblue",fg="red",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="lightsteelblue",fg="red",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="lightsteelblue",fg="red",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="lightsteelblue",fg="red",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        # =============== Right side image ===============
        img7=Image.open(r"C:\Users\Irene\Desktop\Hotel_Management_System\images\hotel7.png")
        img7=img7.resize((520,300),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        lbling=Label(self.root,image=self.photoimg7,bd=0,relief=RIDGE)
        lbling.place(x=760,y=55,width=520,height=300)

        # ============== table frame search system =============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()

        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24, state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="lightsteelblue",fg="red",width=9)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="lightsteelblue",fg="red",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)



         # ============== Show Data Table ================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal",
                                             "noofdays", "NoOfperson"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-In")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No.")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="No. of Days")
        self.room_table.heading("NoOfperson",text="No. of Person")
        
        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
        self.room_table.column("NoOfperson",width=100)

        self.room_table.pack(fill=BOTH,expand=1)


        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # add data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sir_Levi@7",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_noofdays.get(),
                                                                                        self.var_noofperson.get()
                                                                                                
                                                                                 ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong{str(es)}",parent=self.root)


    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sir_Levi@7",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #ger cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6]),
        self.var_noofperson.set(row[7])
    #update function
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Sir_Levi@7",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,Room=%s,meal=%s,noOfdays=%s,NoOfperson=%s where Contact=%s",(
                                                                                                self.var_checkin.get(),
                                                                                                self.var_checkout.get(),
                                                                                                self.var_roomtype.get(),
                                                                                                self.var_roomavailable.get(),
                                                                                                self.var_meal.get(),
                                                                                                self.var_noofdays.get(),
                                                                                                self.var_noofperson.get(),
                                                                                                self.var_contact.get()
                                                                                                
                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

    #delete function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Sir_Levi@7",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset function
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set(""),
        self.var_noofperson.set("")


    # ================ All Data Fetch =====================
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Sir_Levi@7",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()


            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                #name
                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row[0],font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                #gender
                conn=mysql.connector.connect(host="localhost",username="root",password="Sir_Levi@7",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                
                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row[0],font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #email
                conn=mysql.connector.connect(host="localhost",username="root",password="Sir_Levi@7",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                
                lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row[0],font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                #nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="Sir_Levi@7",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                
                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row[0],font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                #Address
                conn=mysql.connector.connect(host="localhost",username="root",password="Sir_Levi@7",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                
                lbladdress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lbladdress.place(x=0,y=120)

                lbl5=Label(showDataframe,text=row[0],font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)

    #search system
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sir_Levi@7",database="management")
        my_cursor=conn.cursor()
        search_by=self.search_var.get()
        search_txt=self.txt_search.get()
        try:
            my_cursor.execute(f"SELECT * FROM room WHERE {search_by} LIKE %s",(f"%{search_txt}%",))
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("",END,values=i)
                conn.commit()
            else:
                messagebox.showinfo("Info","No matching records foound",parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong: {str(es)}",parent=self.root)
        finally:
            conn.close()




    def total(self):
        try:
            inDate = self.var_checkin.get()
            outDate = self.var_checkout.get()
            inDate = datetime.strptime(inDate, "%d/%m/%Y")
            outDate = datetime.strptime(outDate, "%d/%m/%Y")
            no_of_days = abs((outDate - inDate).days)
            self.var_noofdays.set(no_of_days)
            self.var_noofperson.get()
            no_of_persons = int(self.var_noofperson.get())


            meal_cost = 300
            room_cost = 0

            if self.var_roomtype.get() == "Single":
                room_cost = 950
            elif self.var_roomtype.get() == "Double":
                room_cost = 1600
            elif self.var_roomtype.get() == "Luxury":
                room_cost = 2100

            total_room_cost = room_cost * no_of_days * no_of_persons
            total_meal_cost = meal_cost * no_of_days * no_of_persons
            sub_total = total_room_cost + total_meal_cost

            tax = sub_total * 0.09
            total_cost = sub_total + tax

            self.var_paidtax.set("₱" + str("%.2f" % tax))
            self.var_actualtotal.set("₱" + str("%.2f" % sub_total))
            self.var_total.set("₱" + str("%.2f" % total_cost))

        except Exception as e:
            messagebox.showerror("Error", f"Invalid date format. Please enter the date in DD/MM/YYYY format. {str(e)}", parent=self.root)

    







if __name__== "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()



    