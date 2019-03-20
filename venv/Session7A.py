# Container Creation
a = 10
b = 20

# Container Creation and Expression Evaluation
c = a+b

# Container Updation
c = 111

# Container Deletion
# del c

# Execution Statement to read data from Container
# print("c is:",c)

# Function or Method or Procedure Creation
def showData():
    global a
    a = 123
    d = 333
    print("a is:", a)
    print("b is:", b)
    print("c is:", c)

# Execution of a Function
showData()

# print("d is:",d) -> error
print("a is:",a)

