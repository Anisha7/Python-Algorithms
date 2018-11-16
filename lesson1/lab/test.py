import math



def nearlyEqual(x,y):
    epsilon = 10** -7
    return (abs(x-y)<epsilon)

def isPerfectSquare(n):
    
    if n==0 or n==1:
        return True
        
    # 
    if not isinstance(n, int):
        return False
        
    # negative
    if n<0:
        return False
    
    if nearlyEqual(math.sqrt(n) % 1, int):
    #if isinstance(math.sqrt(n) % 1,int):
        return True
        
    else:
        return False



def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True) #Test failing because function tests 4.0 for int
    assert(isPerfectSquare(1234**2) == True) #Test failing again because of the ".0"
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    
    print('Passed.')
    
testIsPerfectSquare()