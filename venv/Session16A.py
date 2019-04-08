# Polymorphism : Only Supports Run Time Polymorphism

class Cab:
    # Constructor
    def __init__(self):
        print(">> Cab Object Constructed")

    # Function/Method
    def bookCab(self, source, destination):
        print(">> Cab booked from {} to {}".format(source, destination))

# MiniCab IS-A Cab
class MiniCab(Cab):
    # def __init__(self):
    #     print(">> MiniCab Object Constructed")

    def bookCab(self, source, destination):
        print(">> MiniCab booked from {} to {}".format(source, destination))

class SharedCab(Cab):
    # def __init__(self):
    #     print(">> MiniCab Object Constructed")

    def bookCab(self, source, destination):
        print(">> SharedCab booked from {} to {}".format(source, destination))


# c1 = Cab()
c1 = MiniCab()
c1.bookCab("Auribises", "SilverArc Mall") # MiniCab

c1 = SharedCab()
c1.bookCab("Auribises", "SilverArc Mall") # SharedCab

"""
    1. Single Level
    A
    |
    B
    
    class A:
        pass
        
    class B(A):
        pass    
        
    2. Multi Level
    A
    |
    B
    |
    C
    
    class A:
        pass
        
    class B(A):
        pass
        
    class C(B):
        pass 
        
    3. Multiple
    A   B
      |
      C  
    class A:
        pass
        
    class B:
        pass
        
    class C(A,B):
        pass
    
    4. Heirarchy
    A
    |
  B   C
  
    5. Hybrid
    A
    |
    B
    |
    C
    |
  D   E    F
    |      |
    G    H   I
                      



"""