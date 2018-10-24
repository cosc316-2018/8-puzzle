class Queue:
    def __init__(self):
        self.items = []

    def show(self):
        print(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]


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


q = Queue()
# this instantiates a queue object as q

q.show()
# this shows the queue instantiation q
for i in range(9):
    q.enqueue(i + 1)
# this is beyond my mortal understanding

q.show()
# this shows the queue instantiation, q

b = BoardState(q)
# this is a board state that takes a queue from 1-10 as arguments, which shockingly makes no sense


b.show()

# handler
# use boardstate stuff to
#
# main method


# set exit condition
