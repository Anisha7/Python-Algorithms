#################################################
# Hw1
#################################################

import cs112_f17_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later8
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Hw1 problems
#################################################

def hotdogPurchase(numHotdogs):
    #1 hot dog= 1 frank and 1 bun
    #1pack of frank= 10pieces
    #1 pack of bun= 8pieces
    #numHotdogs is a non-negative int
    #return smallest number of franks and buns that must be purchased
    if numHotdogs == 0:
        return (0,0)
    elif numHotdogs <= 8:
        return (1,1)
    elif numHotdogs%8 == 0 and numHotdogs%10 == 0:
        n = int(numHotdogs)
        franks = n//10
        buns = n//8
        return (franks,buns)
    elif numHotdogs%8 == 0:
        n = int(numHotdogs)
        franks = n//10 + 1
        buns = n//8
        return (franks,buns)
    elif numHotdogs%10 == 0:
        n = int(numHotdogs)
        franks = n//10
        buns = n//8 +1
        return (franks,buns)
    else:
        n=int(numHotdogs)
        franks = n//10 + 1
        buns = n//8 + 1
        return (franks,buns)

def hotdogExcess(numHotdogs): 
    #use total number of hot dogs 
    #returns number of excess franks and buns you will need to purchase
    numHotdogs=int(numHotdogs)
    x,y = hotdogPurchase(numHotdogs)
    multiplier = x*10 -numHotdogs, y*8 -numHotdogs
    return multiplier


def isRightTriangle(x1, y1, x2, y2, x3, y3):
    #take 6 int or float values that represent vertices of the triangle
    #teturn true if right triangle
    #return false if not right triangle
    #a^2 + b^2 = c^2
    #return 42
    #distance from (x1,y1) to (x2,y2)
    a = math.sqrt(abs(((x1 - x2)**2)+((y1 - y2)**2)))
        #distance from (x1,y1) to (x3,y3)
    # print(a)
    b = math.sqrt(abs(((x1 - x3)**2)+((y1 - y3)**2)))
        #distance from (x2,y2) to (x3,y3)
    # print(b)
    c = math.sqrt(abs(((x2 - x3)**2)+((y2 - y3)**2)))
        #test for right triangle
    # print(c)
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        
        # print(isinstance(a, int))
        if a**2 + b**2 == c**2:
            return True
        elif b**2 + c**2 == a**2:
            return True
        elif c**2 + a**2 == b**2:
            return True
        else:
            return False
    else:
        # a = int(a)
        # b = int(b)
        # c = int(c)
        # print("Printing...")
        # print(a)
        # print(b)
        # print(c)
        # print("a**2:", a**2)
        if almostEqual(a**2 + b**2, c**2):
            return True
        elif almostEqual(b**2 + c**2, a**2):
            return True
        elif almostEqual(c**2 + a**2, b**2):
            return True
        else:
            return False

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def lineIntersection(m1, b1, m2, b2):
    if m1 == m2:
        return None

    else:
        x = (b2-b1)/(m1-m2)
        # y1 = m1*x + b1
        # y2 = m2*x + b2
        return x

def triangleArea(s1, s2, s3):
    #semiperimeter s =  s=1/2(a+b+c) 
    #area =sqrt(s(s-a)(s-b)(s-c)). 
    s = (s1 + s2 + s3)*0.5
    area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    return area

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    #finding points x,y of intersections of the three lines
    x1 = lineIntersection(m1, b1, m2, b2)
    #print("x1:",x1)
    y1 = m1*x1 + b1
    #print("y1:",y1)
    x2 = lineIntersection(m2, b2, m3, b3)
    #print("x2:",x2)
    y2 = m2*x2 + b2
    #print("y2:",y2)
    x3 = lineIntersection(m1, b1, m3, b3)
    #print("x3:",x3)
    y3 = m3*x3 + b3
    #print("y3:",y3)
    
    #finding sides a,b,c of the triangle formed by the three sides
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x1, y1, x3, y3)
    
    #calculating area
    area = triangleArea(a,b,c)
    return area

