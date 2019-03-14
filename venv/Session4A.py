# Conditional Constructs
isInternetConnected = True

# Simple if/else
if isInternetConnected:
    print("You can browse google Maps")
else:
    print("Please Connect to Internet and Try Again")

a = 10
b = 20
c = 30

# Nested if/else
if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
else:
    if b>c:
        print("b is greatest")
    else:
        print("c is greatest")

physics = 50
chemistry = 65
maths = 30

average = (physics + chemistry + maths)//3

# Ladder if/else
if average >=90:
    print(">> Grade A Awarded for Average of:",average)
elif (average >=70 and average < 90):
    print(">> Grade B Awarded for Average of:", average)
elif (average >=50 and average < 70):
    print(">> Grade C Awarded for Average of:", average)
else:
    print(">> Fail")


"""
    Assignment:
    John and Jack Assignment:
    They Plant bricks to create a Wall
    N = 7
                Bricks
    John : 1    1        
    Jack : 2    3
    John : 2    5
    Jack : 4    9 -> 7
    => Jack : 2 7
    
    Who Planted Last Brick(s) and how many ?

    for loop
    if/else


"""
