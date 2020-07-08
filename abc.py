from tkinter import*
import sqlite3
from tkinter import messagebox

def final():
   messagebox.showinfo("Thanks","\nThanks For Shopping\n\nVisit Again")

def payment():
        root=Tk()
        root.geometry('500x500')
        root.title("Payment")
        fname=StringVar()
        def amount():
           name=fname.get()
        
           
        Label(root,text="TOTAL AMOUNT :- ").place(x=130,y=100)
        Entry(root,textvar=fname).place(x=250,y=100)
        Button(root,text="PLACE ORDER",command=final).place(x=120,y=150)
        Button(root,text="CANCEL",command=exit).place(x=220,y=150)
        root.mainloop()

def proceed():
        root=Tk()
        root.geometry('900x900')
        root.title("Proceed")
        root.configure(background="Black")
        Label(root,text="CONFIRM",width=40,font=("bold",40),bg='Black',fg='Brown').place(x=20,y=25)
        Button(root,text="Want More",command=order,width=20, height=10,font=("bold",20),bg='Brown',fg='white').place(x=200,y=300)
        Button(root,text="Proceed",command=payment,width=20, height=10,font=("bold",20),bg='Brown',fg='white').place(x=700,y=300)
        root.mainloop()
        
def order():
        import sqlite3
        x=sqlite3.connect("Pizza.db")
        y=x.execute("SELECT * FROM p3")
        print("\n")
        print("\t\t\t        MENU \n")
        print("Pizza_ID\t\tPizza_Name\t\t\t\tType\t\t\t\t  \tPrice\n")
        for i in y:
                print(i[0],"\t\t\t",i[1],"\t\t\t\t",i[2],"\t\t\t\t  \t",i[3],"\n")


        root=Tk()
        root.geometry('500x500')
        root.title("Menu")
        bill_amount=0 
        pid=StringVar()
        ptype=StringVar()
        pqty=StringVar()
        def menu1():
                 ppid=pid.get()
                 pptype=ptype.get()
                 ppqty=pqty.get()
                 import sqlite3
                 conn=sqlite3.connect('Pizza.db')
                 cursor=conn.execute("select Price from p3 where pid=? and ptype=?",(ppid,pptype))
                 for row in cursor:
                       rate=row[0]
                       bill_amount+=int(rate)*pqty
                 
        Label(root,text="ORDER",width=40,font=("bold",20)).place(x=10,y=25)
        Label(root,text="ID").place(x=100,y=100)
        Entry(root,textvar=pid).place(x=150,y=100)
        Label(root,text="Type").place(x=100,y=200)
        Entry(root,textvar=ptype).place(x=150,y=200)
        Label(root,text="Quantity").place(x=100,y=300)
        Entry(root,textvar=pqty).place(x=150,y=300)
        Button(root,text="Submit",command=proceed).place(x=180,y=400)
        root.mainloop()

def signup():
        root =Tk()
        root.geometry('800x600')
        root.title("Signup")
        Firstname=StringVar()
        Email=StringVar()
        Password=StringVar()
        Contact=StringVar()
        def database():
                name=Firstname.get()
                email=Email.get()
                password=Password.get()
                contact=Contact.get()
                conn=sqlite3.connect("Pizza.db")
                #conn.execute("Create table T1(Firstname text,Email text,password text,contact text)")
                conn.execute("insert into T1(Firstname,Email,password,contact)values(?,?,?,?)",(name,email,password,contact))
                '''c=conn.execute("select * from T1")
                for i in c:
                    print("name",i[0])
                    print("email",i[1])
                    print("password",i[2])
                    print("contact",i[3])
                    print("\n")
                conn.commit()'''
        Label(root,text="SIGNUP FORM",width=40,font=("bold",20)).place(x=10,y=25)
        Label(root,text="NAME :- ").place(x=100,y=120)
        Entry(root,textvar=Firstname).place(x=200,y=120)
        Label(root,text="Email :- ").place(x=100,y=150)
        Entry(root,textvar=Email).place(x=200,y=150)
        Label(root,text="PASSWORD :- ").place(x=100,y=180)
        Entry(root,textvar=Password,show="*",width=15).place(x=200,y=180)
        Label(root,text="CONTACT :- ").place(x=100,y=210)
        Entry(root,textvar=Contact).place(x=200,y=210)
        Button(root, text='Submit',command=order,width=20,bg='teal',fg='white').place(x=200,y=250)

root=Tk()
root.geometry('500x500')
root.title("Login")
Firstname=StringVar()
Password=StringVar()
def db():
     name=Firstname.get()
     password=Password.get()
     import sqlite3
     conn=sqlite3.connect('Pizza.db')
     cursor=conn.execute("select count(*) from T1 where Firstname=? and Password=?",(name,password))
     row=cursor.fetchone();
     c=row[0]
     conn.close()
         
Label(root,text="Login",width=40,font=("bold",20)).place(x=10,y=25)
Label(root,text="USER Name :-").place(x=100,y=100)
Entry(root,textvar=Firstname).place(x=190,y=100)
Label(root,text="Password :-").place(x=100,y=150)
Entry(root,textvar=Password,show="*").place(x=190,y=150)
Button(root,text="Login",command=order).place(x=120,y=200)
Button(root,text="Signup",command=signup).place(x=180,y=200)
root.mainloop()


root.mainloop()


'''def shop():
        items_dict=[]
        bill_amount=0
        print("\n")  
        pid=int(input("Enter Pizza_Id :: "))
        ptype=input("Enter Pizza_Type :: ")
        qty=int(input("Enter Quantity ::"))
        items_dict.append({"pid":pid,"ptype":ptype,"qty":qty} )  
             

        print("Items are :: ")
        for i in range(len(items_dict)):
           print("Pizza_id is ",items_dict[i]["pid"])
           print("Pizza_Type is ",items_dict[i]["ptype"])
           print("Product qty is ",items_dict[i]["qty"])
                  
        
        import sqlite3
        conn=sqlite3.connect('Pizza.db')
        for i in range(len(items_dict)):
           pid=items_dict[i]["pid"]
           ptype=items_dict[i]["ptype"]
           cursor=conn.execute("select Price from  p3 where pid=? and ptype=? ",(pid,ptype,))
           for row in cursor:
                    rate=row[0]
                    
           qty=items_dict[i]["qty"]
           bill_amount+=int(rate)*qty

           print("Price To Pay for this item:\t",bill_amount)
           print("\n\n\t\t\tTotal Amount To Pay::  ",bill_amount)
           print("\n\n\t\t\t\tThanks For Shopping")
           print("\n\t\t\t\t    Visit Again")'''

