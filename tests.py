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
        pos = 3,2
        check_img = [['A','Q','E','O'],
                     ['Z','A','G','I'],
                     ['O','C','G','E'],
                     ['Q','Q','Z','E'],
                     ['Q','T','P','R']]

        lay_value_at(self.filled_img, pos[0]-1, pos[1]-1, 'C')
        self.assertTrue(self.filled_img == check_img)

    def test_vertical_values(self):
        col = 4
        v_pos = 1,3
        check_img = [['A','Q','E','O'],
                     ['Z','A','G','I'],
                     ['O','B','G','E'],
                     ['C','C','C','E'],
                     ['Q','T','P','R']]

        vertical_values(self.filled_img,
                        col-1,
                        v_pos[0]-1,
                        v_pos[1]-1,
                        'C')
        self.assertTrue(self.filled_img == check_img)

    def test_horizontal_values(self):
        row = 4
        h_pos = 2,5

        check_img = [['A','Q','E','O'],
                     ['Z','A','G','C'],
                     ['O','B','G','C'],
                     ['Q','Q','Z','C'],
                     ['Q','T','P','C']]

        horizontal_values(self.filled_img,
                        h_pos[0]-1,
                        h_pos[1]-1,
                        row-1,
                        'C')

        self.assertTrue(self.filled_img == check_img)

    def test_key_in_rect(self):
        top = 2,3
        bottom = 5,4

        check_img = [['A','Q','E','O'],
                     ['Z','A','C','C'],
                     ['O','B','C','C'],
                     ['Q','Q','C','C'],
                     ['Q','T','C','C']]

        key_in_rect(self.filled_img,
                    top[0]-1,
                    top[1]-1,
                    bottom[0]-1,
                    bottom[1]-1,
                    'C')

        self.assertTrue(self.filled_img == check_img)

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

        fill_region(self.empty_img, pos[0], pos[1], 'C')
        self.assertTrue(self.empty_img == all_filled)

        fill_region(self.region_img, pos[0], pos[1], 'C')
        self.assertTrue(self.region_img == region_filled)

    def test_save_matrix(self):
        pass

    def test_matrix_2_str(self):
        pass


if __name__ == '__main__':
    ut.main()