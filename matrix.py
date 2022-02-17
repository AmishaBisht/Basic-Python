'''your code should be able to spit out:

A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
A list of the columns, reading each column top-to-bottom while moving from left-to-right.'''




class Matrix(object):
    def __init__(self, matrix_string):    
        # matrix_string = "1 2\n3 4\n5 6"
        splitted = matrix_string.split('\n')
        # splitted = ["1 2", "3 4", "5 6"]
        self.rows = []
        self.columns = []
        for item in splitted:
            # item = "1 2"
            row = []
            numbers = item.split(" ")
            # for number in item.split(" "):
            for i in range(len(numbers)):
                # number = "1"
                row.append(int(numbers[i]))
                try:
                    self.columns[i]
                except IndexError:
                    self.columns.append([])
                self.columns[i].append(int(numbers[i]))
            # row = [1, 2]
            self.rows.append(row)
            # rows = [[1, 2], [3,4], [5,6]]
    def row(self, index):
        return self.rows[index-1]
    def column(self, index):
        return self.columns[index-1]
