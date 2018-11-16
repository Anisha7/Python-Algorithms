# HW 6
# Anisha Jain, anishaj

# from events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import random

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    
    # start screen target
    data.cx = data.width//2
    data.cy = data.height//2
    data.cr = random.randint(10, 20)
    data.dcx = 5
    data.i = 1
    data.j = -1
    
    # play screen
    data.gamePlay = False
    data.score = 0
    data.timeLeft = 21
    data.margin = 10
    
    # store top left corner position of view
    data.x = 0
    data.y = 0
    data.x2 = data.width*2
    data.y2 = data.height*2
    
    # game play targets
    data.gamecx = 0
    data.gamecy = 0
    data.gamecr = 0
    data.circles = []
    
    # changed to make targets appear every 0.5 sec
    data.timerDelay = 500 

    # timer delay
    data.timerDelayTracker = 0
    
    # player click positions
    data.clickx = 0
    data.clicky = 0
    
    # scrolling
    data.scrollX = 0
    data.scrollY = 0
    
    pass

def mousePressed(event, data):
    # use event.x and event.y
    data.clickx = event.x
    data.clicky = event.y
    #print(data.clickx, data.clicky)

def keyPressed(event, data):
    # use event.char and event.keysym
    if event.keysym == "p":
        data.gamePlay = True
    if event.keysym == "s":
        init(data)
    
    # move game screen based on arrow keys
    if data.gamePlay == True:    
        if event.keysym == "Left":
            data.scrollX += (1/10)*data.width
            
        if event.keysym == "Right":
            data.scrollX -= (1/10)*data.width
            
        if event.keysym == "Up":
            data.scrollY += (1/10)*data.width
            
        if event.keysym == "Down":
            data.scrollY -= (1/10)*data.width
            
    
def timerFired(data):
    # moves circle
    bounceCircle(data)
    timerDelayCountDown(data)


# make target
def drawTarget(canvas, x, y, r):
    
    canvas.create_oval(x - r, y - r,
                            x + r, y + r,
                            width = 3, outline = "red")
    canvas.create_oval(x - 2*r//3 , 
                        y - 2*r//3 ,
                            x + 2*r//3 , 
                            y + 2*r//3 , 
                            width = 3, outline = "red")
    canvas.create_oval(x - r//4, y - r//4,
                            x + r//4, y + r//4, 
                            width = 2, outline = "red", fill = "red")

# change start screen circle's x,y by speed(data.dcx)
# to make it bounce
def bounceCircle(data):
    
    if data.cx >= 0 and data.cx <= data.width - data.cr:
       data.cx += data.i*data.dcx
       # change direction if center collided with border
       if data.cx == 0 or data.cx == data.width - 2*data.cr:
           data.i = data.i * -1
           print("i:", data.i)
           
    if data.cy >= 0 and data.cy <= data.height - data.cr:
       data.cy += data.j * data.dcx
       # change direction if center collided with border
       if data.cy == 0 or data.cy == data.height - 2*data.cr:
           data.j = data.j * -1
           print("j:", data.j)
    
# start screen : play instructions, title, and bouncing target
def drawStartScreen(canvas, data):
    
    # bouncing circle
    drawTarget(canvas, data.cx, data.cy, data.cr)

    # title
    canvas.create_text(data.width//2, data.height//4, anchor = CENTER, 
                        font = ("Ariel", 36) , text = "Targets Game!")
    
    # instructions
    canvas.create_text(data.width//2, data.height - data.height//4, 
                        anchor = CENTER, font = ("Ariel", 26) , 
                        text = "Press 'p' to play")
    pass
 
# draws game state screen: map, targets, score
def drawPlayScreen(canvas, data):
    
    # draw map
    canvas.create_rectangle( data.scrollX, data.scrollY, 
                                data.scrollX + data.x2, 
                                data.scrollY + data.y2,
                                width = 3, fill = "white")
    
    # score and timer
    canvas.create_text(data.x + data.margin, data.y + data.margin, 
                        anchor = NW, font = ("Ariel", 20) , 
                        text = "Time Left: " + str(data.timeLeft))
    canvas.create_text(data.x + data.margin, data.height - data.margin , 
                        anchor = SW, font = ("Ariel", 20) , 
                        text = "Score: " + str(data.score))
    
    # draw random circles
    data.gamecx = random.randint(0, data.width*2)
    data.gamecy = random.randint(0, data.height*2)
    #data.gamecx = random.randint(data.x, data.x2)
    #data.gamecy = random.randint(data.y, data.y2)
    data.gamecr = random.randint(5, 20)
    data.circles +=[(data.gamecx, data.gamecy, data.gamecr)]
    
    for circleTuple in data.circles:
        (data.gamecx, data.gamecy, data.gamecr) = circleTuple
        data.gamecx = data.scrollX + data.gamecx
        data.gamecy = data.scrollY + data.gamecy
        drawTarget(canvas, data.gamecx, data.gamecy, data.gamecr)
    
    targetClicked(data)
    
# when target is clicked, removes target
# adds 1 to score
# when score % 5 = 0, add +1 to data.timeLeft
def targetClicked(data):
    
    newTargetList = []
    
    for circleTuple in data.circles:
        (data.gamecx, data.gamecy, data.gamecr) = circleTuple
        data.gamecx = int(data.scrollX + data.gamecx)
        print(data.gamecx)
        data.gamecy = int(data.scrollY + data.gamecy)
        if data.clickx in range(data.gamecx - data.gamecr, data.gamecx + data.gamecr):
            
            if data.clicky in range(data.gamecy - data.gamecr, data.gamecy + data.gamecr):
                data.score += 1
                
                if data.score % 5 == 0:
                    data.timeLeft += 1
                    
                continue
        else:
            newTargetList += [circleTuple]
    
    data.circles = newTargetList
    
def timerDelayCountDown(data):
    data.timerDelayTracker += data.timerDelay
    
    if data.timeLeft > 0:
        if data.timerDelayTracker == 1000:
            data.timeLeft -= 1
            data.timerDelayTracker = 0

def gameOverState(canvas, data):
    
    canvas.create_rectangle(0, 0, data.width, data.height, 
                            width = 0, fill = "red")
    canvas.create_text(data.width//2, data.height//4 , 
                        anchor = CENTER, font = ("Ariel", 36), fill = "white", 
                        text = "GAME OVER!")
    canvas.create_text(data.width//2, data.height//2 , 
                        anchor = CENTER, font = ("Ariel", 24), fill = "white", 
                        text = "Final Score: " + str(data.score))
    canvas.create_text(data.width//2, data.height - data.height//4 , 
                        anchor = CENTER, font = ("Ariel", 24), fill = "white", 
                        text = "Press 's' to start again")
    pass

def redrawAll(canvas, data):
    # draw in canvas
    # start screen
    if data.gamePlay == False:
        drawStartScreen(canvas, data)
    if data.gamePlay == True:
        drawPlayScreen(canvas, data)
    if data.timeLeft == 0:
        data.gamePlay = False
        gameOverState(canvas, data)
        
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                               fill='white', width=0)
        # canvas.create_rectangle(data.scrollX, data.scrollY, 
        #                         data.scrollX + data.width, 
        #                         data.scrollY + data.height,
        #                         fill='white', width=0)
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

run(300, 300)