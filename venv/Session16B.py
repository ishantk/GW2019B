def areaOfCircle(radius=3):
    area = 3.14 * radius * radius
    return area


print("Area os Circle with radius 2.2 is:",areaOfCircle(2.2))
print("Area os Circle with radius is:",areaOfCircle())
print("Area os Circle with radius 5.1 is:",areaOfCircle(radius=5.1))
print("Area os Circle with radius 6.6 is:",areaOfCircle(6.6))

# Reference Copy
fun = areaOfCircle

print(areaOfCircle)
print(fun)

print("Area os Circle with radius 6.6 is:",fun(6.6))


"""
    Lambda : is a function
             it is capable of computing a single expression
             it has no name
             it will have a reference variable so that we can use it !!
                 
"""

lRef1 = lambda radius : 3.14 * radius * radius
print("Area os Circle with radius 7.7 is:",lRef1(7.7))

lRef2 = lambda length=5, breadth=7 : length * breadth
print("Area of Rectangle is: ",lRef2(10,20))
print("Area of Rectangle is: ",lRef2())
print("Area of Rectangle is: ",lRef2(length=3, breadth=11))
print("Area of Rectangle is: ",lRef2(length=3))