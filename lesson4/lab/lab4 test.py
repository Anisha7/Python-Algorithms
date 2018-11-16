#################################################
# Lab4
# Anisha Jain, anishaj
# Team: Zhenyan, zhenyanw
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

#################################################
# Problems
#################################################

def lookAndSay(a):
    #count how many times a number repeats consecutively. 
    #return tuple (count, number) for each number in string
    
    count = 0
    num  = 0
    newList = []
    
    for i in range(len(a)):
        
        if i == 0:
            count += 1
            num = a[i]
            
        elif a[i] == num:
            count += 1
            
        else:
            newList += [(count, num)]
            count = 1
            num = a[i]
            
        if i == len(a) - 1:
            newList += [(count, num)]
            
    return newList

def inverseLookAndSay(a):
    #take the tuples in list and return the original list 
    #with numbers repeating as specified by the count in tuple
    
    newList = []
    
    for tuple in a:
        
        newList += tuple[0] * [(tuple[1])]
      
    return newList

# removes all characters are not letters
# returns a string with only letters
def removeWhiteSpace(s):
    string = ""
    
    for char in s:
        if char.isalpha():
            string += char
    return string
    
# removes all characters are not letters
# returns a string with only letters
def removeWhiteSpace(s):
    string = ""
    
    for char in s:
        
        if char.isalpha():
            string += char
            
    return string

def separateWords(puzzle):
    
    #print(puzzle)
    
    wordList = []
    wordString = ""
    
    # puzzleString = str(puzzle)
      
    for i in range(len(puzzle)):
        
        if puzzle[i].isalpha() == True:
            wordString += puzzle[i]
            print("wordString: ", wordString)
        
        else:
            wordList += [(wordString)]
            wordString = ""
        
        if i == len(puzzle) - 1:
            wordList += [(wordString)]
    
    goodList = []
    
    for item in wordList:
        if item != "":
            goodList.append(item)
    
    return goodList
    
#Converts puzzle to numbers based on solution indexes
def SolvePuzzleToNums(puzzle, solution):
    
    # remove all characters other than letters from solution
    sol = removeWhiteSpace(solution)
    # copy to prevent aliasing errors
    nums = copy.copy(sol)
    numList = []
    numString = ""
    
    puzzle = separateWords(puzzle)
    #print("puzzle: ", puzzle)
    
    for word in puzzle:
        #print("word: ", word)
        
        for letter in word:
            print("letter: ", letter)
            
            for key in solution:
            
                if letter == key:
                    numString += str(solution.index(key))
        numList += [(numString)]
        numString = ""
        
    return numList

# converts a string of numbers to an integer
def stringToInt(numString):
    #'1234' ==> 1234
    num = 0
    
    for i in range(len(numString)):
        
        digit = int(numString[i])
        exp = len(numString) - i
        print("exp: ", exp)
        num += (digit) * (10 ** exp) // 10
        #print("num: ", num)
    
    return num
    
def solvesCryptarithm(puzzle, solution):
    # puzzle ex. : SEND + MORE = MONEY
    # Solution indexes are numbers associated with those letters
    # Use those to convert puzzle into numbers
    # Check if the equation is true
    
    sum = 0
    numList = SolvePuzzleToNums(puzzle, solution)
    print("numList: ", numList)
    
    for i in range(len(numList)):
        
        numString = numList[i]
        num = stringToInt(numString)
        
        if i != len(numList) - 1:
            sum += num
            print("sum: ", sum)
    
    testSumIndex = len(numList) - 1
    testSum = stringToInt(numList[testSumIndex])      
      
    if sum == testSum:
        return True
    else:
        return False
        
      

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

