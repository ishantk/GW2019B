# Whatever we write in class that becomes property of class
class Counter:

    # Property of Class
    myCounter = 1

    def __init__(self):
        self.count = 1 # Property of Object

    def incrementCount(self):
        self.count = self.count + 1
        Counter.myCounter = Counter.myCounter + 1

    def showCount(self):
        print("Count is: ",self.count," and myCounter is: ",Counter.myCounter)

c1 = Counter() # Object Construction
c2 = Counter() # Object Construction
c3 = c1        # Reference Copy

print("c1 is: ",c1)
print("c2 is: ",c2)
print("c3 is: ",c3)

print("c1 has: ",c1.__dict__)
print("c2 has: ",c2.__dict__)
print("c3 has: ",c3.__dict__)
print(Counter.__dict__)

# c1.incrementCount() -> Counter.incrementCount(c1)
Counter.incrementCount(c1)
c2.incrementCount() # -> Counter.incrementCount(c2)
c3.incrementCount()
c3.incrementCount()

# c1.showCount() # Count is: 4
Counter.showCount(c1)
c2.showCount() # Count is: 2
c3.showCount() # Count is: 4


