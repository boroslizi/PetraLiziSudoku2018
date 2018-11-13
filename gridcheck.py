    elif row_in in ["A", "B", "C"] and column_in in ["a", "b", "c"]:
        for grid1_1 in [board[0][1:4], board[1][1:4], board[2][1:4]]:
            if num in grid1_1:
                print(c_error + error8 + c_end)
    elif row_in in ["A", "B", "C"] and column_in in ["d", "e", "f"]:
        for grid1_2 in [board[0][4:7], board[1][4:7], board[2][4:7]]:
            if num in grid1_2:
                print(c_error + error8 + c_end)
    elif row_in in ["A", "B", "C"] and column_in in ["g", "h", "i"]:
        for grid1_3 in [board[0][7:10], board[1][7:10], board[2][7:10]]:
            if num in grid1_3:
                print(c_error + error8 + c_end)
    elif row_in in ["D", "E", "F"] and column_in in ["a", "b", "c"]:
        for grid2_1 in [board[3][1:4], board[4][1:4], board[5][1:4]]:
            if num in grid2_1:
                print(c_error + error8 + c_end)
    elif row_in in ["D", "E", "F"] and column_in in ["d", "e", "f"]:
        for grid2_2 in [board[3][4:7], board[4][4:7], board[5][4:7]]:
            if num in grid2_2:
                print(c_error + error8 + c_end)
    elif row_in in ["D", "E", "F"] and column_in in ["g", "h", "i"]:
        for grid2_3 in [board[3][7:10], board[4][7:10], board[5][7:10]]:
            if num in grid2_3:
                print(c_error + error8 + c_end)
    elif row_in in ["G", "H", "I"] and column_in in ["a", "b", "c"]:
        for grid3_1 in [board[6][1:4], board[7][1:4], board[8][1:4]]:
            if num in grid3_1:
                print(c_error + error8 + c_end)
    elif row_in in ["G", "H", "I"] and column_in in ["d", "e", "f"]:
        for grid3_2 in [board[6][4:7], board[7][4:7], board[8][4:7]]:
            if num in grid3_2:
                print(c_error + error8 + c_end)
    elif row_in in ["G", "H", "I"] and column_in in ["g", "h", "i"]:
        for grid3_3 in [board[6][7:10], board[7][7:10], board[8][7:10]]:
            if num in grid3_3:
                print(c_error + error8 + c_end)
