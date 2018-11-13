import os
import sys
import pickle
from copy import deepcopy
from grids import easy, medium, hard, win0, winwin
os.system("clear")

COLORS = [
    "\033[91m",  # red
    "\033[34m",  # blue
    "\033[90m",  # grey
    "\033[0m",  # white
    ]

grid0 = []  # original grid, not to be modified
grid = []  # second grid, zeros can be modified

# row and column indexing
index_cap = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9}
index_small = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}

# error messages used
error1 = "\nThis number is already in that row."
error2 = "\nThis number is already in that column."
error3 = "\nOriginal board cannot be modified."
error4 = "\nNumber must be between 1 and 9."
error5 = "\nPlease enter a number from the list below."
error6 = "\nPlease enter either \"y\" or \"n\" after choosing save."
error7 = "\nPlease enter requested characters."


# middle part of long print line in print_sudoku
def long_line(c1, c2):
    return (" {} " + c1 + "│" + c2 + " {} " + c1 + "│" + c2 + " {} " + c1 + "║" + c2)


# printing the original grid
def print_sudoku(board, c_grid, c_end):
    print(c_grid + "\n    a   b   c   d   e   f   g   h   i  " + c_end)
    print(c_grid + "  ╔" + ("═══╤═══╤═══╦"*2) + "═══╤═══╤═══╗" + c_end)
    for i, row in enumerate(board):

            # format comprehension function
            def compr():
                return ([x if x != 0 else " " for x in row])

            print((c_grid + "{} ║" + c_end + (long_line(COLORS[2], COLORS[3]))*3).format(*compr()))
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
    if num in board[int(index_cap[row_in]) - 1]:  # checking row
        os.system("clear")
        print(c_error + error1 + c_end)
    elif num in [col[int(index_small[column_in])] for col in board]:  # checking column
        os.system("clear")
        print(c_error + error2 + c_end)
    elif num > 0 and num < 10:  # checking if number is between 1 and 9
        if grid0[int(index_cap[row_in]) - 1][int(index_small[(column_in)])] == 0:
            board[int(index_cap[row_in]) - 1][int(index_small[(column_in)])] = num
            os.system("clear")
        else:
            os.system("clear")
            print(c_error + error3 + c_end)
    else:
        os.system("clear")
        print(c_error + error4 + c_end)
    return board


# deleting a number
def grid_delete(board, c_error, c_end):
    print("\nDefine place for number to delete.")
    row_in = str(input("\nSelect a row (A - I): "))
    column_in = str(input("Select a column (a - i): "))
    if grid0[int(index_cap[row_in]) - 1][int(index_small[(column_in)])] == 0:
        board[int(index_cap[row_in]) - 1][int(index_small[(column_in)])] = 0
        os.system("clear")
    else:
        os.system("clear")
        print(c_error + error3 + c_end)
    return board


# menu1 & menu2
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
            elif action2 == 2:
                grid0 = medium
            elif action2 == 3:
                grid0 = hard
            elif action2 == 4:
                grid0 = win0
            grid = deepcopy(grid0)
            os.system("clear")
            print_sudoku(grid0, COLORS[2], COLORS[3])
            break
        elif action == 2:
            os.system("clear")
            file = "saved_sudoku.pickle"
            with open(file, "rb") as f:
                grid0 = pickle.load(f)
                grid = deepcopy(grid0)
                os.system("clear")
                print_sudoku(grid0, COLORS[2], COLORS[3])
                break
        else:
            os.system("clear")
            print(COLORS[0] + error5 + COLORS[3])
    except ValueError:
        os.system("clear")
        print(COLORS[0] + error5 + COLORS[3])


# menu3
while True:
    if grid == winwin:  # winning
        print(cbegin + """
     __        __  ___   _   _   _
     \ \      / / |_ _| | \ | | | |
      \ \ /\ / /   | |  |  \| | | |
       \ V  V /    | |  | |\  | |_|
        \_/\_/    |___| |_| \_| (_)

    """ + cend)
        break
    else:
        print("\n[1] Add number")
        print("[2] Delete number")
        print("[3] Save game")
        print("[4] Exit game")
        try:
            action3 = int(input("\nWhat would you like to do? "))
            try:
                if action3 == 1:
                    grid = grid_new(grid, COLORS[0], COLORS[3])
                    print_sudoku(grid, COLORS[2], COLORS[3])
                elif action3 == 2:
                    grid = grid_delete(grid, COLORS[0], COLORS[3])
                    print_sudoku(grid, COLORS[2], COLORS[3])
                elif action3 == 3:
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
                        print_sudoku(grid, COLORS[2], COLORS[3])
                    else:
                        os.system("clear")
                        print(ebegin + error6 + eend)
                        print_sudoku(grid, COLORS[2], COLORS[3])
                elif action3 == 4:
                    break
                else:
                    os.system("clear")
                    print(ebegin + error5 + eend)
                    print_sudoku(grid, COLORS[2], COLORS[3])
            except ValueError:
                os.system("clear")
                print(ebegin + error7 + eend)
                print_sudoku(grid, COLORS[2], COLORS[3])
        except ValueError:
            os.system("clear")
            os.system("clear")
            print(ebegin + error5 + eend)
            print_sudoku(grid, COLORS[2], COLORS[3])
