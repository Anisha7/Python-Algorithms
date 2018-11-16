#################################################
# Hw4
#################################################

import cs112_f17_week4_linter
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

# This is supposed to remove blank lines and comments.
# It has some bugs though...
def buggyCleanUpCode(code):
    lines = code.splitlines()
    #print("len(lines): ", len(lines))
    length = len(lines) - 1
    itemKeep = ""
    print(code)
    
    for i in range(length + 1):
        codeLine = lines[i]
        print(codeLine)
        #codeLine = codeLine.strip()
        #print(codeLine)
        #print("codeLine: ", codeLine)
        #codeLine = codeLine.split("#")
        # Get rid of comments
        #commentIndex = codeLine.find("#")
        #lines[i] = codeLine[:commentIndex]
            
        #if codeLine in string.whitespace: # Get rid of blank lines
            #lines.pop(i)
        #if bool(codeLine.find("#")) == False:
            #continue
        
        if "#" in codeLine:
            commentIndex = codeLine.index("#")
            codeLine = codeLine[:commentIndex]
             
        if codeLine != "":
            itemKeep += codeLine + "\n"
             #codeLine.remove("") 
            
        #else:

    print(itemKeep)
    #return "\n".join(lines)
    return itemKeep

# Scrabble Problem

# Helper function

def makeWords(dictionary, hand):
    
    wordList = []
    length = len(hand)
    handCopy = hand.copy()
    print("handCopy: ",handCopy)
    count = 0
    
    for word in dictionary:
        count = 0
        #print("word: ", word)
        handCopy = hand.copy()
        
        for i in range(len(word)):
            
            wordCount = word.count(word[i])           
            letterCount = hand.count(word[i])
                        
            if wordCount > letterCount:
                continue
            #print("word[i]: ", word[i])
                                        
            if word[i] in handCopy:
                count += 1
                #print("count: ", count)
                handCopy.pop(handCopy.index(word[i]))
                #print("handCopy: ",handCopy)
                
        if count == len(word):
            wordList += [word]
            
    print("wordList: ", wordList)        
    return wordList
            
                        

# Gets scores for words in wordList
def getWordScores(dictionary, letterScores, hand):
    
    wordList = makeWords(dictionary, hand)
    scoreList = []

    #list of letters to find index of letter
    
    for word in wordList:
        letterScore = 0
        #print("word:", word)
        for i in range(len(word)):
            
            j = ord(word[i]) - ord('a')
            #print("letter score:", letterScores[j-1])
            
            letterScore += letterScores[j]
            
            #print(j)
        scoreList += [letterScore]
            
    return scoreList
    
def getMaxScoreIndexes(scoreList):
    
    #scoreList = getWordScores(dictionary, letterScores, hand)
    maxScore = 0
    maxScoreCount = 1
    indexes = []
    
    for i in range(len(scoreList)):
        
        score = int(scoreList[i])
        if score > maxScore:
            maxScore = score
            maxScoreCount = 1
            indexes = [i]
            
        elif score == maxScore:
            maxScoreCount += 1
            indexes += [i]
        
    return (indexes, maxScore)
    
def bestScrabbleScore(dictionary, letterScores, hand):
    
    # helper makeWords()
        # use letters in hand to create every possible combination
        # test that with dictionary
        # if it exists, return list of words
    # helper getWordScores
        # take list of words and letter Scores
        # get score for each word
        # get maxScore and index for it
    # helper getMaxScoreIndexes()
        # gets index for max score
        # if equal max scores, gives index for all max scores
    # actual function
        # get word from list of words at found index
        # return word
    
    wordList = makeWords(dictionary, hand)
    scoreList = getWordScores(dictionary, letterScores, hand)
    #print("scoreList: ", scoreList)
    (indexes, maxScore) = getMaxScoreIndexes(scoreList)
    #print("indexes:", indexes)
    bestWords = []
    #print("wordList: ", wordList)
    
    if len(wordList) > 1:
        
        for i in indexes:
            bestWords += [wordList[i]]
    
    #if len(bestWords) == 1:
        #bestWords = bestWords[0]
        
    if len(wordList) == 1:
        bestWords = wordList[0]
        
    elif len(wordList) < 1 or len(bestWords) < 1:
        return None
    
    #print("bestWords: ", bestWords) 
    return (bestWords, maxScore)

