# File IO in Python
# Read and Write in Files

# file = open("Session16C.py")
# file = open("/Users/ishantkumar/Downloads/notes.txt")
print("File is:",file)
print("Type of File is:",type(file))

print()

fileContents = file.read() # Read Once everything in file
print(fileContents)
print("Type of fileContents is: ",type(fileContents))

print()

# We are trying to re-read the file
fileContents = file.read()
print("After re-read:",fileContents)