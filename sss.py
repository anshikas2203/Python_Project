class shop:
        def __init__(self):
            self.items_dict=[]
            self.bill_amount=0
        def get(self):
                  print("\n")  
                  pid=int(input("Enter Pizza_Id :: "))
                  ptype=input("Enter Pizza_Type :: ")
                  qty=int(input("Enter Quantity ::"))
                  self.items_dict.append({"pid":pid,"ptype":ptype,"qty":qty} )  
             
        def show(self):
                  print("Items are :: ")
                  for i in range(len(self.items_dict)):
                    print("Pizza_id is ",self.items_dict[i]["pid"])
                    print("Pizza_Type is ",self.items_dict[i]["ptype"])
                    print("Product qty is ",self.items_dict[i]["qty"])
                  
        def calculate(self):
            import sqlite3
            conn=sqlite3.connect('Pizza.db')
            for i in range(len(self.items_dict)):
                pid=self.items_dict[i]["pid"]
                ptype=self.items_dict[i]["ptype"]
                cursor=conn.execute("select Price from  p3 where pid=? and ptype=? ",(pid,ptype,))
                for row in cursor:
                    rate=row[0]
                    
                qty=self.items_dict[i]["qty"]
                self.bill_amount+=int(rate)*qty

            print("Price To Pay for this item:\t",self.bill_amount)
            print("\n\n\t\t\tTotal Amount To Pay::  ",self.bill_amount)
            print("\n\n\t\t\t\tThanks For Shopping")
            print("\n\t\t\t\t    Visit Again")
            

if __name__== "__main__":
         S1=shop()
         S1.get()
         S1.show()
         S1.calculate()                                
                                         
               
