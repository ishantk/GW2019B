class User:
    # Constructor of an Object
    # To Standardize the Structure of an Object
    # To limit what data should be in the Object
    # uid, name, phone are inputs to constructor
    def __init__(self, uid, name, phone):
        self.uid = uid
        self.name = name
        self.phone = phone


u1 = User(101,"John","+91 99999 88888")
print(u1.__dict__)

u2 = User(201, "Fionna", "+91 99999 77777")
print(u2.__dict__)

u1.age = 30
u1.address = "Redwood Shores"

del u2.phone

print(u1.__dict__)
print(u2.__dict__)