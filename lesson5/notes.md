# lesson 5
## 2d Lists

### Describe why "[ [0] * cols ] * rows" is not a good way to allocate a 2d list.

	It creates aliases of all the sub lists inside the list, and modifies all of them when any later change is made.

### if a = [ [ 1, 2, 3 ] , [ 4, 5, 6] ] what is len(a)? len(a[1])?

	len(a) = 2
	len(a[1]) = 3

### Why do we use two loops (nested) in order to iterate through a 2d list? (As opposed to one loop.)

	A single loop would only range over each list element in the list, but not get the values for each element inside those  list elements in the list.

### In the context of a 2d list, describe the difference between a shallow copy and a deep copy.  What is a situation where deep copy still isn't good enough?

	A shallow copy (copy.copy(list)) causes aliasing for sub elements in 2d lists.
	A deep copy (copy.deepcopy(list)) gives a deep copy for each level of the list without aliasing. Deep copy preserves aliases, though, if the original list was aliased.

### Why did we write a custom version of print2dList(a) instead of just calling print(a)?

	It’s a nicer, cleaner way to print lists for easier debugging such that the columns align with nice spacing.

### Why does accessing a whole column require a loop, but accessing a whole row does not?

	Rows are default stored, so they can be grabbed but columns need to be built so, it requires a loop. 

### if a = [ [ 1, 2 ] , [ 4, 5, 6], [7, 8, 9, 10] ] what is len(a)? len(a[2])?
```
	len(a) = 3
	len(a[2]) = 4
```
### Describe a problem scenario that a 3d list would help you solve.

	For the shape of each piece of Tetris, since the shape of each piece would be a 2d list, and the 3d list would be a list of those 2d lists.

## Practice
### Graphics and 1D List Practice 

### Why is it a bad idea to modify a list while looping through it?
It modifies the original list, which changes the range of the list, and thus crashes the loop. especially in a for loop.  

### What is aliasing?
Aliasing is when different variables point to the same list. When this happens, modifying either of those lists changes both of them.

###	Give an example of a list comprehension.
```[ i for i in range(10)] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]```

### Assuming canvas already exists, write one line of code that draws a circle in the canvas, centered at (50,100), with radius 20.

    ```canvas.create_oval( x - r, y - r, x + r, y + r )```

### Code Tracing
```
def ct(a):
    b = copy.copy(a)
    c = a[0:len(a)]
    d = a
    a[0] += 1
    b[0] += 2
    c[0] = 3
    d.append(4)
    a = c
    a += [5]
    print(a, b, c, d)
a = [5]
ct(a)
print(a)
```

### Reasoning Over Code
```
def rc(L):
    if (not isinstance(L,list)): return False
    result = []
    while (L != []):
        result.extend([L.pop(),L.pop(0)])
        L = L[1:-1]
    return (result == list(range(2,6)))

```

### Mystery Function
```
def mystery(a):
    # assume a is a list
    b = [ ]
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if ((a[i] == a[j]) and (a[i] not in b)):
                b.append(a[i])
    return b
```
Removes repeating chars in a, giving a list of all chars in a that occur once


### Free Response

###Write the function drawCheckerboard that takes a canvas and 4 positive integers -- width, height, rows, cols -- and draws a rows x cols black-and-white checkerboard into the width x height canvas. The left-top corner cell must be black, and then cells alternate from there. Here, for example, is a 3x4 checkerboard:

###Your checkerboard must entirely fill the canvas, and the cells must be the same size as each other, so they might not be square.



# input: canvas, width, height, rows, cols
# output: black and white checkerboard of rows x cols (left-top cell black.)
```
Def drawCheckerboard():

	cellWidth = width/cols
	cellHeight = height/rows

	for row in range(rows):
		for col in range(cols):

			x0 = cellWidth*col
			y0 = cellHeight*row
			x1 = x0 + cellWidth
			y1 = y0 + cellHeight

			if (row + col) % 2 == 0:
				fill = “black” 
 			else: 
				fill = “white”

			canvas.create_rectangle(x0, y0, x1, y1, fill = fill)

```

###Extra Problem: Free Response
###Write the function repeatingPattern(a) that takes a list a and returns True if a == b*k for some list b and some value k>1, and False otherwise. 
###For example, repeatingPattern([1,2,3,1,2,3]) returns True (b==[1,2,3] and k=2).

```
Def repeatingPattern(a):
	# find pattern

	pattern = []
	for i in range(len(a)):

		if a[i] not in pattern:
			pattern += [a[i]]

		elif a[0] == a[i]:
			break
	
	# check segments

	if len(a) % len(pattern) != 0:
		return False

	while (i < len(a)):

		nextSeg = a[i:i+len(pattern)]

		if pattern != nextSeg:
			return False

		i += len(pattern)

	return True
```

That's it!  Carpe diem!
