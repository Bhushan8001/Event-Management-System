from tkinter import*
from tkinter.tix import IMAGETEXT
from tkinter import ttk,messagebox
import sqlite3

class candidateClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Event Management System | Developed by Group A5")
        self.root.config(bg="white")
        self.root.focus_force()
        ##################################

        # ALL VARIABLES ############

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_candidate_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_year=StringVar()
        




        ## search Frame ##

        SearchFrame=LabelFrame(self.root,text="Search Candidate",font=("goudy old Style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        ## options ##

        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("time new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=440,y=9,width=150,height=30)

        ## title ##
        title= Label(self.root,text="Candidate Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)


        #############  CONTENT   ############
        ###########    row1    ###########
        lbl_candidateid= Label(self.root,text="Candidate ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender= Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact= Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)


        txt_candidateid= Entry(self.root,textvariable=self.var_candidate_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("time new roman",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)

        txt_contact= Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)


        ########## row2 ###########
        lbl_name= Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob= Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_doj= Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=190)

        txt_name= Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob= Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_doj= Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)

        ############# row3   #########
        lbl_email= Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_pass= Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_utype= Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=230)

        txt_email= Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        txt_pass= Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Candidate"),state='readonly',justify=CENTER,font=("time new roman",15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)


        ############### row 4 ######
        lbl_address= Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_year= Label(self.root,text="Year",font=("goudy old style",15),bg="white").place(x=500,y=270)
        
        self.txt_address= Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_year= Entry(self.root,textvariable=self.var_year,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)



        ######### button #######
        
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=350,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=350,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=350,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=350,width=110,height=28)


        ##### Tree View #####
        ##### Candidate Detailes #####

        cand_frame=Frame(self.root,bd=3,relief=RIDGE)
        cand_frame.place(x=0,y=400,relwidth=1,height=150)

        scrolly=Scrollbar(cand_frame,orient=VERTICAL)
        scrollx=Scrollbar(cand_frame,orient=HORIZONTAL)

        self.CandidateTable=ttk.Treeview(cand_frame,columns=("cid","name","email","gender","contact","dob","doj","pass","utype","address","year"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CandidateTable.xview)
        scrolly.config(command=self.CandidateTable.yview)

        self.CandidateTable.heading("cid",text="C ID")
        self.CandidateTable.heading("name",text="Name")
        self.CandidateTable.heading("email",text="Email")
        self.CandidateTable.heading("gender",text="Gender")
        self.CandidateTable.heading("contact",text="Contact")
        self.CandidateTable.heading("dob",text="D.O.B")
        self.CandidateTable.heading("doj",text="D.O.J")
        self.CandidateTable.heading("pass",text="Password")
        self.CandidateTable.heading("utype",text="User type")
        self.CandidateTable.heading("address",text="Address")
        self.CandidateTable.heading("year",text="year")

        self.CandidateTable["show"]="headings"

        self.CandidateTable.column("cid",width=90)
        self.CandidateTable.column("name",width=100)
        self.CandidateTable.column("email",width=100)
        self.CandidateTable.column("gender",width=100)
        self.CandidateTable.column("contact",width=100)
        self.CandidateTable.column("dob",width=100)
        self.CandidateTable.column("doj",width=100)
        self.CandidateTable.column("pass",width=100)
        self.CandidateTable.column("utype",width=100)
        self.CandidateTable.column("address",width=100)
        self.CandidateTable.column("year",width=100)
        self.CandidateTable.pack(fill=BOTH,expand=1)
        self.CandidateTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()


#############################################################################################

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_candidate_id.get()=="":
                messagebox.showerror("Error","Candidate ID Must be Required",parent=self.root)
            else:
                cur.execute("select * from candidate where cid=?",(self.var_candidate_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Candidate ID already assigned ,try different",parent=self.root)    
                else:
                    cur.execute("Insert into candidate (cid,name,email,gender,contact,dob,doj,pass,utype,address,year)values(?,?,?,?,?,?,?,?,?,?,?)",(
                                      
                                      self.var_candidate_id.get(),
                                      self.var_name.get(),
                                      self.var_email.get(),
                                      self.var_gender.get(),
                                      self.var_contact.get(),
                                      
                                      self.var_dob.get(),
                                      self.var_doj.get(),
                                      
                                      self.var_pass.get(),
                                      self.var_utype.get(),
                                      self.txt_address.get('1.0',END),
                                      self.var_year.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Candidate Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from candidate")
            rows=cur.fetchall()
            self.CandidateTable.delete(*self.CandidateTable.get_children())
            for row in rows:
                self.CandidateTable.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    
        

    def get_data(self,ev):
        f=self.CandidateTable.focus()
        content=(self.CandidateTable.item(f))
        row=content['values']
        #print(row)
        self.var_candidate_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
                                      
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
                                      
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])

        self.var_year.set(row[11])


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_candidate_id.get()=="":
                messagebox.showerror("Error","Candidate ID Must be Required",parent=self.root)
            else:
                cur.execute("select * from candidate where cid=?",(self.var_candidate_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Candidate ID",parent=self.root)    
                else:
                    cur.execute("Update candidate set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,year=? where cid=?",(
                    
                    
                                      
                                      
                                      self.var_name.get(),
                                      self.var_email.get(),
                                      self.var_gender.get(),
                                      self.var_contact.get(),
                                      
                                      self.var_dob.get(),
                                      self.var_doj.get(),
                                      
                                      self.var_pass.get(),
                                      self.var_utype.get(),
                                      self.txt_address.get('1.0',END),
                                      self.var_year.get(),
                                      self.var_candidate_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Candidate Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    



    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_candidate_id.get()=="":
                messagebox.showerror("Error","Candidate ID Must be Required",parent=self.root)
            else:
                cur.execute("select * from candidate where cid=?",(self.var_candidate_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Candidate ID",parent=self.root)    
                else:
                    op=messagebox.askyesno("confirm","Do you Really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from candidate where cid=?",(self.var_candidate_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Candidate Deleated Successfully",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)      


    def clear(self):
        self.var_candidate_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
                                      
        self.var_dob.set("")
        self.var_doj.set("")
                                      
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0',END)
        

        self.var_year.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()


    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select * from candidate where" +self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                   self.CandidateTable.delete(*self.CandidateTable.get_children())
                   for row in rows:
                      self.CandidateTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No reccord found",parent=self.root)      
 

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    











if __name__=="__main__":
    root=Tk()
    obj=candidateClass(root)
    root.mainloop()



