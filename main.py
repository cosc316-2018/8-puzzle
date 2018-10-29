from solve import solve_board
from random import randint


def generate_board():
    stack = [x for x in range(9)]
    puzzle = [[stack.pop(randint(0, len(stack) - 1)) for x in range(3)] for y in range(3)]
    return puzzle

    
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
# solve_board(my_board0)
# solve_board(my_board1)
# solve_board(my_board2)
# solve_board(my_board3)
# solve_board(my_board4)
# solve_board(my_board5)

solve_board(generate_board())
