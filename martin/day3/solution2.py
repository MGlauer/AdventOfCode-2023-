def is_symbol(cell: str):
    return not (cell.isdigit() or cell == ".")


def run():
    with open("input.txt") as input_file:
        node_values = {
            (x, y): v
            for (y, l) in enumerate(input_file)
            for (x, v) in enumerate(l.strip())
        }

    nodes = list(node_values.keys())
    width = max(x for (x, y) in nodes) + 1
    height = max(y for (x, y) in nodes) + 1

    # We build a map (star positions (x,y)) -> (numbers around (x,y))asd
    star_neighbors = dict()

    for y in range(height):
        x = 0
        concat_number = ""
        while x < width:
            cell_value = node_values[(x, y)]
            if node_values[(x, y)].isdigit():
                concat_number += cell_value
            if (not node_values[(x, y)].isdigit() and concat_number) or x == width - 1:
                adjacent_cells = [
                    (x + dx, y + dy)
                    for dx in range(-len(concat_number) - 1, 1)
                    for dy in range(-1, 2)
                    if 0 <= x + dx < width and 0 <= y + dy < height
                ]
                for c in adjacent_cells:
                    # If there is a star, store the number
                    if node_values[c] == "*":
                        if c in star_neighbors:
                            star_neighbors[c].append(int(concat_number))
                        else:
                            star_neighbors[c] = [int(concat_number)]
                concat_number = ""
            x += 1

    # sum of the products of stars that are surrounded by exactly two numbers
    print(sum(n[0] * n[1] for _, n in star_neighbors.items() if len(n) == 2))


if __name__ == "__main__":
    run()
