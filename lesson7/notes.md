# lesson 7

## Sets:

### Briefly describe the difference between a set and a list.

	Sets are not ordered and so, they have no indexes. All the elements in a set are unique. Repeated elements are not included in the set. It tracks only one of each. Sets are also immutable, unlike lists, and lists cannot be in a set. Sets are also more efficient than lists.

### Why should you use s=set() to declare an empty set instead of s={}?

	You should use s = set() instead of s = {} for an empty set because s = {} is type dictionary, not set. If the {} has elements inside it, then it will be treated as a set, but not if it is empty.

### Describe a scenario where you think it would better to use a set than a list.  Why is it better in your scenario?

	When checking if an element is part of a certain set, looping through a set is much faster than looping through those elements in a list.

### Imagine I have two sets:  "animals" contains a list of animals in North America.  (For example: {"bear", "squirrel", "mouse", ...})  "pets" contains a list of pets in North American.  (For example: {"dog", "cat", "hamster",...}).  Give one line of python code to determine the animals in North America that are not pets.

	```pets.issuperset(animals)```


## Dictionary

### Briefly describe the difference between a dictionary and a list.

	A dictionary allows us to assign an element to another element, such as capitals for a state, or states for a city.

### Our examples in the videos aren't very practical.  (For example, why would "cow" be associated with 5?)  Given a practical example for a time you might want to use a dictionary.

	It would be useful to use a dictionary when assigning names to certain special mathematical formulas perhaps. So, if one enters the formula name, they would get the formula in return. 

### Why do keys need to be immutable, but values don't?

	Keys are hashed in sets, and mutable values are not hashable. It crashes the program. Values, however, are not hashed, so they can be mutable. 

### 'key in d' is used to determine if a key is in a dictionary.  Describe, at a high-level, how you could determine if a value is in a dictionary. 

	You could create a for loop to go through each key in the dictionary and get the value for each key and check if that value is equal to the value we are looking for. 

## Efficiency Questions:

### What is the big-O of 400n + 32nlogn + 2n**2 + 56?

	O(nlogn)

### Briefly described why we don't care about the constants when determining the big-O.

	The size of the input does not affect the amount of work the function does, thus constants do not matter when determining the big-O.

### When programming, why do we care if our algorithm is O(n**2) vs O(n)?

	We care for efficiency of the function. O(n**2) is greater than O(n), so O(n) is better. It tells us the amount of steps a function does with respect to the size of O(n**2) and O(n).

### What is the difference between code optimization and algorithmic optimization?

	Code optimization involves reducing the length of the code, whereas algorithmic optimization involves coming up with a shorter, faster, and more efficient way to write that function.

### What would be the big-O for this function (assuming that L and M are both lists of size N):
```
def func(L,M):
    for i in L:
        for j in M:
            if i == j:
                return True
```	
	big O is 2N for this case

### Other than the examples given in the video, what is another python list operation that is O(N)?  Describe, at a high-level, why the operation is O(N).  (You'll need to follow the link to a more complete list.)

	Copy is O(N) because in this case, the copied element will still be sized for N objects until another insertion is made. Thus, this particular step is O(n).

### isPrime() does not take a list as input.  How, then, can it have a O(N) runtime when the input isn't n elements?

	It can have O(N) because it is checking for n elements, by checking for all the factors of the input number.

### Assume that I want to search for an item in a sorted list L.  Is it more efficient to use linear search or binary search?  Why?

	Binary searches are more efficient because it uses a sorted list and looks for the middle element and compares it from the element in the middle, and if it is smaller, it looks at the first half of the elements. If not, it looks at the second half. It has to look at and compare to less elements. Thus, it is faster.

### What if L is an unsorted list?  Is it more efficient to use linear search or binary search?  Why?

	A linear search would be more efficient in this case because it is not unsorted, so the binary search would not work for this case.

### We know that the most efficient sorting algorithms are all O(nlogn).  But, imagine we have a list L that is "almost sorted", meaning that only one element of the list is out of place.  Describe an algorithm that is faster than O(nlogn) that you could use to sort this list. 

	selection sort is faster in this case because the list is already almost sorted and does not need to go through the longer process.

	
 Carpe diem!