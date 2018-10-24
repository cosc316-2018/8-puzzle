from board import *

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
