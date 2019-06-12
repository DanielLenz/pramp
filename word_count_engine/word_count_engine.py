import string
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


def parse_string(my_string):
    my_string = my_string.lower()
    my_string = "".join((ch for ch in my_string if ch not in string.punctuation))

    return my_string


def word_count_engine(my_string):

    my_string = parse_string(my_string)
    list_of_words = my_string.split(" ")
    print(list_of_words)
    counter = OrderedCounter(list_of_words)

    output = [[key, str(value)] for key, value in counter.most_common()]

    return output


if __name__ == "__main__":

    test_document = (
        "Practice makes perfect youll only get Perfect by practice just practice"
    )
    print(word_count_engine(test_document))
