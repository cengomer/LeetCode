def isValidSudoko(board):
    for row in board: 
        row_set = set()
        for item in row: 
            if item != ".":
                if item in row_set:
                    return False
    
    for col in range(9): 
        col_set = set()
        for row in range(9):
            item = board[row][col]
            if item != ".":
                if item in col_set:
                    return False
                col_set.add(item)
    

    for box_row in range(0,9,3):
        for box_col in range(0,9,3):
            box_set = set()
            for i in range(3):
                for j in range(3):
                    item = board[box_row + i][box_col + j]
                    if item != ".":
                        if item in box_set:
                            return False
                        box_set.add(item)

            return True    
