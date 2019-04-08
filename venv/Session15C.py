"""
class LEDTv:
    def __init__(self, pid, name, brand, price, screenSize, technology):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.screenSize = screenSize
        self.technology = technology

    def showLEDTvDetails(self):
        print("===",self.pid,"|",self.name,"===")
        print("Brand:",self.brand)
        print("Price:", self.price)
        print("Size:", self.screenSize)
        print("Tech:", self.technology)

class Mobile:
    def __init__(self, pid, name, brand, price, ram, memory, os):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.ram = ram
        self.memory = memory
        self.os = os

    def showMobileDetails(self):
        print("===",self.pid,"|",self.name,"===")
        print("Brand:",self.brand)
        print("Price:", self.price)
        print("RAM:", self.ram)
        print("Memory:", self.memory)
        print("OS:", self.os)

class Shoe:
    def __init__(self, pid, name, brand, price, size, color):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.size = size
        self.color = color

    def showShoeDetails(self):
        print("===",self.pid,"|",self.name,"===")
        print("Brand:",self.brand)
        print("Price:", self.price)
        print("Size:", self.size)
        print("Color:", self.color)

"""

# Challenge : Code was being Re-Used

class Product:
    def __init__(self, pid, name, brand, price):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price

    def showProduct(self):
        print("===", self.pid, "|", self.name, "===")
        print("Brand:", self.brand)
        print("Price:", self.price)

# IS-A Relationship
class LEDTv(Product):

    def __init__(self, pid, name, brand, price, screenSize, technology):
        Product.__init__(self, pid, name, brand, price)
        self.screenSize = screenSize
        self.technology = technology

    def showLEDTvDetails(self):
        Product.showProduct(self)
        print("Size:", self.screenSize)
        print("Tech:", self.technology)

class Mobile(Product):
    def __init__(self, pid, name, brand, price, ram, memory, os):
        Product.__init__(self, pid, name, brand, price)
        self.ram = ram
        self.memory = memory
        self.os = os

    def showMobileDetails(self):
        Product.showProduct(self)
        print("RAM:", self.ram)
        print("Memory:", self.memory)
        print("OS:", self.os)

class Shoe(Product):
    def __init__(self, pid, name, brand, price, size, color):
        Product.__init__(self, pid, name, brand, price)
        self.size = size
        self.color = color

    def showShoeDetails(self):
        Product.showProduct(self)
        print("Size:", self.size)
        print("Color:", self.color)


l1 = LEDTv(101,"OLEDTV", "Samsung",50000, 50, "OLED")
l1.showLEDTvDetails()

print()

m1 = Mobile(201, "iPhoneX","Apple", 80000, 4, 256, "iOS")
m1.showMobileDetails()

print()

s1 = Shoe(301, "AlphaBounce", "Apple", 10000, 8, "Black")
s1.showShoeDetails()