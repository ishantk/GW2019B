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


    def updateCustomer(self):
        sql = "update Customer set name = '{}', phone='{}', age={}, address='{}' where cid = {}".format(self.name, self.phone, self.age, self.address, self.cid)
        print(sql)

        # 1. Create Connection
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

        # 2. Obtain Cursor (Insert/Update/Delete/Retrieve)
        cursor = con.cursor()

        # 3. Execute SQL Statement
        cursor.execute(sql)
        con.commit() # SQL Statements shall be executed as a Transaction
        print(">> Customer",self.name,"Updated")

    def deleteCustomer(self):
        sql = "delete from Customer where cid = {}".format(self.cid)
        print(sql)

        # 1. Create Connection
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

        # 2. Obtain Cursor (Insert/Update/Delete/Retrieve)
        cursor = con.cursor()

        # 3. Execute SQL Statement
        cursor.execute(sql)
        con.commit() # SQL Statements shall be executed as a Transaction
        print(">> Customer with",self.cid,"Deleted")


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

def createCustomer():
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



def updateCustomer():
    c1 = Customer(None, None, None, None, None)
    # c1.showCustomer()

    print()

    print("Enter Customer Details to be Updated:")
    c1.cid = int(input("Enter Customer ID:"))
    c1.name = input("Enter Customer Name: ")
    c1.phone = input("Enter Customer Phone: ")
    c1.age = int(input("Enter Customer Age: "))
    c1.address = input("Enter Customer Address: ")

    save = input("Would you like to update customer (yes/no)")

    if save == "yes":
        c1.updateCustomer()

def delete():
    c1 = Customer(None, None, None, None, None)
    print("Enter Customer Details to be Deleted:")
    c1.cid = int(input("Enter Customer ID:"))

    delete = input("Would you like to delete customer (yes/no)")

    if delete == "yes":
        c1.deleteCustomer()


def showCustomers():
    sql = "select * from Customer"
    print(sql)

    # 1. Create Connection
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

    # 2. Obtain Cursor (Insert/Update/Delete/Retrieve)
    cursor = con.cursor()

    # 3. Execute SQL Statement
    cursor.execute(sql)

    """
    row = cursor.fetchone()
    print(row)
    print(type(row))
    """

    rows = cursor.fetchall()
    # print(rows)
    for row in rows:
        print(row)


# createCustomer()
# updateCustomer()
# delete()

showCustomers()

# with MySQL DB
# Project : Zomato | Create Order | Update Order | Delete Order | View Orders
#                  | What is the total amount for all orders ?
#                  | What is the order with maximum and minimum price
