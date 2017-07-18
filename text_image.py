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


def save_matrix(matrix, filename):
    pass


def matrix_2_str(matrix):
    pass


def main():
    pass


if __name__ == '__main__':
    main()