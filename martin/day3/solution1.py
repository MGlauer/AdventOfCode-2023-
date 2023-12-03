def is_symbol(cell: str):
    return not (cell.isdigit() or cell == ".")


def run():
    with open("input.txt") as input_file:
        node_values = {
            (x, y): v
            for (y, l) in enumerate(input_file)
            for (x, v) in enumerate(l.strip())
        }  # Build a map (x,y) -> (symbol at (x,y))

    nodes = list(node_values.keys())
    width = max(x for (x, y) in nodes) + 1
    height = max(y for (x, y) in nodes) + 1

    adjacent_numbers = []

    for y in range(height):  # For reach row ..
        x = 0
        concat_number = ""
        while x < width:  # .. iterate over each character in that row.
            cell_value = node_values[(x, y)]
            if node_values[(x, y)].isdigit():  # store consecutive numbers
                concat_number += cell_value
            # If the number *or the line* ended
            if (not node_values[(x, y)].isdigit() and concat_number) or x == width - 1:
                adjacent_cells = [
                    (x + dx, y + dy)
                    for dx in range(-len(concat_number) - 1, 1)
                    for dy in range(-1, 2)
                    if 0 <= x + dx < width and 0 <= y + dy < height
                ]  # Collect a cells surrounding the number

                # Check wether surrounding cells contain a symbol
                if any(is_symbol(node_values[c]) for c in adjacent_cells):
                    # if so, store the number
                    adjacent_numbers.append(int(concat_number))
                # delete storesd number
                concat_number = ""
            x += 1
    print(sum(adjacent_numbers))


if __name__ == "__main__":
    run()
