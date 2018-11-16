
def getRowCol(board, row = 0, L = []):
    
    if row == len(board) - 1:
        return L
        
    else:
        for col in range(len(board[0])):
            if board[row][col] != 0:
                L += [(row, col)]
        return getRowCol(board, row + 1)
    
# input: incomplete sudoku board
# output: completed sudoku board
def solveSudoku(board, n = 1, m = 1):
    
    if n == len(board) - 1:
        print(board)
        return board
    
    if m == len(board[0]) - 1:
        return solveSudoku(board, n + 1, 1)
        
    else:
        row = len(board) - n
        col = len(board) - m
        print(row, col)
        
        if board[row][col] == 0:
            for move in range(1, 10):
            
                if isLegalMove(board, row, col, move):
                    board[row][col] = move
                    solution = solveSudoku(board, n, m + 1)
                    
                    if solution != None:
                        print(solution)
                        return solution
                    else:
                        board[row][col] = 0
                        
            return None










#################
def isLegalMove(board, row, col, move):
    b = copy.deepcopy(board)
    b[row][col] = move
    if isLegalSudoku(b):
        return True
    else:
        return False

# input: incomplete sudoku board
# output: completed sudoku board
def solveSudoku(board, n = 0, m = 0):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    if n == len(board):
        return board
    
    if m == len(board[0]):
        return solveSudoku(board, n + 1, m = 0)
        
    else:
        row = len(board) - n
        col = len(board) - m
        if board[row][col] != 0:
            for move in range(1, 10):
                if isLegalMove(board, row, col, move):
                    board[row][col] = move
                    solution = solveSudoku(board, n, m + 1)
                    if solution != None:
                        return solution
                    else:
                        board[row][col] = 0
                        
        return None
                    
                    
                    
# before

# input: incomplete sudoku board
# output: completed sudoku board
def solveSudoku(board, row = 0, col = 0):
    
    if (row,col) == (len(board), len(board[0])):
        return board
        
    else:
        # place and check num 1-9 in each row/col
        for row in range(len(board)):
            
            if board[row][col] == 0:
                
                for num in range(1, 10):
                    board[row][col] = num
                    
                    if isLegalSudoku(board):
                        break
            
            else:
                board = solveSudoku(board, col + 1)

        return board
        
        
# # input: incomplete sudoku board
# # output: completed sudoku board
# def solveSudoku(board):
#     pass
#     if None:
#         return None
#         
#     else:
#         # place and check num 1-9 in each row/col
#         for row in range(len(board)):
#             for col in range(len(board[row])):
#                 if board[row][col] == 0:
#                     for num in range(1, 10):
#                         board[row][col] = num
#                         if isLegalSudoku(board):
#                             break
#                         
     