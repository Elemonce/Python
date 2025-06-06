from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        ...

# 1. To use a decorator @abstractmethod, the class's metaclass must be ABCMeta or derived from it.
    @property
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @property
    def perimeter(self):
        return 2 * pi * self.radius

    @property
    def area(self):
        return pi * self.radius ** 2
    
# In python, classes are objects as well. When reading the lines of code, python creates a Circle object out of the description.
# This object (or also a class, in this case) is capable of creating other objects, or instances. But still, it's an object. 

# Like all objects, you can assign it to a variable.
AnotherCircle = Circle

# You can attach attributes to it
AnotherCircle.test = "foo" # Or Circle.test = "foo"
print(Circle.test)

# You can pass it as a function paramater
print(AnotherCircle) # the class is still Circle

print(AnotherCircle(radius=5)) # the name of the object is still Circle

def choose_class(name):
    if name == "foo":
        class Foo(object):
            pass
        return Foo # Return the class, not an instance
    else:
        class Bar:
            pass
        return Bar # Return the class, not an instance

MyClass = choose_class("foo") # The function returns a class, not an instance

def add(number1, number2):
    return number1 + number2

MyClass.add = add

print(MyClass.add(3, 2))

class Test:
    pass

print(type(Test))
print(type(Circle(5)))

# You can also create a class using type() function.
# type(name, bases, attrs); name - name of the classes, bases - tuple of the parent class (for inheritance, can be empty); attrs - dictionary containing attributes' names and values

SomeClass = type("SomeClass", (), {"boolean_attribute": True, "string_attribute":"test"}) # The name of the variable (class SomeClass) could be different from the first paramater of type
                                                                                          # The actual name of the class is the "name" parameter of type.
print(SomeClass)
some_class = SomeClass()
print(some_class.boolean_attribute)


def print_attribute(self):
    print(self.attribute)

def print_something():
    print("something")
    return 1

    
                                                                                                                                     # passing print_something() here executes the function; however, the value of print_something (the attribute)
                                                                                                                                     # in the class is 1, as that's what the return value of the function is
SomeClassChild = type("SomeClassChild", (SomeClass,), {"attribute": "hello from someclasschild", "print_attribute": print_attribute, "print_something": print_something()})

some_class_child = SomeClassChild()
print(some_class_child.boolean_attribute) # inherits from SomeClass
print(some_class_child.attribute)
some_class_child.print_attribute()
print(some_class_child.print_something) # prints 1 (So, in the class, print_something is just an attribute rather than a function, as its value is assigned to the return value of the function rather than the function itself)


def one_more_method(self):
    print(self, "One more method")

SomeClassChild.one_more_method = one_more_method # You can add functions to a class after creating it

some_class_child.one_more_method()


# Metaclasses
# A metaclass is what creates class objects. (A "class factory.")


# Type is a metaclass
# Everything is an object in Python. That includes integers, strings, functions, and classes. All of them have been created from a class. 

age = 35
print(age.__class__) # class int
print(age.__class__.__class__) # class type


# Custom metaclasses
# The main purpose of a metaclass is to change the class automatically, when it's created.
# You usually do this for APIs, where you want to create classes matching the current context.


# Imagine you decide that all classes in your module should have their attributes written in uppercase. One way to do it is to use __metaclass__ at the module level.
# This way, all the classes of this module will be created using this metaclass.

# __metaclass__ can be a callable; it doesn't need to be a formal class.

# the same arguments will be passed to the metaclass as those that are usually passed to "type"
def upper_attr(future_class_name, future_class_parents, future_class_attrs):
    """
    Return a class object, with the list of its attributes turned
    into uppercase.
    """

    # Pick up any attribute that doesn't start with __ and uppercase it.
    # The key is the attribute name and the value is the attribute's value
    uppercase_attrs = {
        attr if attr.startswith("__") else attr.upper() : v
        for attr, v in future_class_attrs.items()
    }

    # let "type" do the class creation
    return type(future_class_name, future_class_parents, uppercase_attrs)

# __metaclass__ = upper_attr # This will affect all classes in the module (Python 2 not python 3)

TestClass = upper_attr("TestClass", (), {"test_attribute": "something"})


print(hasattr(TestClass, "test_attribute"))
print(hasattr(TestClass, "TEST_ATTRIBUTE"))


print(isinstance(object, type))

