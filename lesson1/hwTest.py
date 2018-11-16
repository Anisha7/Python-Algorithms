import math
import cs112_f17_linter
import decimal

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
   
    print("Root 1:")
    print(root1)
   
    #code works upto here
   
    #a*x**3 + b*x**2 + c*x + d
    # = (x-r)*(a*x**2 + (b + a*r)*x + c + b*r + a*r**2
    
    #formulas to find root2 and root3
    #https://en.wikipedia.org/wiki/Cubic_function#Factorization
    under_root_not_squared = ((b**2) - (4*a*c) - (2*a*b*r) - (3*(a**2)*(r**2)))
    print(under_root_not_squared)
    if under_root_not_squared < 0:
        UnderRoot = -math.sqrt(-under_root_not_squared)
    else:
        UnderRoot = math.sqrt(under_root_not_squared)
    
    print("UnderRoot: ", UnderRoot)
    #getting math domain error here for the above equation
    root2 = ((-b - r*a + UnderRoot)/(2*a))
    root3 = ((-b - r*a - UnderRoot)/(2*a))
    
    # root1 = root1.real
    # root2 = root2.real
    # root3 = root3.real
    
    
    print(root2)
    print(root3)
    
    return root1, root2, root3
    
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
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

testFindIntRootsOfCubicCase()

def testBonusFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed.')

testBonusFindIntRootsOfCubic()