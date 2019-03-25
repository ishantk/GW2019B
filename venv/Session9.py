"""

    Object Oriented Programming in Python

    Object:
        MULTI VALUE CONTAINER
            Homogeneous Data Storage Container
            Hetrogeneous Data Storage Container

    We modularize data in a software as Objects

    amazon.in
        data ?

    OLA/Uber
        data ?

        User        ->      Object
            name    ->      Attributes
            phone
            email
            age
            gender
            city
            state

        Driver
            name
            phone
            email
            age
            gender
            city
            state
            experience
            licenseNum

        Vehicle
            regNum
            make
            model
            color
            type

        Ride
            source
            destination
            typeOfCab
            fare
            discount


        Let us code Object !!

"""

# Structure of Object
# Textual Representation of Object
class User:
    pass

class Driver:
    pass

# A new User object will be created in memory
u1 = User()
u2 = User()

# A new Driver object will be created in memory
d1 = Driver()

print("u1 is:",u1)
print("u2 is:",u2)
print("d1 is:",d1)

# u1 and d1 are not Objects. They are reference variables pointing to the Object

print("Data in Object of u1:",u1.__dict__)
print("Data in Object of u2:",u2.__dict__)
print("Data in Object of d1:",d1.__dict__)

# Create Attributes in Object along-with value
u1.name = "John"
u1.phone= "+91 99999 88888"
u1.age = 20
u1.city = "Ludhiana"
u1.zipCode = 141002

u2.name = "Sia"
u2.phone= "+91 77777 88888"
u2.email = "sia@example.com"

d1.name = "Fionna"
d1.phone= "+91 89898 78787"
d1.age = 20
d1.experience = 5
d1.licenseNum = "BBAPC3312"

print("Data in Object of u1:",u1.__dict__)
print("Data in Object of u2:",u2.__dict__)
print("Data in Object of d1:",d1.__dict__)

del d1.phone
del u1.age
del u2.phone

print("Data in Object of u1:",u1.__dict__)
print("Data in Object of u2:",u2.__dict__)
print("Data in Object of d1:",d1.__dict__)


