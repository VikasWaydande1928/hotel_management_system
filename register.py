from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()

        # bg img
        self.bg = ImageTk.PhotoImage(file=r"E:\hotel_management_system\images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # left img
        self.bg1 = ImageTk.PhotoImage(file=r"E:\hotel_management_system\images\thought-good-morning-messages-LoveSove.jpg")
        lbl_bg1 = Label(self.root, image=self.bg1)
        lbl_bg1.place(x=50, y=100, width=470, height=550)

        # Main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=900, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 25, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # Labels and entries
        # first name
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        # last name
        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=350, y=100)

        l_name_entry = ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman", 15, "bold"))
        l_name_entry.place(x=370, y=130, width=250)

        # Contact
        contact = Label(frame , text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        # Email
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # Security question
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place ?", "Your Girlfriend Name ?", "Your Pet Name ?")
        self.combo_security_Q.place(x=50, y=270)
        self.combo_security_Q.current(0)

        # Security Answer
        security_A = Label(frame,text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # Password
        pswrd = Label(frame,text="Create Password", font=("times new roman", 15, "bold"), bg="white")
        pswrd.place(x=50, y=320)

        l_name_entry = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        l_name_entry.place(x=50, y=350, width=250)

        # Confirm Password
        confirm_pswrd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswrd.place(x=370, y=310)

        self.confirm_pswrd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.confirm_pswrd.place(x=370, y=340, width=250)

        # CheckButton
        Checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0, bg="white")
        Checkbtn.place(x=50, y=390)

                #===Register Button==========
        img=Image.open(r"E:\hotel_management_system\images\register-now-button1.jpg")
        img=img.resize((180,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=50,y=455,width=180)

        img1=Image.open(r"E:\hotel_management_system\images\loginpng.png")
        img1=img1.resize((180,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b2.place(x=350,y=455,width=180)

        #==========Function Declaration=============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_contact.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password doesn't Match")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms & conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Pass@123",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                        self.var_fname.get(),
                                                                        self.var_lname.get(),
                                                                        self.var_contact.get(),
                                                                        self.var_email.get(),
                                                                        self.var_securityQ.get(),
                                                                        self.var_securityA.get(),
                                                                        self.var_pass.get()
                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Regesterd Successfully")







if __name__ == '__main__':

   root = Tk()
   obj = Register(root)
   root.mainloop()