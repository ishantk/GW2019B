file = open("Session17.py","r")

# Read Line by Line
"""
line = file.readline()
print(line)

line = file.readline()
print(line)

"""

lines = file.readlines()
print("type of lines is:",type(lines))

for line in lines:
    print(line)


"""
    read() will read the entire file once at a time
    readline() will read the line by line
    readlines() will read all the lines into a list

    > WAP where count number of objects in a python file
      a = 10
      nums = (10, 20, 30, 40, 50)
      
    > Which type of objects and with count
    int      -> 2
    float    -> 5
    Employee -> 3  
    
    
    
"""




