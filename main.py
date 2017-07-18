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
    function = command[0]

    #
    # User provided a empty string as input and pressed enter
    if not command:
        print('Please, insert a valid command')
        return

    #
    # The input wasn't any valid command
    if function not in valid_commands:
        print_error('command')
        return

    global image

    if function == 'G':
        print_guide()
        return

    if function == 'P':
        print(matrix_2_str(image))
        return

    if function == 'X':
        print("Goodbye :'( ")
        sys.exit(0)
        return

    # Initilization command
    if function == 'I':
        initialize_zero_valued_img(command[1:])
        return

    #
    # The commands below are executed on filled images
    # If the image wasn't initialized, the other commands
    # will not work properly. So we block their calls if the
    # image wasn't initialized
    if not image:
        print_error('empty')
        return

    # Clear matrix command
    if function == 'C':
        clear_matrix(image)

    # Lay value at image command
    if function == 'L':
        lay_value_into_image(command[1:])

    # Vertical line filling command
    if function == 'V':
        vertical_image_filling(command[1:])

    # Horizontal line filling command
    if function == 'H':
        horizontal_image_filling(command[1:])

    # Rectagle filling command
    if function == 'K':
        key_rect_in_image(command[1:])

    # Region filling command
    if function == 'F':
        fill_image_region(command[1:])

    # Save to file command
    if function == 'S':
        save_image_to_file(command[1:])


def initialize_zero_valued_img(args):
    global image
    if len(args) != 2:
        print_error('syntax')
        return

    try:
        cols = int(args[0])
        rows = int(args[1])
        image = initialize_matrix(cols, rows)

    except ValueError as e:
        print_error('value')
        return


def lay_value_into_image(args):
    if len(args) != 3:
        print_error('syntax')
        return

    global image
    try:
        col = int(args[0]) - 1
        row = int(args[1]) - 1

        if not check_bounds(image, col, row):
            print_error('bounds')

        value = args[2]
        lay_value_at(image, col, row, value)


    except ValueError as e:
        print_error('value')
        return


def vertical_image_filling(args):
    if len(args) != 4:
        print_error('syntax')
        return

    global image
    try:
        col = int(args[0]) - 1
        row_upper = int(args[1]) - 1
        row_lower = int(args[2]) - 1

        if not check_vertical_bounds(image, row_upper):
            print_error('bounds')

        if not check_vertical_bounds(image, row_lower):
            print_error('bounds')

        if not check_horizontal_bounds(image, col):
            print_error('bounds')

        if row_upper > row_lower:
            print_error('interval')

        value = args[3]
        vertical_values(image, col, row_upper, row_lower, value)

    except ValueError as e:
        print_error('value')
        return


def horizontal_image_filling(args):
    if len(args) != 4:
        print_error('syntax')
        return

    global image
    try:
        col_left = int(args[0]) - 1
        col_right = int(args[1]) - 1
        row = int(args[2]) - 1

        if not check_horizontal_bounds(image, col_left):
            print_error('bounds')

        if not check_horizontal_bounds(image, col_right):
            print_error('bounds')

        if not check_vertical_bounds(image, row):
            print_error('bounds')

        if col_left > col_right:
            print_error('interval')

        value = args[3]
        horizontal_values(image, col_left, col_right, row, value)

    except ValueError as e:
        print_error('value')
        return


def key_rect_in_image(args):
    if len(args) != 5:
        print_error('syntax')
        return

    global image
    try:
        col_top = int(args[0]) - 1
        row_top = int(args[1]) - 1
        col_bottom = int(args[2]) - 1
        row_bottom = int(args[3]) - 1
        value = args[4]

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


def fill_image_region(args):
    if len(args) != 3:
        print_error('syntax')
        return

    global image
    try:
        col = int(args[0]) - 1
        row = int(args[1]) - 1
        value = args[2]

        if not check_bounds(image, col, row):
            print_error('bounds')

        fill_region(image, col, row, value)

    except ValueError as e:
        print_error('value')
        return


def save_matrix_to_file(args):

    if len(args) != 1:
        print_error('syntax')
        return

    global image

    if "'" not in args[0]:
        print_error('syntax')
        return

    if args[0].count("'") != 2:
        print_error('syntax')
        return

    if len(args[0]) < 3:
        print_error('filename')
        return

    filename = args[0].strip("'")
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