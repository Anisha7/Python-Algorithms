# Lesson 1
## Strings

### Why is len('a\nb') equal to 3 and not 4?

	‘\n’ is a single new-line character, so it counts as 1 addition to the length, not two.

### List a character that is easier to include in a string delimited by double-quotes rather than single-quotes.

	“”“String
	String”””

### List each escape sequence and what they mean.

	“String ‘string’”
	‘String “String” \’string\’!’

### What is type(string.digits)?  Why?

	There is no type. It gives a NameError.

### For any string s where len(s)>1, is it definitely true that ((s[1:] in s) == True)?

	Yes

### What is the empty string?  What is its type?  What is its length?
	
	An empty string is a string with no characters in it. 	

### What is "abcde"[-1]?
	
	e

### What is 'abcde'[-1][-1]?  Briefly explain why that works, but 'abcde'[1][1] crashes.

	e. [1][1] crashes because that index is out of range. It does not exist.

### Briefly, why did we write the function reverseString in the video, rather than just using s[::-1] in our code?

	They don’t read cleanly. The function is clearer.

### Briefly, what is the difference between split and splitlines?

	Split splits the individual characters or sets of data from a list and split lines splits a line of data from a list of lines of data.

### What does it mean that Strings are immutable?

	Unchangeable strings. You cannot modify the string object.

### What is the difference between a string method and a string function?

	The string function str converts another character to a string, whereas the string method takes in strings.

### What is the difference between chr and ord?

	ord gives the integer order of the entered string. Chr gives the string based on the integer order entered.

### What is the difference between lower and islower?

	Lower converts the string to lower case. Checks if a character is in lower case.

### How do you left-align text using the string formatting operator?

	 Use negative field width for left-align:
		print(“%-10s %-10s” % (“something”, “something”))

### Why would a Basic File IO crash if you run it in the browser?

	It would crash if I don’t have the file to open.

## Practice

### Briefly explain what break and continue do. 

Break stops the function from running further. Continue tells the function to stop here but go back to loop through the function again.

### Name one situation in which you would use a for loop vs a while loop.

If I know the length of how long I want to iterate, I would use a for loop. If I don't know the length, I would use a while loop. Ex. For adding all the elements in a list of integers, I would use a for loop since I know the length of the list.

### What happens when the bounds of a for loop look like this: “for i in range(5,3)”?
	It would just skip the loop and move on. 
 
## Code Tracing
### 1
```
def	ct1(x, y):
	for z	in range(y, x):
		print(42, z, end=’ ')
	for z	in range(x, y):
		if(z < y//2):
		    if (z%2 == 0): print(2, z, end=' ')
		    elif (z%5 == 0): print(5, z, end=' ')
		elif	(x+y+z == 27):
			print(27, z, end=' ')
	w = 0
	for z	in range(x, 10*x, x):
		if (z	< 5*x): continue
		elif (z >= 7*x): return w
		w += z
	return 99
print(ct1(3, 12)) #prints 5 values
```


### 2
```
def g(z):
    for x in range(1,z,3):
       print("#", x, ":", end = “”)
       for y in range(z, x, -2):
           return (x,y)
       print()
g(6)
```

## Reasoning Over Code
### 1
```
def g(z):    
    assert((type(z) == int) and (100 > z > 0))    
    step = total = 0    
    while (total < 25):       
        step += 1        
    for y in range(1,6,step):           
        total += y  
    return (step == z)
```
Z is an int between 0 and 100

Total : 0. 1. 4. 12. 12. 
Step: 1. 2. 5. 13. 14.
Y = 1. 3. 8. 

z= 13?


## Free Response 1

###A number n is a stepping number (a coined term) if it is a non-negative int and its digits are strictly increasing from left to right. For example, 1379 is a stepping number because 1 < 3 < 7 < 9, but 13379 is not because 3 is not strictly greater than 3. Note that a one-digit number is always a stepping number. With this in mind, write the function nthSteppingNumber(n) that takes a possibly-negative int n and returns the nth stepping number. 

###Here are a couple test cases: 
```
assert(nthSteppingNumber(0) == 0) 
assert(nthSteppingNumber(10) == 12) assert(nthSteppingNumber(433) == 145679)
```

```
def isSteppingNumber (n) :
	#strictly decreasing from r to l
	prevDigit = None
	while (n > 0): #go through all the digits
		currDigit = n % 10
		if( prevDigit == None ) :
			prevDigit = currDigit
		elif (currDigit >= prevDigit):
			return False
		else:
			prevDigit = currDigit


def nthSteppingNumber (n) :

	count = 0 #how many stepping numbers we’ve found
	guess = 0 #0, 1, 2 , 3 potential candidates for stepping
	
	while(count <= n):
		guess += 1
		if ( isSteppingNumber (guess) ):
			count += 1
	return guess






	length = getNumberLength (n)
	
	for i in range(1, length):
		num = getKthDigit(n, i)
		nextNum = getKthDigit(n, i+1)
		if num == nextNum:
			return False
		if num > nextNum:
			return False

	return True

```


## Free Response 2

###Say that the 'oddest' digit of a number (a coined term) is the odd digit that occurs the most in that number, with ties going to the larger digit, or 0 if the number has no odd digits. For example, the oddest digit of 123454321 is 3. Similarly, the oddest digit of -123123 is also 3. With this in mind, write the function sameOddestDigit(m, n) that takes two possibly-negative int values and returns True if they have the same oddest digit and False otherwise. So:
```
sameOddestDigit(123454321, -123123) == True sameOddestDigit(123454321, -123122) == False sameOddestDigit(2468, 24689) == False 
sameOddestDigit(2468, 20000) == True 
```
###Hint: You may want to write one or two well-chosen helper functions.

```
def sameOddestDigit (n, m):
	#return true or false
	#finds oddest digit
	#digit count
	return oddestDigit (n) == oddestDigit (m)

def oddestDigit (n):
	n = abs(n)
	oddestDigit = 0
	bestCount = 0
	
	for i in range (1, 10, 2) :
		count = digitCount (n , 1)
		if count >= bestCount:
			oddestDigit = i
			bestCount = count
	return oddestDigit

def digitCount (n, digit):
	count = 0
	while (n>0):
		if n%10 == digit:
			count += 1
		n //= 10
	return count


	count = 0 #keeps track of repeating odd digits
	prevCount = 0 
	mLength = numberLength(m)
	nLength = numberLength(n)	

	for i in range(1, mLength):
		mdigit = getKthDigit (m, i)
		prevmDigit = getKthDigit (m, i+1)
		if mdigit == prevmDigit:
			count += 1


		for num in range  (1, nLength):
			ndigit = getKthDigit (n, num)
			if mdigit == ndigit:
				

```



That's it for lesson 2!  Carpe diem!
