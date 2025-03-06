from conf import DEFAULT_DELIMITER, DEFAULT_BUFFER_SIZE


class NegativeNumberException(Exception):
    pass


def ondemand_char_gettr(number_string: str):
    """
    On demand text getter
    :param number_string: a string of delimiter-separated numbers
    """
    char_accumulator = ""
    for char in number_string:
        char = char.strip()
        if char.isnumeric():
            char_accumulator += char
        elif char.isascii() and char_accumulator.isnumeric():
            yield int(char_accumulator)
            char_accumulator = ""
    else:
        if char_accumulator.isnumeric():
            yield int(char_accumulator)


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
    elif not numbers.strip() or not numbers.strip(DEFAULT_DELIMITER):
        return numbers_sum

    for number in ondemand_char_gettr(numbers):
        numbers_sum += number
    return numbers_sum


if __name__ == "__main__":
    print("Hey! Have a great day")
