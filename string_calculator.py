skip_char = "\n"


class NegativeNumberException(Exception):
    pass


def add(numbers: str, default_delimiter=",") -> int:
    """
    String calculator to calculate the sum of all the integers in the string
    :param numbers: a string of delimiter-separated numbers
    :param default_delimiter: specifies the default delimiter
    :return: an integer, sum of the numbers
    :raises NegativeNumberException: raises an exception
    """
    numbers_sum = 0

    if not isinstance(numbers, str):
        return numbers_sum
    elif not numbers.strip():
        return numbers_sum

    # using accumulator pattern to compute sum
    for char in numbers.split(default_delimiter):
        number = int(char)
        numbers_sum += number

    return numbers_sum


# test cases
assert add("") == 0
assert add(" ") == 0

assert add(1) == 0
assert add((1,)) == 0
assert add([1, 2]) == 0

assert add("1,2,3") == 6
