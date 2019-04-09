file = open("/Users/ishantkumar/Downloads/auri_student.csv")
data = file.read()
# data = file.readlines()

# for line in data:
#     print(line)

print(data)

file.close()

print()

file = open("/Users/ishantkumar/Downloads/flex.png")
data = file.read()
print(data)