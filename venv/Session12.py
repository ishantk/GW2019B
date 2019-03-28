class Student:

    # This shall be overwritten by below constructor
    def __init__(self):
        pass

    def __init__(self, roll, name, phone, email, address):
        self.roll = roll
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def showStudent(self):
        print("==Student Details==")
        print(self.roll,"belongs to",self.name)


# s1 = Student() # Error
"""
s1 = Student(101, "John", "+91 99999 88888", "john@example.com", "Redwood Shores")
s2 = Student(201, "Fionna", "+91 77777 88888", "fionna@example.com", "Country Homes")

print(s1.__dict__)
print(s2.__dict__)

s1.showStudent()
s2.showStudent()

"""

# Collection Of Objects
students = []
reply = "yes"

while reply == "yes":

    print("Add Student Details:")

    roll = int(input("Enter Student Roll Number: "))
    name = input("Enter Student Name: ")
    phone = input("Enter Student Phone: ")
    email = input("Enter Student Email: ")
    address = input("Enter Student Address: ")

    s = Student(roll, name, phone, email, address)
    students.append(s)

    reply = input("Do you want to add another student (yes/no): ")

for s in students:
    s.showStudent()