# !/usr/bin/python
# -*- coding: utf8 -*-
""" MODULE LEVEL DOCSTRING: WRITE SOMETHING HERE LATER
"""


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


def event_loop():
    """ Function that handles the user input

    This project will receive a series of user inputs regarding the creation,
    filling and manipulation of simple bidimentional matrices. This function
    takes care of checking the validity of user input, provide feeback for
    invalid values and calling the due functions for each command.

    Commands:
        I M N:      Initialize an empty (zero-valued) MxN ( colsXrows ) matrix.
                    Here, the value zero is defined by the letter O not the
                    number 0. Also, be aware that this command does not follow
                    the common matrices dimension convention, which is rowsXcols

        C:          Sets the current matrix values to zero

        L X Y C:    Set matrix position (X,Y) with value C

        V X Y1 Y2 C:Sets matrix positions (X, Y1-Y2) with value C

        H X X1 Y2 C:Sets matrix positions (X1-X2, Y) with value C

        K X1 Y1 X2 Y2 C : Sets a rectangular region, with bounds (X1,Y1) for
                          top-left corner and (X2,Y2) to bottom-right corner

        F X Y C : Fills a region with value C. A region is defined by the X,Y
                  position with value C and neighbor zero valued (O) positions,
                  both horizontaly and verticaly.

        S filename: Saves the matrix to a file with name "filename"

        X : Exits the program

    """
    pass


def main():
    pass


if __name__ == '__main__':
    main()