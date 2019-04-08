class Point:

    count = 0

    def __init__(self):
        Point.count = Point.count + 1

    def showObjectCount(self):
       print("Point Objects: ",Point.count)


p1 = Point()
p2 = Point()
p3 = Point()
p4 = p1
p5 = Point()
p6 = p3


p1.showObjectCount() # Point Objects : 4