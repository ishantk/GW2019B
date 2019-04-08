# HAS-A Relationship
# Person HAS-AN Address
"""
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
"""
class Person:
    def __init__(self, name, age, addresses):
        self.name = name
        self.age = age
        self.addresses = addresses

class Address:
    def __init__(self, adrsLine, city):
        self.adrsLine = adrsLine
        self.city = city

a1 = Address("Pristine Magnum", "Bengaluru")
a2 = Address("Country Homes", "Pune")

aList = [a1, a2]

# p1 = Person("Fionna Flynn", 20, a1)    # 1 to 1
p1 = Person("Fionna Flynn", 20, aList)   # 1 to many
p2 = Person("John Watson", 20, None)     # 1 to None

