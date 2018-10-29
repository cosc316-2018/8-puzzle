from solve import solve_board
from random import randint


def generate_board():
    stack = [x for x in range(9)]
    puzzle = [[stack.pop(randint(0, len(stack) - 1)) for x in range(3)] for y in range(3)]
    return puzzle



solve_board(generate_board())
