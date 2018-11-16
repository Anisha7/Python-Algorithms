def almostEqual(d1, d2, epsilon = 10**-7):
	return (abs(d2-d1) < epsilon)

def isAlmostSquare(n):
    print("testing")
	if almostEqual(n, int(n)) and almostEqual(n**0.5, int):
		return True
	elif (n+1)**(1/2) == int or (n+2)**(1/2) == int or (n-1)**(1/2) == int or (n-2)**(1/2) == int:
		return True
	else:
		return False
	

#isAlmostSquare(4)

def RoundbyTenth(n):
    if n - int(n) < 0.5:
        return int(n)
    elif n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return n
#takes two floats x and y, and returns the distance to the nearest lattice point, rounded to the nearest 1/10th.
def NLPD(x,y):
    #Test if lattice point: works. Write actual function.
    # if x == int(x) and y == int(y):
    #     return True
    # else:
    #     return False
        
    distance = abs(y - x)
    
    return RoundbyTenth(distance)

def NLPDtest():
    #used only to check for lattice point
    #commented code
    print("Testing NLPD...")
    assert(NLPD(2,5) == True)
    assert(NLPD(2.5,9) == False)
    print("done")
#NLPDtest()

def rc(n,m):
    if(not isinstance(n,int) or not isinstance(m, int)):
        print("not int")
        return False
    if(m < 100 or m>999 or n < 10 or n > 99):
        print("use different m,n")
        return False

    a = n%10

    b = m%100
    c = m//100

    return ((a == b + 1) and (almostEqual(a**2 + b**2, c**2)))

rc(20, 200)

def f(x): return 3*x +1
def g(x): return min(x//10%10, x%10)
def h(x):
	if (x > 0): return g(x) + g(f(x))
	else: return g(max(2, f(abs(x))))
def ct2(x):
	print(h(x))
print(h(x+5))
print(ct2(4)) 
