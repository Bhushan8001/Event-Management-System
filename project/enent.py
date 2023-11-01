from tkinter import*
from tkinter.tix import IMAGETEXT
from candidate import candidateClass
from forum import forumClass
from function import functionClass
from result import resultClass
import sqlite3
from tkinter import messagebox
import time
import os
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Event Management System | Developed by A5")
        self.root.config(bg="white")

        ## title ##

        self.icon_title=PhotoImage(file="image/download.png")
        title=Label(self.root,text="Event Management System",image= self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70) 

        # button  #
        btn_logout=Button(self.root,text="LOGOUT",command=self.logout,font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=1100,y=10,height=50,width=150)


        # clock #
        self.lbl_clock=Label(self.root,text="Welcome to Event Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        
        # LEFT Menu #
        LeftMenu= Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=250,height=565)

        self.icon_side=PhotoImage(file="image/side.png")

        lbl_menu=Label(LeftMenu,text="MENU",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)


        ## Button ##
       
        btn_cadidate=Button(LeftMenu,text="CANDIDATE",command=self.candidate,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_forum=Button(LeftMenu,text="FORUM",command=self.forum,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_event=Button(LeftMenu,text="EVENT",command=self.function,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_result=Button(LeftMenu,text="RESULT",command=self.result,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="EXIT",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        ## content ##

        self.lbl_candidate=Label(self.root,text="Total Candidates\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_candidate.place(x=300,y=120,height=150,width=300)

        self.lbl_forum=Label(self.root,text="Total Forums\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_forum.place(x=650,y=120,height=150,width=300)

        self.lbl_event=Label(self.root,text="Events\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_event.place(x=1000,y=120,height=150,width=300)

        self.lbl_result=Label(self.root,text="Results\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_result.place(x=300,y=300,height=150,width=300)


        # footer #
        lbl_footer=Label(self.root,text="EMS- Event Management System | Developed by BHUSHAN\n For Any Problem Contact: 987XXXX01 ",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

        self.update_content()

##############################################################################################################################################################
    

    def candidate(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=candidateClass(self.new_win)

    def forum(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=forumClass(self.new_win)    

    def function(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=functionClass(self.new_win) 

    def result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)      

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        
        try:
            cur.execute("select * from result")
            result=cur.fetchall()
            self.lbl_result.config(text=f'Total Results\n[{str(len(result))}]')

            cur.execute("select * from function")
            function=cur.fetchall()
            self.lbl_event.config(text=f'Total Events\n[{str(len(function))}]')

            cur.execute("select * from forum")
            forum=cur.fetchall()
            self.lbl_forum.config(text=f'Total Forums\n[{str(len(forum))}]')

            cur.execute("select * from candidate")
            candidate=cur.fetchall()
            self.lbl_candidate.config(text=f'Total candidate\n[{str(len(candidate))}]')

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Event Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)





        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)   

    def logout(self):
        self.root.destroy()
        os.system("python login.py")             

           





if __name__=="__main__":
    root = Tk()
    obj=IMS(root)
    root.mainloop()    


   

