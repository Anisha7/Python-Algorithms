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

That's it for lesson 2!  Carpe diem!

