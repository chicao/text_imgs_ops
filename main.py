# !/usr/bin/python
# -*- coding: utf8 -*-
""" Main program module that handles the event loop and user input

This module holds the main parsing of arguments and operations of the image
matrix manipulation

"""
import sys
from text_image import TextImage


def print_error(error_type):
    """ Print user interaction error messages

    The user should alway receive information of the consequences of its actions
    within the program. While there is information of success, warning of errors
    and invalid inputs should be passed

    This function handles error messages by their flagged type.

    Args:
        error_type (str): Error key to inform the user of possible program
        misbehaviour due to invalid inputs or unexpected system errors

    """

    errors = {'command': (" >  INVALID COMMAND\n"
                         " >     This input is not a valid command\n"),
              'syntax': (" >  INVALID COMMAND SYNTAX\n"
                         " >     This command requires correct argument\n"
                         " >     values to proceed\n"),
              'empty': (" >  INVALID COMMAND\n"
                        " >     This input is not a valid command\n"),
              'value': (" > INVALID COMMAND INPUT\n"
                        " >     The commands require integer values for image\n"
                        " >     dimensions input\n"),
              'bounds': (" > INVALID IMAGE BOUNDS\n"
                         " >     The commands require integer values for\n"
                         " >     image positions that are with the\n"
                         " >     image size\n"),
              'interval': (" > INVALID IMAGE POSITION INTERVAL\n"
                           " >     The commands require integer values for\n"
                           " >     image positions that required that the  \n"
                           " >     first is greater than the second\n"),
              'filename': (" > INVALID FILENAME FORMAT\n"
                           " >     To save a file properly, input a file name\n"
                           " >     with at least 3 letters\n"),
              'file': (" > SYSTEM ERROR\n"
                       " >     An error occured while trying to save a file.\n"
                       " >     Check the file path and access permission\n"),
              'other': (" >  AN ERROR OCCURRED\n"
                        " >       Please, keep in mind to use the\n"
                        " >       designated commands\n"),
        }

    message = errors['other']
    if error_type in errors:
        message = errors[error_type]

    header = "----------------------    ERROR    -------------------------\n"
    footer = "------------------------------------------------------------\n\n"

    print(header + message + footer)


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
    """ Handle the argument passing and objet call for command functions

    The commands passed arguments needs to process each input to the
    due function to be executed. This function figures if the method needs a
    value, its number of arguments and so on. Basically, it maps, converts and
    pass the arguments for each command to the TextImage due method

    Args:
        image (TextImage) : Object representing the image matrix and its
            functions
        command (str) : The command the user has input
        args (list(str)): a list of user input strings that should be the
            methods arguments
    """

    #
    # Not image related operations
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

    # Handle matrix bound methods of the text image
    # Each command has a similar way of calling the matrix methods,
    # such as row and columns position definitions and value settings,
    # but each one has a particularity, such as method call name, argument
    # quantity and dimension mapping. So, the following dict handles each
    # commmand in its particularities:
    #
    #       args : the number of arguments that the function requires
    #       has_value: specifies the need of a value to be inserted/processed
    #       map_dimension: flags if should map the passed position to due
    #                      zero valued bounds
    #       name: name of the TextImage method to be called with the processed
    #             arguments
    #
    function = {
        'C': {'args':0,
              'has_value': False,
              'map_dimension': False,
              'name': 'clear_matrix'},
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
    # as the other args, so it is set apart from the list
    value = ''

    # If the command requires value, it removes it from the current args list
    if function[command]['has_value']:
        value = args[-1]
        args = args[:len(args)-1]

    # Parse the arguments and pass it to the due function
    try:
        # Convert the numeric arguments from strings
        args = [int(arg) for arg in args]

        # This flags if it is necessary to do a subtraction operation before
        # passing the argument, since matrix operations are zero indexed,
        # while user interface operations aren't
        if function[command]['map_dimension']:
            args = [arg - 1 for arg in args]

        # Get TextImage method to be executed with its due arguments
        method = getattr(image,
                         function[command]['name'])

        # Reattach value to the argument list
        if value:
            args.append(value)

        # Unpack the parsed arguments to the due command function
        method(*args)

    # Handle expected exceptions raised from the TextImage class
    except ValueError:
        # Raised when parsing string into integers
        print_error('value')
        return

    except IndexError:
        # Raised while checing argument bounds in the image matrix
        print_error('bounds')
        return

    except AttributeError:
        # Raised when the attribute matrix is not properly set into the image
        print_error('empty')
        return
    except OSError:
        # Raised when failed to save file due to system issues
        print_error('file')
        return


def event_loop():
    """ User interaction loop

    It keeps inside a loop until the user exits the program with a valid 'X'
    command.

    """
    print_guide(initial=True)
    image = TextImage()
    while True:
        user_input = input("(press 'G' for guidance)> ")
        handle_user_input(image, user_input)


if __name__ == '__main__':
    event_loop()
