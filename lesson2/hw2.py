#################################################
# Hw2
#################################################

import cs112_f17_hw2_linter
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

# Gets the kth digit of n!
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


# Put your solution to isPrime here!
def isPrime(n):
    if (n == 2):
        return True
        
    if (n < 2):
        return False
        
    if (n % 2 == 0):
        return False
        
    mfactor = roundHalfUp(n**0.5)
    
    for factor in range(3, mfactor+1, 2):
        
        if (n % factor == 0):
            return False
            
    return True
    
#################################################

#Takes an int x and returns true if int x contains any off digits
def containsOddDigits(x):
    
    #Steps
        #Check if x is an integer
            #Check each digit of x for an odd number
                #return true
            #return false
    
    #Variables
    count = 0 #keeps track of the number of odds in the digit
    
    if x == int(x):
        l = numberLength(x) #number of digits in x
        
        for dig in range(1, l+1):
            num = getKthDigit(x, dig)
            #print("num", num)
            
            if num%2 != 0:
                count += 1
                #print("count:", count)
                
        if count > 0:
            return True
        else:
            return False
    else:
        return False
            
    #return 42

#Takes int a and int b
#Returns the number of multiples of 7 that occur in the range of integers a to b
def countMultiplesOfSeven(x, y):
    
    #Steps
        #create for loop for range a to b
            #Test if each number is a multiple of 7
                #count how many multiples there are
        #return count
    
    #Variables
    count = 0 #number of multiples
    
    for num in range(x, y+1):
        
        if num % 7 == 0:
            count += 1
            #print("count:", count)
            
    return count
    
    #return 42

#prints number triangle as big as int n
def printNumberTriangle(n):
    #Steps
        #create for loop for num in the range of 1 to n
            #print number length amount of rows
            #print nums in columns
                #1 num in 1st row
                #2 in 2nd...so on
    
    n = int(n)
    num = 1 #all numbers
    count = 0
    
    for row in range(n):
        #print("row:", row)
        num = row + 1
        for col in range(row + 1):
            
            print(num, end="")
            num -=1
            
        print()
    
    #print(42)

#non-neg int n --> returns sum of the squares of its digits
#123 --> 1**2 + 2**2 + 3**2 = 14
def sumOfSquaresOfDigits(x):
    #Steps
        #Take non-neg int n
            #Get each digit using getKthDigit
            #Use number length
                #Store these digits
                #Square them
                #Add them
    x = abs(x)
    x = int(x)
    l = numberLength(x)
    prev_digit_square = 0
    
    for dig in range(1, l+1):
        
        if l > 0:
            digit = getKthDigit(x, dig)
            #print("digit:", digit)
            digit_square = digit**2
            #print("digitsquare:", digit_square)
            
        prev_digit_square += digit_square
        #print("prev_dig:", prev_digit_square)
        
    return prev_digit_square

#a number n with for ex. digits ab is happy if a**2 + b**2 = 1 or 
#the result x's digits ab return true for that function and so on. 
#It is unhappy if it reaches 4
def isHappyNumber(x):
    #steps
        #create a loop for sumOfSquareDigits to evaluate for its result as well
        #check if it is equal to 1
        #return true if it is
    
    dig_square = sumOfSquaresOfDigits(x) #first squared sum of digits
    
    if x<1:
        return False
        
    if dig_square == 1:
        return True
    
    #Checks for happy number
    #loop for squared sums of digits until determined as 
    #Happy Number or Unhappy Number
    while dig_square != 1:
        dig_square = sumOfSquaresOfDigits(dig_square)
        if dig_square == 1:
            return True
        elif dig_square == 4:
            return False
    

#A happy prime that is happy and prime
#returns nth happy prime 
def nthHappyPrime(n):
    #steps
        #determine if num is happy and prime
        
    #variables
    
    n += 1
    num = 0 #all numbers until we find nth happy prime
    happy_prime = 0 #Tracks number of happy primes
    
    if n<0 or n==float:
        return None
        
    while happy_prime < n:
        num += 1
        if isHappyNumber(num) and isPrime(num):
            happy_prime += 1

            
    if happy_prime == n:
        return num
        
    return None
    
    #return 42

##### Bonus #####

def play112(game):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testContainsOddDigits():
    print('Testing containsOddDigits()... ', end='')
    assert(containsOddDigits(1246) == True)
    assert(containsOddDigits(8663) == True)
    assert(containsOddDigits(224) == False)
    assert(containsOddDigits(115) == True)
    assert(containsOddDigits(8) == False)
    assert(containsOddDigits(9) == True)
    print('Passed!')

def testCountMultiplesOfSeven():
    print('Testing countMultiplesOfSeven()... ', end='')
    assert(countMultiplesOfSeven(3, 16) == 2)
    assert(countMultiplesOfSeven(13, 15) == 1)
    assert(countMultiplesOfSeven(7, 22) == 3)
    assert(countMultiplesOfSeven(8, 28) == 3)
    assert(countMultiplesOfSeven(15, 18) == 0)
    assert(countMultiplesOfSeven(15, 6) == 0)
    print('Passed!')

def testPrintNumberTriangle():
    import sys, io
    print('Testing printNumberTriangle()... ', end='')
    tmpOut = sys.stdout

    oneOutput = io.StringIO()
    sys.stdout = oneOutput
    printNumberTriangle(1)
    oneCheck = oneOutput.getvalue()

    fourOutput = io.StringIO()
    sys.stdout = fourOutput
    printNumberTriangle(4)
    fourCheck = fourOutput.getvalue()

    sevenOutput = io.StringIO()
    sys.stdout = sevenOutput
    printNumberTriangle(7)
    sevenCheck = sevenOutput.getvalue()

    sys.stdout = tmpOut

    assert(oneCheck == "1\n")
    assert(fourCheck == "1\n21\n321\n4321\n")
    assert(sevenCheck == "1\n21\n321\n4321\n54321\n654321\n7654321\n")
    print('Passed!')

def testSumOfSquaresOfDigits():
    print('Testing sumOfSquaresOfDigits()... ', end='')
    assert(sumOfSquaresOfDigits(5) == 25)
    assert(sumOfSquaresOfDigits(12) == 5)
    assert(sumOfSquaresOfDigits(234) == 29)
    print('Passed!')

def testIsHappyNumber():
    print('Testing isHappyNumber()... ', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Passed!')

def testNthHappyPrime():
    print('Testing nthHappyPrime()... ', end='')
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(5) == 79)
    assert(nthHappyPrime(6) == 97)
    assert(nthHappyPrime(-3) == None)
    print('Passed!')

def testBonusPlay112():
    print("Testing play112()... ", end="")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testContainsOddDigits()
    testCountMultiplesOfSeven()
    testPrintNumberTriangle()
    testSumOfSquaresOfDigits()
    testIsHappyNumber()
    testNthHappyPrime()
    testBonusPlay112()

def main():
    cs112_f17_hw2_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
