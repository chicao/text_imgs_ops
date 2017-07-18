# !/usr/bin/python
# -*- coding: utf8 -*-
""" MODULE LEVEL DOCSTRING: WRITE SOMETHING HERE LATER
"""
import sys

def initialize_matrix(cols, rows):
    return [['O']*rows]*cols


def clear_matrix(matrix):
    for col in matrix:
        for pos in range(len(col)):
            col[pos] = 'O'


def lay_value_at(matrix, col, row, value):
    if not check_bounds(matrix, col, row):
        return

    matrix[col][row] = value


def vertical_values(matrix, col, row_up, row_down, value):
    if row_up > row_down:
        return

    if not check_horizontal_bounds(matrix, col):
        return

    if not check_vertical_bounds(matrix, row_up):
        return

    if not check_vertical_bounds(matrix, row_down):
        return

    for pos in range(row_up, row_down+1):
        matrix[col][pos] = value


def horizontal_values(matrix, col_left, col_right, row, value):
    if col_left > col_right:
        return

    if not check_horizontal_bounds(matrix, col_left):
        return

    if not check_horizontal_bounds(matrix, col_right):
        return

    if not check_vertical_bounds(matrix, row):
        return

    for pos in range(col_left, col_right+1):
        matrix[pos][row] = value


def key_in_rect(matrix, col_top, row_top, col_bottom, row_bottom, value):
    if col_top > col_bottom:
        return

    if row_top > row_bottom:
        return

    if not check_bounds(matrix, col_top, row_top):
        return

    if not check_bounds(matrix, col_bottom, row_bottom):
        return

    for col in range(col_top, col_bottom+1):
        for row in range(row_top, row_bottom+1):
            matrix[col][row] = value


def fill_region(matrix, col, row, value):
    if matrix[col][row] != 'O':
        return

    size = len(matrix), len(matrix[0])

    matrix[col][row] = value

    if col > 0:
        fill_region(matrix, col-1, row, value)

    if row > 0:
        fill_region(matrix, col, row-1, value)

    if col < size[0]-1:
        fill_region(matrix, col+1, row, value)

    if row < size[1]-1:
        fill_region(matrix, col, row+1, value)


def check_bounds(matrix, col, row):
    if not check_horizontal_bounds(matrix, col):
        return False

    if not check_vertical_bounds(matrix, row):
        return False

    return True


def check_horizontal_bounds(matrix, col):
    if not len(matrix):
        return False

    bound = len(matrix)
    return col < bound


def check_vertical_bounds(matrix, row):
    if not len(matrix):
        return False

    bound = len(matrix[0])
    return row < bound


def save_matrix(matrix, filename):
    pass


def matrix_2_str(matrix):
    size = len(matrix), len(matrix[0])
    output = ['']*size[0]

    for j in range(size[1]):
        for i in range(size[0]):
            output[j] += matrix[i][j]
        output[j] += '\n'

    return ''.join(output)


def print_help(initial=False):

    header = ("------------------- TEXT IMAGE COMMANDS -------------------\n"
        )

    message = ("-----------------------------------------------------------\n\n"
               " Create a text document as emulation of 2D images\n\n"
               " Usage:\n\n"
               " H:\n"
               "      Prints this help message\n\n"
               " I M N:\n"
               "      Initialize an empty ('O') MxN ( colsXrows ) image\n\n"
               " C:\n"
               "      Sets the current matrix values to zero\n\n"
               " L X Y C:\n"
               "      Set matrix position (X,Y) with value C\n\n"
               " V X Y1 Y2 C:\n"
               "      Sets matrix positions (X, Y1-Y2) with value C\n\n"
               " H X X1 Y2 C:\n"
               "      Sets matrix positions (X1-X2, Y) with value C\n\n"
               " K X1 Y1 X2 Y2 C:\n"
               "      Sets a rectangular region, with bounds (X1,Y1) for\n"
               "      top-left corner and (X2,Y2) to bottom-right corner\n\n"
               " F X Y C:\n"
               "      Fills a region with value C. A region is defined by the\n"
               "      X,Y position with value C and neighbor zero valued (O)\n"
               "      positions, both horizontaly and verticaly.\n\n"
               " S 'filename':\n"
               "      Saves the matrix to a file with name 'filename'\n\n"
               " X:\n"
               "      Exits the program\n\n"
               "-----------------------------------------------------------\n\n"
        )

    if initial:
        message = header + message

    print(message)


def handle_user_input(user_input):

    valid_commands = ['H', 'X', 'I', 'C', 'L', 'V', 'H', 'K', 'F', 'S']
    command = user_input.split()

    if not command:
        print('Please, insert a valid command')
        return

    if command[0] not in valid_commands:
        print_syntax_error()
        return

    if command[0] == 'H':
        print_help()

    if command[0] == 'X':
        print("Goodbye :'( ")
        sys.exit(0)


def print_syntax_error():
    error = (
        "----------------------    ERROR    -------------------------\n"
        " >  INVALID COMMAND SYNTAX\n"
        "------------------------------------------------------------\n\n"
        )
    print(error)


def event_loop():
    print_help(initial=True)

    while True:
        user_input = input("(for help press 'H')> ")
        handle_user_input(user_input)


def main():
    event_loop()


if __name__ == '__main__':
    main()