def group_by(xs, key_function):
    d = {}
    for x in xs:
        if d.get(key_function(x)) is None:
            d[key_function(x)] = [x]
        else:
            d[key_function(x)].append(x)
    
    return d


