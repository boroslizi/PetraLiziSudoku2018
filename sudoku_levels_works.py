import os
import sys
import pickle
from copy import deepcopy
from grids import easy, medium, hard, win0, winwin
os.system("clear")

# different colors used for printing
COLORS = {"red": "\033[91m", "blue": "\033[34m", "grey": "\033[90m", "white": "\033[0m"}

# row and column indexing
INDEX_CAP = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9}
INDEX_SMALL = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}

# error messages used
ERRORS = [
    "\nThis number is already in that row.",
    "\nThis number is already in that column.",
    "\nOriginal board cannot be modified.",
    "\nNumber must be between 1 and 9.",
    "\nPlease enter a number from the list below.",
    "\nPlease enter either \"y\" or \"n\" after choosing save.",
    "\nPlease enter requested characters.",
    "\nThis number is already in that grid."
    ]


# printing the original grid
def print_sudoku(board, c_grid, c_end):
    print(c_grid + "\n    a   b   c   d   e   f   g   h   i  " + c_end)
    print(c_grid + "  ╔" + ("═══╤═══╤═══╦"*2) + "═══╤═══╤═══╗" + c_end)
    for i, row in enumerate(board):

            # middle part of long print line in print_sudoku
            def long_line(c1, c2):
                return (" {} " + c1 + "│" + c2 + " {} " + c1 + "│" + c2 + " {} " + c1 + "║" + c2)

            # format comprehension function
            def compr():
                return ([x if x != 0 else " " for x in row])

            print((c_grid + "{} ║" + c_end + (long_line(COLORS["grey"], COLORS["white"]))*3).format(*compr()))
            if i % 3 == 2 and i < 8:
                print(c_grid + "  ╠" + ("═══╪═══╪═══╬"*2) + "═══╪═══╪═══╣" + c_end)
            elif i == 8:
                print(c_grid + "  ╚" + ("═══╧═══╧═══╩"*2) + "═══╧═══╧═══╝" + c_end)
            else:
                print(c_grid + "  ╟" + ("───┼───┼───╫")*2 + "───┼───┼───╢" + c_end)


# printing a new grid after adding a new number
def grid_new(board, c_error, c_end):
    row_in = str(input("\nSelect a row (A - I): "))
    column_in = str(input("Select a column (a - i): "))
    num = int(input("Enter a number (1-9): "))
    os.system("clear")
    if num in board[int(INDEX_CAP[row_in]) - 1]:  # checking row
        print(c_error + ERRORS[0] + c_end)
    elif num in [col[int(INDEX_SMALL[column_in])] for col in board]:  # checking column
        print(c_error + ERRORS[1] + c_end)
    elif num > 0 and num < 10:  # checking if number is between 1 and 9
        if grid0[int(INDEX_CAP[row_in]) - 1][int(INDEX_SMALL[(column_in)])] == 0:
            board[int(INDEX_CAP[row_in]) - 1][int(INDEX_SMALL[(column_in)])] = num
        else:
            print(c_error + ERRORS[2] + c_end)
    else:
        print(c_error + ERRORS[3] + c_end)
    return board


# deleting a number
def grid_delete(board, c_error, c_end):
    print("\nDefine place for number to delete.")
    row_in = str(input("\nSelect a row (A - I): "))
    column_in = str(input("Select a column (a - i): "))
    os.system("clear")
    if grid0[int(INDEX_CAP[row_in]) - 1][int(INDEX_SMALL[(column_in)])] == 0:
        board[int(INDEX_CAP[row_in]) - 1][int(INDEX_SMALL[(column_in)])] = 0
    else:
        print(c_error + ERRORS[2] + c_end)
    return board


# printing menu1
def print_menuOne():
    print(COLORS["blue"] + r"""
  ____                _           _                _____       _
 / ___|   _   _    __| |   ___   | | __  _   _    |___ /      / |
 \___ \  | | | |  / _` |  / _ \  | |/ / | | | |     |_ \      | |
  ___) | | |_| | | (_| | | (_) | |   <  | |_| |    ___) |  _  | |
 |____/   \__,_|  \__,_|  \___/  |_|\_\  \__,_|   |____/  (_) |_|

    """ + COLORS["white"])
    print("\nWelcome to the Sudoku Game!\nMenu:")
    print("[1] Print New Board")
    print("[2] Load Saved Game")


