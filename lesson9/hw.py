#################################################
# HW 10
# Anisha Jain - anishaj

#################################################

import cs112_f17_week10_linter
import math

## helper from notes
# Helper function for print2dList.
# This finds the maximum length of the string
# representation of any item in the 2d list
def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in range(rows):
        for col in range(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen

# Because Python prints 2d lists on one row,
# we might want to write our own function
# that prints 2d lists a bit nicer.
def print2dList(a):
    if (a == []):
        # So we don't crash accessing a[0]
        print([])
        return
    rows = len(a)
    cols = len(a[0])
    fieldWidth = maxItemLength(a)
    print("[ ", end="")
    for row in range(rows):
        if (row > 0): print("\n  ", end="")
        print("[ ", end="")
        for col in range(cols):
            if (col > 0): print(", ", end="")
            # The next 2 lines print a[row][col] with the given fieldWidth
            formatSpec = "%" + str(fieldWidth) + "s"
            print(formatSpec % str(a[row][col]), end="")
        print(" ]", end="")
    print("]")

######################################################################
# Functions
######################################################################

# flattens a list, removing embedded lists
# returns a 1D list with elements in same order
def flattenHelper(L):

    if not isinstance(L, list):
        return [L]
    
    if len(L) == 0:
        return []
        
    else:
        
        return flattenHelper(L[0]) + flattenHelper(L[1:])
      
# uses recursive helper to flatten list
# flattens L only if L is a list        
def flatten(L):
    if isinstance(L, list):
        return flattenHelper(L)
    else:
        return L
        

# decorator function that prevents program from crashing
# if function fails
def noError(f):
    def g(*args):
        try:
            return f(*args)
        except:
            return None
    return g
    
     
def getLegalPoints(s, r = 0, c = 0):

    d = dict()
    
    # first diagonal
    m = []
    for i in range(5):
        m += [(r+i, c+i)]
            
    d[s[0]] = m
    d[s[12]] = m
    
    # second diagonal
    m = []
    n = 0
    for i in range(4, -1, -1):
        m += [(r+i, c + n)]
        n += 1
            
    d[s[6]] = m
    d[s[18]] = m
    
    # vertical rows
    n = 0
    L = []
    for char in s[1:6]:
        for i in range(5):
            L += [(r + i, c + n)]
        
        d[char] = L
        
        d[s[17-n]] = L
        n += 1
        L = []

    # horizontal rows
    n = 0
    L = []
    for char in s[7:12]:
        for i in range(5):
            L += [(r + n, c + i)]
                  
        d[char] = L
        d[s[23-n]] = L
        n += 1
        L = []
    return d

# helper: checks if board is full
def isfull(board):
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] == 0:
                return False
    return True

# checks if point is on board
def isValid(point):
    if point >= 0 and point < 5:
        return True
    return False


# checks if letter after key isValid
# for that move, t
def isLegalABCHelper(board, t, key, d):
    # t = (r,c) of b; key = b
    (r,c) = t
    L1 = chr(ord(key) + 1)
    # L1 = letter after b (if check for "B", c = "C")
    if L1 == "Z":
        return True
    upR = r + 1
    downR = r - 1
    upC = c + 1
    downC = c - 1
    
    for tuple in d[L1]:
        if tuple == (upR, c) or tuple == (downR, c):
            return True
        if tuple == (r, upC) or tuple == (r, downC):
            return True
        if tuple == (upR, downC) or tuple == (upR, upC):
            return True
        if tuple == (downR, downC) or tuple == (downR, upC):
            return True
            
    return False
        
def isLegalABC(board, t, key, d):
    (r, c) = t

    L1 = chr(ord(key) - 1)
    
    upR = r + 1
    downR = r - 1
    upC = c + 1
    downC = c - 1
    
    # checks if next letter's points are valid for this t
    #if isLegalABCHelper(board, t, key, d) == False:
        #return False
    
    # checks all 8 locations around letter for prev letter
    if isValid(upR):
        if board[upR][c] == L1:
            return True
            
    if isValid(downR):
        if board[downR][c] == L1:
            return True
    
    if isValid(upC):
        if board[r][upC] == L1:
            return True
            
    if isValid(downC):
        if board[r][downC] == L1:
            return True
    
    if isValid(upR) and isValid(upC):
        if board[upR][upC] == L1:
            return True
    
    if isValid(upR) and isValid(downC):
        if board[upR][downC] == L1:
            return True
    
    if isValid(downR) and isValid(downC):
        if board[downR][downC] == L1:
            return True
    
    if isValid(downR) and isValid(upC):
        if board[downR][upC] == L1:
            return True
        
    return False
        
# solves the ABC board
# d = dictionary with all possible moves
def solveABCWrapper(d, board, b = "B"):

    if isfull(board) == True:
        return board
    
    if b == "Z":
        return board
        
    else:
        # choose location for move
        # generate all possible moves
        if b == "P":
            print(d[b])
        for t in d[b]:    
            (r,c) = t

            if board[r][c] == 0:
                board[r][c] = b
                
                if isLegalABC(board, t, b, d):
                    
                    #print("legal board: ")
                    print2dList(board)
                    #print("letter: ", b, "  tuple: ", t)
                    # recurse with next letter (if B, recurse with C)
                    solution = solveABCWrapper(d, board, chr(ord(b) + 1))
                        
                    if solution != None:
                        return solution

                    else: board[r][c] = 0

                else: board[r][c] = 0
                #print("board after UNDO")
                #print2dList(board)
        return None
                
           
