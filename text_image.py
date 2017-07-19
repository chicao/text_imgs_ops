class TextImage(object):

    def __init__(self):
        self.image = []
        self.cols = 0
        self.rows = 0

    def initialize_matrix(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.image = []
        for _ in range(cols):
            row = ['O' for _ in range(rows)]
            self.image.append(row)

    def clear_matrix(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.image[i][j] = 'O'

    def lay_value_at(self, col, row, value):
        if not self.check_bounds(col, row):
            return

        self.image[col][row] = value


    def vertical_values(self, col, row_up, row_down, value):
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
        if not self.check_horizontal_bounds(col):
            return False

        if not self.check_vertical_bounds(row):
            return False

        return True


    def check_horizontal_bounds(self, col):
        if col < 0:
            return False

        return col < self.cols


    def check_vertical_bounds(self, row):
        if row < 0:
            return False

        return row < self.rows

    def save_matrix(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

        return

    def image_2_str(self):
        output = ['']*self.cols

        for j in range(self.rows):
            for i in range(self.cols):
                output[j] += self.image[i][j]
            output[j] += '\n'

        return ''.join(output)

    def __str__(self):
        return self.image_2_str()
