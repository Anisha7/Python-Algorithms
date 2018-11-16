  #################################################
# Lab1
#################################################

import cs112_f17_linter
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

#################################################
# Lab1 problems
#################################################


def nearestOdd(n):

    if n==0:
        return -1
    if isinstance(n, int) and n%2==0 and n>0:
        return n-1
    elif  isinstance(n, int) and n%2==0 and n<0:
        return n-1
        
    elif isinstance(n, float) and (abs(n)//1)%2==0 and (n>0):
       return int(n) +1
    
    elif isinstance(n, float) and (abs(n)//1)%2==0 and n<0:
        #return abs(int(n))
        return int(n) -1
    
    else:
        return int(n)
        

        
def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    
    if x2>=x1 and x2<=x1+w1 and y2<= y1+h1 and y2>=y1:
        return True
    elif x1>=x2 and x1<=x2+w2 and y1<= y2+h2 and y1>=y2:
        return True
    else:
        return False
#not working for all cases

def isPerfectSquare(n):

    if n==0 or n==1:
        return True
    if not isinstance(n, int):
        return False
    if n<0:
        return False
    if almostEqual(math.sqrt(n),int(math.sqrt(n))):
        return True
    else:
        return False

def getKthDigit(n, k):
    if not isinstance(n,int) or isinstance(n,float):
        return None
    elif n==0:
        return None
    n=abs(n)
    #if k <= 0:
        #return False
    if isinstance(n, int) and isinstance(k, int):
        for i in range(k):
            n//=10
        return n%10
    else:
        return False

def setKthDigit(n, k, d):
    lola = n==int(n) and k>0 and k==int(k)
    cola = d>=0 and d<=9
    if lola and cola:
        getKthDigit()
        return n-getKthDigit*10

    else:
        return None

def colorBlender(rgb1, rgb2, midpoints, n):
    if n<7 or n>9:
        return None
    lola = isinstance(rgb1, int) and isinstance(rgb2, int)
    cola = isinstance(midpoints, int) and isinstance(n, int)
    mola = midpoints>0 and n>0
    if lola and cola and mola:
         w= rgb1-rgb2
         x= w/midpoints
         return rgb1 + n*x
    else:
        return None

#################################################
# Lab1 Test Functions
################################################

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print('Passed.')

def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
#     assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
#     assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
#     assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
#     assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
#     assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
#     assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
#     assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6) == True)
#     assert(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6) == False)
#     print('Passed.')

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed.')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed.')

#################################################
# Lab1 Main
################################################

def testAll():
    testNearestOdd()
    testRectanglesOverlap()
    testIsPerfectSquare()
    testGetKthDigit()
    testSetKthDigit()
    testColorBlender()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        'as,break,class,continue,del,except,finally,for,' +
        'global,in,is,lambda,nonlocal,pass,raise,repr,' +
        'try,while,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,range,repr,reversed,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_f17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
