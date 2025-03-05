class NegativeNumberException(Exception):
    pass


def add(numbers: str) -> int:
    """
    String calculator to calculate the sum of all the integers in the string
    :param numbers: string of numbers with delimiter
    :return: sum of all the integers in the string
    :raises NegativeNumberException: raises an exception
    """
    numbers_sum = 0
    return numbers_sum


# test cases
assert add("") == 0