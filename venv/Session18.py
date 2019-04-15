file = open("data.txt","r")

four = "1 0 0 1"
seven = "1 1 1 1"
zero = "0 1 1 0"

n1 = 0
n2 = 0
n3 = 0


line = file.readline()
line = line.strip()

print(type(line))

if line == four:
    n1 = 4
elif line == seven:
    n2 = 7
elif line == zero:
    n3 = 0

print("n1 is:",n1)