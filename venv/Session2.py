"""
    Containers : Data Storage Containers

    We use PL to create/develop a Software !!

    Architecture:
    MODEL
    VIEW
    CONTROLLER

    MVC Design Pattern

    Uber/OLA App

    MODEL : Represents Data which software will take as input or give as output
            source location, destination location, type of cab

    VIEW  : Represents User Interface

    CONTROLLER : Logical Set of Rules.
                 1. Nearest Driver
                 2. Find Shortest Distance
                 3. Least Time

                 Generate an Output which is again data
                 Here, data shall be driver details to the customer


    Model is the most important component based on which we should start our software
    > Data Storage Container
        1. Single Value Container
        2. Multi Value Container
            2.1 Homogeneous
            2.2 Hetrogeneous

        Instagram SV / MV ?
            Profile Pic     -> SV
            Album of Pics           -> MV | Homo
            Album of Pics + Videos  -> MV | Hetro


        Any Container which we wish to create will have 4 operations
        1. Create
        2. Update
        3. Read
        4. Delete
"""

# 1. Create Operation
a = 10
# a is a reference variable which holds the HashCode of data 10
print("HashCode of a is:",id(a)) # id(a) will give us HashCode
print("HashCode of a is:",hex(id(a)))
print("HashCode of a is:",oct(id(a)))
print("HashCode of a is:",bin(id(a)))

print()

# 2. Update operation
a = 20
print("HashCode of a after updating data is:",id(a))
print("HashCode of a after updating data is:",hex(id(a)))
print("HashCode of a after updating data is:",oct(id(a)))
print("HashCode of a after updating data is:",bin(id(a)))

print()

b = 20
print("HashCode of b is:",id(b))

# 2. Update operation
b = 30
print("HashCode of b after updating data is:",id(b))

print()

# Multi Value Container
# 1. Create Operation
c = 10, 20, 30, 40, 50      # Homo
d = 10, 20, 30, 40, 50      # Homo

e = 10, 'A', 2.2, 'Hello'   # Hetro

print("HashCode of c is:",id(c))
print("HashCode of d is:",id(d))
print("HashCode of e is:",id(e))

# 2. Update Operation
c = 11, 13, 15

print("HashCode of c after update is:",id(c))

# 3. Read Operation
print(a)
print(b)
print(c)
print(d)
print(e)

print()

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 4. Delete Operation
del a
del b
del c
del d
del e

print(a)
print(b)
print(c)
print(d)
print(e)