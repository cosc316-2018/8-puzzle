class BoardState:
    # a dictionary created using list comprehensions
    # stores the row and column values of the perfect board
    # as a class attribute
    PERFECT_BOARD_INDICES = {
                                [[1, 2, 3], [4, 5, 6], [7, 8, 0]][x][y] :
                                    {
                                        'row': x,
                                        'col': y
                                    }
                                for x in range(3)
                                for y in range(3)
                            }

    def __init__(self, board, parent):
        self.parent = parent
        self.board = board
        self.stepcost = self.findsteps()
        self.manhattan = self.manhattan_distance()
        self.priority = self.manhattan + self.stepcost
        # self.board = [q.items[i: i + 3] for i in range(0, len(q.items), 3)]

    def show_board(self):
        print(self.board)

    def findsteps(self):
        if self.parent is None:
            return 0
        else:
            return self.parent.stepcost + 1

    def md_calc(self, value, x, y):
        '''A helper function for manhattan_distance().
        Compares the current board state to a perfect board state,
        returning the manhattan distance for the specific value that is
        indexed.'''

        # access the class attribute to get the perfect row and column indices
        # for the specific value
        perfect_row = self.PERFECT_BOARD_INDICES[value]['row']
        perfect_col = self.PERFECT_BOARD_INDICES[value]['col']

        # calculate and return the manhattan distance
        return abs(x - perfect_row) + abs(y - perfect_col)

    def manhattan_distance(self):
        '''Calculates the total manhattan distance for a board -
        finding the distance between each value and where it should be,
        and adding up the resulting distance values.'''

        # using list comprehensions to generate a list of manhattan distances for
        # all the values in their current board positions
        manhattans = [self.md_calc(self.board[x][y], x, y) for x in range(3) for y in range(3)]

        # return the sum of all the manhattan distances - this is the manhattan
        # distance for the entire board
        return sum(manhattans)
