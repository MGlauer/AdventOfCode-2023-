import re

def get_winning_numbers(line):

    game_pattern = rf"^Card\s+(\d+): ([^|]+) \| ([^\n]+)$"
    # Determine game number
    match = re.match(game_pattern, line)
    print(line)
    print(match.groups())
    card_id, left, right = match.groups()
    game_id = int(card_id)
    left = {int(x) for x in left.split(" ") if x}
    right = {int(x) for x in right.split(" ") if x}

    intersection = left.intersection(right)
    if intersection:
        return 2 ** (len(intersection)-1)
    else:
        return 0

def run():
    with open("input.txt") as input_file:
        print(
            sum(map(get_winning_numbers, input_file))
        )  # Iterate over all lines in file and produce the sum of `get_first_and_last_digit(line)`


if __name__ == "__main__":
    run()
