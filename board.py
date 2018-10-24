from queue import Queue

class BoardState:
    # i definitely can't find the banter section in PEP8
    def __init__(self, q):
        # currently all 0
        self.board = [q.items[i: i + 3] for i in range(0, len(q.items), 3)]
        # should automatically know what the next boards are
        # be careful tho bc it can freak out at the end when it runs out of options
        # THIS IS AN IMPORTANT METHOD WE JUST DONT KNOW HOW TO USE IT YET
        # def create_next_board()
        # hey yall why not put it in the class and assign it to the _init_ function
        # has to run all the time - shouldnt be manual
        # Calculate the next possible board states

    # most 4 options, least 2

    def show(self):
        print(self.board)

    def manhattan_distance(self):
        pass

    def check_duplicate(self):
        # see if we've seen this board before
        # is the board already in the Queue
        # if board in queue:
        #        move to second best priority in that level
        #    else:
        #        keep on keepin on
        pass
