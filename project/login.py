from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib
import time
class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | Developed by A5")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.otp=' '




        ###### images ######
        self.phone_image=ImageTk.PhotoImage(file="image/phone.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)

        ##### Login_Frame ######
        self.candidate_id=StringVar()
        self.password=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)


        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Candidate ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        

        text_candidate_id=Entry(login_frame,textvariable=self.candidate_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        text_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded Mt Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)


        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)


        btn_froget=Button(login_frame,text="Forget Password?",command=self.forget_window,font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)


        #### Frame2 @###

        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)

        lbl_reg=Label(register_frame,text="Event Management System", font=("times new roman",13),bg="white").place(x=0,y=20,relwidth=1)
        

        # ###### Animation Images #############
        self.im1=ImageTk.PhotoImage(file="image/im1.png")
        self.im2=ImageTk.PhotoImage(file="image/im2.png")
        self.im3=ImageTk.PhotoImage(file="image/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)


        self.animate()
        






    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)    



    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        
        try:
            if self.candidate_id.get()=="" or self.password.get()=="":
                messagebox.showerror('error',"All field are required",parent=self.root)
            else:    
                cur.execute("select utype from candidate where cid=? AND pass=?",(self.candidate_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror('error',"Invalid username/password",parent=self.root)
                else:     
                    print(user)
                    if user[0]=="Admin": 
                        self.root.destroy()
                        os.system("python enent.py")   
                    else:
                        self.root.destroy()
                        os.system("python result.py") 


        except Exception as ex:

            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)  


    def forget_window(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        
        try:
            if self.candidate_id.get()=="":
                messagebox.showerror('Error',"Candidate ID must be required",parent=self.root)   
            else:
                cur.execute("select email from candidate where cid=?",(self.candidate_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror('error',"Invalid Candidate ID,try again",parent=self.root)
                else: 
                    ########## forget Window ###########
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()
                    
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror("Error","connection Error,try again",parent=self.root)
                    else:


                         #call send_send_email_function
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title('RESET PASSWORD')
                        self.forget_win.geometry('400x500+500+100')
                        self.forget_win.focus_force()

                        title=Label(self.forget_win,text='RESET PASSWORD',font=('goudy old style',15,'bold'),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                        lbl_reset=Label(self.forget_win,text="Enter OTP sent on registered Email",font=("times new roman",15)).place(x=20,y=60)
                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg = 'lightyellow').place(x=20,y=100,width=250,height=30)
                        self.btn_reset=Button(self.forget_win,text="SUBMIT",command=self.validate_otp,font=("times new roman",15),bg='lightblue')
                        self.btn_reset.place(x=280,y=100,width=100,height=30)

                        lbl_new_pass=Label(self.forget_win,text="New Password",font=("times new roman",15)).place(x=20,y=160)
                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg = 'lightyellow').place(x=20,y=190,width=250,height=30)
                
                        lbl_c_pass=Label(self.forget_win,text="Confirm Password",font=("times new roman",15)).place(x=20,y=225)
                        txt_c_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg = 'lightyellow').place(x=20,y=255,width=250,height=30)

                        self.btn_update=Button(self.forget_win,text="UPDATE",command=self.update_password,state=DISABLED,font=("times new roman",15),bg='lightblue')
                        self.btn_update.place(x=150,y=300,width=100,height=30)
                   
                    
        
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 



    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror("Error","Password is Required",parent=self.forget_win)
        elif self.var_new_pass.get()!= self.var_conf_pass.get():
            messagebox.showerror("Error","Password & confirm password should be must be same",parent=self.forget_win)
        else:
            con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        
        try:
            cur.execute("Update candidate SET pass=? where cid=?",(self.var_new_pass.get(),self.candidate_id.get()) )
            con.commit()
            messagebox.showinfo("Success","Password Updated successfully",parent=self.forget_win)
            self.forget_win.destroy()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 
    




    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP, Try again",parent=self.forget_win)    
            




    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)

        self.otp=int(time.strftime('%H%M%S'))+int(time.strftime('%S'))
        
        subj='EMS-reset password otp'
        msg=f'Dear Sir/Madam, \n\n Your Reset OPT is {str(self.otp)}.\n\nwith Regards,\nEms Team'
        msg="subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'





root=Tk()
obj=Login_system(root)
root,mainloop()    


