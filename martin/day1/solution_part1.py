def get_first_and_last_digit(line):
    """
    Returns the concatenation of the first and last digit in `line`.
    """
    digits = [c for c in line if c.isdigit()]  # get all digits
    return 10 * int(digits[0]) + int(
        digits[-1]
    )  # Concatenation of two single digits a,b is equivalent to 10*a+b


def run():
    with open("input.txt") as input_file:
        print(
            sum(map(get_first_and_last_digit, input_file))
        )  # Iterate over all lines in file and produce the sum of `get_first_and_last_digit(line)`


if __name__ == "__main__":
    run()
