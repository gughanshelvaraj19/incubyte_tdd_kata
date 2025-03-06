from typing import Generator, Union
from functools import lru_cache

from conf import DEFAULT_DELIMITER, OUTPUT_FILE


class NegativeNumberException(Exception):
    """
    Negative number exception
    """

    pass


def stream_file(inout_file):
    with open(inout_file, "r") as file:
        for line in file:
            yield line


def ondemand_char_gettr(number_string: str) -> Union[Generator, tuple]:
    """
    On demand text getter
    :param number_string: a string of delimiter-separated numbers
    :return Generator: an integer number iterable or None
    """
    char_accumulator = ""
    idx = None
    for idx, char in enumerate(number_string):
        char = char.strip()

        # filters numeric characters
        if char.isnumeric():
            char_accumulator += char
        # filters non-numeric character and yields accumulated numeric chars
        elif char.isascii() and char_accumulator.isnumeric():
            numeric_value: int = int(char_accumulator)

            # skips yielding values greater than 1000
            if numeric_value > 1000:
                char_accumulator = ""
                continue

            # validates for negative number and yield negative value if exists
            has_minus = number_string[abs(idx - len(char_accumulator) - 1)] == "-"
            yield numeric_value if not has_minus else -numeric_value
            char_accumulator = ""
    else:
        # yields last accumulated numeric value
        if char_accumulator.isnumeric():
            leftover_value: int = int(char_accumulator)
            if idx:
                has_minus = number_string[idx - len(char_accumulator)] == "-"
                yield leftover_value if not has_minus else -leftover_value
    return ()


@lru_cache(maxsize=3)
def add(numbers: str, raise_exception: bool = True) -> int:
    """
    String calculator to calculate the sum of all the integers in the string
    :param numbers: a string of delimiter-separated numbers
    :param raise_exception: disable or enable raise exception, defaults to enable
    :return: an integer sum of all numbers in string
    :raises NegativeNumberException: raises an exception
    """
    numbers_sum = 0
    negatives_exists = False

    # validates input string
    if not isinstance(numbers, str):
        return numbers_sum
    elif not numbers.strip() or not numbers.strip(DEFAULT_DELIMITER):
        return numbers_sum

    # using accumulator pattern for summation of numbers
    with open("negatives.txt", "w") as fp:
        for number in ondemand_char_gettr(numbers):
            if number < 0:
                negatives_exists = True
                fp.write(str(number) + ",")
                continue
            numbers_sum += number

    if negatives_exists and raise_exception:
        raise NegativeNumberException(
            f"Negative numbers not allowed <{''.join(stream_file(OUTPUT_FILE))}>"
        )

    return numbers_sum


if __name__ == "__main__":
    print("Hey! Thanks for this opportunity, it was fun solving. :)")
