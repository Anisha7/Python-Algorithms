# Lab6
# Anisha Jain, anishaj
# Team: Zhenyan, zhenyanw

# events-example0.py
# Barebones timer, mouse, and keyboard events
# code follows specs given on http://www.cs.cmu.edu/~112/notes/notes-tetris/2_2_CreatingTheBoard.html



from tkinter import *
import random
import copy

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    
    # grid setup
    data.rows = 15
    data.cols = 10
    data.margin = (data.width/data.cols) * 3
    #data.marginy = (data.height - data.marginx)/3
    #data.squareSize = 20
    data.squareSize = (data.width - data.margin) / data.cols
    
    board = []
    for i in range(data.rows):
        board.append(["blue"]*data.cols) 
    
    data.board = board # tracks color of blocks, blue if empty
    
    # testing
    #data.board[0][0] = "red"
    #data.board[0][9] = "white"
    #data.board[14][0] = "green"
    #data.board[14][9] = "gray"
    
    #print(data.board)
    # indicates which cells are painted
    #sPiece = []
    #for i in range(data.rows):
       # sPiece.append(["False"]*data.cols)
    #data.sPiece = sPiece
    
    data.tetrisPieces = []
    data.tetrisPieceColors = []
    
    # draw falling piece
    data.x1 = 3
    data.y1 = 0
    
    setUpTetrisPieces(data)
    newFallingPiece(data)
    
    data.score = 0
    data.isGameOver = False

    
def setUpTetrisPieces(data):
    # Seven "standard" pieces (tetrominoes)
    # From notes
    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]
    
    tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", "orange" ]
    data.tetrisPieces = tetrisPieces
    data.tetrisPieceColors = tetrisPieceColors
    
def playTetris():
    
    rows = 15
    cols = 10
    margin = (data.width/data.cols) * 3
    #data.squareSize = 20
    squareSize = (data.width - data.margin) / data.cols
    
    pass

