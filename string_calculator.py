from typing import Generator, Union
from functools import lru_cache

from conf import DEFAULT_DELIMITER


class NegativeNumberException(Exception):
    """
    Negative number exception
    """

    pass


def ondemand_char_gettr(number_string: str) -> Union[Generator, tuple]:
    """
    On demand text getter
    :param number_string: a string of delimiter-separated numbers
    :return Generator: an integer number iterable or None
    """
    char_accumulator = ""
    for char in number_string:
        char = char.strip()

        # filters numeric characters
        if char.isnumeric():
            char_accumulator += char
        # filters non-numeric character and yields accumulated numeric chars
        elif char.isascii() and char_accumulator.isnumeric():
            numeric_value: int = int(char_accumulator)
            if numeric_value > 1000:
                char_accumulator = ""
                continue
            yield numeric_value
            char_accumulator = ""
    else:
        # yields last accumulated numeric value
        if char_accumulator.isnumeric():
            yield int(char_accumulator)
    return ()


@lru_cache(maxsize=3)
def add(numbers: str) -> int:
    """
    String calculator to calculate the sum of all the integers in the string
    :param numbers: a string of delimiter-separated numbers
    :return: an integer sum of all numbers in string
    :raises NegativeNumberException: raises an exception
    """
    numbers_sum = 0

    # validates input string
    if not isinstance(numbers, str):
        return numbers_sum
    elif not numbers.strip() or not numbers.strip(DEFAULT_DELIMITER):
        return numbers_sum

    # using accumulator pattern for summation of numbers
    for number in ondemand_char_gettr(numbers):
        # filters number greater than 1000
        numbers_sum += number
    return numbers_sum


if __name__ == "__main__":
    print("Hey! Thanks for this oppurtunity, it was fun solving. :)")
