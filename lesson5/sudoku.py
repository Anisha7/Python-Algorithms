#################################################
# hw5 library
# Anisha Jain, anishaj
###################ee##############################


import math, string, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

### Your lab5 functions below ###

# Sudoku Helpers

# input: 1d list of length n**2 with integers 0 to n**2 inclusive
# output: True or False, if values, except 0, are not repeated
def areLegalValues(values):
    
    valueList = copy.copy(values)
    n = math.sqrt(len(valueList)) # length of each block in board
    
    for num in valueList:
        #print("num: ", num)
        if num != int(num):
            return False
                
        elif num >= 0 and num <= n**2:
            
            if num == 0:
                continue
                
            elif valueList.count(num) != 1:
                #print("count: ", valueList.count(num))
                return False
                
        else:
            return False

    return True

# input: 2d list of 1d lists (rows) and the row number
# output: True or False, if row passes areLegalValues   
def isLegalRow(board, row):
    
    rowList = board[row]
    n = math.sqrt(len(rowList)) # length of each block in board
    
    if row >= 0 and row < (n**2):
        if areLegalValues(rowList):
            return True
        
        else:
            return False
    
# input: 2d list of 1d lists (rows) and the column number   
# output: True or False, if column passes areLegalValues
def isLegalCol(board, col):
    
    colList = []
    
    for row in board:
        
        #print(row)
        colList += [row[col]]
        
    #print("colList: ", colList)
    
    if areLegalValues(colList) == True:
        return True
    else:
        return False

# Helper for isLegalBlock
# Uses block to get outer range num for row 
# ex. if block = 2: rowRange = 3
def getRowRange(board, block):
    
    n = int(math.sqrt(len(board)))
    #print("n: ", n)
    num = block/n
    rowRange = 0
    
    for i in range(0, (n**2) + 1, n):
        #print("i: ", i)
        #print("block: ", block)
        if block == 0:
            rowRange = n
            break
        
        elif (block < i) == True:
            
            rowRange = i
            break
        
        elif block == n**2:
            
            rowRange = n**2
            
    return rowRange

# Helper for isLegalBlock
# Uses block to get outer range num for col
# ex. if block = 2: colRange = 6
def getColRange(board, block):
    
    n = int(math.sqrt(len(board)))
    blockCol = block % n 
    #print("blockCol: ", blockCol)
    # this gives the number for all aligning columns 
    # stacked on top of each other
    
    listN = []
    
    for i in range(n, int((n**2))+1, n):
        
        listN += [i]
        # adds numbers skipping by n upto n**2 
        # to get column range blocks
    #print(listN)
    colRange = listN[blockCol]
         
    
    return colRange

# input: board and block number
# output: a list of numbers in a sudoku block
def getBlockList(board, block):
    
    blockList = []
    n = int(math.sqrt(len(board)))

        
    rowRange = getRowRange(board, block)
    colRange = getColRange(board, block) 
    
    for row in range(rowRange - n, rowRange):
        for col in range(colRange - n, colRange):
            blockList += [board[row][col]]
    
    return blockList
    
# input: 2d list of 1d lists (rows) and the block number
# block: 0 is the left-top block, and nums go across then down
# create 1d list of length n**2 holding values of block
# output: True or False, if block passes areLegalValues   
def isLegalBlock(board, block):
    
    blockList = getBlockList(board, block)
    n = math.sqrt(len(board))

    if areLegalValues(blockList):
        return True
    else:
        return False

# input: n**2 x n**2 - 2d list
# output: True or False, if board is legal
def isLegalSudoku(board):
    
    n = int(math.sqrt(len(board)))
    
    for i in range(0, (n**2)):
        
        if isLegalRow(board, i) == False:
            return False
    
    for i in range(0, (n**2)):
        
        if isLegalCol(board, i) == False:
            return False
            
    for blockI in range(0, (n**2) + 1, n):
        
        if isLegalBlock(board, blockI) == False:
            return False
    
    return True


#################################################
# Test Functions
#################################################

    
def testAreLegalValues():
    print("testing areLegalValues()...", end = "")
    
    values = [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ]
    assert(areLegalValues(values) == True)
    
    values = [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ]
    assert(areLegalValues(values) == True)
    
    values = [ 0, 9, 8, 0, 9, 0, 0, 6, 0 ]
    assert(areLegalValues(values) == False)
    
    values = [ 8, 0, 8, 12, 6, 0, 0, 0, 3 ]
    assert(areLegalValues(values) == False)
    
    values = [ 8, 0, 0, 0, 6.2, 0, 0, 0, 3 ]
    assert(areLegalValues(values) == False)
    
    values = [ -8, 0, 0, 0, 6, 0, 0, 0, -3 ]
    assert(areLegalValues(values) == False)
    
    print("Passed")

