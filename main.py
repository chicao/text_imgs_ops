# !/usr/bin/python
# -*- coding: utf8 -*-
""" Main program module that handles the event loop and user input

This module holds the main parsing of arguments and operations of the image
matrix manipulation

"""
import sys
from text_image import TextImage


def print_error(error_type):
    error = "----------------------    ERROR    -------------------------\n"

    if error_type == 'command':
        error += (" >  INVALID COMMAND\n"
                  " >     This input is not a valid command\n")

    elif error_type == 'syntax':
        error += (" >  INVALID COMMAND SYNTAX\n"
                  " >     This command requires correct argument values \n"
                  " >     to proceed\n")

    elif error_type == 'empty':
        error +=  (" >  UNITIALIZED IMAGE\n"
                   " >     This command requires a initialized image\n")

    elif error_type == 'value':
        error +=  (" > INVALID COMMAND INPUT\n"
                   " >     The commands require integer values for image\n"
                   " >     dimensions input\n")

    elif error_type == 'bounds':
        error +=  (" > INVALID IMAGE BOUNDS\n"
                   " >     The commands require integer values for image\n"
                   " >     positions that are with the image size\n")

    elif error_type == 'interval':
        error +=  (" > INVALID IMAGE POSITION INTERVAL\n"
                   " >     The commands require integer values for image\n"
                   " >     positions that required that the first is greater\n"
                   " >     than the second\n")

    elif error_type == 'filename':
        error +=  (" > INVALID FILENAME FORMAT\n"
                   " >     To save a file properly, input a file name with\n"
                   " >     at least 3 letters\n")

    elif error_type == 'file':
        error +=  (" > SYSTEM ERROR\n"
                   " >     An error occured while trying to save a file.\n"
                   " >     Check the file path and access permission\n")

    else:
        error += (" >  AN ERROR OCCURRED\n"
                  " >       Please, keep in mind to use the\n"
                  " >       designated commands\n")

    error += "------------------------------------------------------------\n\n"

    print(error)


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
               "    G:\n"
               "      Prints this guide message\n\n"
               "    I M N:\n"
               "      Initialize an empty ('O') MxN ( colsXrows ) image\n\n"
               "    C:\n"
               "      Sets the current matrix values to zero\n\n"
               "    L X Y C:\n"
               "      Set matrix position (X,Y) with value C\n\n"
               "    V X Y1 Y2 C:\n"
               "      Sets matrix positions (X, Y1-Y2) with value C\n\n"
               "    H X X1 Y2 C:\n"
               "      Sets matrix positions (X1-X2, Y) with value C\n\n"
               "    K X1 Y1 X2 Y2 C:\n"
               "      Sets a rectangular region, with bounds (X1,Y1) for\n"
               "      top-left corner and (X2,Y2) to bottom-right corner\n\n"
               "    F X Y C:\n"
               "      Fills a region with value C. A region is defined by the\n"
               "      X,Y position with value C and neighbor zero valued (O)\n"
               "      positions, both horizontaly and verticaly.\n\n"
               "    S 'filename':\n"
               "      Saves the matrix to a file with name 'filename'\n\n"
               "    P:\n"
               "      Prints the current state of the text image\n\n"
               "    X:\n"
               "      Exits the program\n\n"
               "-----------------------------------------------------------\n\n"
        )

    # Appends the header if required in the argument
    if initial:
        message = header + message

    print(message)


def handle_user_input(image, user_input):
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
    # Command related operations
    #

    # Splits the string. The arguments must be separated by spaces
    # Commands argument counting and parsing are done ahead
    command = user_input.split()

    # User provided an empty string as input and pressed enter
    if not command:
        print_error('command')
        return

    # Gets the fist splited string, expected to be a valid command
    # and get its related arguments
    function = command[0]
    args = command[1:]

    # The input wasn't identified as any valid command
    if function not in valid_commands:
        print_error('command')
        return

    # Handle the parsing of the arguments
    handle_function_calls(image, function, args)


def handle_function_calls(image, command, args):

    #
    # Not populated matrix related operations
    #

    # Print the helping guide
    if command == 'G':
        print_guide()
        return

    # Exit the program
    if command == 'X':
        print("Goodbye :'( ")
        sys.exit(0)
        return

    # Print the text image
    if command == 'P':
        print(image)
        return

    #
    # Most of the commands below are executed on filled images
    # If the image wasn't initialized, the other commands
    # will not work properly. So we block their calls if the
    # image wasn't initialized
    if not image.image and command != 'I':
        print_error('empty')
        return

    # Clear matrix command
    if command == 'C':
        image.clear_matrix()
        return

    # Handle matrix bound methods of the text image
    # Each command has a similar way of calling the matrix methods,
    # such as row and columns position definitions and value settings,
    # but each one has a particularity, such as method call name, argument
    # quantity and dimension mapping. So, the following dict handles each
    # commmand in its particularities
    function = {
        'I': {'args':2,
              'has_value': False,
              'map_dimension': False,
              'name': 'initialize_matrix'
              },
        'L': {'args':3,
              'has_value': True,
              'map_dimension': True,
              'name': 'lay_value_at'
              },
        'V': {'args':4,
              'has_value': True,
              'map_dimension': True,
              'name': 'vertical_values'
              },
        'H': {'args':4,
              'has_value': True,
              'map_dimension': True,
              'name': 'horizontal_values'
              },
        'K': {'args':5,
              'has_value': True,
              'map_dimension': True,
              'name': 'key_in_rect'
              },
        'F': {'args':3,
              'has_value': True,
              'map_dimension': True,
              'name': 'fill_region'
              },
        'S': {'args':1,
              'has_value': True,
              'map_dimension': False,
              'name': 'save_matrix'
              },
        }

    # Check if the number of arguments is correct
    if len(args) != function[command]['args']:
        print_error('syntax')
        return

    # Separate the value from the argument parsing
    # Although 'value' is a argument, it isn't manipulated
    # as the other args, so it is set apart from the others
    value = ''

    # If the command requires value, it removes it from the argument list
    if function[command]['has_value']:
        value = args[-1]
        args = args[:len(args)-1]

    # Parse the arguments and pass it to the due function
    try:
        args = [int(arg) for arg in args]

        # This flags if it is necessary to do a subtraction operation before
        # passing the argument, since matrix operations are zero indexed,
        # while user interface operations aren't
        if function[command]['map_dimension']:
            args = [arg - 1 for arg in args]

        method = getattr(image,
                         function[command]['name'])

        # Reattach value to the argument list
        if value:
            args.append(value)

        # Unpack the parsed arguments to the due functions
        method(*args)

    # Handle expected exceptions raised from the TextImage class
    except ValueError as e:
        # Raised when parsing string into integers
        print_error('value')
        return

    except IndexError as e:
        # Raised while checing argument bounds in the image matrix
        print_error('bounds')
        return

    except AttributeError as e:
        # Raised when the attribute matrix is not properly set into the image
        print_error('empty')
        return
    except OSError as e:
        # Raised when failed to save file due to system issues
        print_error('file')
        return


def event_loop():
    print_guide(initial=True)
    image = TextImage()
    while True:
        user_input = input("(press 'G' for guidance)> ")
        handle_user_input(image, user_input)


if __name__ == '__main__':
    event_loop()