# printing menu2
def print_menuTwo():
    print("\n[1] Easy")
    print("[2] Medium")
    print("[3] Hard")


# printing menu3
def print_menuThree():
    print("\n[1] Add number")
    print("[2] Delete number")
    print("[3] Save game")
    print("[4] Exit game")


# printing win text
def print_win():
    print(COLORS["blue"] + r"""
     __        __  ___   _   _   _
     \ \      / / |_ _| | \ | | | |
      \ \ /\ / /   | |  |  \| | | |
       \ V  V /    | |  | |\  | |_|
        \_/\_/    |___| |_| \_| (_)

    """ + COLORS["white"])


# menu1 & menu2 & menu3
for i in range(1):
    grid0 = []  # original grid, not to be modified
    grid = []  # second grid, zeros can be modified
    print_menuOne()
    try:
        action = int(input("\nWhat would you like to do? "))
        if action == 1:  # "Print New Board"
            os.system("clear")
            print_menuTwo()
            action2 = int(input("\nChoose a level! "))
            if action2 == 1:
                grid0 = easy
            elif action2 == 2:
                grid0 = medium
            elif action2 == 3:
                grid0 = hard
            elif action2 == 4:
                grid0 = win0
            grid = deepcopy(grid0)
            os.system("clear")
            print_sudoku(grid0, COLORS["grey"], COLORS["white"])
            # innen kivettem egy break-et és ezért működik (előtte csak a sudoku-ig rajzolta ki)
        elif action == 2:  # "Load Saved Game"
            os.system("clear")
            file = "saved_sudoku.pickle"
            with open(file, "rb") as f:
                grid0 = pickle.load(f)
                grid = deepcopy(grid0)
                os.system("clear")
                print_sudoku(grid0, COLORS["grey"], COLORS["white"])
                break
        else:
            os.system("clear")
            print(COLORS["red"] + ERRORS[4] + COLORS["white"])
    except ValueError:
        os.system("clear")
        print(COLORS["red"] + ERRORS[4] + COLORS["white"])
    while True:
        if grid == winwin:  # winning (csak grid0=win0 esetén működik :)
            print_win()
            break
        else:
            print_menuThree()
            try:
                action3 = int(input("\nWhat would you like to do? "))
                try:
                    if action3 == 1:  # "Add number"
                        grid = grid_new(grid, COLORS["red"], COLORS["white"])
                        print_sudoku(grid, COLORS["grey"], COLORS["white"])
                    elif action3 == 2:  # "Delete number"
                        grid = grid_delete(grid, COLORS["red"], COLORS["white"])
                        print_sudoku(grid, COLORS["grey"], COLORS["white"])
                    elif action3 == 3:  # "Save game"
                        file = "saved_sudoku.pickle"
                        with open(file, "wb") as f:
                            pickle.dump(grid, f)
                        saving = input("Are you sure you want to save and quit? (y/n)")
                        if saving == "y":
                            os.system("clear")
                            print("Sudoku game saved!\n")
                            break
                        elif saving == "n":
                            os.system("clear")
                            print_sudoku(grid, COLORS["grey"], COLORS["white"])
                        else:
                            os.system("clear")
                            print(COLORS["red"] + ERRORS[5] + COLORS["white"])
                            print_sudoku(grid, COLORS["grey"], COLORS["white"])
                    elif action3 == 4:  # "Exit game"
                        break
                    else:
                        os.system("clear")
                        print(COLORS["red"] + ERRORS[4] + COLORS["white"])
                        print_sudoku(grid, COLORS["grey"], COLORS["white"])
                except ValueError:
                    os.system("clear")
                    print(COLORS["red"] + ERRORS[6] + COLORS["white"])
                    print_sudoku(grid, COLORS["grey"], COLORS["white"])
            except ValueError:
                os.system("clear")
                print(COLORS["red"] + ERRORS[4] + COLORS["white"])
                print_sudoku(grid, COLORS["grey"], COLORS["white"])