def getStarPoints(canvas, centerX, centerY, diameter, numPoints, color):
    cx = centerX
    cy = centerY
    r = diameter/2
    rSmall = r * (3/8)
    #angle = 360/numPoints
    angle = 90
    outpointList = []
    inpointList = []
    
    for i in range(1, numPoints + 1):
        
        
        xOut = cx + r*math.cos(math.radians(angle))
        yOut = cy - r*math.sin(math.radians(angle))
        outpointList += [(xOut, yOut)]
        
        angle += 360/numPoints    
        
    
    inangle = 90 + 30    
    for i in range(1, numPoints + 1):
        
        xIn = cx + rSmall*math.cos(math.radians(inangle))
        yIn = cy - rSmall*math.sin(math.radians(inangle))
        inpointList += [(xIn, yIn)]
    
        inangle += 360/numPoints
       
        
    orderedList = []
    for i in range(len(outpointList)):
        orderedList += [(outpointList[i])] + [(inpointList[i])]
        #angle += 360/numPoints
        
    print(orderedList)
    print(outpointList)
    print(inpointList)
    return orderedList
    
def drawStar(canvas, centerX, centerY, diameter, numPoints, color):
    
    canvas.create_text(centerX, centerY, text="return 42", font="Arial 20 bold")

    cx = centerX
    cy = centerY
    r = diameter/2
    
    # outer circle
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width = 1, outline = "black")
    
    # inner circle
    rSmall = r * (3/8)
    canvas.create_oval(cx-rSmall, cy-rSmall, cx+rSmall, cy+rSmall, 
                width = 1, outline = "black")
    
    # star

    pointList = getStarPoints(canvas, centerX, centerY, diameter, numPoints, color)
    canvas.create_polygon(pointList, 
            fill = color, width = 0)
    
    

def drawStarHelper(centerX, centerY, diameter, numPoints, color, 
                   winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    drawStar(canvas, centerX, centerY, diameter, numPoints, color)

    root.mainloop()

def drawRedStripes(winWidth=950, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    
    stripeHeight = winHeight/13 #constant
    stripeCount = winHeight/stripeHeight
    
    y2 = stripeHeight #changing point
    y = 0
    
    for i in range(int(stripeCount)):
        canvas.create_rectangle(0, y, winWidth, y2,
            fill = "#B22234")
        
        y += 2*stripeHeight
        y2 += 2*stripeHeight
        
    root.mainloop()

def drawUnitedStatesFlag(winWidth=950, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    
    #background white rectangle
    canvas.create_rectangle(0, 0, winWidth, winHeight, 
                        fill = "#FFFFFF", width = 0)
    
    #red stripes
    drawRedStripes(winWidth=950, winHeight=500)
    
    #Small blue square
    canvas.create_rectangle(0, 0, winWidth*(2/5), winHeight*(7/13),
            fill = "#3C3B6E", width = 0)



    root.mainloop()

def testDrawStar():
    print("Testing drawStar()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawStarHelper(250, 250, 500, 5, "gold")
    #drawStarHelper(300, 400, 100, 4, "blue")
    #drawStarHelper(300, 200, 300, 9, "red")
    print("Done!")

def testDrawUnitedStatesFlag():
    print("Testing drawUnitedStatesFlag()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawUnitedStatesFlag()
    drawUnitedStatesFlag(winWidth=570, winHeight=300)
    print("Done!")

#################################################
# Test Functions
#################################################

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testSolvesCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS"))
    # from http://www.cryptarithms.com/default.asp?pg=1
    assert(solvesCryptarithm("NUMBER+NUMBER=PUZZLE", "UMNZP-BLER"))
    assert(solvesCryptarithm("TILES+PUZZLES=PICTURE", "UISPELCZRT"))
    assert(solvesCryptarithm("COCA+COLA=OASIS", "LOS---A-CI"))
    assert(solvesCryptarithm("CROSS+ROADS=DANGER", "-DOSEARGNC"))

    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDR-") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY-ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONY","OMY--ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","MOY--ENDRS") == False)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testLookAndSay()
    testInverseLookAndSay()
    testSolvesCryptarithm()
    testDrawStar()
    testDrawUnitedStatesFlag()

def main():
    testAll()

if __name__ == '__main__':
    main()
