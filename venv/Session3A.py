# Types of Multi Value Containers in Python

# SVC
a = 10
print(a)

# MVC
#1. Tuple - IMMUTABLE (Which cannot be changed after creation)
# b = 10, 20, 30, 40, 50
b = (10, 20, 30, 40, 50, 20)
# b[0] = 111    # Update Operation is not Possible in Tuple
# b.append(222) # Nothing Like append in Tuple
print(b[0])
print(b)
print(type(b))

# c = 10, 'A', "John", 2.2
c = (10, 'A', "John", 2.2)
print(c)
print(type(c))

#2. List - MUTABLE (Which can be changed after creation)
d = [10, 20, 30, 40, 50, 20]
e = [10, 'A', "John", 2.2]

d[0] = 111       # Update Data in List
d.append(222)    # Adding Data in List

print(d)
print(type(d))
print(e)
print(type(e))

#3. Set
f = {10, 20, 30, 40, 50, 20}
g = {10, 'A', "John", 2.2, "John"}

# f[0] = 111   # Unable to perform Update
# print(f[0])  # Cannot be done as Set works on Hashing and not Indexing
print(f)
print(type(f))
print(g)
print(type(g))

#4. Dictionary | JSON (Java Script Object Notation)
myStudents = {101:"John", 201:"Jennie", 111:"Fionna", 333:"Sia"}
print(myStudents)
print(type(myStudents))
print(myStudents[101])
