def take_while(xs, condition):
    lst1 = []
    lst2 = []

    for i in range(len(xs)):
        if condition(xs[i]):
            lst1.append(xs[i])
        else:
            lst2 += xs[i:]
            break
    
    return (lst1, lst2)