# Controller
# Mathematical Operations or set of Rules : Algorithmic Approach

# OPERATORS
#1. Arithmetic Operators
# + , -, *, /, //, %, **
a = 10
b = 3

c = a+b
d = a-b
e = a/b
f = a//b
g = a%b
h = a ** b

print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

# Conditional Operators -> bool -> True/False
# >, <, >=, <=, ==, !=

print(a>b)
print(a<b)

result = (a==b)
print("Result is:",result)
print(type(result))

# Logical Operators
# and or not
x = 10
y = 20
z = 30

# result = y>x and y>z
result = y>x or y>z
print("Result is:",result)

orderBill = 1375
restaurant = "ABC"

print("Can we offer discount: ",(orderBill>1000 and restaurant=="ABC"))

#Bitwise Operatos
# &, |, ^
# . . 64 32 16 8 4 2 1

num1 = 11               # 1 0 1 1
num2 = 5                # 0 1 0 1
num3 = num1 & num2      # 0 0 0 1   ->

num4 = num1 | num2      # 1 1 1 1   -> 15
num5 = num1 ^ num2      # 1 1 1 0   -> 14

print(num3)
print(num4)
print(num5)

# Shift Operators
# >>, <<
num1 = 11               # 1 0 1 1
num2 = 2                # 0 0 1 0

num3 = num1 >> num2     # 1 0 1 1 -> _ _ 1 0 -> 0 0 1 0
print("num3 is:",num3)

print("Fetch Back Original:",(num3 << num2))


num4 = num1 // (2 ** num2)
print(num4)

num5 = num1 << num2          # 1 0 1 1 -> 1 0 1 1 _ _ -> 1 0 1 1 0 0
print(num5)

num6 = num1 * (2 ** num2)
print(num6)

# Shifting Negative Numbers : Try Out
a1 = 10
a2 = 20

print(a1 is a2)
print(a1 is not a2)






