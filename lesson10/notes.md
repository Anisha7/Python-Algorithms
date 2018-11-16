# lesson 10

## OOP Part 2

### What is the difference between a superclass and a subclass?

	A subclass can use methods from superclass but superclass cannot use methods from a subclass.

### What does super().__init__(x) do?

	It will treat self of the subclass as if it was in the superclass. So, we will be able to use the init specified in the superclass and add subclass specific init as well.

### Using the code from 1.3, add two new lines that print type(b) == object and isinstance(b, object). What are the results? Why do you think you got these results?
```
	print(type(b) == object) # prints False
	print(isinstance(b, object)) # prints True
```
	isinstance checks for all levels (whether it is in the superclass), whereas type only checks inside the subclass.

### Give an example of a case where you might want to use a class attribute and a case where you might want to use a static method.

	We could use a class attribute for a game where all players have the same moves, so they can all be allocated the same list of moves.
	We could use a static method when different classes use the same method, and to prevent polluting the namespace, such that we could have more than one f(x), for different classes. Perhaps when calculating prices for different items with different discounts, so classes could specify different discounts and f(x) calculates the discounted price.

### Section 4 demonstrates how you can access the properties of an instance with __dict__. Write a line of code that assigns a new property to an instance of A using __dict__.

	a.__dict__['y'] = 50

### What core method needed to be added to make MovingDot move?

	step method, which adds a value to the x. 

### Let's say we want to change our code to make the dots squares instead of circles. Where in the code should we make this modification?

	In the draw function for the superclass if we want all the circles to be squares, or in the subclass if it is for specific subclass circles.

### Why is it a bad idea to check if drawnCard.suit == 1?

	We don't know for sure that there was only 1 diamond or if there were more than 1. 

Carpe Diem!

