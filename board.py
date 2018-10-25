class BoardState:
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

    def find_position(self, value, x, y):
        '''Another helper function for manhattan_distance().
        Finds where the number currently is.'''

        perfect_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        perfect_row = 0
        perfect_col = 0

        for row in range(len(perfect_board)):
            try:
                item_location = perfect_board[row].index(item)
                #checks for WHERE the number 6 is
            except:
                item_location = None
                #if 6 isnt there, return none
            if item_location:
                print(row, item_location)
                perfect_row = row
                perfect_col = item_location
                break

        return abs(x - perfect_row) + abs(y - perfect_col)

    def manhattan_distance(self):
        '''Calculates the total manhattan distance for a board -
        finding the distance between each value and where it should be,
        and adding up the resulting distance values.'''
        manhattans = 0
        for a in range(9):
            for x in range(3):
                for y in range(3):
                    if self.board[x][y] == a:
                        manhattans += self.find_position(a, x, y)
                        
        return manhattans



    def check_duplicate(self):
        # see if we've seen this board before
        # is the board already in the Queue
        # if board in queue:
        #        move to second best priority in that level
        #    else:
        #        keep on keepin on
        pass
