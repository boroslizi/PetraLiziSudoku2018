import os
import sys
import pickle
from copy import deepcopy
from grids import easy, medium, hard
os.system("clear")

# original numbers color (lol, álmodik a nyomor)
cbegin = "\033[34m"
cend = "\033[0m"

# grid color
gbegin = "\033[90m"
gend = "\033[0m"

# error color
ebegin = "\033[91m"
eend = "\033[0m"

# original grid, not to be modified
grid0 = []

# second grid, zeros can be modified
grid = []

# row and column indexing
index_cap = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9}
index_small = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}


# middle part of long print line in print_sudoku
def long_line():
    return (" {} " + gbegin + "│" + gend + " {} " + gbegin + "│" + gend + " {} " + gbegin + "║" + gend)


# printing the original grid
def print_sudoku(board):
    print(gbegin + "\n    a   b   c   d   e   f   g   h   i  " + gend)
    print(gbegin + "  ╔" + ("═══╤═══╤═══╦"*2) + "═══╤═══╤═══╗" + gend)
    for i, row in enumerate(board):
            print((gbegin + "{} ║" + gend + (long_line())*3).format(*[x if x != 0 else " " for x in row]))
            if i % 3 == 2 and i < 8:
                print(gbegin + "  ╠" + ("═══╪═══╪═══╬"*2) + "═══╪═══╪═══╣" + gend)
            elif i == 8:
                print(gbegin + "  ╚" + ("═══╧═══╧═══╩"*2) + "═══╧═══╧═══╝" + gend)
            else:
                print(gbegin + "  ╟" + ("───┼───┼───╫")*2 + "───┼───┼───╢" + gend)


# printing a new grid after adding a new number
def grid_new(board):
    row_in = str(input("\nSelect a row (A - I): "))
    column_in = str(input("Select a column (a - i): "))
    num = int(input("Enter a number (1-9): "))
    if num in board[int(index_cap[row_in]) - 1]:
        os.system("clear")
        print(ebegin + "\nThis number is already in that row." + eend)
    elif num in [col[int(index_small[column_in])] for col in board]:
        os.system("clear")
        print(ebegin + "\nThis number is already in that column." + eend)
    elif num > 0 and num < 10:
        if grid0[int(index_cap[row_in]) - 1][int(index_small[(column_in)])] == 0:
            board[int(index_cap[row_in]) - 1][int(index_small[(column_in)])] = num
            os.system("clear")
        else:
            os.system("clear")
            print(ebegin + "\nOriginal board cannot be modified." + eend)
    else:
        os.system("clear")
        print(ebegin + "\nNumber must be between 1 and 9." + eend)
    return board


# deleting a number
def grid_delete(board):
    print("\nDefine place for number to delete.")
    row_in = str(input("\nSelect a row (A - I): "))
    column_in = str(input("Select a column (a - i): "))
    if grid0[int(index_cap[row_in]) - 1][int(index_small[(column_in)])] == 0:
        board[int(index_cap[row_in]) - 1][int(index_small[(column_in)])] = 0
        os.system("clear")
    else:
        os.system("clear")
        print(ebegin + "\nOriginal board cannot be modified." + eend)
    return board


# menu
while True:
    print("\nWelcome to the Sudoku Game!\nMenu:")
    print("[1] Print New Board")
    print("[2] Load Saved Game")
    try:
        action = int(input("\nWhat would you like to do? "))
        if action == 1:
            os.system("clear")
            print("\n[1] Easy")
            print("[2] Medium")
            print("[3] Hard")
            action2 = int(input("\nChoose a level! "))
            if action2 == 1:
                grid0 = easy
                grid = deepcopy(grid0)
                os.system("clear")
                print_sudoku(grid0)
                break
            elif action2 == 2:
                grid0 = medium
                grid = deepcopy(grid0)
                os.system("clear")
                print_sudoku(grid0)
                break
            elif action2 == 3:
                grid0 = hard
                grid = deepcopy(grid0)
                os.system("clear")
                print_sudoku(grid0)
                break
        elif action == 2:
            os.system("clear")
            file = "saved_sudoku.pickle"
            with open(file, "rb") as f:
                grid0 = pickle.load(f)
                grid = deepcopy(grid0)
                os.system("clear")
                print_sudoku(grid0)
                break
        else:
            os.system("clear")
            print(ebegin + "\nPlease enter a number from the list below." + eend)
    except ValueError:
        os.system("clear")
        print(ebegin + "\nPlease enter a number from the list below." + eend)


# menu3
while True:
    print("\n[1] Add number")
    print("[2] Delete number")
    print("[3] Save game")
    print("[4] Exit game")
    try:
        action3 = int(input("\nWhat would you like to do? "))
        try:
            if action3 == 1:
                grid = grid_new(grid)
                print_sudoku(grid)
            elif action3 == 2:
                grid = grid_delete(grid)
                print_sudoku(grid)
            elif action3 == 3:
                file = "saved_sudoku.pickle"
                with open(file, "wb") as f:
                    pickle.dump(grid, f)
            elif action3 == 4:
                break
            else:
                os.system("clear")
                print(ebegin + "\nPlease enter a number from the list below." + eend)
                print_sudoku(grid)
        except (ValueError, KeyError):
            os.system("clear")
            print(ebegin + "\nPlease enter requested characters." + eend)
            print_sudoku(grid)
    except ValueError:
        os.system("clear")
        os.system("clear")
        print(ebegin + "\nPlease enter a number from the list below." + eend)
        print_sudoku(grid)
