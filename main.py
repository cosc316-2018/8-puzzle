from board import BoardState
from queue import Queue
import copy

def swap(board,x,y,x1,y1):
    '''Swaps two elements.'''
    board1 = copy.deepcopy(board.board)
    board1[x][y], board1[x1][y1] = board1[x1][y1], board1[x][y]
    return BoardState(board1, board)

def make_kids(b):
    '''Creates the "kid" boards - all of the next possible boards from the
    current position. '''
    board = b.board
    kids = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                if x == 0:
                    kids.append(swap(b, x, y, x+1, y))
                if x == 1:
                    kids.append(swap(b, x, y, x - 1, y))
                    kids.append(swap(b, x, y, x + 1, y))
                if x == 2:
                    kids.append(swap(b, x, y, x - 1, y))
                if y == 0:
                    kids.append(swap(b, x, y, x, y + 1))
                if y == 1:
                    kids.append(swap(b, x, y, x, y + 1))
                    kids.append(swap(b, x, y, x, y - 1))
                if y == 2:
                    kids.append(swap(b, x, y, x, y - 1))
                break
    return kids

def is_possible(board):
    '''Checks if the board is possible to be solved. Returns a boolean.'''
    inversions = 0
    a = [board[x][y] for x in range(3) for y in range(3)]
    b = [board[x][y] for x in range(3) for y in range(3)]

    b.sort()
    for x in range(9):
        if b[x] != x:
            return False
    a.remove(0)
    for x in a:
        f = a.index(x)
        g = a[f:]
        for y in g:
            if y > x:
                inversions += 1
    if inversions % 2 == 0:
        return True
    else:
        return False

def the_show(board):
    '''Checks the current board and compares it to the perfect board.
    It then runs a while loop and the "make_kids" until the current board matches the goal board.'''
    if not is_possible(board):
        print("Bro, not cool. Enter a valid board next time.")
        return
    q = Queue()
    q.put(BoardState(board, None))
    goal_state = [
       [1,2,3],
        [4,5,6],
        [7,8,0],
        ]
    done = False
    visited = Queue()
    while not done:
        current = q.push()
        # print(current.board)
        visited.put(current)
        if current.board == goal_state:
            print(current.board)
            return
        a = make_kids(current)
        for x in a:
            if q.instances(x) == 0 and visited.instances(x) == 0:
                q.put(x)
            elif q.instances(x) != 0:
                q[0].stepcost = 0

# Boards 0 and 4 are not possible. Boards 1, 2, 3 and 5 are possible.
my_board0 = [
       [7,4,8],
        [2,6,0],
        [1,5,3],
        ]

my_board1 = [
       [5,2,8],
        [4,1,7],
        [0,3,6],
        ]

my_board2 = [
       [5,2,6],
        [4,0,8],
        [7,3,1],
        ]

my_board3 = [
       [1,3,7],
        [4,2,5],
        [6,0,8],
        ]

my_board5 = [
       [2,0,5],
        [4,6,3],
        [8,7,1],
        ]

my_board4 = [
       [6,3,7],
        [4,2,5],
        [6,0,8],
        ]

#Test cases
the_show(my_board0)
the_show(my_board1)
the_show(my_board2)
the_show(my_board3)
the_show(my_board4)
the_show(my_board5)
