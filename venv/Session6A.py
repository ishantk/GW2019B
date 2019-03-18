def bye():
    return "Bye !!"

# This is not Reference Copy
# This is executing a Function and getting back returned data into b
b = bye()

# Reference Copy !!
c = bye


def hello(name):
    print("Hello,",name)

#Lets print name of the function
print(hello)

# Reference Copy
hh = hello
print(hh)

# Execution of Function
hello("John")
hh("Fionna")

