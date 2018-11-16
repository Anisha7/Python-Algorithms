#################################################
# Lab2
#team: kjchin , zhenyanw
#################################################

import cs112_f17_week2_linter
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

# Put your solution to getKthDigit here!
def getKthDigit(n, k):
    
    if k <= 0:
        return None
    
    k -= 1
    
    positive_num = abs(n)
    return (positive_num // (10 ** k)) % 10
    

# See if you can rewrite isPrime from lecture here!

#################################################

def numberLength(x):
    count=0
    x = abs(x)
    while x>0:
        x = x//10
        count += 1
    return count



def countMatchingDigits(x, y):
    
    # variables
    count = 0
    x_len = numberLength(x) 
    y_len = numberLength(y)
    x_value = 0 # tracks value of x's digits
    y_value = 0 # tracks value of y's digits
    
    for x_pos in range (1, x_len + 1):
        x_value = getKthDigit(x, x_pos)
        #print("x_pos: ", x_pos)
        #print(x_value)
        
        for y_pos in range (1, y_len + 1):
            y_value = getKthDigit(y, y_pos)
            #print("y_pos: ", y_pos)
            #print(y_value)
            
            if x_value == y_value:
                count += 1
    return count
    

def rotateNumber(x):
    #1234 returns 4123
    
    l = numberLength(x) - 1
    y = x%10
    x = x//10
    z = y*(10**l)
    return x + z

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

def isCircularPrime(x):
    if x <= 0:
        return False
    l = numberLength(x)
    count = l
    success = 0
    while x > 0 :
        if success == l:
            return True
        if isPrime(x):
            for i in range(1,l+1):
                x = rotateNumber(x)
                if isPrime(x):
                    success += 1
                else:
                    return False
        else:   
            return False


#input: n (number), to get nth circular prime
#edge case: input is zero
def nthCircularPrime(n):
    
    #variables
    n += 1
    num = 0 #all numbers until we find nth circular prime
    prime = 0 #number of circular primes
    
    while prime < n:
        num += 1
        #print("num:", num)
        if isCircularPrime(num):
            print("isCircularPrime(num):", isCircularPrime(num), "num:", num)
            prime += 1
            print("prime:", prime)
            #print("num:", num)
            
            if prime == n:
                return num
    return None


def isEmirpsPrime(n):
    l = numberLength(n)
    rotated_num = 0
    previous_num = rotateNumber(rotateNumber(n))
    success_count = 0
            
    if isCircularPrime(n):
        for num in range (1, l):
            rotated_num = rotateNumber(n)
            print("loop:", num)
            print("rotated_num:", rotated_num != n)
            print("prev_num:", previous_num, rotated_num)
            if rotated_num != n:
                #if previous_num != rotated_num:
                success_count += 1
            else:
                print("Prints false here")
                return False
            previous_num = rotated_num
        if success_count == l-1:
            return True
    return False
            
    # while loop with num for checking all numbers up to n
        #Check if num is a circular Prime
            # If yes, track the number of circular primes in var 'prime'
                # Check if we found nth circular prime (prime == n)
                    # Return nth circular prime (num)

def nthEmirpsPrime(n):
    #non-neg int n 
    #returns nth "Emirp Prime" ( a prime number which 
    #becomes a different prime when decimal digits are reversed
    #13 = true because 31 is a different prime
    
    #check if n is a circular prime
        #check when rotated, if it is different each time
            #return the nearest Emirp Prime
    
    #variables
    n += 1
    numb = 0 #numbers until nth emirp
    emirp = 0 #number of emirps
    
    while emirp < n:
        numb += 1
        print("numb:",numb)
        if isEmirpsPrime(numb):
            emirp += 1
            print("emirp:",emirp)
            
            if emirp == n:
                print ("numb:",numb)
                return numb
    #return None
        
        

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testNumberLength():
    print('Testing numberLength()... ', end='')
    assert(numberLength(12) == 2)
    assert(numberLength(3) == 1)
    assert(numberLength(89) == 2)
    assert(numberLength(12345) == 5)
    assert(numberLength(120021) == 6)
    assert(numberLength(5000) == 4)
    print('Passed!')

def testCountMatchingDigits():
    print('Testing countMatchingDigits()... ', end='')
    assert(countMatchingDigits(1234, 2071) == 2)
    assert(countMatchingDigits(2203, 1527) == 2)
    assert(countMatchingDigits(5, 1253) == 1)
    assert(countMatchingDigits(18737, 7) == 2)
    assert(countMatchingDigits(1220, 7322) == 4)
    assert(countMatchingDigits(1234, 5678) == 0)
    print('Passed!')

def testRotateNumber():
    print('Testing rotateNumber()... ', end='')
    assert(rotateNumber(1234) == 4123)
    assert(rotateNumber(4123) == 3412)
    assert(rotateNumber(3412) == 2341)
    assert(rotateNumber(2341) == 1234)
    assert(rotateNumber(5) == 5)
    assert(rotateNumber(111) == 111)
    print('Passed!')

def testIsCircularPrime():
    print('Testing isCircularPrime()... ', end='')
    assert(isCircularPrime(2) == True)
    assert(isCircularPrime(11) == True)
    assert(isCircularPrime(13) == True)
    assert(isCircularPrime(79) == True)
    assert(isCircularPrime(197) == True)
    assert(isCircularPrime(1193) == True)
    print('Passed!')

def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(4) == 11)
    assert(nthCircularPrime(5) == 13)
    assert(nthCircularPrime(11) == 79)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(25) == 1193)
    print('Passed!')

def testNthEmirpsPrime():
    print('Testing nthEmirpsPrime()... ', end='')
    assert(nthEmirpsPrime(0) == 13)
    assert(nthEmirpsPrime(5) == 73)
    assert(nthEmirpsPrime(10) == 149)
    assert(nthEmirpsPrime(20) == 701)
    assert(nthEmirpsPrime(30) == 941)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testNumberLength()
    testCountMatchingDigits()
    testRotateNumber()
    testIsCircularPrime()
    testNthCircularPrime()
    testNthEmirpsPrime()

def main():
    cs112_f17_week2_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
