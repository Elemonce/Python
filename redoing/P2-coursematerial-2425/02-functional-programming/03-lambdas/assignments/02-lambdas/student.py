class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


def group_by(xs, key_function):
    result = {}
    for x in xs:
        key = key_function(x)
        if key not in result:
            result[key] = []
        result[key].append(x)
    return result


def partition(xs, condition):
    true_list = []
    false_list = []

    for x in xs:
        if condition(x):
            true_list.append(x)
        else:
            false_list.append(x)

    return (true_list, false_list)

# group_by_suit(cards) groups cards by their suit.
# group_by_value(cards) groups cards by their value.
# partition_by_color(cards) splits cards into two lists: the first list contains only black cards, the second list only red cards. The color of a card is determined by its suit: spades and clubs are black, hearts and diamonds are red.


# group_by_suit = lambda cards : 

def group_by_suit(cards):
    get_suit = lambda card : card.suit

    return group_by(cards, get_suit)


def group_by_value(cards):
    get_value = lambda card : card.value

    return group_by(cards, get_value)

def partition_by_color(cards):
    # is_black = lambda card : True if card.suit in ("spades", "clubs") else False
    is_black = lambda card : card.suit in ("spades", "clubs")

    return partition(cards, is_black)