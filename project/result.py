from tkinter import*
from tkinter.tix import IMAGETEXT
from tkinter import ttk,messagebox
import sqlite3

class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Event Management System | Developed by Group A5")
        self.root.config(bg="white")
        self.root.focus_force()


        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_cid=StringVar()

        self.var_cat=StringVar()
        self.var_forum=StringVar()
        self.cat_list=[]
        self.forum_list=[]
        self.fetch_cat_sup()

        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        btn_logout=Button(self.root,text="LOGOUT",font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=1100,y=10,height=50,width=150)

        
     

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)


        ###### title #############
        title= Label(product_Frame,text="Candidate Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)


        ####### column1 ########ndidate

        lbl_cat= Label(product_Frame,text="Name",font=("goudy old style",15),bg="white").place(x=30,y=60)
        lbl_forum= Label(product_Frame,text="Forum",font=("goudy old style",15),bg="white").place(x=30,y=110)
        lbl_eventName= Label(product_Frame,text="Event_name",font=("goudy old style",15),bg="white").place(x=30,y=160)
        lbl_price= Label(product_Frame,text="price",font=("goudy old style",15),bg="white").place(x=30,y=210)
        lbl_qty= Label(product_Frame,text="C_qty",font=("goudy old style",15),bg="white").place(x=30,y=260)
        lbl_status= Label(product_Frame,text="Stauts",font=("goudy old style",15),bg="white").place(x=30,y=310)

        


        ## column2 ##

        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)


        cmb_forum=ttk.Combobox(product_Frame,textvariable=self.var_forum,values=self.forum_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_forum.place(x=150,y=110,width=200)
        #cmb_forum.current(0)

        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg='lightyellow').place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg='lightyellow').place(x=150,y=210,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg='lightyellow').place(x=150,y=260,width=200)


        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)


        ######### button #######
        
        btn_add=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)


        ## search Frame ##

        SearchFrame=LabelFrame(self.root,text="Search Candidate",font=("goudy old Style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        ## options ##

        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","name","forum","name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=440,y=9,width=150,height=30)

        
        
###############################################################################        
        
        
        
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,relwidth=1,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(p_frame,columns=("candidate","Name","Forum","Event_name","price","qty","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("candidate",text="C ID")
        self.product_table.heading("Name",text="Name")
        self.product_table.heading("Forum",text="Forum")
        self.product_table.heading("Event_name",text="E_name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="Quantity")
        self.product_table.heading("Status",text="Status")
        

        self.product_table["show"]="headings"

        self.product_table.column("candidate",width=90)
        self.product_table.column("Name",width=100)
        self.product_table.column("Forum",width=100)
        self.product_table.column("Event_name",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("qty",width=100)
        self.product_table.column("Status",width=100)
        
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        



########## function ##################################################################################
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.forum_list.append("Empty")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select name from function ")
            cat=cur.fetchall()
            self.cat_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
              

            cur.execute("select name  from forum")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.forum_list[:]
                self.forum_list.append("Select")
                for i in sup:
                    self.forum_list.append(i[0])
              
            
             



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_forum.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error","all filds are  Required",parent=self.root)
            else:
                cur.execute("select * from result where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already present, try different",parent=self.root)    
                else:
                    cur.execute("Insert into result (candidate,name,Forum,Event_name,price,qty,Status)values(?,?,?,?,?,?,?)",(
                                      
                                      self.var_cat.get(),
                                      self.var_forum.get(),
                                      self.var_name.get(),
                                      self.var_price.get(),
                                      self.var_qty.get(),
                                      self.var_status.get(),
                    ))
                                      
                                      
                    con.commit()
                    messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from result")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    
        

    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_cid.set(row[0])
        self.var_cat.set(row[2])
        self.var_forum.set(row[1])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
        
       


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_candidate_id.get()=="":
                messagebox.showerror("Error","Please selct event from list",parent=self.root)
            else:
                cur.execute("select * from function where eid=?",(self.var_cid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Event",parent=self.root)    
                else:
                    cur.execute("Update event set candidate=?,forum=?,name=?,price=?,qty=?,status=? where candidate=?",(
                    
                    
                                      
                                    self.var_cat.get(),
                                    self.var_forum.get(),
                                    self.var_name.get(),
                                    self.var_price.get(),
                                    self.var_qty.get(),
                                    self.var_status.get(),
                                    self.var_cid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Event Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    



    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cid.get()=="":
                messagebox.showerror("Error","Select event from the List",parent=self.root)
            else:
                cur.execute("select * from function where candidate=?",(self.var_cid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid function",parent=self.root)    
                else:
                    op=messagebox.askyesno("confirm","Do you Really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from function where eid=?",(self.var_cid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Event Deleated Successfully",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)      


    def clear(self):
           
        self.var_cat.set("Select"),
        self.var_forum.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Active"),
        self.var_cid.set("")
           
                                   
       
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
                cur.execute("select * from function where" +self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                   self.product_table.delete(*self.product_table.get_children())
                   for row in rows:
                      self.product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No reccord found",parent=self.root)      
 

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    


        









if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()
