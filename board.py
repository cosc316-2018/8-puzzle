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

    def __init__(self):
        # currently all 0
        # self.board = [q.items[i: i + 3] for i in range(0, len(q.items), 3)]
        self.board = [[5, 8, 1], [2, 0, 6], [3, 7, 4]]
        # should automatically know what the next boards are
        # be careful tho bc it can freak out at the end when it runs out of options
        # THIS IS AN IMPORTANT METHOD WE JUST DONT KNOW HOW TO USE IT YET
        # def create_next_board()
        # hey yall why not put it in the class and assign it to the _init_ function
        # has to run all the time - shouldnt be manual
        # Calculate the next possible board states

    # most 4 options, least 2

    def show_board(self):
        print(self.board)

    def find_location(self, value):
        for row in range(3):
            try:
                item_location = perfect_board[row].index(value)
                # print(row, item_location)
                #checks for WHERE the number 6 is
            except:
                item_location = None
                #if 6 isnt there, return none
            if item_location:
                print(value, row, item_location)
                break

    def md_calc(self, value, x, y):
        '''Another helper function for manhattan_distance().
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



    def check_duplicate(self):
        # see if we've seen this board before
        # is the board already in the Queue
        # if board in queue:
        #        move to second best priority in that level
        #    else:
        #        keep on keepin on
        pass
