file = open("Session17.py","r")
data = file.read(15)
print(data)

data = file.read(5)
print(data)

file.close() # Release Memory Resources
print("Is File Closed? ",file.closed)