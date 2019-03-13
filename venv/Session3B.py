# Read Data from User and store it in a container
data = input("Enter some data: ")
print("You Entered:",data)
print("Type of data is:",type(data))

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = num1 + num2
# print("num3 is: ",num3)
print("sum of",num1,"and",num2,"is:",num3)
print("sum of {} and {} is {}".format(num1,num2,num3))