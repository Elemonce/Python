def age_condition(human):
    if human.age < 18:
        return True
    return False

def partition(lst, condition):
    lst1 = []
    lst2 = []

    for element in lst:
        if condition(element):
            lst1.append(element)
        else:
            lst2.append(element)

    return (lst1, lst2)

def children_and_adults(people):
    return partition(people, age_condition)
