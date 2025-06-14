def titles(movies):
    return [movie.title for movie in movies]


# def movie_title(movie):
#     return movie.title

# def titles(movies):
#     return list(map(movie_title, movies))

# def titles(movies):
#     return list(map(lambda movie: movie.title, movies))

def titles_and_years(movies):
    return [(movie.title, movie.year) for movie in movies]

def titles_and_actor_counts(movies):
    return [(movie.title, len(movie.actors)) for movie in movies]

def reverse_words(sentence):
    # The string whose method is called is inserted in between each given string. (in this case, the string whose method is called is " ") The return value is the new concatenated string with the called string's value in between every single other string in the list.
    return " ".join([word[::-1] for word in sentence.split(" ")])