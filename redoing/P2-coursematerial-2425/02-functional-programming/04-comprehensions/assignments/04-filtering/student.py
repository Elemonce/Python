# Write the following functions:

# movies_from_year(movies, year) returns the titles of movies from the given year.
# movies_with_actor(movies, actor) returns the titles of movies that have actor in it.
# divisors(n) returns the divisors of n in increasing order. For example, divisors(12) should return [1, 2, 3, 4, 6, 12].

def movies_from_year(movies, year):
    return [movie.title for movie in movies if movie.year == year]

# def movie_title(movie):
#     return movie.title

# def movies_from_year(movies, year):
    # return list(map(movie_title, movies) for movie in movies if movie.year == year)
    
    # This doesn't work because we create a map object for every movie whose year satisfies the if statement.
    # That means that if there are 10 out of 20 movies that satisfy the condition, the return value is going to be
    # a list of 10 map objects with each of them contaning 20 movies.
    # return list(map(lambda movie : movie.title, movies) for movie in movies if movie.year == year)

    # filtered_movies = filter(lambda movie : movie.year == year, movies)
    # return list(map(lambda movie: movie.title, filtered_movies))
    # return list(map(movie_title, filtered_movies))


def movies_with_actor(movies, actor):
    return [movie.title for movie in movies if actor in movie.actors]

# def movie_title(movie):
#     return movie.title

# def movies_with_actor(movies, actor):
#     filtered_movies = filter(lambda movie : actor in movie.actors, movies)
#     return list(map(lambda movie: movie.title, filtered_movies))
    # return list(map(movie_title, filtered_movies))


def divisors(n):
    return [i for i in range(1, n+1) if n % i == 0]

# Can't use mapping because there's nothing to map (get output out of input)
# def divisors(n):
#     def is_divisor(number):
#         return n % number == 0
    
#     numbers = range(1, n+1)

#     # return list(filter(is_divisor, numbers))
#     return list(filter(lambda number : n % number == 0, numbers))
