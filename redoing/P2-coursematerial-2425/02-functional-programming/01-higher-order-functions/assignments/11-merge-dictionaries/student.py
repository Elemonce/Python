def merge_dictionaries(d1, d2, merge_function):
    d = {}

    keys = set(d1.keys()).union(d2.keys())

    for key in keys:
        if key in d1.keys() and key in d2.keys():
            d[key] = merge_function(d1[key], d2[key])
        elif key in d1.keys():
            d[key] = d1[key]
        else:
            d[key] = d2[key]

    return d