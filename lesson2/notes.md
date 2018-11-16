# Lesson 2
## "for loops"

### Briefly explain the meaning of each value m, n, and k in the expression range(m, n, k).

	The numbers range from m to n, skipping by k. For example, range(0,10,3) = 0 + 3 + 6 + 9, where the series starts from 0 and each number is added by k, as long as they are less than n. 


## "nested for loops"

### In the first example in this section, why do we use end="" in the inner print statement, but not in the outer print statement?

	We use end=“” in the inner print statement but not in the outer print statement because we want the code to print out the coordinates in one line for only the inner print material. This keeps all the rows organized such that each row consists of points with the same x-coordinate. 

### What is the mystery star shape?

	It is a square star, represented as one object that we can repeat and display however we wish with the help of code. 

### Modify the code for the mystery star shape so that it prints the same shape, only upside down (so the last row becomes the first row, and so on).  Include your code here.

	def printMysteryStarShape(n):
    		for row in range(n):
        		print(row, end=" ")
        		for col in range(n - row):
            			print("*", end=" ")
        		print()

	printMysteryStarShape(5)

## "while loops"

### When in general would you prefer a "while" loop to a "for" loop?

	When you do not know how many iterations you will make or how many times you will go through the loop, it is better to use while loops.

### Why do we need to use a while loop in the leftmostDigit example?

	We need to use a while loop in the leftmostDigit example because we do not know how many digits the number inputted will have, and to find the left most digit, we need to keep integer-dividing by 10 until we are left with just the left most digit.

### What is the bug in the buggySumToN example?

	Counter is set to a value before total += counter is called.

## "break and continue" video:

### What precisely does a break statement do?

	Ends the loop when passed.

### What precisely does a continue statement do?

	Ends the pass to the loop that it is on but goes back to the top of the loop to start the next pass.

## "isPrime"

### What would go wrong if we omitted the if statement at the start of isPrime?

	We would get 0 and 1 as prime numbers, which would be a logical error since they are not prime numbers. We would also get True for n<2.

### What is it that makes fasterIsPrime so much faster than isPrime?  (Hint: it's not the bit about evens and odds (that helps, but not nearly so much as something else.))

	Only going up to the square root makes fasterIsPrime faster because if we have not found a factor up to the square root, there must not be a factor.

## "nthPrime"

### In addition to its parameter n, nthPrime uses two local variables -- found and guess.  What precisely do each of these values mean here?

	Guess is a counter, and found is the number we need to find.	

### Why does nthPrime use a while loop instead of a for loop?

	nthPrime uses a while loop because because it is an indeterminate range. We do not know how many numbers we need to check.

## Practice

### Why do we use roundHalfUp instead of Python’s builtin round function? How do they differ from the int function? 

Python’s round function rounds very inconsistently (always rounds to the nearest even). It rounds some floats up and some down. This is why we must write our own function : roundHalfUp because it is consistent and works well, by rounding to the nearest integer.  The int function differs from these two because it does not round the number; it simple removes the float (decimal) portion of the number, leaving just the integer part of it. 

### What is a potential danger of using global variables?

If two functions use the same global, they will conflict with each other and even accidentally modify variables for the other function.

### Write a one-line example of short circuit evaluation.

Red == True or Yellow == False

3 or 0

### Code Tracing

#### 1. 
```
def ct1(x, y, z):
	print(y ** x - x * z + y // x)
	y += max(x,y,z) // min(x,y,z)
	z %= x
	return	(100*y	+ 10*x	+ z)

print(ct1(2, 3, 5))
```

Scratch                            console
9 - 10 + 1 =                       0
y (new) = 5//2 + 3 = 5
z = 1			
100*5 + 10*2 + 1 	     521

#### 2.
```
def f(x): return 3*x +1
def g(x): return min(x//10%10, x%10)
def h(x):
	if (x > 0): return g(x) + g(f(x))
	else: return g(max(2, f(abs(x))))
def ct2(x):
	print(h(x))
	print(h(x+5))
print(ct2(4)) 
```

Scratch                             		 console
x = 4         			
g(4) = min(4//10%10, 4%10)		                0
f(4) = 13				                        13
g(f(4))= min(1, 3)			                    1
h(4)					                        14
					                            None
h(4+5)= h(9)
g(9) = min(0, 9)			                    0
f(9) = 27+1				                        28
h(9)					                        28
					                            28	



x = 4
	h (4)
		g(4) + g(f(4)) = min(0,4) + min(1,3)
				= 0 + 1
				=1
	h (4 - 5) = h (-1)
		g(max(2, f (abs(-1)) )) = 0
			g(max(2,4))
			min (0,4) = 0
1
0
None
		



### Reasoning Over Code

#### Find an argument for the following function that makes it return True.
```
def rc(n,m):
    if((not isinstance(n,int) or not isinstance(m, int)):
        return False
    if(m < 100 or m>999 or n < 10 or n > 99):
        return False

    a = n%10

    b = m%100
    c = m//100

    return ((a == b + 1) and (almostEqual(a**2 + b**2, c**2)))
```
m and n are integers
m is between 100 and 999
n is between 10 and 99

a is the ones digit for n
b is the last two digits of m
c is the first digit of m

Pythogoreon triple, because a**2 + b**2 = c**2
Maybe a = 4 and b = 3 and c = 5
n = 84
m = 503

So rc(84, 503)

### Free Response 
####  Write the function isAlmostSquare(n) that takes any Python value and returns True if it is an int within 2 (inclusive) of a perfect square, and False otherwise. For example, since 25 is a perfect square (5**2), the function returns False if n is 22, True if n is 23, 24, 25, 26 or 27, and False if n is 28. It also returns False (without crashing) if n is 25.0 or "25", as those are not ints.
```
def almostEqual(d1, d2, epsilon = 10**-7)
	return (abs(d2-d1) < epsilon)

def isAlmostSquare(n):
	if almostEqual(n, int(n)) and n**(1/2) == int:
		return True
	elif (n+1)**(1/2) == int or (n+2)**(1/2) == int or (n-1)**(1/2) == int or (n-2)**(1/2) == int:
		return True
	else:
		return False

import math

def isAlmostSquare(n):
	if not isinstance(n, int): return False
	if n < 0: return False
	root = math.sqrt(n)
	low = int(root)
	high = roundHalfUp(root+0.5) # or use int(root+1)
	low = low**2
	high = high**2
	

```






2. A lattice point is a point (x,y) where x and y are both integers. So (1, 1) and (83, 72) are lattice points, but (1.5, 2) is not. With this in mind, write the function nearestLatticePointDistance(x, y), which you may abbreviate NLPD(x,y), which takes two floats x and y, and returns the distance to the nearest lattice point, rounded to the nearest 1/10th.

def RoundbyTenth(n):
#rounds to the nearest lattice
    if n - int(n) < 0.5:
        return int(n)
    elif n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return n

#use round(n, 1)

#takes two floats x and y, and returns the distance to the nearest lattice point, rounded to the nearest 1/10th.
def NLPD(x,y):
    distance = abs(y - x)
    return RoundbyTenth(distance)

#correct answer

Def NLP(x,y):
	newX = roundHalfUp(x)
	newY = roundHalfUp(y)
	dist = distance(x,y,newX,newY)

Def distance(x1,y1,x2,y2):

That's it for lesson 2!  Carpe diem!

