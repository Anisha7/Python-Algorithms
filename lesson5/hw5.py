import cs112_f17_week5_linter
from tkinter import *
from sudoku import *

#########################################################
# Customize these functions
# You will need to write many many helper functions, too.
#########################################################

def init(data):
    # load data.xyz as appropriate
    
    # Making board
    rows = 9
    cols = 9
    board = []
    
    for i in range(rows):
        board.append(["E"]*cols) 
    data.boardH = board # tracks initial board values
    data.userBoard = copy.deepcopy(board) # tracks user input
    data.margin = 20
    data.squareSize = (data.width - data.margin) / 9
    data.fullBoard = copy.deepcopy(board) # gets completed sudoku
    print(data.fullBoard)
    data.playGame = "Yes"
    
def checkIfFull(dataList):
    
    #fullBoard = data.fullBoard
    for i in range(len(dataList)):
        for j in range(len(dataList[0])):
            
            if dataList[i][j] == 'E':
                return False
 
    return True
    
def drawBoard(canvas, data):
    
    #canvas.create_rectangle()
    margin = data.margin
    squareSize = data.squareSize
    #print(len(data.board[0]))
    #print("squareSize: ", squareSize)

    canvas.create_rectangle(0, 0, data.width, data.height,
                    width = 0, fill = "black")
    
    # create sudoku grid
    for row in range(len(data.boardH)):
        for col in range(len(data.boardH[row])):
            color = "pink"
            
            # highlighting a cell
            [rowH, colH] = data.highlightCell
            #print(rowH, colH)
            if rowH == row and colH == col:
                color = "purple"
            
            # draw board
            left = (squareSize * col) + margin/2
            #print("left: ", left)
            top = (squareSize * row) + margin/2
            right = (squareSize * (col + 1)) + margin/2
            bottom = (squareSize * (row + 1)) + margin/2

            canvas.create_rectangle(left, top, right, bottom,
                    width = 1, fill = color, outline = "purple")
             
                    
            # Add initial numbers
            x = ((left + right)/2) 
            y = ((top + bottom)/2) 
            
            if data.board[row][col] != 0:
                num = data.board[row][col]

                canvas.create_text(x, y, font = ("Ariel", 25), text = num) 
                # Makes sure these values are unchangeable
                data.userBoard[row][col] = 'Not'
                data.fullBoard[row][col] = data.board[row][col]
            # append values given by user to board
            if data.userBoard[row][col] != 'Not' and\
             data.userBoard[row][col] != 'E':
                num = data.userBoard[row][col]
                
                canvas.create_text(x, y, font = ("Ariel", 25), 
                    fill = "blue", text = num)
                    
                data.fullBoard[row][col] = data.userBoard[row][col]

def checkWin(canvas, data):                
    # checks if player won the game 
    if checkIfFull(data.fullBoard) == True:
        if isLegalSudoku(data.fullBoard):
            canvas.create_rectangle(20, data.height/4, data.width - 20, 
                data.height - data.height/4 , fill = "pink")
            canvas.create_text(data.width/2, data.height/3 + 30, 
                font = ("Ariel", 40), text = "You Win!")
            canvas.create_text(data.width/2, data.height/2 + 50, 
                font = ("Ariel", 40), text = "Press Tab to play again")
            
            data.playGame = "No"
            
# style board to separate each nxn block for n**2 sudoku
def styleBoard(canvas, data):  

    margin = data.margin
    squareSize = data.squareSize  
    
    for row in range(0, len(data.board), 3):
        for col in range(0, len(data.board[row]), 3):
            
            left = ((squareSize * col) + (margin/2))
            top = ((squareSize * row) + margin/2) 
            right = ((squareSize * (col + 1)) + margin/2) *3
            bottom = ((squareSize * (row + 1)) + margin/2) *3
            #print(left,top,right,bottom)
            canvas.create_rectangle(left, top, right - 20, bottom - 20,
                    width = 2.5)


def keyPressed(event, data):
    # use event.char and event.keysym
    
    # moving on board and highlighting cell
    [rowH, colH] = data.highlightCell
    if data.playGame == "Yes":
        
        if event.keysym == "Down":
            if rowH < 9:
                rowH += 1
            data.highlightCell = [rowH, colH]
            
        if event.keysym == "Up":
            if rowH > 0:
                rowH -= 1
            data.highlightCell = [rowH, colH]
            
        if event.keysym == "Right":
            if colH < 9:
                colH += 1
            data.highlightCell = [rowH, colH]
            
        if event.keysym == "Left":
            if colH > 0:
                colH -= 1
            data.highlightCell = [rowH, colH]
    
        
        # get numbers entered by user
        # append it to the data.userBoard at data.highlightCell
        for numKey in range(1, 10):
            print(numKey)
            if event.keysym == str(numKey):
                print(data.userBoard)
                if data.userBoard[rowH][colH] != 'Not':
                    #[rowH, colH] = data.highlightedCell
                    data.userBoard[rowH][colH] = numKey
                
                print("data.userBoard: ",data.userBoard[rowH][colH])
                print(data.userBoard)
    
    # allows game replay            
    if data.playGame == "No":
        if event.keysym == "Tab":
            data.playGame == "Yes"
            init(data)

                

def redrawAll(canvas, data):
    # draw in canvas
    drawBoard(canvas, data)
    styleBoard(canvas, data)
    checkWin(canvas, data)
    pass

########################################
# Do not modify the playSudoku function.
########################################

def playSudoku(sudokuBoard, width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.board = sudokuBoard
    data.highlightCell = [0,0]
    
    # Initialize any other things you want to store in data
    init(data)

    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    # set up events
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))

    # Draw the initial screen
    redrawAll(canvas, data)

    # Start the event loop
    root.mainloop()  # blocks until window is closed
    print("bye!")

def main():
    cs112_f17_week5_linter.lint() # check style rules
    
    # board = [
    #         [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    #         [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    #         [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    #         [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    #         [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    #         [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    #         [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    #         [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    #         [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    #     ]
    
    board = [
                [1,2,3,4,5,6,7,8,9],
                [5,0,8,1,3,9,6,2,4],
                [4,9,6,8,7,2,1,5,3],
                [9,5,2,3,8,1,4,6,7],
                [6,4,1,2,9,7,8,3,5],
                [3,8,7,5,6,4,0,9,1],
                [7,1,9,6,2,3,5,4,8],
                [8,6,4,9,1,5,3,7,2],
                [2,3,5,7,4,8,9,1,6]
            ]
    playSudoku(board)

if __name__ == '__main__':
    main()