###### Autograded Bonus ########
# (place non-autograded bonus below #ignore-rest line!) #

def runSimpleProgram(program, args):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

def deciferProgram(program):
    
    # Steps
    # Get variable name and get its value
    # Put it in a list?
    #use buggy clean up code
    programC = buggyCleanUpCode(program)
    #print("programC: ",programC)
    tupleList = []
    
    for line in programC.splitlines():
        items = line.split(" ")
        if len(items) > 2:
            items.pop(2)
        #print("items: ", items)
        
        tupleList += [(items)]

    #print("tupleList: ", tupleList)
    
    return tupleList

def runSimpleTortoiseProgram(program, winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    canvas.create_text(winWidth/2, winHeight/2,
                       text='Go Tortoise Go!')
                       
    commandList = deciferProgram(program)
    
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    color = ""
    move = 0
    left = 0
    right = 0
    
    for tuple in commandList:
        
        #(var, command) = tuple
        #print("tuple: ", tuple)
        var = tuple[0] 
        command = tuple[1]

        if var == "color":
            
            color = command
            if command == "none":
                color = "white"
            print("color: ", color)
            
        if var == "move":
            print(command)
            move += int(command)
            print("move: ", move)
            
            # draw line when move is found
            if left != None:
                x2 = x + (move * math.cos(math.radians(left)))
                y2 = y + (move * math.sin(math.radians(left)))
                canvas.create_line(x,y,x2,y2, width = 1, fill = color)
                print("left")
                print("x2: ", x2)
                print("y2: ", y2)
                x = x2
                y = y2
            
            elif right != None:
                
                x2 = x + (move * math.cos(math.radians(right)))
                y2 = y + (move * math.sin(math.radians(right)))
                canvas.create_line(x,y,x2,y2, width = 1, fill = color)
                print("right")
                print("x2: ", x2)
                print("y2: ", y2)
                x = x2
                y = y2
                
            else:
                
                x2 = x + move
                y2 = y
                canvas.create_line(x,y,x2,y2, width = 1, fill = color) 
                
                x = x2
                y = y2  
            move = 0     
            #root.mainloop()
            
        if var == "left":
            left = - int(command)
            print("left: ", left)
            
        if var == "right":
            right = int(command)
            print("right: ", right)
        

    root.mainloop()

def testRunSimpleTortoiseProgram1():
    runSimpleTortoiseProgram("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""", 300, 400)

def testRunSimpleTortoiseProgram2():
    runSimpleTortoiseProgram("""
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
""")

def testRunSimpleTortoiseProgram():
    print("Testing runSimpleTortoiseProgram()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    testRunSimpleTortoiseProgram1()
    testRunSimpleTortoiseProgram2()
    print("Done!")

#################################################
# Test Functions
#################################################

def testBuggyCleanUpCode():
    print("Testing buggyCleanUpCode()...", end="")
    
    spacyCode = """
def func(x):
    return None
            
    #function does nothing
            
"""
    nonSpacyCode = """
    def func(x):
        return None
    """
    
    #assert(buggyCleanUpCode(spacyCode) == nonSpacyCode)
    
    print("Passed")

def testMakeWords():
    print("Testing makeWords()...", end="")
    
    answer = ['to']
    dictionary = ['to','cat', 'bat']
    hand = ['o','t', 't']
    assert(makeWords(dictionary, hand) == answer)
    
    answer = ['cat']
    dictionary = ['to','cat', 'bat']
    hand = ['a','t', 'c']
    assert(makeWords(dictionary, hand) == answer)
    
    answer = ['cat', 'bat']
    dictionary = ['to','cat', 'bat']
    hand = ['a','t', 'c', 'b']
    assert(makeWords(dictionary, hand) == answer)
    
    answer = []
    dictionary = ['tto','cat', 'bat']
    hand = ['o','t']
    assert(makeWords(dictionary, hand) == answer)
    
    print("Passed")

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    print("score: ", bestScrabbleScore(dictionary1(), letterScores1(),\
     list("b")))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    print("testScore: ", bestScrabbleScore(dictionary2(),\
     letterScores2(), list("xyz")))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testBuggyCleanUpCode()
    testMakeWords()
    testBestScrabbleScore()
    testRunSimpleTortoiseProgram()
    testRunSimpleProgram()

def main():
    cs112_f17_week4_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
