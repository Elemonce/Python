def count_movies_from_year(movies, year):
    counter = 0
    for movie in movies:
        if movie.year == year:
            counter += 1
    return counter

def select_movies_with_actor(movies, actor):
    result_movies = []
    for movie in movies:
        if actor in movies.actors:
            result_movies.append(movie)
    return result_movies


def sum_movie_duration_from_period(movies, start_year, end_year):
    total_duration = 0
    for movie in movies:
        if movie.year >= start_year and movie.year < end_year:
            total_duration += movie.duration
    return total_duration


def get_directors_of_actor(movies, actor):
    directors = []
    for movie in movies:
        if actor in movie.actors:
            directors.append(movie.director)
    return directors

def find_string_starting_with(strings, character):
    for string in strings:
        if len(string) != 0 and string[0].lower() == character:
            return string
    return None

def find_number_greater_than(numbers, threshold):
    for number in numbers:
        if number > threshold:
            return number
    return None

def repeat(function, n):
    for _ in range(n):
        function()

    return None