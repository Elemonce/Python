# xs = ['a', 'b', 'c']
# ys = [1, 2, 3]
# # list(zip(xs, ys))
# # [('a', 1), ('b', 2), ('c', 3)]


# # xs = ['a', 'b', 'c']
# # list(enumerate(xs))
# # [(0, 'a'), (1, 'b'), (2, 'c')]

# Write the following functions and rely on comprehensions and the functions above.

# movie_count(movies, director) returns the number of movies made by director.
# longest_movie_runtime_with_actor(movies, actor) returns the runtime duration of the longest movie in which actor appears.
# has_director_made_genre(movies, director, genre) returns True is director made a movie of the given genre.
# is_prime(n) checks whether n is a prime number, i.e., that it is only divisible by 1 and itself.
# is_increasing(ns) checks whether the values in ns appear in nondecreasing order. For example, is_increasing([1, 1, 2, 3, 4, 6]) should return True, whereas is_increasing([3, 2, 1]) should yield False.
# count_matching(xs, ys) counts how many of the corresponding elements are equal. For example, count_matching([1, 2, 3], [3, 2, 1]) should return 1, because only equal values on equal positions are counted.
# weighted_sum(ns, weights) should multiply each value in ns with its corresponding weight in weights and return the sum of these products. For example, weighted_sum([a, b, c], [x, y, z]) should return a * x + b * y + c * z.
# alternating_caps(string) should change the case of each character such that they alternate between upper and lower case. For example, alternating_caps("abcdef") should return AbCdEf.
# find_repeated_words(sentence) first collects all words in the given string sentence. A word is defined as a series of letters (can be both upper and lowercase). Next, the function has to look for repeated consecutive words
#  and collect them in a set. The case of letters should be ignored: "dog" and "Dog" are to be considered the same word.
#  For example, find_repeated_words("This sentence has has repeated words. Words.") should return the set {'has', 'words'}.
#  The returned set should contain all of its words in lower case. Note also that interpunction, spaces, etc. should also have no impact on deciding whether a word is repeated or not.


def movie_count(movies, director):
    return len([movie for movie in movies if movie.director == director])

def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])

def has_director_made_genre(movies, director, genre):
    return any([True if movie.director == director and genre in movie.genres else False for movie in movies])

def is_prime(n):
    return len([number for number in range(1, n+1) if n % number == 0]) == 2

def is_increasing(ns):
    return all([True if ns[i] <= ns[i+1] else False for i in range(0, len(ns) - 1)])

def count_matching(xs, ys):
    return sum([1 if len(ys) - 1 >= i and xs[i] == ys[i]  else 0 for i in range(len(xs))])

def weighted_sum(ns, weights):
    return sum([ns[i] * weights[i] if len(weights) - 1 >= i else 0 for i in range(len(ns))])

def alternating_caps(string):
    return "".join(string[i].upper() if i % 2 == 0 else string[i] for i in range(len(string)))


    # return {word[i][1] for i in range (len(enum))}

def find_repeated_words(sentence):
    changed = " ".join(sentence.lower().split()).replace(",", "").replace(".", "")
    # variable = "".join("".join(changed.lower().split(",")).split("."))
    variable_lst = changed.split(" ")
    
    return {variable_lst[i] for i in range(len(variable_lst) -1) if variable_lst[i] == variable_lst[i+1]}


def find_repeating_words(sentence):
    variable = "".join("".join(sentence.lower().split(",")).split("."))
    variable_lst = variable.split(" ")

    enum = list(enumerate(variable_lst))

    # words = set()
    # for number, word in enum:
    #     for number2, word2 in enum:
    #         if word == word2 and number != number2:
    #             words.add(word)

    # return words

    # words = set()
    # for i in range(len(enum)):
    #     for j in range(len(enum)):
    #         if enum[i][1] == enum[j][1] and enum[i][0] != enum[j][0]:
    #             words.add(enum[i][1])

    # return words

    return {enum[i][1] for i in range(len(enum)) for j in range(len(enum)) if enum[i][1] == enum[j][1] and enum[i][0] != enum[j][0]}







print(find_repeating_words("I am am somebody and and you are are somebody else and we are having a great day."))





# xs = ['a', 'b', 'c']
# ys = ['a', 'b']
# # ys = [1, 2, 3]

# lst = list(zip(xs, ys))

# print(lst)

print()
print(find_repeating_words("this is is a test this is also a test"))


print(" ".join("jfeuw jeiwf fjwie     jfweiofwe    ewfj wei f".split()))