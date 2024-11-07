from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"E:\hotel_management_system\images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"E:\hotel_management_system\images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=170,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #username label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=190,width=270)

        #password label
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=235)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=270,width=270)

        #username icon
        img2=Image.open(r"E:\hotel_management_system\images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=329,width=25,height=25)

        #password icon
        img3=Image.open(r"E:\hotel_management_system\images\lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=409,width=25,height=25)

        #Login Btn
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red",cursor="hand2")
        loginbtn.place(x=110,y=320,width=120,height=40)

        #register
        registerbtn=Button(frame,text="New User Register ",command=self.rigister_window,font=("times new roman",11,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="black",activebackground="black",cursor="hand2")
        registerbtn.place(x=14,y=365,width=160)

        #forgot password
        loginbtn=Button(frame,text="Forgot Password ?",command=self.forgot_password_window,font=("times new roman",11,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="black",activebackground="black",cursor="hand2")
        loginbtn.place(x=11,y=390,width=160)

    def rigister_window(self):
        self.new_window=Toplevel()
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "Vikas" and self.txtpass.get() == "Pass@123":
            messagebox.showinfo("Success", "Welcome User..!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Pass@123",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                self.txtuser.get(),
                                                                self.txtpass.get()
                                                                    ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
#=======================Reset Password=====================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter Security Answer",parent=self.root)
        elif self.txt_new_pass.get()=="":
            messagebox.showerror("Error","Please Enter New Password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Pass@123",database="management")
            my_cursor=conn.cursor()
            query1=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value1=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query1,value1)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer",parent=self.root)
            else:
                query2=("update register set password=%s where email=%s")
                value2=(self.txt_new_pass.get(),self.txtuser.get())
                my_cursor.execute(query2,value2)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset, Please login with new password",parent=self.root)



#======================Forget Password=====================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter Email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Pass@123",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+200")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",15,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                # Security Question
                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,font=("times new roman", 13, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place ?", "Your Girlfriend Name ?", "Your Pet Name ?")
                self.combo_security_Q.place(x=50, y=110)
                self.combo_security_Q.current(0)

                # Security Answer
                security_A = Label(self.root2,text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2,font=("times new roman", 13))
                self.txt_security.place(x=50, y=180, width=180)

                #new password
                new_password = Label(self.root2,text="Enter New Password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_new_pass = ttk.Entry(self.root2,font=("times new roman", 13))
                self.txt_new_pass.place(x=50, y=250, width=180)


                #btn
                btn=Button(self.root2,text=" Reset ",command=self.reset_pass,font=("times new roman", 15, "bold"),fg="white", bg="green",cursor="hand2")
                btn.place(x=110,y=290)

        
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
        b2=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b2.place(x=350,y=455,width=180)

        #==========Function Declaration=============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_contact.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
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


    def return_login(self):
        self.root.destroy()




class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #==========1st image================
        img1=Image.open(r"E:\hotel_management_system\images\taj.jpg")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)


        #============logo===========
        img2=Image.open(r"E:\hotel_management_system\images\logo.jpg")
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #============TITLE===========   
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",   font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #==============main frame==============
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #===========menu==========
        lbl_menu=Label(main_frame,text="MENU", font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #===========btn frame===========
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)

        # report_btn=Button(btn_frame,text="REPORT",font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand2")
        # report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)

        #================RIGHT side image============
        img3=Image.open(r"E:\hotel_management_system\images\aasads.jpg")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)

        #===========down images=================
        img4=Image.open(r"E:\hotel_management_system\images\slide3.jpg")
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)

        ####=======
        img5=Image.open(r"E:\hotel_management_system\images\khana.jpg")
        img5=img5.resize((230,190),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)


    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()

            





if __name__ == '__main__':
    main()