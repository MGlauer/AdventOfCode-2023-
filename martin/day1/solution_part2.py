import re

NUMBER_LOOKUP = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    **{str(i): i for i in range(10)},
}  # mapping zero->0, ..., nine->9, 0->0,..., 9->9,

NUMBER_REGEX = "|".join(
    NUMBER_LOOKUP.keys()
)  
# Regular expression that matches all digits as words or as numbers
# Looks like this: zero|one|two|three|four|five|six|seven|eight|nine|0|1|2|3|4|5|6|7|8|9

def get_first_and_last_digit(line):
    """
    For a given line, returns the first occurence and last occurence of any digit
    """
    first = NUMBER_LOOKUP[re.search(NUMBER_REGEX, line)[0]]  # Look for the first number

    # Reverse the string, and look for the first occurence of a reversed
    # number. Given a string s, s[::-1] reverses that string.
    last = NUMBER_LOOKUP[re.search(NUMBER_REGEX[::-1], line[::-1])[0][::-1]]
    return 10 * int(first) + int(last)


def run():
    with open("input.txt") as input_file:
        print(sum(map(get_first_and_last_digit, input_file)))


if __name__ == "__main__":
    run()
