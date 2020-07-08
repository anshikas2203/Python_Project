from tkinter import*
import sqlite3
from tkinter import messagebox

def final():
   messagebox.showinfo("Thanks","\nThanks For Shopping\n\nVisit Again")
#payment page
def payment():
        root=Tk()
        root.geometry('1360x700')
        root.title("Payment")
        root.configure(background="aqua")
        fname=StringVar()
        def amount():
           name=fname.get()
        Label(root,text="TOTAL AMOUNT",width=40,font=("bold",20),bg='aqua',fg='black').place(x=130,y=100)
        Entry(root,textvar=fname).place(x=650,y=110)
        Button(root,text="PLACE ORDER",command=final,width=19, height=4,font=("bold",20),bg='Black',fg='brown').place(x=200,y=300)
        Button(root,text="CANCEL",command=exit,width=19, height=4,font=("bold",20),bg='Black',fg='brown').place(x=700,y=300)
       
        root.mainloop()
#to order more than one time or proceed to payment page 
def proceed():
        root=Tk()
        root.geometry('1360x700')
        root.title("Proceed")
        root.configure(background="black")
        Label(root,text="CONFIRM",width=40,font=("bold",40),bg='Black',fg='Brown').place(x=20,y=25)
        Button(root,text="Want More",command=order,width=20, height=10,font=("bold",20),bg='Brown',fg='white').place(x=200,y=300)
        Button(root,text="Proceed",command=payment,width=20, height=10,font=("bold",20),bg='Brown',fg='white').place(x=700,y=300)
        root.mainloop()
#menu 
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
        root.geometry('760x700')
        root.configure(background="lightgreen")
       # canvas = Canvas(width = 300, height = 200, bg = 'lightgreen')
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
                 
        Label(root,text="ORDER",width=50,height=1,font=("bold",20),bg='lightgreen',fg='black').place(x=25,y=25)
        Label(root,text="ORDER ID",width=9,height=2,font=("bold",17),bg='lightgreen',fg='black').place(x=250,y=100)
        Entry(root,textvar=pid).place(x=420,y=120)
        Label(root,text="TYPE   ",width=9,height=2,font=("bold",17),bg='lightgreen',fg='black').place(x=250,y=200)
        Entry(root,textvar=ptype).place(x=420,y=220)
        Label(root,text="Quantity",width=9,height=2,font=("bold",17),bg='lightgreen',fg='black').place(x=250,y=300)
        Entry(root,textvar=pqty).place(x=420,y=320)
        Button(root,text="Submit",command=proceed,width=20,height=5,font=("bold",15),bg='black',fg='green').place(x=290,y=420)
            
#signup page
def signup():
        root =Tk()
        root.geometry('1360x700')
        root.title("Signup") 
        root.configure(background="magenta")
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
                conn.execute("insert into T1(Firstname,Email,password,contact)values(?,?,?,?)",(name,email,password,contact))
                
        Label(root,text="SIGNUP FORM",width=50,height=3,font=("bold",25),bg='magenta',fg='black').place(x=150,y=10)
        Label(root,text="NAME",width=6,height=5,font=("bold",17),bg='magenta',fg='black').place(x=500,y=150)
        Entry(root,textvar=Firstname).place(x=650,y=205)
        Label(root,text="Email",width=6,height=1,font=("bold",17),bg='magenta',fg='black').place(x=500,y=250)
        Entry(root,textvar=Email).place(x=650,y=255)
        Label(root,text="Password",width=10,height=1,font=("bold",17),bg='magenta',fg='black').place(x=500,y=300)
        Entry(root,textvar=Password,show="*").place(x=650,y=305)
        Label(root,text="Contact",width=8,height=1,font=("bold",17),bg='magenta',fg='black').place(x=500,y=350)
        Entry(root,textvar=Contact).place(x=650,y=355)
        Button(root, text='Submit',command=order,width=20,height=5,font=("bold",15),bg='black',fg='magenta').place(x=550,y=450)
#login page 
root=Tk()
root.geometry('1060x700')
root.title("Login")
canvas = Canvas(width = 1000, height = 1300,bg='teal')
canvas.pack(expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'th.gif')
canvas.create_image(300, 300, image = gif1)
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

Label(root,text="LOGIN",width=40,font=("bold",40),bg='teal',fg='Black').place(x=20,y=25)
Label(root,text="USER NAME",width=10,height=8,font=("bold",17),bg='teal',fg='white').place(x=500,y=100)
Entry(root,textvar=Firstname).place(x=710,y=200)
Label(root,text="PASSWORD",width=10,height=3,font=("bold",17),bg='teal',fg='white').place(x=500,y=250)
Entry(root,textvar=Password,show="*").place(x=710,y=285)
Button(root,text="LOGIN",command=order,width=15, height=5,font=("bold",15),bg='white',fg='black').place(x=450,y=400)
Button(root,text="SIGNUP",command=signup,width=15, height=5,font=("bold",15),bg='white',fg='black').place(x=750,y=400)
root.mainloop()


