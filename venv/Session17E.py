class Order:

    def __init__(self, oid, phone, price):
        self.oid = oid
        self.phone = phone
        self.price = price

    def orderToCSV(self):
        return "{},{},{}\n".format(self.oid,self.phone,self.price)


o1 = Order(1,"9915571177",500)
o2 = Order(2,"9915571177",700)
o3 = Order(3,"9915500000",200)

print(o1.orderToCSV())
print(o2.orderToCSV())
print(o3.orderToCSV())

file = open("orders.csv","a")
file.write(o1.orderToCSV())
file.write(o2.orderToCSV())
file.write(o3.orderToCSV())

file.close()


# CW/HW:
"""
    1. Take User Input and keep on appending the orders in a csv file
    2. Read CSV File and sort the data as per price
    3. Group the data as per customer along with count and total
    4. Take input as phone number from user, read the file 
        and tell how much customer has spent till now
        eg: 9915571177 -> 1200

"""
