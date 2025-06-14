# Write the following functions:

# title_to_director(movies) returns a dict whose keys are movie titles and values are the corresponding director.
# director_to_titles(movies) returns a dict where keys are directors and values are lists of movie titles by that director. You will need to combine different kinds of comprehensions for this one. Note that we are not looking for an efficient solution.

def title_to_director(movies):
    return {movie.title : movie.director for movie in movies}
    
def director_to_titles(movies):
    return {movie_d.director : [movie.title for movie in movies if movie.director == movie_d.director] for movie_d in movies}