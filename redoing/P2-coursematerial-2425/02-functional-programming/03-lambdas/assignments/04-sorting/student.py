# Write the following functions. Each function must leave its argument unmodified and return a new list.

# sort_by_age(people) orders the Persons by increasing age.
# sort_by_decreasing_age(people) orders the Persons by decreasing age.
# sort_by_name(people) orders the Persons by name, alphabetically.
# sort_by_name_then_age(people) orders the Persons by name, and in case of equal names, by increasing age
# sort_by_name_then_decreasing_age(people) orders the Persons by name, and in case of equal names, by decreasing age


def sort_by_age(people):
    # people.sort(key = lambda person : person.age)
    # return people

    # Using sorted instead because .sort() modifies given list rather than creates a copy and returns None
    return sorted(people, key=lambda person : person.age)

def sort_by_decreasing_age(people):
    return sorted(people, key=lambda person : person.age, reverse=True)


def sort_by_name(people):
    return sorted(people, key=lambda person : person.name)


def sort_by_name_then_age(people):
    return sorted(people, key=lambda person : (person.name, person.age))

def sort_by_name_then_decreasing_age(people):
    people = sort_by_decreasing_age(people) 
    people = sort_by_name(people)

    return people

def print_name_and_age(people):
    for human in people:
        print(human.name, human.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


lst = [        Person('John', 18),
        Person('Sarah', 19),
        Person('Peter', 19),
        Person('John', 20),
        Person('Kim', 17),
        Person('Kim', 18),
        Person('Kim', 19)]


print(print_name_and_age(sort_by_name_then_decreasing_age(lst)))