def newFallingPiece(data):
    
    # from Notes
    randomIndex = random.randint(0, len(data.tetrisPieces) - 1)
    randomColorIndex = random.randint(0, 5)
    data.fallingPiece = copy.deepcopy(data.tetrisPieces[randomIndex])
    data.fallingPieceColor = copy.deepcopy(data.tetrisPieceColors[randomColorIndex])
    
    fallingPieceRow = 0
    fallingPieceCol = (data.cols//2) - (data.squareSize//2)
    
    print(data.fallingPiece)
    
    data.x1 = 3
    data.y1 = 0
    #data.colorRandom = data.fallingPieceColor[randomColorIndex]

def drawFallingPiece(canvas, data):

    x1 = data.x1
    x2 = x1 + 1
    y1 = data.y1
    y2 = y1 + 1
    
    squareSize = data.squareSize
    margin = data.margin
    
    for i in range(len(data.fallingPiece)):

        for j in range(len(data.fallingPiece[0])):
            if data.fallingPiece[i][j] == True:
                color = data.fallingPieceColor
                
                left = (squareSize * x1) + margin/2
                #print("left: ", left)
                top = (squareSize * y1) + margin/2
                right = (squareSize * (x2)) + margin/2
                bottom = (squareSize * y2) + margin/2
            
                canvas.create_rectangle(left, top, right, bottom,
                    width = 3, fill = color, outline = "black")
                
                  
            x1 += 1
            x2 += 1

        x1 = data.x1
        x2 = x1 + 1
        y1 += 1
        y2 += 1

def placeFallingPiece(data):
    # load corresponding positions on the board
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            
            if data.fallingPiece[row][col] == True:
                data.board[data.y1 + row][data.x1 + col] = data.fallingPieceColor
    
    #print(data.board)
    
    removeFullRows(data)

def fallingPieceIsLegal(data):
    # check if falling piece's move is legal
    
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            
            if data.fallingPiece[row][col] == True:
                
                # check if rotation is off board
                if (data.y1 + row) > 14 or (data.y1 + row) < 0:
                    return False
                if (data.x1 + col) > 9 or (data.x1 + col) < 0:
                    return False
                
                # check for collision with full block on board
                if data.board[data.y1 + row][data.x1 + col] == "blue":
                    continue
                    
                else:
                    #print("collided")
                    return False
    return True

        
def moveFallingPiece(data, drow, dcol):
    # moves the falling piece based on change specs
    # provided in keypressed function
    #print("initial data.x1: ", data.x1)
    #print("initial data.y1: ", data.y1)
    #if isLegalFallingPiece(data):
    data.x1 = data.x1 + dcol
    data.y1 = data.y1 + drow
    
    
    # check if falling piece is legal
    # unmake move if falling piece is not legal
    if fallingPieceIsLegal(data) != True:
        data.x1 = data.x1 - dcol
        data.y1 = data.y1 - drow
        return False
        #print("unmove")
    return True

def rotateFallingPiece(data):
    # rotates the falling piece by 90 degrees
    
    oldFallingPiece = copy.deepcopy(data.fallingPiece)
    oldCol = data.x1
    oldRow = data.y1
    oldRows = len(oldFallingPiece)
    oldCols = len(oldFallingPiece[0])
    
    newRows = oldCols
    newCols = oldRows
    
    centerRow = oldRow + oldRows//2
    oldCenterRow = oldRow + oldRows//2
    
    # new fallingPieceRow
    newRow = oldCenterRow - newRows//2
    
    centerCol = oldCol + oldCols//2
    oldCenterCol = oldCol + oldCols//2
    
    # new fallingPieceCol
    newCol = oldCenterCol - newCols//2
    
    newCenterRow = newRow + newRows//2 
    newCenterCol = newCol + newCols//2 
    
    newPiece = []
    newPieceList = []
    
    # need to use centerRow and centerCol to calculate new
    # fallingPieceRow and fallingPieceCol
    # newRow and newCol is that...
    
    
    
    for col in range(oldCols - 1, -1, -1):
        for row in range(oldRows):

            #print(oldFallingPiece[col][row])
            newPiece += [oldFallingPiece[row][col]]
        
        newPieceList += [newPiece]
        newPiece = []
        
    #print(oldFallingPiece)
    print(newPieceList)
    data.fallingPiece = newPieceList
    
    # check for collisions
    if fallingPieceIsLegal(data) != True:
        data.fallingPiece = oldFallingPiece
        
    # check if it goes off the board
    

def mousePressed(event, data):
    # use event.x and event.y
    pass

def removeFullRows(data):
    newBoard = copy.deepcopy(data.board)
    fullRows = 0
    
    for row in range(len(newBoard)):
        if "blue" in newBoard[row]:
            continue
        else:
            fullRows += 1
            newBoard.pop(row)
            newBoard.insert(0, ["blue"]*data.cols)
    
    data.board = newBoard
    #print("newBoard: ", newBoard)
    #print("data,board: ", data.board)
            
    data.score += fullRows**2
    
def keyPressed(event, data):
    # use event.char and event.keysym
    
    if event.keysym == "r":
        init(data)
        
    print(event.keysym)
    
    if event.keysym == "Up":
        if data.y1 != 0:
            rotateFallingPiece(data)
            
    if event.keysym == "Down":
        if data.y1 < 15 - len(data.fallingPiece):
            
            moveFallingPiece(data, 1, 0)
            #print("len: ", len(data.fallingPiece))
        #print("data.y1: ",data.y1)
        
    if event.keysym == "Left":
        if data.x1 != 0:
            
            moveFallingPiece(data, 0, -1)
            #print(data.y1)
            
    if event.keysym == "Right":
        if data.x1 < 10 - len(data.fallingPiece[0]):
            
            moveFallingPiece(data, 0, 1)
            #print("len: ", len(data.fallingPiece))
        
        #print("data.x1: ",data.x1)
    

def timerFired(data):
    moveFallingPiece(data, 1, 0)
    
    if moveFallingPiece(data, 1, 0) == False:
        placeFallingPiece(data)
        
        newFallingPiece(data)
        if fallingPieceIsLegal(data) == False:
            data.isGameOver = True

    
def drawBoard(canvas, data):

    # canvas.create_text()
    
    squareSize = data.squareSize
    margin = data.margin
    #marginy = data.marginy
    
    # create board grid
    for row in range(len(data.board)):
        for col in range(len(data.board[row])):
            color = data.board[row][col]
            # draw board
            left = (squareSize * col) + margin/2
            #print("left: ", left)
            top = (squareSize * row) + margin/2
            right = (squareSize * (col + 1)) + margin/2
            bottom = (squareSize * (row + 1)) + margin/2

            canvas.create_rectangle(left, top, right, bottom,
                    width = 5, fill = color, outline = "black")
                    
def drawScore(canvas, data):
        canvas.create_text(data.width/2, data.squareSize, 
                font = ("Ariel", 25), fill = "Purple", text = "Score: " + str(data.score))
    
def redrawAll(canvas, data):
    # draw in canvas
    # draw the background
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "orange")
    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)
    drawScore(canvas, data)
    
    if data.isGameOver == True:
        canvas.create_rectangle(0, data.height/4, data.width, 
                data.height - data.height/4, fill = "black")
        canvas.create_text(data.width/2, data.height/2, 
                font = ("Ariel", 25), fill = "White", text = "Game Over!")
        
    
    pass

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
    data.timerDelay = 500 # milliseconds
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

run(300, 400)