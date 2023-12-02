import re
import math

def min_colors(line):
    colors = {"red": 0, "green": 0, "blue": 0}
    draw_pattern = rf"(\d+) ({'|'.join(colors.keys())})"
    for amount, color in re.findall(draw_pattern, line):
        colors[color] = max(colors[color], int(amount))
    return math.prod(colors.values())

def run():
    with open("input.txt") as input_file:
        print(
            sum(map(min_colors, input_file))
        )

if __name__ == "__main__":
    run()
