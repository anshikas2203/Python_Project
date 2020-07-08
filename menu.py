import tkinter
from tkinter import*

'''import sqlite3
root=Tk()
root.geometry('500x500')
root.title("Menu")
pid=StringVar()
pizza=StringVar()
ptype=StringVar()
price=StringVar()
def menu1():
 ppid=pid.get()
 ppizza=pizza.get()
 pptype=ptype.get()
 pprice=price.get()
 x=sqlite3.connect("Pizza.db")

 #x.execute("Create table p3(pid text,pizza text,ptype text,price text)")
 x.execute("INSERT INTO p3(pid,pizza,ptype,price) VALUES(?,?,?,?)",(ppid,ppizza,pptype,pprice))
 #x.execute("DELETE FROM p3 where pid=2 ",) 
 y=x.execute("SELECT * FROM p3")
 print("\n")
 print("\t\t\t        MENU \n")
 print("Pizza_ID\t\tPizza_Name\t\t\t\tType\t\t\t\t  \tPrice\n")
 for i in y:
    print(i[0],"\t\t\t",i[1],"\t\t\t\t",i[2],"\t\t\t\t  \t",i[3],"\n")
 x.commit()
Label(root,text="Menu",width=40,font=("bold",20)).place(x=10,y=25)
Label(root,text="ID").place(x=100,y=100)
Entry(root,textvar=pid).place(x=150,y=100)
Label(root,text="Pizza").place(x=100,y=150)
Entry(root,textvar=pizza).place(x=150,y=150)
Label(root,text="Type").place(x=100,y=200)
Entry(root,textvar=ptype).place(x=150,y=200)
Label(root,text="Price").place(x=100,y=250)
Entry(root,textvar=price).place(x=150,y=250)
Button(root,text="Submit",command=menu1).place(x=180,y=300)
root.mainloop()'''

class showmenu:
    def showmenu1(self):
            import sqlite3
            x=sqlite3.connect("Pizza.db")
            y=x.execute("SELECT * FROM p3")
            print("\n")
            print("\t\t\t        MENU \n")
            print("Pizza_ID\t\tPizza_Name\t\t\t\tType\t\t\t\t  \tPrice\n")
            for i in y:
                print(i[0],"\t\t\t",i[1],"\t\t\t\t",i[2],"\t\t\t\t  \t",i[3],"\n")
        
if __name__=="__main__":     
     m1=showmenu()     
     m1.showmenu1()

