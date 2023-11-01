from tkinter import*
from tkinter.tix import IMAGETEXT
from tkinter import ttk,messagebox
import sqlite3

class forumClass:
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

        self.var_forum_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
       
        




        ## search Frame ##

        

        ## options ##

        lbl_search=Label(self.root,text="No.",bg="white",font=("time new roman",15))
        lbl_search.place(x=700,y=80)
        

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=800,y=80,width=160)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=980,y=79,width=100,height=28)

        ## title ##
        title= Label(self.root,text="Forum Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)


        #############  CONTENT   ############
        ###########    row1    ###########
        lbl_forum_invoice= Label(self.root,text="No.",font=("goudy old style",15),bg="white").place(x=50,y=80)

        txt_forum_invoice= Entry(self.root,textvariable=self.var_forum_invoice,font=("goudy old style",15),bg="lightyellow").place(x=180,y=80,width=180)
        

        ########## row2 ###########
        lbl_name= Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=120)
        
        txt_name= Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=120,width=180)
       

        ############# row3   #########
        lbl_contact= Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=160)
    
        txt_contact= Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=180,y=160,width=180)
        


        ############### row 4 ######
        lbl_desc= Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=200)
       
        
        self.txt_desc= Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=200,width=470,height=120)
        


        ######### button #######
        
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)


        ##### Tree View #####
        ##### Candidate Detailes #####

        cand_frame=Frame(self.root,bd=3,relief=RIDGE)
        cand_frame.place(x=700,y=120,width=380,height=370)

        scrolly=Scrollbar(cand_frame,orient=VERTICAL)
        scrollx=Scrollbar(cand_frame,orient=HORIZONTAL)

        self.forumTable=ttk.Treeview(cand_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.forumTable.xview)
        scrolly.config(command=self.forumTable.yview)

        self.forumTable.heading("invoice",text="No")
        self.forumTable.heading("name",text="Name")
        self.forumTable.heading("contact",text="Contact")
        self.forumTable.heading("desc",text="Description")
       

        self.forumTable["show"]="headings"

        self.forumTable.column("invoice",width=90)
        self.forumTable.column("name",width=100)
        self.forumTable.column("contact",width=100)
        self.forumTable.column("desc",width=100)
        
        self.forumTable.pack(fill=BOTH,expand=1)
        self.forumTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()


#############################################################################################

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_forum_invoice.get()=="":
                messagebox.showerror("Error","Invoice must be Required",parent=self.root)
            else:
                cur.execute("select * from forum where invoice=?",(self.var_forum_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice NO. already assigned ,try different",parent=self.root)    
                else:
                    cur.execute("Insert into forum (invoice,name,contact,desc)values(?,?,?,?)",(
                                      
                                      self.var_forum_invoice.get(),
                                      self.var_name.get(),
                                      
                                      self.var_contact.get(),
                                      
                                      
                                      self.txt_desc.get('1.0',END),
                                      
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Forum Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from forum")
            rows=cur.fetchall()
            self.forumTable.delete(*self.forumTable.get_children())
            for row in rows:
               self.forumTable.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    
        

    def get_data(self,ev):
        f=self.forumTable.focus()
        content=(self.forumTable.item(f))
        row=content['values']
        #print(row)
        self.var_forum_invoice.set(row[0])
        self.var_name.set(row[1])
       
        self.var_contact.set(row[2])
                                      
       
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3])

       


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_forum_invoice.get()=="":
                messagebox.showerror("Error","Invoive NO. Must be Required",parent=self.root)
            else:
                cur.execute("select * from forum where invoice=?",(self.var_forum_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice NO. ",parent=self.root)    
                else:
                    cur.execute("Update forum set name=?,contact=?,desc=? where invoice=?",(
                    
                    
                                      
                                      
                                      self.var_name.get(),
                                      
                                      self.var_contact.get(),
                                      
                                      
                                      self.txt_desc.get('1.0',END),
                                      
                                      self.var_forum_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","forum Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    



    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_forum_invoice.get()=="":
                messagebox.showerror("Error","Invoice No.Must be Required",parent=self.root)
            else:
                cur.execute("select * from forum where invoice=?",(self.var_forum_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice NO.",parent=self.root)    
                else:
                    op=messagebox.askyesno("confirm","Do you Really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from forum where invoice=?",(self.var_forum_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","forum Deleated Successfully",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)      


    def clear(self):
        self.var_forum_invoice.set("")
        self.var_name.set("")
      
        self.var_contact.set("")
                                      
        
        self.txt_desc.delete('1.0',END)
        

        
        self.var_searchtxt.set("")
        
        self.show()


    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice NO. should be required",parent=self.root)
            else:
                cur.execute("select * from forum where invoice=?",(self.var_searchtxt.get(),))
                rows=cur.fetchone()
                if rows!=None:
                   self.forumTable.delete(*self.forumTable.get_children())
                   for row in rows:
                     self.forumTable.insert('',END,values=rows)
                else:
                    messagebox.showerror("Error","No reccord found",parent=self.root)      
 

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    











if __name__=="__main__":
    root=Tk()
    obj=forumClass(root)
    root.mainloop()



