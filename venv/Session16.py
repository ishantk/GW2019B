# OVERRIDING -> Re-Defining the same method in Child which was in Parent
class Parent:

    def showVehicle(self):
        print("Vehicle is Maruti Swift")

class Child(Parent):

    # Overriding
    def showVehicle(self):
        # Parent.showVehicle(self)
        print("Vehicle is Honda City")

print("Parent Class Dictionary ",Parent.__dict__)
print("Child Class Dictionary ",Child.__dict__)

c1 = Child()
print("c1 Dictionary", c1.__dict__)

c1.showVehicle() # -> Child.showVehicle(c1)