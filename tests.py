# -*- coding: utf8 -*-
""" Tests for image matrix operations

The text image processing simulation requires processing of multidimensional
lists. These operations are very sensitive to user input and proper
function testing will result in better reliability of the image matrices
manipulations.
"""

import unittest as ut
from text_image import TextImage


class TestTextImgManipulations(ut.TestCase):
    """ Test case for text image manipulations

    The setUp method is to ensure that each test will have a proper data
    to use as test manipulation and matrix criation checking

    Attributes:
        empty_img (list(list)): An empty 2d list for population and matrix
                                initialization checking
        filled_img (list(list)): A filled 2d list for functions manipulations
        region_img (list(list)): A partially filled 2d list for testing filling
                                 regions
        cols (int): column quantity
        rows (int): rows quantity
    """

    def setUp(self):

        self.empty_img = [['O', 'O', 'O', 'O'],
                          ['O', 'O', 'O', 'O'],
                          ['O', 'O', 'O', 'O'],
                          ['O', 'O', 'O', 'O'],
                          ['O', 'O', 'O', 'O']]

        self.filled_img = [['A', 'Q', 'E', 'O'],
                           ['Z', 'A', 'G', 'I'],
                           ['O', 'B', 'G', 'E'],
                           ['Q', 'Q', 'Z', 'E'],
                           ['Q', 'T', 'P', 'R']]

        self.region_img = [['O', 'O', 'O', 'O'],
                           ['O', 'D', 'A', 'O'],
                           ['O', 'I', 'I', 'I'],
                           ['I', 'O', 'O', 'O'],
                           ['I', 'O', 'O', 'O']]

        self.cols = 5
        self.rows = 4

        tmp_image = TextImage()
        tmp_image.image = self.filled_img
        tmp_image.cols = self.cols
        tmp_image.rows = self.rows
        self.image = tmp_image

    def test_initialize_matrix(self):

        # Test initialize filled matrix
        self.image.initialize_matrix(self.cols, self.rows)
        self.assertTrue(self.image.image == self.empty_img)

        # Test initialize empty matrix
        self.image.image = []
        self.image.initialize_matrix(self.cols, self.rows)
        self.assertTrue(self.image.image == self.empty_img)
        self.assertTrue(self.image.cols == self.cols)
        self.assertTrue(self.image.rows == self.rows)

        #
        # Test for different dimensions

        # Test for cols == rows
        cols = 3
        rows = 3

        check_img = [['O', 'O', 'O'],
                     ['O', 'O', 'O'],
                     ['O', 'O', 'O']]

        self.image.initialize_matrix(cols, rows)
        self.assertTrue(self.image.image == check_img)
        self.assertTrue(self.image.cols == cols)
        self.assertTrue(self.image.rows == rows)

        # Test for cols > rows
        cols = 3
        rows = 2
        check_img = [['O', 'O'],
                     ['O', 'O'],
                     ['O', 'O']]

        self.image.initialize_matrix(cols, rows)
        self.assertTrue(self.image.image == check_img)
        self.assertTrue(self.image.cols == cols)
        self.assertTrue(self.image.rows == rows)

        # Test for cols < rows
        cols = 2
        rows = 3
        check_img = [['O', 'O', 'O'],
                     ['O', 'O', 'O']]

        self.image.initialize_matrix(cols, rows)
        self.assertTrue(self.image.image == check_img)
        self.assertTrue(self.image.cols == cols)
        self.assertTrue(self.image.rows == rows)

    def test_clear_matrix(self):
        # Test cleaning a filled matrix
        self.image.clear_matrix()
        self.assertTrue(self.image.image == self.empty_img)

        # Test cleaning a empty image
        with self.assertRaises(AttributeError):
            self.image.image = []
            self.image.clear_matrix()

    def test_lay_value_at(self):

        # Test value input
        pos = 3,2
        check_img = [['A', 'Q', 'E', 'O'],
                     ['Z', 'A', 'G', 'I'],
                     ['O', 'C', 'G', 'E'],
                     ['Q', 'Q', 'Z', 'E'],
                     ['Q', 'T', 'P', 'R']]

        self.image.lay_value_at(pos[0]-1, pos[1]-1, 'C')
        self.assertTrue(self.filled_img == check_img)

        # Test lay value out of bounds
        pos = 10, 11
        with self.assertRaises(IndexError):
            self.image.lay_value_at(pos[0]-1, pos[1]-1, 'C')

        # Test lay value out of bounds (negative)
        pos = -10, 0
        with self.assertRaises(IndexError):
            self.image.lay_value_at(pos[0]-1, pos[1]-1, 'C')

        # Test lay value into empty matrix
        with self.assertRaises(AttributeError):
            pos = 3, 2
            self.image.image = []
            self.image.lay_value_at(pos[0]-1, pos[1]-1, 'C')

    def test_vertical_values(self):
        # Test vertical value input
        col = 4
        v_pos = 1, 3
        check_img = [['A', 'Q', 'E', 'O'],
                     ['Z', 'A', 'G', 'I'],
                     ['O', 'B', 'G', 'E'],
                     ['C', 'C', 'C', 'E'],
                     ['Q', 'T', 'P', 'R']]

        self.image.vertical_values(col-1,
                                   v_pos[0]-1,
                                   v_pos[1]-1,
                                   'C')
        self.assertTrue(self.image.image == check_img)

        # Test vertical value out of bounds
        col = 8
        v_pos = 1, 11
        with self.assertRaises(IndexError):
            self.image.vertical_values(col-1,
                                       v_pos[0]-1,
                                       v_pos[1]-1,
                                       'C')

        # Test vertical value out of bounds
        col = 2
        v_pos = 6, 11
        with self.assertRaises(IndexError):
            self.image.vertical_values(col-1,
                                       v_pos[0]-1,
                                       v_pos[1]-1,
                                       'C')

        # Test vertical value out of bounds (negative)
        col = -1
        v_pos = -3, 5
        with self.assertRaises(IndexError):
            self.image.vertical_values(col-1,
                                       v_pos[0]-1,
                                       v_pos[1]-1,
                                       'C')

        # Test vertical value invalid interval
        col = 2
        v_pos = 3, 1
        with self.assertRaises(IndexError):
            self.image.vertical_values(col-1,
                                       v_pos[0]-1,
                                       v_pos[1]-1,
                                       'C')

        # Test vertical value valid negative interval
        col = 2
        v_pos = -3, -1
        with self.assertRaises(IndexError):
            self.image.vertical_values(col-1,
                                       v_pos[0]-1,
                                       v_pos[1]-1,
                                       'C')

        # Test vertical value into empty matrix
        with self.assertRaises(AttributeError):
            col = 3
            v_pos = 2, 4
            self.image.image = []
            self.image.vertical_values(col-1,
                                       v_pos[0]-1,
                                       v_pos[1]-1,
                                       'C')

    def test_horizontal_values(self):
        # Test horizontal value input
        row = 4
        h_pos = 2, 5

        check_img = [['A', 'Q', 'E', 'O'],
                     ['Z', 'A', 'G', 'C'],
                     ['O', 'B', 'G', 'C'],
                     ['Q', 'Q', 'Z', 'C'],
                     ['Q', 'T', 'P', 'C']]

        self.image.horizontal_values(h_pos[0]-1,
                                     h_pos[1]-1,
                                     row-1,
                                     'C')

        self.assertTrue(self.image.image == check_img)

        # Test horizontal value out of bounds
        row = 6
        h_pos = 2, 5
        with self.assertRaises(IndexError):
            self.image.horizontal_values(h_pos[0]-1,
                                         h_pos[1]-1,
                                         row-1,
                                         'C')

        # Test horizontal value out of bounds
        row = 4
        h_pos = 10, 12
        with self.assertRaises(IndexError):
            self.image.horizontal_values(h_pos[0]-1,
                                         h_pos[1]-1,
                                         row-1,
                                         'C')

        # Test horizontal value out of bounds (negative)
        row = -3
        h_pos = -4, -1
        with self.assertRaises(IndexError):
            self.image.horizontal_values(h_pos[0]-1,
                                         h_pos[1]-1,
                                         row-1,
                                         'C')

        # Test horizontal value valid negative interval
        row = 4
        h_pos = -5, -2
        with self.assertRaises(IndexError):
            self.image.horizontal_values(h_pos[0]-1,
                                         h_pos[1]-1,
                                         row-1,
                                         'C')

        # Test horizontal value invalid interval
        row = 4
        h_pos = 5, 2
        with self.assertRaises(IndexError):
            self.image.horizontal_values(h_pos[0]-1,
                                         h_pos[1]-1,
                                         row-1,
                                         'C')

        # Test horizontal value into empty matrix
        with self.assertRaises(AttributeError):
            row = 4
            h_pos = 2, 5
            self.image.image = []
            self.image.horizontal_values(h_pos[0]-1,
                                         h_pos[1]-1,
                                         row-1,
                                         'C')

    def test_key_in_rect(self):
        top = 2, 3
        bottom = 5, 4

        check_img = [['A', 'Q', 'E', 'O'],
                     ['Z', 'A', 'C', 'C'],
                     ['O', 'B', 'C', 'C'],
                     ['Q', 'Q', 'C', 'C'],
                     ['Q', 'T', 'C', 'C']]

        self.image.key_in_rect(top[0]-1,
                               top[1]-1,
                               bottom[0]-1,
                               bottom[1]-1,
                               'C')

        self.assertTrue(self.image.image == check_img)

        # Test top out of bounds
        top = 4, 8
        bottom = 3, 4
        with self.assertRaises(IndexError):
            self.image.key_in_rect(top[0]-1,
                                   top[1]-1,
                                   bottom[0]-1,
                                   bottom[1]-1,
                                   'C')

        # Test bottom value out of bounds
        top = 1, 1
        bottom = 10, 14
        with self.assertRaises(IndexError):
            self.image.key_in_rect(top[0]-1,
                                   top[1]-1,
                                   bottom[0]-1,
                                   bottom[1]-1,
                                   'C')

        # Test values out of bounds (negative)
        top = 5, -5
        bottom = -22, 2
        with self.assertRaises(IndexError):
            self.image.key_in_rect(top[0]-1,
                                   top[1]-1,
                                   bottom[0]-1,
                                   bottom[1]-1,
                                   'C')

        # Test rectangle creation into empty matrix
        with self.assertRaises(AttributeError):
            top = 3, 4
            bottom = 4, 5
            self.image.image = []
            self.image.key_in_rect(top[0]-1,
                                   top[1]-1,
                                   bottom[0]-1,
                                   bottom[1]-1,
                                   'C')

    def test_fill_region(self):

        # Test fill regions
        pos = 4, 3

        all_filled = [['C', 'C', 'C', 'C'],
                      ['C', 'C', 'C', 'C'],
                      ['C', 'C', 'C', 'C'],
                      ['C', 'C', 'C', 'C'],
                      ['C', 'C', 'C', 'C']]

        region_filled = [['O', 'O', 'O', 'O'],
                         ['O', 'D', 'A', 'O'],
                         ['O', 'I', 'I', 'I'],
                         ['I', 'C', 'C', 'C'],
                         ['I', 'C', 'C', 'C']]

        # Test fill empty matrix
        self.image.image = self.empty_img
        self.image.fill_region(pos[0],
                               pos[1],
                               'C')
        self.assertTrue(self.image.image == all_filled)

        # Test fill subregion matrix
        self.image.image = self.region_img
        self.image.fill_region(pos[0],
                               pos[1],
                               'C')
        self.assertTrue(self.image.image == region_filled)

        # Test fill out of bounds
        with self.assertRaises(IndexError):
            pos = 5, 5
            self.image.fill_region(pos[0],
                                   pos[1],
                                   'C')

        # Test fill out of bounds (negative)
        with self.assertRaises(IndexError):
            pos = -2, -10
            self.image.fill_region(pos[0],
                                   pos[1],
                                   'C')

        # Test fill empty matrix
        with self.assertRaises(AttributeError):
            pos = 4, 3
            self.image.image = []
            self.image.fill_region(pos[0],
                                   pos[1],
                                   'C')

    def test_matrix_2_str(self):
        converted = ('AZOQQ\n'
                     'QABQT\n'
                     'EGGZP\n'
                     'OIEER\n')
        output = self.image.image_2_str()
        self.assertTrue(converted == output)


if __name__ == '__main__':
    ut.main()
