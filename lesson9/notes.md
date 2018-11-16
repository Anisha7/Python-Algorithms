# lesson 9
## Exceptions

### Consider the lastChar(s) function given on the notes page.  Write a simple try/except block that calls lastChar('') without the program crashing.
```
	try:
		print(lastChar(''))
	except:
		print("Empty String Not Acceptable")
```
## Functions Redux

### When using variable length args, why would you put a * in front of the argument when calling the function?

	The * tells python to package the input in a format that args can use. Args converts the input into a tuple, so if we don't use a *, in the case of inputs like lists, args would put the list inside the tuple, instead of its elements. 

### What is the problem with using a mutable default argument?

	It will alter the already existing list each time the function is called. So in a case where we alter an empty list, each time we add an item to the list (while calling the function separately), it will return the list with all the items added by all the function calls thus far.

### Look back at the animation framework used for this course.  Inside, we make use of lambda functions and functions as parameters.  Briefly describe how each is being used.

	When a button is pressed, mousePressedWrapper is called, since root.bind has "<Button-1>" as a parameter. It is called again for key and keyPressedWarapper, which does call keyPressedWrapper. This is done through the function bind in class root or Tk().

### What is the differences between making use of *args and **kwargs?

	It packages times into a dictionary instead of tuples.

### What is one reason you can think of to declare a function inside another function instead of making it global as we usually do?

	If it is a helper function fir that function specifically, but is not useful to any other functions, it can be declared inside that function for efficiency purposes.

### Describe, in your own words, what a function decorator does.  What is the relationship between function decorators and functions that return functions?

	Decorators make the function it is called on return the decorator function, taking in that function. This is what functions that return functions do as well, in a different format. 

## Recursion Part 2 Questions:

### Why would you need to expand the size of the stack?

	For recursive functions that need to deal with large numbers. 

### Why is the memoized version of fib so much faster than the regular version?

	It does not have to do the same work over and over again because the memoized version saves the work that the function had already done in a dictionary. 

### Which advanced worked examples (from 1-5) was the most interesting to you?  Why?

	I found the permutations example very interesting. I remember trying to use just for loops to get all possible permutations on older assignments, and this recursive solution was such nicer and neater.

### In your own words, describe what a fractal is.

	A fractal is a drawing that is drawn using recursion.

### What is another problem you can think of that you might be able to solve using backtracking?

	Getting shortest path in a map, or solving checkers.


Carpe Diem!
