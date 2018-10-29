from board import BoardState
from queue import Queue
import copy


def swap(board,x,y,x1,y1):
    '''Swaps two elements.'''
    board1 = copy.deepcopy(board.board)
    board1[x][y], board1[x1][y1] = board1[x1][y1], board1[x][y]
    return BoardState(board1, board)


def create_children(brd):
    '''Creates the descendants of this board - all of the next possible boards from the
    current position. '''
    board = brd.board
    children = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                if x == 0:
                    children.append(swap(brd, x, y, x+1, y))
                if x == 1:
                    children.append(swap(brd, x, y, x - 1, y))
                    children.append(swap(brd, x, y, x + 1, y))
                if x == 2:
                    children.append(swap(brd, x, y, x - 1, y))
                if y == 0:
                    children.append(swap(brd, x, y, x, y + 1))
                if y == 1:
                    children.append(swap(brd, x, y, x, y + 1))
                    children.append(swap(brd, x, y, x, y - 1))
                if y == 2:
                    children.append(swap(brd, x, y, x, y - 1))
                break
    return children


def is_possible(board):
    '''Checks if the board is possible to be solved. Returns a boolean.'''
    inversions = 0
    a = [board[x][y] for x in range(3) for y in range(3)]
    b = [board[x][y] for x in range(3) for y in range(3)]

    # a check for whether any invalid values exist in the board
    b.sort()
    for x in range(9):
        if b[x] != x:
            print('Invalid value found in board')
            return False

    a.remove(0)
    for x in a:
        f = a.index(x)
        g = a[f:]
        for y in g:
            if y > x:
                inversions += 1
    
    print('Number of Inversions:', inversions)
    if inversions % 2 == 0:
        return True
    else:
        return False


def solve_board(board):
    '''Checks the current board and compares it to the perfect board.
    It then runs a while loop and the "create_children" until the current board matches the goal board.'''
    # show initial board configuration
    show_board(board)
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

    visited = Queue()
    while True:
        current = q.push()
        visited.put(current)
        if current.board == goal_state:
            print('Board solved successfully!!')
            show_board(current.board)            
            return
        a = create_children(current)
        for x in a:
            if q.instances(x) == 0 and visited.instances(x) == 0:
                q.put(x)
            elif q.instances(x) != 0:
                q[0].stepcost = 0


def show_board(board):
        print('\n')
        print('\n  -----------')
        # uses board to refer to list of list that represents the grid
        for row in board:
            print(' |', end=' ')
            for column in row:
                print(str(column), end=' | ')
            print('\n  -----------')
        print('\n')
        return ''