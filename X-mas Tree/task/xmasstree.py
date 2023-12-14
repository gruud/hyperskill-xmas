"""Hyperskill"""

def create_output(width, height) -> list:
    """Create a buffer for the xmas tree representation"""
    return [[" " for x in range(width)] for x in range(height)]


def create_frame(postcard):
    postcard[0] = ["-" for i in postcard[0]]
    postcard[len(postcard) - 1] = ["-" for i in postcard[0]]
    for row in range(1, len(postcard) - 1):
        postcard[row][0] = "|"
        postcard[row][len(postcard[row]) - 1] = "|"


def print_tree(buffer, size, decorations_step, offset_row=0, offset_col=0):
    decoration_counter = decorations_step
    offset_col = size - 1 if offset_col == 0 else offset_col

    buffer[offset_row][offset_col] = "X"
    buffer[offset_row + 1][offset_col] = "^"


    for line in range(1, size):
        num_spaces = offset_col - line - 1
        num_dots = 2 * line - 1
        tree_row_offset = offset_row + line + 1

        buffer[tree_row_offset][num_spaces + 1] = "/"
        buffer[tree_row_offset][num_spaces + 2 + num_dots] = "\\"

        dots = ""
        for j in range(num_dots):
            if j % 2 == 1:
                if decoration_counter % decorations_step == 0:
                    buffer[tree_row_offset][num_spaces + 2 + j] = "O"
                else:
                    buffer[tree_row_offset][num_spaces + 2 + j] = "*"
                decoration_counter += 1
            else:
                buffer[tree_row_offset][num_spaces + 2 + j] = "*"

    buffer[offset_row + size + 1][offset_col - 1] = "|"
    buffer[offset_row + size + 1][offset_col + 1] = "|"




def add_greetings(postcard, width, height):
    greetings = "Merry Xmas"
    greetings_line = height - 1 - 2
    start_index = int((width / 2)) - int(len(greetings) / 2)
    for i in range(len(greetings)):
        postcard[greetings_line][start_index + i] = greetings[i]


def print_postcard(postcard):
    for row in postcard:
        print("".join(row))

def main():
    """Main program.

    The trinkets can go only atatt the odd positions
    """

    inputs = [int(x) for x in input().split()]

    output = create_output(50, 30)
    if len(inputs) == 2:
        output = create_output(inputs[0] * 2 + 2, inputs[0] + 2)
        print_tree(output, inputs[0], inputs[1])
    if len(inputs) % 4 == 0:
        output = create_output(50, 30)
        create_frame(output)
        add_greetings(output, width=50, height=30)

        for i in range(0, len(inputs), 4):
            params = inputs[i:i+4]
            print_tree(output, params[0], params[1], params[2], params[3])

    print_postcard(output)



if __name__ == "__main__":
    main()
