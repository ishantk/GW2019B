class Student:
    def __init__(self, roll, name, age):
        self.rollNum = roll
        self._fullName = name
        self.__age = age

    def showStudentDetails(self):
        print("{} belongs to {} and is {} years old".format(self.rollNum, self._fullName, self.__age))

    # Protected : Please do not use it !!
    def _hello(self):
        print("Hello dear {}".format(self._fullName))

    # Private : Please do not use it !!
    def __bye(self): # -> __bye shall be mangled to _Student__bye() | Name Mangling
        print("B.Bye dear {}".format(self._fullName))


s1 = Student(1, "John", 20)
s2 = Student(2, "Fionna", 22)

print(s1.__dict__)
print(s2.__dict__)

s1.showStudentDetails()
s2.showStudentDetails()

s1._hello()
s2._hello()

# s1.__bye() -> error

print(Student.__dict__)

s1._Student__bye()
s2._Student__bye()

print(s1.__dict__)

print("s1 roll num is:",s1.rollNum)
print("s1 full name is:",s1._fullName)
print("s1 age is:",s1._Student__age)

# Name Mangling : Will append _ClassName in front of __VarName
