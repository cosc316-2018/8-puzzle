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

def solve_board(board):
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