"""
def addNums(a, b, c):
    sum = a + b + c
    print("Sum is: ",sum)

addNums(10, 20, 30)

"""


# def addNums(nums):
def addNums(*nums): # Variable Inputs
    print(nums)
    print(type(nums))

    sum = 0
    for n in nums:
        sum = sum + n

    print("Sum of Numbers is:",sum)

# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# addNums(numbers)
addNums(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
addNums(10, 20, 30, 40, 50)
addNums(10, 20)