def testIsLegalRow():
    print("testing isLegalRow()...", end = "")
    
    board = [
                [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
                [ 6, 0, 1, 1, 9, 5, 0, 0, 0 ],
                [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
                [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
                [ 4, 0, 0, -8, 0, 3, 0, 0, 1 ],
                [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
                [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
                [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
                [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]
    
    assert(isLegalRow(board, 0) == True)
    assert(isLegalRow(board, 1) == False)
    assert(isLegalRow(board, 3) == True)
    assert(isLegalRow(board, 4) == False)
    
    print("Passed")
    
def testIsLegalCol():
    print("testing isLegalRow()...", end = "")
    
    board = [
                [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
                [ 6, 0, 1, 1, 9, 5, 0, 0, 0 ],
                [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
                [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
                [ 4, 0, 0, -8, 0, 3, 0, 0, 1 ],
                [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
                [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
                [ 0, 6, 0, 4, 1, 9, 0, 0, 5 ],
                [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]
    
    assert(isLegalCol(board, 0) == True)
    assert(isLegalCol(board, 1) == False)
    assert(isLegalCol(board, 3) == False)
    assert(isLegalCol(board, 4) == True)
    
    print("Passed")

def testGetRowRange():
    print("testing getRowRange()...", end = "")
    
    board = [
                [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
                [ 6, 0, 1, 1, 9, 5, 0, 0, 0 ],
                [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
                [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
                [ 4, 0, 0, -8, 0, 3, 0, 0, 1 ],
                [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
                [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
                [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
                [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]
            
    assert(getRowRange(board, 0) == 3)
    assert(getRowRange(board, 1) == 3)
    assert(getRowRange(board, 2) == 3)
    assert(getRowRange(board, 3) == 6)
    assert(getRowRange(board, 4) == 6)
    assert(getRowRange(board, 9) == 9)
            
    print("Passed")
    
def testGetColRange():
    print("testing getColRange()...", end = "")
    
    board = [
                [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
                [ 6, 0, 1, 1, 9, 5, 0, 0, 0 ],
                [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
                [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
                [ 4, 0, 0, -8, 0, 3, 0, 0, 1 ],
                [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
                [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
                [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
                [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]
            
    assert(getColRange(board, 0) == 3)
    assert(getColRange(board, 1) == 6)
    assert(getColRange(board, 2) == 9)
    assert(getColRange(board, 3) == 3)
    assert(getColRange(board, 4) == 6)
    assert(getColRange(board, 8) == 9)
            
    print("Passed")
    
def testGetBlockList():
    print("testing getBlockRange()...", end = "")
    
    board = [
                [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
                [ 6, 0, 1, 1, 9, 5, 0, 0, 0 ],
                [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
                [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
                [ 4, 0, 0, -8, 0, 3, 0, 0, 1 ],
                [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
                [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
                [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
                [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]
    
    result = [5,3,0,6,0,1,0,9,8]
    assert(getBlockList(board, 0) == result)
    result = [0,7,0,1,9,5,0,0,0]
    assert(getBlockList(board, 1) == result)
            
            
    print("Passed")
    
def testIsLegalBlock():
    print("testing isLegalBlock()...", end = "")
    
    board = [
                [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
                [ 6, 0, 1, 1, 9, 5, 0, 0, 0 ],
                [ 0, 9, 8, 0, 0, 0, 0, 6, 6 ],
                [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
                [ 4, 0, 0, -8, 0, 3, 0, 0, 1 ],
                [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
                [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
                [ 0, 0, 0, 4, 1, 9, 0, 8, 5 ],
                [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]

    assert(isLegalBlock(board, 0) == True)
    assert(isLegalBlock(board, 2) == False)
    assert(isLegalBlock(board, 8) == False)
            
    print("Passed")
    
def testIsLegalSudoku():
    print("testing isLegalSudoku()...", end = "")
    
    board = [
                [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
                [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
                [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
                [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
                [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
                [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
                [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
                [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
                [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]

    assert(isLegalSudoku(board) == True)
    
    board = [
                [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
                [ 6, 0, 1, 1, 9, 5, 0, 0, 0 ],
                [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
                [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
                [ 4, 0, 0, -8, 0, 3, 0, 0, 1 ],
                [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
                [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
                [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
                [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]
            
    assert(isLegalSudoku(board) == False)
    
    print("Passed")
    
    
#################################################
# testAll and main
#################################################

def testAll():
    testAreLegalValues()
    testIsLegalRow()
    testIsLegalCol()
    testGetRowRange()
    testGetColRange()
    testGetBlockList()
    testIsLegalBlock()
    testIsLegalSudoku()

def main():
    testAll()

if __name__ == '__main__':
    main()
