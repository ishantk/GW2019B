str1 = "Hello"
str2 = "Hello"

print(hex(id(str1)))
print(hex(id(str2)))

str3 = "John, Jennie, Jim, Jack, Joe"

# String Comparison : Comparing HashCodes
if str1 == str2:
    print("Strings are Equal")
else:
    print("Strings are Not Equal")

# Strings are IMMUTABLE -> We cannot change them
str4 = str3.upper()
print("str3 is:",str3)
print("str4 is:",str4)

length = len(str4)
print("Length is:",length)

print(str3[0])
print(str3[length-1])
print(str3[-1])
print(str3[-6])

# str3 = "John, Jennie, Jim, Jack, Joe"

print("slicing positive index:",str3[1 : 4])      # 1 inclusive, 4 exclusive, less than 4
print("slicing negative index:",str3[-5 : -1])

print("slicing:",str3[0 : len(str3)])

# Print Reverse of String
for i in range(0, len(str3), 1):
    print(str3[i], end="")

print()

for i in range(-1, -(len(str3)+1), -1):
    print(str3[i], end="")
