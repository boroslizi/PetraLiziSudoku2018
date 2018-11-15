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
    if 0 < num < 10:  # checking if number is between 1 and 9
        if num in board[int(INDEX_CAP[row_in]) - 1]:  # checking row
            print(c_error + ERRORS[0] + c_end)
        elif num in [col[int(INDEX_SMALL[column_in])] for col in board]:  # checking column
            print(c_error + ERRORS[1] + c_end)
        elif row_in in ["A", "B", "C"] and column_in in ["a", "b", "c"]:
            for grid1_1 in [board[0][1:4], board[1][1:4], board[2][1:4]]:
                if num in grid1_1:
                    print(c_error + ERRORS[7] + c_end)
        elif row_in in ["A", "B", "C"] and column_in in ["d", "e", "f"]:
            for grid1_2 in [board[0][4:7], board[1][4:7], board[2][4:7]]:
                if num in grid1_2:
                    print(c_error + ERRORS[7] + c_end)
        elif row_in in ["A", "B", "C"] and column_in in ["g", "h", "i"]:
            for grid1_3 in [board[0][7:10], board[1][7:10], board[2][7:10]]:
                if num in grid1_3:
                    print(c_error + ERRORS[7] + c_end)
        elif row_in in ["D", "E", "F"] and column_in in ["a", "b", "c"]:
            for grid2_1 in [board[3][1:4], board[4][1:4], board[5][1:4]]:
                if num in grid2_1:
                    print(c_error + ERRORS[7] + c_end)
        elif row_in in ["D", "E", "F"] and column_in in ["d", "e", "f"]:
            for grid2_2 in [board[3][4:7], board[4][4:7], board[5][4:7]]:
                if num in grid2_2:
                    print(c_error + ERRORS[7] + c_end)
        elif row_in in ["D", "E", "F"] and column_in in ["g", "h", "i"]:
            for grid2_3 in [board[3][7:10], board[4][7:10], board[5][7:10]]:
                if num in grid2_3:
                    print(c_error + ERRORS[7] + c_end)
        elif row_in in ["G", "H", "I"] and column_in in ["a", "b", "c"]:
            for grid3_1 in [board[6][1:4], board[7][1:4], board[8][1:4]]:
                if num in grid3_1:
                    print(c_error + ERRORS[7] + c_end)
        elif row_in in ["G", "H", "I"] and column_in in ["d", "e", "f"]:
            for grid3_2 in [board[6][4:7], board[7][4:7], board[8][4:7]]:
                if num in grid3_2:
                    print(c_error + ERRORS[7] + c_end)
        elif row_in in ["G", "H", "I"] and column_in in ["g", "h", "i"]:
            for grid3_3 in [board[6][7:10], board[7][7:10], board[8][7:10]]:
                if num in grid3_3:
                    print(c_error + ERRORS[7] + c_end)
        elif grid0[int(INDEX_CAP[row_in]) - 1][int(INDEX_SMALL[(column_in)])] == 0:  # ez az else már nem fut le
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


# choosing level
def load_level(level):
    grid0 = level
    os.system("clear")
    print_sudoku(grid0, COLORS["grey"], COLORS["white"])
    return grid0


# menu1 & menu2
while True:
    grid0 = []  # original grid, not to be modified
    grid = []  # second grid, zeros can be modified
    print_menuOne()
    action = input("\nWhat would you like to do? ")
    if action == "1":  # "Print New Board"
        os.system("clear")
        print_menuTwo()
        action2 = input("\nChoose a level! ")
        while action2 not in ["1", "2", "3", "4"]:  # instead of the original else (which did not work ha)
            os.system("clear")
            print(COLORS["red"] + ERRORS[4] + COLORS["white"])
            print_menuTwo()
            action2 = input("\nChoose a level! ")
        if action2 == "1":  # Easy
            grid0 = load_level(easy)
            grid = deepcopy(grid0)
            break
        elif action2 == "2":  # Medium
            grid0 = load_level(medium)
            grid = deepcopy(grid0)
            break
        elif action2 == "3":  # Hard
            grid0 = load_level(hard)
            grid = deepcopy(grid0)
            break
        elif action2 == "4":  # Supereasy to win :)
            grid0 = load_level(win0)
            grid = deepcopy(grid0)
            break
    elif action == "2":  # "Load Saved Game"
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

# menu3
while grid != winwin:  # winning (only for grid0=win0)
    print_menuThree()
    action3 = input("\nWhat would you like to do? ")
    try:
        if action3 == "1":  # "Add number"
            grid = grid_new(grid, COLORS["red"], COLORS["white"])
            print_sudoku(grid, COLORS["grey"], COLORS["white"])
        elif action3 == "2":  # "Delete number"
            grid = grid_delete(grid, COLORS["red"], COLORS["white"])
            print_sudoku(grid, COLORS["grey"], COLORS["white"])
        elif action3 == "3":  # "Save game"
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
        elif action3 == "4":  # "Exit game"
            break
        else:
            os.system("clear")
            print(COLORS["red"] + ERRORS[4] + COLORS["white"])
            print_sudoku(grid, COLORS["grey"], COLORS["white"])
    except (ValueError, KeyError):
        os.system("clear")
        print(COLORS["red"] + ERRORS[6] + COLORS["white"])
        print_sudoku(grid, COLORS["grey"], COLORS["white"])

if grid == winwin:
    print_win()

# no main() because then --> "grid0 is not defined" error and we would need more time to fix that
