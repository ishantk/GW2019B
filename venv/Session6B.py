# Default Values to Inputs of a Function
# Default Arguments
# def add(a, b=10): OK
# def add(a=10, b): ERR
def add(a, b=10):
    c = a+b
    return c

print("Addition is:",add(10, 20)) # add(10, 20) -> Executing a Function
print("Addition is:",add(11))