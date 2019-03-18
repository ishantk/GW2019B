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

    N = 3
                Bricks
    John : 1    1
    Jack : 2    3
    => Jack : 3

    N = 11
                Bricks
    John : 1    1
    Jack : 2    3
    John : 2    5
    Jack : 4    9
    John : 3    12 | 12-11 = 1
                   | 12-9  = 3

    N = 13
                Bricks
    John : 1    1
    Jack : 2    3
    John : 2    5
    Jack : 4    9
    John : 3    12
    Jack : 6    18   >
                     N - BC = 1

    Who Planted Last Brick(s) and how many ?

    for loop
    if/else

"""

def brickProblem():
    N = int(input("How many bricks ? "))
    brickCount = 0

    for john in range(1, N+1):

        brickCount = brickCount + john
        if brickCount > N:
            print(">> John Planted Last Brick(s)",(brickCount-N))
            break # is used to terminate the loop (Explore continue keyword)
        elif brickCount == N:
            print(">> John Planted Last Brick(s)", john)
            break
        else:
            print(">> John Planted", john, "Brick(s)")

        jack = john*2

        brickCount = brickCount + jack
        if brickCount >= N:
            print("** Jack Planted Last Brick(s) ",(brickCount-N))
            break # is used to terminate the loop (Explore continue keyword)
        elif brickCount == N:
            print("** Jack Planted Last Brick(s)", jack)
            break
        else:
            print("** Jack Planted", jack, "Brick(s)")

brickProblem()