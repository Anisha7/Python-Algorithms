# hw10 rough

def flatten1(L):
    print("L: ", L)
    if not isinstance(L, list):
        print("L2: ", L)
        return L
    
    if len(L) == 0:
        return []
        
    else:
        
        return [flatten1(L.pop(0))] + flatten1(L)

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

from tkinter import *

def init(data):
    data.level = 1
    data.x = data.width//2
    data.y = data.height//2
    data.l = data.width//6

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
        #t += [(xc - r, yc - r), (xc + r, yc - r)]
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


