#################################################
# Hw3
#################################################

import cs112_f17_week3_linter
import math
import string

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

#Problem 1

#create helper function that will reorder a string in alphabetical order

def getAlphabeticalOrder(s):
    #ex. cba ==> abc
    
    letter = "z" #each letter in string s
    orderedString = "" 
    smallestIndex = 0
    
    while len(s) > 0:
        #print("s:", s)
        #Get first letter for alphabetical order
        for i in range(len(s)):
            #print("letter:", letter)
            #print("s[i]: ", s[i])
            if letter >= s[i]:
                letter = s[i]
                smallestIndex = i
            
            #s = s.replace(s[i], "") 
                #Index out of range error if used
        s = s[:smallestIndex] + s[smallestIndex + 1 :]
        #s = s.replace(, "")
        #This replaces all the 'letter' letters from string s.
        #Is there a way to replace only the one at the index s[i]?
            #ex. cbaa ==> aabc
        
        orderedString += letter
        letter = "z"
    
    print("orderedString: ", orderedString)
    #remove already added letter from string s
    
        
    return orderedString

# Input: s (string)
# Output
# Counts number of letters and returns tuple: num_letters and count_string

def countDigit(s):
    s = s.lower()
    string = ""
    count_string = ""
    
    for char in s:
        
        if char not in string:
            
            count = s.count(char)
            string += char
            count_string += str(count)

    return (string, count_string)

       
#Gets number that occurs the most in string

def getMaxNumber(s):
    maxNum = 0
    #(letter, count) = countDigit(s)
    count = s
    
    for i in range(0, len(count)):
        
        countNum = int(count[i])
        #print(countNum)
        #print(countNum > maxNum)
        
        if countNum > maxNum:
            maxNum = countNum
            
        #if countNum == maxNum:
            
    #print("maxNum: ", maxNum)
            
    return maxNum


#Gets letter associated with the maxNumber found above

def getLetterAtMaxNumber(strings):
    #(letter, count) = countDigit(s)
    (letter, count) = strings
    charLetter = ""
    maxNum = getMaxNumber(count)
    
    for num in range(len(count)):
    
        charLetter = letter[count.index(str(maxNum))]
        
    
    return charLetter


#removes number and letter from strings count 
#and letter that have been used

def getNewString(strings):
    
    (letter, count) = strings
    
    maxNum = getMaxNumber(count)
    print("maxNum:", maxNum)
    charLetter = getLetterAtMaxNumber(strings)
    
    
    count = count.replace(str(maxNum), "")
    print("new count: ", count)
    letter = letter.replace(charLetter, "")
    print("new letter: ", letter)
    
    return (letter, count)



#use this in mostFrequentLetters to reorder strings with the same count
    #save this into a separate string and then add it to the newString


# Input:  string s, case does not matter
# Output: lower case string containting the letters of 
       # s in most frequently used order; 
       # if tie, return in alphabetic order
       
def mostFrequentLetters(s):
    s = getAlphabeticalOrder(s)
    (letter, count) = countDigit(s)
    strings = (letter, count)
    newString = ""

    for num in range(len(count)):
        
        charLetter = getLetterAtMaxNumber(strings)
        print("charLetter: ", charLetter)
        
        strings = getNewString(strings)
        print("strings:", strings)
        
    
        newString += charLetter
        
    return newString

#End of Problem 1

#Problem 2

# gets the characters in string msg until n characters 
def getMsgChar(msg, n):
    msg = msg.replace(" ", "")
    msgLength = len(msg)
    
    # while n > 0:
    print("n: ", n)
    print("msgLength: ", msgLength)
    
    # for char in msg: 
    if msgLength > n:
 
        print("msg:", msg[n])
        msgChar = msg[n]
        print("msgChar: ", msgChar)
            
            
    elif msgLength <= n:
                
        if n - msgLength < msgLength:
            msgChar = msg[n - msgLength]
            print("msgChar: ", msgChar)
            # for n that is less than 2*msgLength
            # give the string character at position 
                
        else:
            # In order for string character to reloop to first n:
            newN = n - msgLength
            while newN >= msgLength:
                newN -= msgLength
                print("newN: ", newN)
                    
            msgChar = msg[newN]
            print("msgChar: ", msgChar)
                
    return msgChar
                
