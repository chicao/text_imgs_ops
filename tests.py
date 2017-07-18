import unittest as ut
from letters_valued_image import (initialize_matrix,
                                 clear_matrix)

class TestUserCommands(ut.TestCase):
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

        self.cols = 5
        self.rows = 4

    def tearDown(self):
        pass

    def test_initialize_matrix(self):
        init = initialize_matrix(self.cols, self.rows)
        self.assertTrue(init == self.empty_img)

    def test_clear_matrix(self):
        self.assertTrue(self.empty_img != self.filled_img)
        clear_matrix(self.filled_img)
        self.assertTrue(self.empty_img == self.filled_img)

    def test_lay_value_at(self):
        pass

    def test_vertical_values(self):
        pass

    def test_horizontal_values(self):
        pass

    def test_key_in_rect(self):
        pass

    def test_fill_region(self):
        pass

    def test_save_matrix(self):
        pass

    def test_matrix_2_str(self):
        pass


if __name__ == '__main__':
    ut.main()