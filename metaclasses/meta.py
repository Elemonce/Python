class UpperCase(type):
    # __new__ is the method called before __init__
    # it's the method that creates the object and returns it 
    # while __init__ just initializes the object passed as parameter
    # __new__ is used when one wants to control how the object is created

    # here the created object is the class, and we want to customize it
    # so we override __new__

    # Some stuff can be done with __init__ and with overriding __call__

    # __new__ always receives the class it's defined in as the first parameter, just like we have self 
    # for ordinary methods that receive the instance as the first parameter 
    def __new__(cls, clsname, bases, attrs):
        uppercase_attrs = {
            attr if attr.endswith("__") else attr.upper() : value
            for attr, value in attrs.items()
        }
        
        return super().__new__(cls, clsname, bases, uppercase_attrs)
    


class Bird(metaclass=UpperCase):
    # An attribute is anything that you access by dot (bird.color, bird.sing()), so, both properties/values and methods.
    is_animal = True


    # A metaclass does not affect attributes in __init__ because this method is only executed when an instance is created.
    def __init__(self, color, beak):
        self.color = color
        self.beak = beak



bird = Bird("red", "pointy")

print(hasattr(bird, "color")) # True (attributes)
print(hasattr(bird, "is_animal")) # False
print(hasattr(bird, "IS_ANIMAL")) # True



# Everything is an object, even type
# Everything has a type
# Not everything is a type
# type is its own type, which is an exception.


# How can type inherit from object if object is an instance of type?
# - CPython (It can be defined as both an interpreter and a compiler, as it compiles Python code into bytecode before interpreting it).

# 1. Create empty shells.
#   - The interpreter allocates raw space for type and object
#   - Those aren't fully formed yet.

# 2. Wire them together manually. 


# Instances of a metaclass are classes.
# Instances of object are objects.