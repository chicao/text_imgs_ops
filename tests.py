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

        self.empty_img = [['O','O','O','O'],
                          ['O','O','O','O'],
                          ['O','O','O','O'],
                          ['O','O','O','O'],
                          ['O','O','O','O']]

        self.filled_img = [['A','Q','E','O'],
                           ['Z','A','G','I'],
                           ['O','B','G','E'],
                           ['Q','Q','Z','E'],
                           ['Q','T','P','R']]

        self.region_img = [['O','O','O','O'],
                           ['O','D','A','O'],
                           ['O','I','I','I'],
                           ['I','O','O','O'],
                           ['I','O','O','O']]

        self.cols = 5
        self.rows = 4

        tmp_image = TextImage()
        tmp_image.image = self.filled_img
        tmp_image.cols = self.cols
        tmp_image.rows = self.rows
        self.image = tmp_image

    def tearDown(self):
        pass

    def test_initialize_matrix(self):
        self.image.initialize_matrix(self.cols, self.rows)
        self.assertTrue(self.image.image == self.empty_img)

    def test_clear_matrix(self):
        self.image.image = self.filled_img
        self.image.cols = self.cols
        self.image.rows = self.rows

        self.image.clear_matrix()
        self.assertTrue(self.image.image == self.empty_img)

    def test_lay_value_at(self):
        pos = 3,2
        check_img = [['A','Q','E','O'],
                     ['Z','A','G','I'],
                     ['O','C','G','E'],
                     ['Q','Q','Z','E'],
                     ['Q','T','P','R']]

        self.image.lay_value_at(pos[0]-1, pos[1]-1, 'C')
        self.assertTrue(self.filled_img == check_img)


    def test_vertical_values(self):
        col = 4
        v_pos = 1,3
        check_img = [['A','Q','E','O'],
                     ['Z','A','G','I'],
                     ['O','B','G','E'],
                     ['C','C','C','E'],
                     ['Q','T','P','R']]

        self.image.vertical_values(col-1,
                                   v_pos[0]-1,
                                   v_pos[1]-1,
                                   'C')
        self.assertTrue(self.image.image == check_img)

    def test_horizontal_values(self):
        row = 4
        h_pos = 2,5

        check_img = [['A','Q','E','O'],
                     ['Z','A','G','C'],
                     ['O','B','G','C'],
                     ['Q','Q','Z','C'],
                     ['Q','T','P','C']]

        self.image.horizontal_values(h_pos[0]-1,
                                     h_pos[1]-1,
                                     row-1,
                                     'C')

        self.assertTrue(self.image.image == check_img)

    def test_key_in_rect(self):
        top = 2,3
        bottom = 5,4

        check_img = [['A','Q','E','O'],
                     ['Z','A','C','C'],
                     ['O','B','C','C'],
                     ['Q','Q','C','C'],
                     ['Q','T','C','C']]

        self.image.key_in_rect(top[0]-1,
                                top[1]-1,
                                bottom[0]-1,
                                bottom[1]-1,
                                'C')

        self.assertTrue(self.image.image == check_img)

    def test_fill_region(self):
        pos = 4,3

        all_filled = [['C','C','C','C'],
                      ['C','C','C','C'],
                      ['C','C','C','C'],
                      ['C','C','C','C'],
                      ['C','C','C','C']]

        region_filled = [['O','O','O','O'],
                         ['O','D','A','O'],
                         ['O','I','I','I'],
                         ['I','C','C','C'],
                         ['I','C','C','C']]

        self.image.image = self.empty_img

        self.image.fill_region(pos[0],
                               pos[1],
                               'C')
        self.assertTrue(self.image.image == all_filled)


        self.image.image = self.region_img
        self.image.fill_region(pos[0],
                               pos[1],
                               'C')
        self.assertTrue(self.image.image == region_filled)

    def test_matrix_2_str(self):
        converted = ('AZOQQ\n'
                     'QABQT\n'
                     'EGGZP\n'
                     'OIEER\n')
        output = self.image.image_2_str()
        self.assertTrue(converted == output)


if __name__ == '__main__':
    ut.main()