def count(xs, condition):
    count = 0
    for x in xs:
        if condition(x):
            count += 1

    return count

def count_older_than(people, min_age):
    def is_of_min_age(human):
        return human.age >= min_age

    return count(people, is_of_min_age)


def indices_of(xs, condition):
    indices = []

    for i in range(len(xs)):
        if condition(xs[i]):
            indices.append(i)
    
    return indices


def indices_of_cards_with_suit(cards, suit):
    def is_of_suit(card):
        return card.suit == suit

    return indices_of(cards, is_of_suit)


