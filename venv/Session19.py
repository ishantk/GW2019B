import mysql.connector

class Customer:
    def __init__(self, cid, name, phone, age, address):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.age = age
        self.address = address

    def showCustomer(self):
        print("==",self.cid,self.name,"==")
        print(self.phone)
        print(self.age)
        print(self.address)
        print("=================")

    def saveCustomer(self):
        sql = "insert into Customer values(null,'{}','{}', {}, '{}')".format(self.name, self.phone, self.age, self.address)
        print(sql)

        # 1. Create Connection
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

        # 2. Obtain Cursor (Insert/Update/Delete/Retrieve)
        cursor = con.cursor()

        # 3. Execute SQL Statement
        cursor.execute(sql)
        con.commit() # SQL Statements shall be executed as a Transaction
        print(">> Customer",self.name,"Saved")


# c1 = Customer(1, "John", "+91 99999 88888", 30, "Redwood Shores")
# c1.showCustomer()
# c1.saveCustomer()


# Create a Table in MySQL DB : Install XAMPP
"""
SQL Syntax for creating table:

create table Customer(
    cid int primary key auto_increment,
    name varchar(256),
    phone varchar(20),
    age int,
    address varchar(512)
)

insert into Customer values(null,'Fionna','+91 99999 77777', 22, 'Country Homes')

"""

c1 = Customer(None, None, None, None, None)
# c1.showCustomer()

print()

print("Enter Customer Details to Register")
c1.name = input("Enter Customer Name: ")
c1.phone = input("Enter Customer Phone: ")
c1.age = int(input("Enter Customer Age: "))
c1.address = input("Enter Customer Address: ")

# c1.showCustomer()

save = input("Would you like to save customer (yes/no)")

if save == "yes":
    c1.saveCustomer()


# HW: Save the Object in DB


# For Firebase : https://firebase.google.com/docs/firestore/quickstart
