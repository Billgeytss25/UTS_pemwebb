# Base class
class BaseClass:
    def method1(self):
        print("Method 1 from BaseClass")

    def method2(self):
        print("Method 2 from BaseClass")

# Child class 1 (inherits from BaseClass)
class ChildClass1(BaseClass):
    def method3(self):
        print("Method 3 from ChildClass1")

    def method4(self):
        print("Method 4 from ChildClass1")

# Child class 2 (inherits from BaseClass)
class ChildClass2(BaseClass):
    def method5(self):
        print("Method 5 from ChildClass2")

    def method6(self):
        print("Method 6 from ChildClass2")

# Creating objects of ChildClass1 and ChildClass2 and calling methods
child1_obj = ChildClass1()
child1_obj.method1()  # From BaseClass
child1_obj.method3()  # From ChildClass1

child2_obj = ChildClass2()
child2_obj.method2()  # From BaseClass
child2_obj.method6()  # From ChildClass2
