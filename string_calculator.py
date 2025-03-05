class NegativeNumberException(Exception):
    pass


def add(numbers: str) -> int:
    """
    String calculator to calculate the sum of all the integers in the string
    :param numbers: a string of delimiter-separated numbers
    :return: an integer, sum of the numbers
    :raises NegativeNumberException: raises an exception
    """
    numbers_sum = 0

    if not isinstance(numbers, str):
        return numbers_sum
    elif not numbers.strip():
        return numbers_sum

    return numbers_sum


# test cases
assert add("") == 0
assert add(" ") == 0

assert add(1) == 0
assert add((1,)) == 0
assert add([1, 2]) == 0
