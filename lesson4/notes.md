# Lesson 4
## Graphics

### How would you modify the provided code to make a 400x800 window?

	runDrawing(400, 800)

### What do the four main variables in create_rectangle represent?

	x1,	y1,	x2,	y2
	left, 	top,   	right, 	bottom

### How do you get rid of the rectangle's outline?

	Set outline’s width to 0. 

### Why do we use rectWidth/2 and rectHeight/2 instead of rectWidth and rectHeight when drawing the inner rectangle?

	Because the edges are determined from the center point for the smaller rectangle, which is half the big rectangle. 

### Find the RGB values for your favorite color on http://www.rapidtables.com/web/color/RGB_Color.htm and write a line of code to generate a rectangle in that color. Paste your code here.
```
	def rgbString(red, green, blue):
    		return "#%02x%02x%02x" % (red, green, blue)

	def draw(canvas, width, height):
    		lightSkyBlue = rgbString(135,206,250)
    		pistachio = rgbString(147, 197, 114)
    		maroon = rgbString(176, 48, 96)
    		canvas.create_rectangle(0, 0, width/2, height/2, fill=lightSkyBlue)
    		canvas.create_rectangle(width/2, height/2, width, height, fill=lightSkyBlue)
```    

### How did we change the position of the 'Carpe Diem!' text without changing the given x and y values?

	By changing the anchor to the direction for text location.

### Why did we use x1 instead of x0 + width*3/3 for the third stripe of the flag?

	Because x1 in that case is the right most edge, and will be equal to x0 + width*3/3, since it is the right-most rectangle.

### Why do we use cy - r*sin(angle) when rotating around the circle?

	In order to go up on the screen, we need to subtract from the center point for it to rotate clockwise. 
		

### Note the current time, then add a call to drawClock into draw that displays that time. Then trace through the code by hand. Make sure you understand how the minute and hour hands were generated in the correct positions. Include your new line of code below.

```
	drawClock(canvas, 25, 25, 175, 150, 12, 31)
```

## 1d Lists and Tuples

### Why is type([1,3,5,7]) == type(["a", "b", "c", "d"]) True?

	It is true because they are both lists.

### What do you think a[:2] is, if a = [2, 3, 5, 7, 11, 13]? Check to see if you're right after making a prediction.

	a[:2] = [2, 3]

### What problems could arise in your code due to function parameters being aliases?

	The same list could be modified, where the expected result would be two lists with different modifications, but aliases would cause the same list to have both modifications.

### Why should you check (if value in a) before calling a.index(value)?

	To prevent it from crashing. If the value is not in a, asking for the index of that value will cause it to crash.

### If a = [2, 3, 4, 5], what happens when you run a.insert(1, 42)?

	It would insert 42 at index of 1 in list a.

### What happens if you call .pop() on an empty list?

	There is a “pop index out of range” error.

### We demonstrated two correct ways to swap elements in a list. Which do you think is clearer?

	Parallel assignment is clearer, in my opinion, because it is more straightforward and less messy.

### Why is it a bad idea to modify a list while looping through it?

	It will crash because the index would be out of range.

### Is [] < [0]? Why or why not?

	Yes, because [0] has more elements than [].

### We demonstrated multiple ways to make a non-aliased copy of a. Which one do you think is best and why?

	copy is a better method than aliasing because copying actually creates a separate string, whereas alias assigns the same string to two variables. So, if we change a copied string, only that string will change, but if we change an aliased string, both the strings will change.

### Write a line of code that sorts a list of strings based on the length of the strings.
```
	list = [“string”, “string1”, “string2”]
	
	for string in list:
		for num in range(len(string)):
			string = sorted(string)
	return list
```

### Why do some list functions not use return statements?

	Destructive modifications do not return anything.

### How are tuples different from lists?

	Tuples are immutable, unlike lists.

### Write a list comprehension that has the same result as the following code:
```
	lst = []
	for i in range(10):
    		lst.append(i * 3)

	lst = [i for i in range(10)]
	lst.append(i*3)
```

### We can change the delimiter (the text that separates values) in a piece of text using a combination of split and join. Write a line of code that change's the delimiter of the string s from "\t" to ",".
```
	s = s.split(“\t”)
	print(s.join(“,”))
```

That's it!  Carpe diem!
