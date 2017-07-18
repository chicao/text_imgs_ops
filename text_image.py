# !/usr/bin/python
# -*- coding: utf8 -*-
""" MODULE LEVEL DOCSTRING: WRITE SOMETHING HERE LATER
"""
import sys

image = []

def initialize_matrix(cols, rows):
    init = []
    for _ in range(cols):
        row = ['O' for _ in range(rows)]
        init.append(row)

    return init


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
    if col < 0:
        return False

    return col < bound


def check_vertical_bounds(matrix, row):
    if not len(matrix):
        return False

    bound = len(matrix[0])
    if row < 0:
        return False
    return row < bound


def save_matrix(matrix, filename):
    pass


def matrix_2_str(matrix):
    if not matrix:
        return '<empty>'

    size = len(matrix), len(matrix[0])
    output = ['']*size[0]

    for j in range(size[1]):
        for i in range(size[0]):
            output[j] += matrix[i][j]
        output[j] += '\n'

    return ''.join(output)


def print_guide(initial=False):

    header = ("------------------- TEXT IMAGE COMMANDS -------------------\n"
        )

    message = ("-----------------------------------------------------------\n\n"
               " Create a text document as emulation of 2D images\n\n"
               " Usage:\n\n"
               " G:\n"
               "      Prints this guide message\n\n"
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
               " P:\n"
               "      Prints the current state of the text image\n\n"
               " X:\n"
               "      Exits the program\n\n"
               "-----------------------------------------------------------\n\n"
        )

    if initial:
        message = header + message

    print(message)


def handle_user_input(user_input):

    valid_commands = ['G', 'X', 'P', 'I', 'C', 'L', 'V', 'H', 'K', 'F', 'S']
    command = user_input.split()

    if not command:
        print('Please, insert a valid command')
        return

    if command[0] not in valid_commands:
        print_error('syntax')
        return

    global image

    if command[0] == 'P':
        print(matrix_2_str(image))
        return

    if command[0] == 'G':
        print_guide()

    if command[0] == 'X':
        print("Goodbye :'( ")
        sys.exit(0)

    if command[0] == 'I':

        if len(command) != 3:
            print_error('syntax')
            return

        try:
            cols = int(command[1])
            rows = int(command[2])
            image = initialize_matrix(cols, rows)

        except ValueError as e:
            print_error('value')
            return

    if not image:
        print_error('empty')
        return

    if command[0] == 'C':
        clear_matrix(image)


    if command[0] == 'L':

        if len(command) != 4:
            print_error('syntax')
            return

        try:
            col = int(command[1]) - 1
            row = int(command[2]) - 1

            if not check_bounds(image, col, row):
                print_error('bounds')

            value = command[3]
            lay_value_at(image, col, row, value)


        except ValueError as e:
            print_error('value')
            return

    if command[0] == 'V':

        if len(command) != 5:
            print_error('syntax')
            return

        try:
            col = int(command[1]) - 1
            row_upper = int(command[2]) - 1
            row_lower = int(command[3]) - 1

            if not check_vertical_bounds(image, row_upper):
                print_error('bounds')

            if not check_vertical_bounds(image, row_lower):
                print_error('bounds')

            if not check_horizontal_bounds(image, col):
                print_error('bounds')

            if row_upper > row_lower:
                print_error('interval')

            value = command[4]
            vertical_values(image, col, row_upper, row_lower, value)

        except ValueError as e:
            print_error('value')
            return

    if command[0] == 'H':

        if len(command) != 5:
            print_error('syntax')
            return

        try:
            col_left = int(command[1]) - 1
            col_right = int(command[2]) - 1
            row = int(command[3]) - 1

            if not check_horizontal_bounds(image, col_left):
                print_error('bounds')

            if not check_horizontal_bounds(image, col_right):
                print_error('bounds')

            if not check_vertical_bounds(image, row):
                print_error('bounds')

            if col_left > col_right:
                print_error('interval')

            value = command[4]
            horizontal_values(image, col_left, col_right, row, value)

        except ValueError as e:
            print_error('value')
            return

def print_error(error_type):
    error = "----------------------    ERROR    -------------------------\n"

    if error_type == 'syntax':
        error += (" >  INVALID COMMAND SYNTAX\n"
                  " >     This command requires arguments to proceed\n")

    elif error_type == 'empty':
        error +=  (" >  UNITIALIZED IMAGE\n"
                   " >     This command requires a initialized image\n")

    elif error_type == 'value':
        error +=  (" > INVALID COMMAND INPUT"
                   " >     The commands require integer values for image\n"
                   " >     dimensions input\n")

    elif error_type == 'bounds':
        error +=  (" > INVALID IMAGE BOUNDS"
                   " >     The commands require integer values for image\n"
                   " >     positions that are with the image size\n")

    elif error_type == 'interval':
        error +=  (" > INVALID IMAGE POSITION INTERVAL"
                   " >     The commands require integer values for image\n"
                   " >     positions that required that the first is greater\n"
                   " >     than the second\n")

    else:
        error += (" >  AN ERROR OCCURRED\n"
                  " >       Please, keep in mind to use the\n"
                  " >       designated commands\n")

    error += "------------------------------------------------------------\n\n"

    print(error)


def event_loop():
    print_guide(initial=True)

    while True:
        user_input = input("(press 'G' for guidance)> ")
        handle_user_input(user_input)


def main():
    event_loop()


if __name__ == '__main__':
    main()