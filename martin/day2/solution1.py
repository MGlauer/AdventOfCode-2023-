import re

def max_colors(line):
    max_dict = {"red": 12, "green":13, "blue":14}
    colors = {"red":0, "green":0, "blue":0}
    # Regex that matches '[number] [color]'
    draw_pattern = rf"(\d+) ({'|'.join(colors.keys())})"
    # Regex that matches 'Game [number]'
    game_pattern = rf"^Game (\d+)"

    # Determine game number
    match = re.match(game_pattern, line)
    game_id = int(match.groups()[-1])

    # Iterate all parts of the line that match matches "[number] [color]"
    for amount, color in re.findall(draw_pattern, line):
        # store if previous occurance of color was bigger
        colors[color] = max(colors[color], int(amount))
    if any(colors[c] > max_dict[c] for c in colors):
        return 0
    else:
        return game_id

def run():
    with open("input.txt") as input_file:
        print(
            sum(map(max_colors, input_file))
        )  # Iterate over all lines in file and produce the sum of `get_first_and_last_digit(line)`


if __name__ == "__main__":
    run()
