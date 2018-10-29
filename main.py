from solve import solve_board
from random import randint


def generate_board():
    '''Generate a random puzzle to be solved by the 8-puzzle solving algorithm'''
    num_list = [x for x in range(9)]
    # adds a random value from the list of numbers to the puzzle
    #and then removes that value from the list
    puzzle = [[num_list.pop(randint(0, len(num_list) - 1)) for x in range(3)] for y in range(3)]
    return puzzle


solve_board(generate_board())
