class Parent:

    a = 0

    def __init__(self, x):
        self.x = x
        print(">> Parent Object Constructed")

    def show(self):
        print("x is:",self.x)


class Child(Parent):
    pass

"""
p1 = Parent(20)
p1.y = 10

print(p1.__dict__)
print(Parent.__dict__)
"""

c1 = Child(10)

print(c1.__dict__)
print(Child.__dict__)

print("a is:",Child.a)

print(Parent.__dict__)

c1.show()

# H.W.: test protected and private concepts in this IS-A Relation