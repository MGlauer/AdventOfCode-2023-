import re

def get_winning_numbers(line):

    game_pattern = rf"^Card\s+(\d+): ([^|]+) \| ([^\n]+)$"
    # Determine game number
    match = re.match(game_pattern, line)
    card_id, left, right = match.groups()
    card_id = int(card_id)
    left = {int(x) for x in left.split(" ") if x}
    right = {int(x) for x in right.split(" ") if x}

    intersection = left.intersection(right)
    return (card_id, len(intersection))

def run():
    with open("input.txt") as input_file:
        matches = dict(map(get_winning_numbers, input_file))
    total_winnings = dict()
    # Calculate the winnings of each card in reverse
    # and reuse results.
    for i in reversed(matches.keys()):
        total_winnings[i] = 1 + sum(total_winnings[i+j+1] for j in range(matches[i]))
    print(sum(total_winnings.values()))
if __name__ == "__main__":
    run()
