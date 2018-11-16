#################################################
# Lab3
# Anisha Jain - anishaj
# Team: Zhenyan - zhenyanw
#################################################


#################################################

import cs112_f17_week10_linter
import math
import os
#from sudoku import *

#################################################
# Helper functions
#################################################
 

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
   
      
######################################################################
# Functions
######################################################################

def findLargestFile(path, c=0, size = None, largestFile = '/'):
    
    
    print("path: ", path)
    print("largest File: ", largestFile)
    
    # when checked all files, return largest file
    if c == len(os.listdir(path)):
        if largestFile == '/':
            return ""
        return largestFile
    
    else:
        
        print("list: ",os.listdir(path))
        for move in os.listdir(path):
            c += 1
            newPath = path + '/' + move
            
            if move == '.DS_Store':
                continue
                
            if (os.path.isdir(newPath) == True):
                # if folder, get path to largest file in folder
                clargestFile = findLargestFile(newPath, 0, size, largestFile)   
                    
            if (os.path.isdir(newPath) == False):
                # if file, get path to file
                clargestFile = newPath
            
            m = os.path.getsize(clargestFile)
            if size == None or m > size:
                # set largest file to new largest file
                largestFile = clargestFile
                size = os.path.getsize(clargestFile)
        
        if largestFile == '/':
            return ""
            
        print("largestFileReturn..: ", largestFile)
        return largestFile   


def isLegalMove(board, row, col, move):
    
    board[row][col] = move
    if isLegalSudoku(board):
        return True
    else:
        return False

def getRowCol(board, row = 0, L = []):
    
    if row == len(board) - 1:
        return L
        
    else:
        for col in range(len(board[0])):
            if board[row][col] == 0:
                L += [(row, col)]
        return getRowCol(board, row + 1)
    
# input: incomplete sudoku board
# output: completed sudoku board
def solveSudoku(board, row = 0):
    
    # if all rows are checked
    if row == len(board):
        return board
    # try two nested for loops (with row col)
    else:
        
        for col in range(len(board[0])):
            if board[row][col] == 0:
                
                for move in range(1, 10):
                    
                    if isLegalMove(board, row, col, move):
                        board[row][col] = move
                        solution = solveSudoku(board)
                    
                        if solution != None:
                            #print(solution)
                            return solution
                        else:
                            board[row][col] = 0
                   # else:
                       # board[row][col] = 0
                            
                return None
        return solveSudoku(board, row + 1)
    
                
def solveSudoku1(board, r = 0):
    
    for i in range(len(board)):
        if 0 in board[i]:
            break
        return board
        
    else:
        for row in range(0, 9):
            r = row
            for col in range(0,9):
                if board[row][col] == 0:
                    for move in range(1,10):
                        board[row][col] = move
                        if isLegalSudoku(board):
                            solution = solveSudoku(board)
                            
                            if solution != None:
                                return solution
                            
                            board[row][col] = 0
                        
                    return None
                
                
   
    
#################################################
# Graphics
#################################################

from tkinter import *

def init(data):
    data.level = 1
    data.points = []

def teddyFace(canvas, xc, yc, r):
    w = r//10
    # face
    canvas.create_oval(xc-r, yc-r, xc+r, yc+r, 
                        width = w, fill = "brown")
    
    # eyes
    canvas.create_oval(xc - r//3 -r//6, (yc - r//2) -r//6, 
                        xc - r//3 +r//6, (yc - r//2 )+r//6,
                        fill="black")
    canvas.create_oval(xc + r//3 -r//6, (yc - r//2) -r//6, 
                        xc + r//3 +r//6, (yc - r//2 )+r//6,
                        fill="black")

    # nose
    canvas.create_oval((xc)-r//2, (yc+ r/4)-r//2, 
                        (xc) +r//2, (yc+ r/4)+r//2,
                        width = w, fill="Tan")
    canvas.create_oval(xc-r//6, yc-r//6, xc+r//6, yc+r//6,
                        fill="black")
    
    # mouth
    canvas.create_arc(xc, yc + r//2, 
                        xc + r//4, yc + r//2,
                        style = ARC, width = 4, start = 0, 
                        extent = 130)
    
    canvas.create_arc(xc - r//4, yc + r//2, 
                        xc, yc + r//2,
                        style = ARC, width = 4, start = 0, 
                        extent = 130)
        
        
