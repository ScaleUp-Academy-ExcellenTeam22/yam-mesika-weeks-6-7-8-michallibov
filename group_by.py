import itertools


def group_by(key_func, iterable) -> dict:
    """
    This function gets a key function that is going to be the key of the dictionary and
    an iterable object from which we built a dictionary
    :param key_func: the key of the dictionary
    :param iterable: the iterable object from which we built a dictionary
    :return: a dictionary in which the key is the key_func and the values are taken from
    the iterable object.
    """
    dict_of_len = {k: list(g) for k, g in itertools.groupby(sorted(iterable, key=key_func), key_func)}
    return dict_of_len


if __name__ == '__main__':
    print(group_by(len, {"hi", "bye", "yo", "try"}))
