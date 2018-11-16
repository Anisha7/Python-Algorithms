# lesson 8

##Object-Oriented Programming Questions:

### What is the different between an instance and a class?

	Class is the type of an instance. 

### Why doesn't our code crash when we call A('yellow', True), even though our __init__ function has three parameters?

	Self is an instance. It does not need to be entered, as it is used to store/change values in that instance. 

### Why should we write __repr__ instead of __str__ in most cases?

	Because python uses __repr__ instead of __str__ if __repr__ is defined and __str__ isn't, and it is also computer readable.

### Write a one-line __hash__ method for a class, Book, which has two variables, title and author.
```
    class Book(object):
	def __hash__(self):
		return hash ((self.title, self.author))
```

## Recursion:

### Pick an example from the 'Popular Recursion' section and explain why it is recursive.

	The Droste Effect is recursive because the lady holding tray has a box with an image of that lady holding that tray and so on. It is recursive. 

### Why do all (non-infinite) recursive functions need to have a base case?

	The base case gives at least one situation where the function will not be recursive, such that the function will not be infinitely recursive, since that would crash with stack overflow. 

### In 'Recursive Math', what's the functional difference between the function f5 and the function f7?

	f5: As x increases, the change between the numbers in list also increases. (Triangular Numbers, quadratic function)
	f7: Multiplying instead of adding, so it gives the powers of 2. 

### Why is the base case for the recursive function power different from the base cases of rangeSum and listSum?

	It is different because we would get the same result (1) if we use a power of 0. For sum or range, we can start at 0, since that will not effect the future results in the way it would for power function.

### Add a print statement to the top of the basic rangeSum and the divide-and-conquer rangeSum, and count how many times each function is called on the same input. Describe what you observe and do your best to explain it.

	basic: It ran 7 times until it hit the base, where recursion stops.

	divide-and-conquer: It ran 11 times until it hit the base, where recursion stops.

	The basic ran less times because it compares when the lo is more than high, instead of equality, which took longer to meet. 

### Section 9 shows how functions can be implemented in both iterative and recursive ways. Of course, there can be multiple different iterative and recursive approaches to solve a problem. Describe two approaches, one iterative and one recursive, which you could use to solve the second example, reverse. These approaches should be different than the ones shown on the website.

	Iterative: 
    ```
    def reverse(s):
		return s[::-1]
    ```

	Recursive: 
    ```
    def reverse(s):
        new = ""
        
        if s = "":
            return new
        else:
            new = new + s[-1]
            s.pop(-1)
            return new
    ```

Carpe Diem!
				