def teddyTuples(xc, yc, r, level):
    if level == 0:
        return [(xc, yc, r)]
    
    else:
        #t += [(xc - r, yc - r), (xc + r, yc - r)]
        return [(xc, yc, r)] +\
                teddyTuples(xc-r, yc-r, r//2, level-1) \
                + teddyTuples(xc+r, yc-r, r//2, level-1)

def fractalTeddy1(canvas, xc, yc, r, level):
    
    t = teddyTuples(xc, yc, r, level)
    for point in t:
        (xc, yc, r) = point
        teddyFace(canvas, xc, yc, r)
        
def fractalTeddy2(canvas, xc, yc, r, t):
    
    if len(t) == 0:
        teddyFace(canvas, xc, yc, r)
    
    else:
        for point in t:
            (x, y, r2) = point
            fractalTeddy2(canvas, x, y, r2, t[1:])
            
        

def fractalTeddy(canvas, xc, yc, r, level):
    
    if level == 0:
        return teddyFace(canvas, xc, yc, r)
    
    else:

        fractalTeddy(canvas, xc - r, yc - r, r//2, level - 1)
        fractalTeddy(canvas, xc + r, yc - r, r//2, level - 1)
        
def runTeddyFractalViewer():
    pass
    
def keyPressed(event, data):
    # from notes
    if (event.keysym in ["Up", "Right"]):
        data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (data.level > 0)):
        data.level -= 1

def redrawAll(canvas, data):
    fractalTeddy1(canvas, data.width//2, data.height//2, 100, data.level)
    
    # recursive fractal teddy
    #t = teddyTuples(data.width//2, data.height//2, 100, data.level)
    #fractalTeddy2(canvas, data.width//2, data.height//2, 100, t)
    #teddyFace(canvas, data.width//2, data.height//2, 100)
    
    # from notes
    canvas.create_text(250, 25,
                       text = "Level %d Fractal Teddy" % (data.level),
                       font = "Arial 26 bold")
    canvas.create_text(250, 50,
                       text = "Use arrows to change level",
                       font = "Arial 10")

def mousePressed(event, data): pass

def timerFired(data): pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")




#################################################
# Test Functions
#################################################

def testGetLargestFile():
    print('Testing getLargestFile()...', end='')
    assert(findLargestFile("sampleFiles/folderA") ==
                        "sampleFiles/folderA/folderC/giftwrap.txt")
    print("**********Pass 1!")
    assert(findLargestFile("sampleFiles/folderB") ==
                        "sampleFiles/folderB/folderH/driving.txt")
    print("**********Pass 2!")
    assert(findLargestFile("sampleFiles/folderB/folderF") == "")
    print("**********Pass 3!")
    print('Passed')
    
def testSolveSudoku():
    print('Testing solveSudoku()...', end='')
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
    #print(getRowCol(board))
    solved = solveSudoku(board)
    solution = [
                [5, 3, 4, 6, 7, 8, 9, 1, 2], 
                [6, 7, 2, 1, 9, 5, 3, 4, 8], 
                [1, 9, 8, 3, 4, 2, 5, 6, 7], 
                [8, 5, 9, 7, 6, 1, 4, 2, 3], 
                [4, 2, 6, 8, 5, 3, 7, 9, 1], 
                [7, 1, 3, 9, 2, 4, 8, 5, 6], 
                [9, 6, 1, 5, 3, 7, 2, 8, 4], 
                [2, 8, 7, 4, 1, 9, 6, 3, 5], 
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
               ]
    
    print(solved)
    assert(solved == solution)
    print('Passed!')
    
#################################################
# testAll and main
#################################################

def testAll():
    testGetLargestFile()
    testSolveSudoku()
    pass

def main():
    cs112_f17_week10_linter.lint() # check style rules
    testAll()
    run(500, 500)
    
if __name__ == '__main__':
    main()
