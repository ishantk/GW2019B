#    *args -> Variable Arguments -> TUPLE
def addNums(*args):

    print(args)
    print(type(args))

    sum = 0

    for n in args:
        sum = sum + n

    print("Sum is:",sum)


addNums(10,20)
addNums(10,20,30,40,50)

print("***********")

# **kwargs -> keyword arguments -> Dictionary
def showData(**kwargs):
    print(kwargs)
    print(type(kwargs))

showData(eid=101, name="John Watson", salary=10000)