#takes two strings
#returns string by replacing non-whitespace characters in pattern
#with non-whitespace characters in message
#remove leading or trailing newlines in the pattern
def patternedMessage(msg, pattern):
    msg = msg.replace(" ", "")
    patternLength = len(pattern)
    msgLength = len(msg)
    print("msg:", msg)
    for i in range(0, patternLength):
        
        if pattern[i] != " ":
            
            msgChar = getMsgChar(msg, i)
            newMessage = pattern.replace(pattern[i], msgChar)
            
            print("newMessage:", newMessage)
            
    return newMessage
   
#takes encoding from encodeColumnShuffleCipher in lab 3
#runs it in reverse
def decodeColumnShuffleCipher(message):
    return 42

#
def decodeColumnShuffleCipherNoDashes(message):
    return 42

##### Bonus #####

def topLevelFunctionNames(code): return 42
def getEvalSteps(expr): return 42
def bonusEncode1(msg): return 42
def bonusDecode1(msg): return 42
def bonusEncode2(msg): return 42
def bonusDecode2(msg): return 42
def bonusEncode3(msg): return 42
def bonusDecode3(msg): return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################
def testMostFrequentLetters():
    print("Testing mostFrequentLetters()... ", end="")
    
    s = "We attack at Dawn"
    result = "atwcdekn"
    assert(mostFrequentLetters(s) == result)
    print("Pass One ")
    
    s = "Note that digits, punctuation, and whitespace are not letters!"
    result = "teanioscdhpruglw"
    assert(mostFrequentLetters(s) == result)
    print("Pass Two ")
    s = ""
    result = ""
    assert(mostFrequentLetters(s) == result)
    print("Pass Three ")
    
    print("Passed!")
    
def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        msg,pattern = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        print("I'm here observed:", observed)
        print("soln:", soln)
        assert(observed == soln)
    print("Passed!")

def testDecodeColumnShuffleCipher():
    print("Testing decodeColumnShuffleCipher()...", end="")
    msg = "0213WTAWACD-EATNTKA-"
    result = "WEATTACKATDAWN"
    assert(decodeColumnShuffleCipher(msg) == result)

    msg = "210DNAIRBWHNYRCSYR-UEYHEBTTIESNOBE-SDLWTAIIPKEALEH-"
    result = "SUDDENLYAWHITERABBITWITHPINKEYESRANCLOSEBYHER"
    assert(decodeColumnShuffleCipher(msg) == result)

    print("Passed!")

def testDecodeColumnShuffleCipherNoDashes():
    print("Testing decodeColumnShuffleCipherNoDashes()...", end="")

    # This is a place holder to force testing to fail.  Replace this with
    # real testcases.
    assert("Replace Me With Real Tests" == False)

    print("Passed!")

##### Bonus #####

def testBonusTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

def testBonusGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

import random

def testBonusDecode(testFn, encodeFn, decodeFn):
    print("Testing " + testFn + "...", end="")
    s1 = ""
    for c in range(15):
        if (random.random() < 0.80):
            s1 += random.choice(string.ascii_letters)
        else:
            s1 += random.choice(" \n\n") + random.choice(string.digits)
    for s in ["a", "abc", s1]:
        assert(decodeFn(encodeFn(s)) == s)
    print("Passed!")

def testBonusDecode1():
    testBonusDecode("testBonusDecode1", bonusEncode1, bonusDecode1)

def testBonusDecode2():
    testBonusDecode("testBonusDecode2", bonusEncode2, bonusDecode2)

def testBonusDecode3():
    testBonusDecode("testBonusDecode3", bonusEncode3, bonusDecode3)

#################################################
# testAll and main
#################################################

def testAll():
    testMostFrequentLetters()
    testPatternedMessage()
    testDecodeColumnShuffleCipher()
    testDecodeColumnShuffleCipherNoDashes()
    testBonusTopLevelFunctionNames()
    testBonusGetEvalSteps()
    testBonusDecode1()
    testBonusDecode2()
    testBonusDecode3()
def main():
    cs112_f17_week3_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
