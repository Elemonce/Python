# Write the following functions:

# directors(movies) collects all directors in a set.
# common_elements(xs, ys) should return the set of values that occur both in xs and ys.

def directors(movies):
    return {movie.director for movie in movies}

# def directors(movies):
#     def movie_director(movie):
#         return movie.director
#     return set(map(movie_director, movies))


def common_elements(xs, ys):
    return {value for value in xs if value in ys}

# def common_elements(xs, ys):
#     return set(filter(lambda x : x in xs and x in ys, xs))