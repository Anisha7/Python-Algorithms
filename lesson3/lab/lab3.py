#################################################
# Lab3
# Anisha Jain - anishaj
# Team: Zhenyan - 
#################################################

import cs112_f17_week3_linter
import math

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

def getKthDigit(n, k):
    
    if k <= 0:
        return None
    
    k -= 1
    
    positive_num = abs(n)
    return (positive_num // (10 ** k)) % 10
    
# Counts the number of digits in x!
def numberLength(x):
    count=0
    x = abs(x)
    
    while x>0:
        x = x//10
        count += 1
        
    return count
#################################################

def commonWords(i, j):
    



# Takes two strings and returns the longest string that occurs in both
def longestCommonSubstring(s1, s2):
    
    
    
    
    
    
    
    count = 0
    prevCount = 0
    result = ""
    longestString = ""
    
    for char1 in s1:

        for char2 in s2:
            prevCount = count
            prevResult = result
 
            if char1 == char2:
                count += 1
                
                print("count:",count)
                print("char1:", char1)
                # add string characters
                result += char1
                
                print("count:",count)
                print("prevCount:", count)
            
    
    print(result)
    print(prevResult)
    
    if len(prevResult) > len(result):
        longestString = prevResult
    elif len(prevResult) < len(result):
        longestString = result
    elif len(prevResult) == len(result):
        longestString = result.upper
    
    if count > prevCount:
        return prevResult
        
    # return 42
    # returns all common letters. Need to restart when it hits a non-common one.
    # not ok for upper case yet

# returns the student with average grade
# helper function
def getStudentAvg(gradebook):
    num = 0
    gradebook = gradebook.replace("-","")
    gradebookItem = gradebook.split(",")
    
    
    length = len(gradebookItem) #a way to count the number of splits
    print("length:", length)
    
    for stud in gradebook.splitlines():
        
        for grade in gradebookItem:
            grade = grade.strip() 
            
            print("grade:", grade)
            
            if not grade.isdigit():
                name = grade
                print("name:", name)
                
            if grade.isdigit(): 
                grade = int(grade)
                
                if grade < 0:
                    grade[1:]
                
                num += grade
                print("num:", num)

        avg = num // length
        print("avg:", avg)
        
    return str(name + ", " + str(avg))
        
        #num divided by the number of grades given...
                
            # get/store the grade (number)
        # average all the numbers
        # print name, number
    
        # use isDigit, wont work for     
        # negatives so use or statement
        # if neg, new digit, slice s[1:]
    
# returns student with best average
def bestStudentAndAvg(gradebook):
    # Use getStudentAvg helper function
        # Compare the numbers
        # return largest number with name
    prevAvg = ""
    avg = ""
    
    for stud in gradebook.splitlines():
        
        prevAvg = avg
        print("prevAvg:", prevAvg)
        
        avg = getStudentAvg(gradebook)
        print("avg:", avg)
        
        if avg < prevAvg:
            avg = prevAvg
            
    return avg
            
    #return 42    

# helper function
def wordWrap(text, width):
    result = ""
    while text != "":
        row = text[:width].strip()
        result += "\n"
        text = text[width:]
    return result.replace("","-").strip()
    
def getCharAtKey(message, key):
    #grabs character at pos given by key
    length = numberLength(key)
    
    for col in message:
        for i in range(1, length + 1):
            print("ah")    
    return 42


def encodeColumnShuffleCipher(message, key):
    message = wordWrap(message, 4)
    
    # goes through columns and 
    # rearranges them based on key
    for col in message:
        for num in key:
            # move the columns as specified
            # by key
                # helper function
                    # grab character at position in key 
                    #and add the strings together 
                    #in that order
                        #int of key
            # Generate newMessage
    #return key + newMessage
            return 42    

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed!")

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:92")
    gradebook   =   """
#   ignore  blank   lines   and lines   starting    with    #'s
wilma,93,95

fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:94")
    gradebook = "fred,0"
    assert(bestStudentAndAvg(gradebook) ==  "fred:0")
    gradebook = "fred,-1\nwilma,-2"
    assert(bestStudentAndAvg(gradebook) ==  "fred:-1")
    gradebook = "fred,100"
    assert(bestStudentAndAvg(gradebook) ==  "fred:100")
    gradebook = "fred,100,110"
    assert(bestStudentAndAvg(gradebook) ==  "fred:105")
    gradebook = "fred,49\nwilma" + ",50"
    assert(bestStudentAndAvg(gradebook) ==  "wilma:50")
    print("Passed!")
    
def testEncodeColumnShuffleCipher():
    print("Testing encodeColumnShuffleCipher()...", end="")
    
    msg = "WEATTACKATDAWN"
    result = "0213WTAWACD-EATNTKA-"
    assert(encodeColumnShuffleCipher(msg, "0213") == result)
    
    msg = "SUDDENLYAWHITERABBITWITHPINKEYESRANCLOSEBYHER"
    result = "210DNAIRBWHNYRCSYRUEYHEBTTIESNOBESDLWTAIIPKEALEH"
    assert(encodeColumnShuffleCipher(msg,"210") == result)

    print("Passed!")
    

#################################################
# testAll and main
#################################################

def testAll():
    testLongestCommonSubstring()
    testBestStudentAndAvg()
    testEncodeColumnShuffleCipher()

def main():
    cs112_f17_week3_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
