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

# DAO or Data Access Object Design Pattern
class DBHelper:

    def saveCustomer(self, customer):
        sql = "insert into Customer values(null,'{}','{}', {}, '{}')".format(customer.name, customer.phone, customer.age, customer.address)
        print(sql)

        # 1. Create Connection
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

        # 2. Obtain Cursor (Insert/Update/Delete/Retrieve)
        cursor = con.cursor()

        # 3. Execute SQL Statement
        cursor.execute(sql)
        con.commit() # SQL Statements shall be executed as a Transaction
        print(">> Customer",customer.name,"Saved")


"""
c1 = Customer(0, "Harry", "+91 77777 88888", 20, "Pristine Magnum")
c1.showCustomer()

db = DBHelper()
db.saveCustomer(c1)
"""