# uses solveABC wrapper to solve ABC puzzle
# sets up dictionary and board for wrapper
def solveABC(constraints, aLocation):
    
    d = getLegalPoints(constraints)
    board = []
    
    for i in range(5):
        board.append([0]*5) 
    
    (r,c) = aLocation
    board[r][c] = "A"

    return solveABCWrapper(d, board)
    
#################################################
# HFractal
#################################################

from tkinter import *

def init(data):
    data.level = 0
    data.x = data.width//2
    data.y = data.height//2
    data.l = data.width//6

# draws the H
def drawH(canvas, x, y, l):
    
    canvas.create_line(x - l, y, 
                        x + l, y, width = 3)
                        
    canvas.create_line(x - l, y - l, 
                        x - l, y + l, width = 3)
                        
    canvas.create_line(x + l, y - l, 
                        x + l, y + l, width = 3)

def hTuples(x, y, l, level):
    if level == 0:
        return [(x, y, l)]
    
    else:
        return [(x, y, l)] +\
                hTuples(x - l, y - l,
                l//2, level - 1) \
                + hTuples(x - l, y + l,
                l//2, level - 1) \
                + hTuples(x + l, y - l,
                l//2, level - 1) \
                + hTuples(x + l, y + l,
                l//2, level - 1)

# uses list of points from recursive hTuples
# draws H fractal
def hFractalViewer(canvas, x, y, l, level):
    
    t = hTuples(x, y, l, level)
    for point in t:
        (x, y, l) = point
        drawH(canvas, x, y, l)

# recursive fractal viewer
# test to get right points
def hFractalViewer1(canvas, x, y, l, level):
    if level == 0:
        drawH(canvas, x, y, l)
    
    else:
        hFractalViewer(canvas, x - l, y - l,
                l//2, level - 1)
        hFractalViewer(canvas, x - l, y + l,
                l//2, level - 1)
        hFractalViewer(canvas, x + l, y - l,
                l//2, level - 1)
        hFractalViewer(canvas, x + l, y + l,
                l//2, level - 1)
        
def hFractal():
    run(500, 500)
    
def keyPressed(event, data):
    # from notes
    if (event.keysym in ["Up", "Right"]):
        data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (data.level > 0)):
        data.level -= 1

def redrawAll(canvas, data):
    #drawH(canvas, data)
    hFractalViewer(canvas, data.x, data.y, data.l, data.level)
    
    # from notes
    canvas.create_text(250, 25,
                       text = "Level %d Fractal H" % (data.level),
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

def testflatten():
    print("testing flatten()...", end = "")
    
    assert(flatten([1,[2]]) == [1,2])
    assert(flatten([1,2,[3,[4,5],6],7]) == [1,2,3,4,5,6,7])
    assert(flatten(['wow', [2,[[]]], [True]]) == ['wow', 2, True])
    assert(flatten([]) == [])
    assert(flatten([]) == [])
    assert(flatten([[]]) == [])
    assert(flatten(3) == 3)
    
    print("Passed")
    
def testNoErrorDecorator():
    print("Testing @noError decorator...", end="")
    @noError
    def f(x, y): return x/y
    assert(f(1, 5) == 1/5)
    assert(f(1, 0) == None)

    @noError
    def g(): return 1/0
    assert(g() == None)

    @noError
    def h(n):
        if (n == 0): return 1
        else: return h(n+1)
    assert(h(0) == 1)
    assert(h(-1) == 1)
    assert(h(1) == None)

    print("Passed!")
    
def testSolveABC():
    print('Testing solveABC()...', end='')
    constraints = "CHJXBOVLFNURGPEKWTSQDYMI"
    aLocation = (0,4)
    board = solveABC(constraints, aLocation)
    solution = [['I', 'J', 'K', 'L', 'A'],
                ['H', 'G', 'F', 'B', 'M'],
                ['T', 'Y', 'C', 'E', 'N'],
                ['U', 'S', 'X', 'D', 'O'],
                ['V', 'W', 'R', 'Q', 'P']
               ]
    assert(board == solution)
    print("Pass1")
    constraints =  'TXYNFEJOQCHIMBDSUWPGKLRV'
    aLocation = (2, 4)
    board = solveABC(constraints, aLocation)
    
    solution = [['V', 'U', 'S', 'O', 'P'], 
                ['W', 'T', 'N', 'R', 'Q'], 
                ['X', 'L', 'M', 'C', 'A'], 
                ['K', 'Y', 'H', 'D', 'B'], 
                ['J', 'I', 'G', 'F', 'E']
                ]
    assert(board == solution)
    print("Pass2")
    print('Passed All!')
    
#################################################
# testAll and main
#################################################

def testAll():
    testflatten()
    testNoErrorDecorator()
    hFractal()
    testSolveABC()

def main():
    cs112_f17_week10_linter.lint() # check style rules
    testAll()
    
    
    

if __name__ == '__main__':
    main()
