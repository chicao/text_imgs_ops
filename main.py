# !/usr/bin/python
# -*- coding: utf8 -*-
""" MODULE LEVEL DOCSTRING: WRITE SOMETHING HERE LATER
"""
import sys
from text_processing import *

image = []

def print_guide(initial=False):
    """ Prints the program guide to the user

    This shows how the commands should be formated, so the user have some way
    to guide itself in the operations of the text manipulation.

    Args:
        initial (bool): Flag to add the program header to the output string
    """

    #
    # The header is used on the event loop initialization
    header = ("--------------------------------------------------------------\n"
              "--------------------  TEXT IMAGE COMMANDS  -------------------\n"
              "--------------------------------------------------------------\n"
        )

    #
    # A command is mapped to show the user this help guide
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

    # Appends the header if required in the argument
    if initial:
        message = header + message

    print(message)


def handle_user_input(user_input):
    """ Handle the user input from the prompt

    The user can effectively make operations by calling the correct command
    syntax described on the help guide. However, any user is prone to errors
    while manipulating information from a program interface. This function
    parses the user commands, warn she/he for the correct command syntax,
    check value inputs and provide feedback on later processing stages.

    The commands are called from here.

    Args:
        user_input (str): String containing the user input from the command line

    """

    #
    # List of valid commands
    valid_commands = ['G', 'X', 'P', 'I', 'C', 'L', 'V', 'H', 'K', 'F', 'S']

    #
    # Splits the string. The arguments must be separated by spaces
    # Commands argument counting and parsing are done ahead
    command = user_input.split()

    #
    # User provided a empty string as input and pressed enter
    if not command:
        print('Please, insert a valid command')
        return

    #
    # The input wasn't any valid command
    if command[0] not in valid_commands:
        print_error('command')
        return

    global image

    if command[0] == 'G':
        print_guide()

    if command[0] == 'P':
        print(matrix_2_str(image))
        return

    if command[0] == 'X':
        print("Goodbye :'( ")
        sys.exit(0)

    if command[0] == 'I':
        initialize_zero_valued_img(command)

    if not image:
        print_error('empty')
        return

    if command[0] == 'C':
        clear_matrix(image)

    if command[0] == 'L':
        lay_value_into_image(command)

    if command[0] == 'V':
        vertical_image_filling(command)

    if command[0] == 'H':
        horizontal_image_filling(command)

    if command[0] == 'K':
        key_rect_in_image(command)

    if command[0] == 'F':
        fill_image_region(command)

    if command[0] == 'S':
        save_image_to_file(command)


def initialize_zero_valued_img(command):
    global image
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


def lay_value_into_image(command):
    if len(command) != 4:
        print_error('syntax')
        return

    global image
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


def vertical_image_filling(command):
    if len(command) != 5:
        print_error('syntax')
        return

    global image
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


def horizontal_image_filling(command):
    if len(command) != 5:
        print_error('syntax')
        return

    global image
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


def key_rect_in_image(command):
    if len(command) != 6:
        print_error('syntax')
        return

    global image
    try:
        col_top = int(command[1]) - 1
        row_top = int(command[2]) - 1
        col_bottom = int(command[3]) - 1
        row_bottom = int(command[4]) - 1
        value = command[5]

        if not check_bounds(image, col_top, row_top):
            print_error('bounds')

        if not check_bounds(image, col_bottom, row_bottom):
            print_error('bounds')

        if col_top > col_bottom:
            print_error('interval')

        if row_top > row_bottom:
            print_error('interval')

        key_in_rect(image, col_top, row_top, col_bottom, row_bottom, value)

    except ValueError as e:
        print_error('value')
        return


def fill_image_region(command):
    if len(command) != 4:
        print_error('syntax')
        return

    global image
    try:
        col = int(command[1]) - 1
        row = int(command[2]) - 1
        value = command[3]

        if not check_bounds(image, col, row):
            print_error('bounds')

        fill_region(image, col, row, value)

    except ValueError as e:
        print_error('value')
        return


def save_matrix_to_file(command):

    if len(command) != 2:
        print_error('syntax')
        return

    global image

    if "'" not in command[1]:
        print_error('syntax')
        return

    if command[1].count("'") != 2:
        print_error('syntax')
        return

    if len(command[1]) < 3:
        print_error('filename')
        return

    filename = command[1].strip("'")
    save_matrix(image, filename)


def print_error(error_type):
    error = "----------------------    ERROR    -------------------------\n"

    if error_type == 'command':
        error += (" >  INVALID COMMAND\n"
                  " >     This input is not a valid command\n")

    elif error_type == 'syntax':
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

    elif error_type == 'filename':
        error +=  (" > INVALID FILENAME FORMAT"
                   " >     To save a file properly, input a file name with\n"
                   " >     at least 3 letters\n")

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