def bonusFindIntRootsOfCubic(a, b, c, d):
    # y = a*x**3 + b*x**2 + c*x + d
    #formulas to find root1 : Cubic Formula
    #https://math.vanderbilt.edu/schectex/courses/cubic/
    p = (-b)/(3*a)
    q = (p**3) + ((b*c - 3*a*d)/(6*(a**2)))
    r = c/(3*a)
    c = c.real
    c= int(c)
    p1= (q**2 + (r - (p)**2)**3)**(1/2)
    root1 = (q + p1)**(1/3) + (q-p1)**(1/3) + p
    root1 = root1.real
    root1 = int(root1)
    print("Root 1:")
    print(root1)
   
    #a*x**3 + b*x**2 + c*x + d
    # = (x-r)*(a*x**2 + (b + a*r)*x + c + b*r + a*r**2
    
    #formulas to find root2 and root3
    #https://en.wikipedia.org/wiki/Cubic_function#Factorization
    under_root_not_squared = ((b**2) - (4*a*c) - (2*a*b*r) - (3*(a**2)*(r**2)))
    # print(under_root_not_squared)
    # if under_root_not_squared < 0:
    #     UnderRoot = -math.sqrt(-under_root_not_squared)
    # else:
    #     UnderRoot = math.sqrt(under_root_not_squared)
    # 
    # print("UnderRoot: ", UnderRoot)
    # #getting math domain error here for the above equation
    # root2 = ((-b - r*a + UnderRoot)/(2*a))
    # root3 = ((-b - r*a - UnderRoot)/(2*a))
    
    
    #testing without math.sqrt
    root2 = ((-b - r*a + (under_root_not_squared)**0.5)/(2*a))
    root3 = ((-b - r*a - (under_root_not_squared)**0.5)/(2*a))
    
    # root1 = root1.real
    root2 = root2.real
    root3 = root3.real
    
    root2 = int(root2)
    root3 = int(root3)
    
    print("root2:",root2)
    print("root3:",root3)
    
    return (root1, root2, root3)

#################################################
# Hw1 Test Functions
#################################################

def testHotdogPurchase():
    print('Testing hotdogPurchase()... ', end='')
    assert(hotdogPurchase(0) == (0,0))
    assert(hotdogPurchase(13) == (2,2))
    assert(hotdogPurchase(26) == (3,4))
    assert(hotdogPurchase(39) == (4,5))
    assert(hotdogPurchase(50) == (5,7))
    assert(hotdogPurchase(61) == (7,8))
    assert(hotdogPurchase(80) == (8,10))
    assert(hotdogPurchase(88) == (9,11))
    print('Passed.')

def testHotdogExcess():
    print('Testing hotdogExcess()... ', end='')
    assert(hotdogExcess(0) == (0,0))
    assert(hotdogExcess(13) == (7,3))
    assert(hotdogExcess(26) == (4,6))
    assert(hotdogExcess(39) == (1,1))
    assert(hotdogExcess(50) == (0,6))
    assert(hotdogExcess(61) == (9,3))
    assert(hotdogExcess(80) == (0,0))
    assert(hotdogExcess(88) == (2,0))
    print('Passed.')
 
def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')

def testLineIntersection():
    print("Testing lineIntersection()...", end="")
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(almostEqual(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(almostEqual(lineIntersection(10,0,-4,35), 2.5))
    print("Passed. (Add more tests to be more sure!)")

def testDistance():
    print("Testing distance()...", end="")
    assert(almostEqual(distance(0, 0, 1, 1), 2**0.5))
    assert(almostEqual(distance(3, 3, -3, -3), 6*2**0.5))
    assert(almostEqual(distance(20, 20, 23, 24), 5))
    print("Passed. (Add more tests to be more sure!)")

def testTriangleArea():
    print("Testing triangleArea()...", end="")
    assert(almostEqual(triangleArea(3,4,5), 6))
    assert(almostEqual(triangleArea(2**0.5, 1, 1), 0.5))
    assert(almostEqual(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed. (Add more tests to be more sure!)")

def testThreeLinesArea():
    print("Testing threeLinesArea()...", end="")
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed. (Add more tests to be more sure!)")

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    print(result1, result2, result3)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed.')

#################################################
# Hw1 Main
#################################################

def testAll():
    testHotdogPurchase()
    testHotdogExcess()
    testIsRightTriangle()
    testDistance()
    testLineIntersection()
    testTriangleArea()
    testThreeLinesArea()
    testBonusFindIntRootsOfCubic()

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
