def squareOfNum(num):
    return num * num

lRef1 = lambda num : num * num

Numbers = [10, 11, 33, 57, 21]

# result = map(squareOfNum, Numbers)
result = map(lRef1, Numbers)
print(result)
print(type(result))
print(list(result)) # Convert result into list


lRef2 = lambda n : n % 2 == 0
Data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = map(lRef2, Data)
print(list(result))

result = filter(lRef2, Data)
print(result)
print(type(result))
print(list(result))

X = [10, 20, 30, 40, 50, 60]
Y = [11, 22, 33, 44, 55]

lm = lambda P, Q : P + Q
print("Sum of 10 and 20 is:",lm(10,20))

result = map(lm, X, Y)
print(list(result))


from functools import reduce
population = [100, 200, 300, 400, 500]
result = reduce(lm, population)
print(result)

# Explore  with Dictionaries !! :)
employees = [
                {"eid":101, "name":"john", "salary":10000},
                {"eid":201, "name":"jennie", "salary":20000},
                {"eid":301, "name":"jack", "salary":30000}
            ]

# Problem:
"""
    lambda expression
    which gives bonus to employees
    bonus 10%
    -> +1
    Implement map function with Lambda Expression to solve the problem 
    
"""

print(employees)
