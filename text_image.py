"""Code for the TextImage class that holds text instance and manipulation

This module holds only the class implementation of the TextImage class. So,
if any new text image operation is necessary, it is added as a class method.
Any manipulation will need a image matrix, so holding an object to attach
operations to a matrix reference will simplify coding and avoid bad practices
such as globals variables declarations.
"""

class TextImage(object):
    """ Object that holds a text image matrix and its operations

    This is a wrapper for an multidimensional 2d list of str objects.
    This matrix will have columns and rows in such a way that it makes
    operations easy to call.

    The matrix start

    However, it is the responsibility of the programmer to assure that
    the indexes IN THE CALL are correct. While the user interface deals
    with indexes that start with one, this class deals with the zero indexed
    lists. This makes possible to change the user input interfaces without
    changing the underlining implementation of index references and bound
    checking.

    The class initialization gives precedence to a already given 2d list
    instead to the number of rows and columns. So if you give a image
    argument, the object will be filled and will set cols and rows with
    the list dimentions. Otherwise, will set an empty image matrix with
    size cols X rows.

    Args:
        image (list(list)): a 2d list to instantiate
        cols (int): number of columns to instantiate a empty image
        rows (int): number of rows to instantiate a empty image

    Attributes:
        image (list(list)): a 2d list (matrix) representing the image
        cols (int): number of columns of the image matrix
        rows (int): number of rows of the image matrix

    """

    def __init__(self, image=[], cols=0, rows=0):

        #
        # If a image was passed, instantiate the object with it
        if image:
            self.image = image
            self.cols = len(image)
            self.rows = len(image[0])
            return

        #
        # If no image was passed, instantiate an empty matrix
        self.cols = cols
        self.rows = rows
        self.initialize_matrix(cols, rows)

    def is_image_set(self):
        """Check if the class attribute image is setted with values

        If there is not an emtpy image, if flags to true. False, otherwise

        Returns:
            bool: flag of emtpy image attribute
        """
        if not self.image:
            return False

        if self.image:
            return all(self.image)

    def initialize_matrix(self, cols, rows):
        """ (Re)Initialize the image attribute with an empty matrix

        Args:
            cols (int): number of columns to instantiate a empty image
            rows (int): number of rows to instantiate a empty image
        """
        self.cols = cols
        self.rows = rows
        self.image = []
        for _ in range(cols):
            row = ['O' for _ in range(rows)]
            self.image.append(row)

    def clear_matrix(self):
        """ Set the image matrix to a zero valued ('O') attribute"""

        if not self.is_image_set():
            return

        for i in range(self.cols):
            for j in range(self.rows):
                self.image[i][j] = 'O'

    def lay_value_at(self, col, row, value):
        """ Input a value in a matrix position

        Args:
            col (int): Horizontal position of the insertion
            row (int): Vertical position of the insertion
            value (str): value to be inserted
        Raises:
            AttributeError: The operation is not possible due to an empty
                image of the class
        """

        if not self.is_image_set():
            raise AttributeError

        if not self.check_bounds(col, row):
            return

        self.image[col][row] = value

    def vertical_values(self, col, row_up, row_down, value):
        """ Insert a vertical line of values from a row to another

        Args:
            col (int): Horizontal position of the insertion
            row_up (int): Initial vertical position of the insertion
            row_down (int): Final vertical position of the insertion
            value (str): value to be inserted
        Raises:
            AttributeError: The operation is not possible due to an empty
                image of the class
            IndexError: The operation is not possible due invalid indexes
                or intervals (row_down less than or equal to row_up)
        """

        if not self.is_image_set():
            raise AttributeError

        if row_up > row_down:
            raise IndexError

        if not self.check_horizontal_bounds(col):
            raise IndexError

        if not self.check_vertical_bounds(row_up):
            raise IndexError

        if not self.check_vertical_bounds(row_down):
            raise IndexError

        for pos in range(row_up, row_down+1):
            self.image[col][pos] = value


    def horizontal_values(self, col_left, col_right, row, value):
        """ Insert a horizontal line of values from a column to another

        Args:
            col_left (int): Initial horizontal position of the insertion
            col_right (int): Final horizontal position of the insertion
            row (int): Vertical position of the insertion
            value (str): value to be inserted
        Raises:
            AttributeError: The operation is not possible due to an empty
                image of the class
            IndexError: The operation is not possible due invalid indexes
                or intervals (col_right less than or equal to col_left)
        """

        if not self.is_image_set():
            raise AttributeError

        if col_left > col_right:
            raise IndexError

        if not self.check_horizontal_bounds(col_left):
            raise IndexError

        if not self.check_horizontal_bounds(col_right):
            raise IndexError

        if not self.check_vertical_bounds(row):
            raise IndexError

        for pos in range(col_left, col_right+1):
            self.image[pos][row] = value

    def key_in_rect(self, col_top, row_top, col_bottom, row_bottom, value):
        """ Insert a rectangle from top-left to bottom-right positions

        Args:
            col_top (int): Top horizontal position of the rectangle
            row_top (int): Top verticaal position of the rectangle
            col_bottom (int): Bottom horizontal position of the rectangle
            row_bottom (int): Bottom vertical position of the rectangle
            value (str): value to be inserted

        Raises:
            AttributeError: The operation is not possible due to an empty
                image of the class
            IndexError: The operation is not possible due invalid indexes
                or intervals (row_down less than or equal to row_up)
        """

        if not self.is_image_set():
            raise AttributeError

        if col_top > col_bottom:
            raise IndexError

        if row_top > row_bottom:
            raise IndexError

        if not self.check_bounds(col_top, row_top):
            raise IndexError

        if not self.check_bounds(col_bottom, row_bottom):
            raise IndexError

        for col in range(col_top, col_bottom+1):
            for row in range(row_top, row_bottom+1):
                self.image[col][row] = value

    def fill_region(self, col, row, value):
        """ Fills an empty ('O' valued) region of the image

        Args:
            col (int): Initial horizontal position of the fill
            row (int): Initial vertical position of the fill
            value (str): value to fill the region

        Raises:
            AttributeError: The operation is not possible due to an empty
                image of the class
            IndexError: The operation is not possible due invalid indexes
                or intervals (row_down less than or equal to row_up)
        """

        if not self.is_image_set():
            raise AttributeError

        if not self.check_bounds(col, row):
            raise IndexError


        if self.image[col][row] != 'O':
            return

        self.image[col][row] = value

        if col > 0:
            self.fill_region(col-1, row, value)

        if row > 0:
            self.fill_region(col, row-1, value)

        if col < self.cols - 1:
            self.fill_region(col+1, row, value)

        if row < self.rows - 1:
            self.fill_region(col, row+1, value)


    def check_bounds(self, col, row):
        """ Checks if the given position is in the image bounds

        Args:
            col (int): Horizontal position of be checked
            row (int): Vertical position of the checked
        Returns:
            bool: Flags if the position is in the image bounds
        """

        if not self.check_horizontal_bounds(col):
            return False

        if not self.check_vertical_bounds(row):
            return False

        return True


    def check_horizontal_bounds(self, col):
        """ Checks if the given horizontal position is in the image bounds

        Args:
            col (int): Horizontal position of be checked
        Returns:
            bool: Flags if the position is in the image bounds
        """

        if col < 0:
            return False

        return col < self.cols


    def check_vertical_bounds(self, row):
        """ Checks if the given vertical position is in the image bounds

        Args:
            col (int): Horizontal position of be checked
        Returns:
            bool: Flags if the position is in the image bounds
        """

        if row < 0:
            return False

        return row < self.rows

    def image_2_str(self):
        """ Format the image matrix to a human readable format

        Returns:
            str: Human readable format of the image matrix
        """

        if not self.is_image_set():
            return ''

        output = ['']*self.cols

        for j in range(self.rows):
            for i in range(self.cols):
                output[j] += self.image[i][j]
            output[j] += '\n'

        return ''.join(output)

    def __str__(self):
        """ Human readable representation of the class value"""
        return self.image_2_str()

    def __repr__(self):
        """ Representation of the class value"""
        return "TextImage(cols=%s, rows=%s)" % self.cols, self.rows

    def save_matrix(self, filename):
        """ Saves the string representation of the image matrix to a file

        Args:
            filename (str): filename to be used in the saving

        Raises:
            OSError: The operation was not possible due some system related,
            error such as permissions, full disk, invalid filename and so on
        """
        try:
            with open(filename, 'w') as f:
                f.write(str(self))
        except:
            raise OSError

