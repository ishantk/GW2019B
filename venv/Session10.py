"""

    Algo Test | Functions

    A : 1
    B : 2
    C : 3
    .
    ..
    ...
    ..
    .
    Z : 26

    Problem1:
    Enter some String of Your Choice?
    Input : ABC
    1 + 2 + 3 = 6 -> F

    if sum is > 26 than divide by 26 and you shall get a remainder

    sum       -> 29
    remainder -> 3 -> C
    remainder -> 0 | A or Z

    Problem2:
    Enter Word1
    Enter Word2

    ABC
    ABC
    Addition
    2 4 6
    B D F

    Hints : String Slicing

"""

alphabets = {"A":1, "B":2}

data = input("Enter Some String of your Choice: ")
print("Processing",data,"...")