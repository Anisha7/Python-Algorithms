#################################################
# Lab3
# Anisha Jain - anishaj
# Team: Zhenyan - zhenyanw
#################################################

'''
Better Big Oh:

1.
    Original:
    def slow1(a):
        (b, c) = (copy.copy(a), 0) # O(1)
        while (b != [ ]): # O(N)
            b.pop() # O(1)
            c += 1 # O(1)
        return c # O(1)
    
    1. This function counts how many elements are in a list a.
    
    2. The worst-case big-oh runtime is O(N) because the while 
        loop runs N times where N is the len(a).
        
    3. Improved:
        def fast1(a):
            return len(a) 
    
    4. The big O of this function is O(1) since the len(a) function  
        does not need to iterate over the list to get the length. 
        It is a known value to the python list, and it returns that
        value in O(1) time.
    
2. 
    Original:
    def slow2(a):
        n = len(a) # O(1)
        count = 0 
        for i in range(n): # O(N**2)
            for j in range(n): # O(N)
                if (a[i] == a[j]): O(1)
                    count += 1
        return (count == n)
        
    1. It checks for repeating digits in a list a. If the number 
        has no repeating digits, it returns true. 
        If it does, then it returns false.
    
    2. The worst-case big-oh runtime is O(N**2) because there
        is a for loop of length N inside of another for loop
        of length N.
    
    3. def fast2(a):
            l = copy.copy(a)
        
            for i in range(len(a)):
                l = l[0: i] + l[i+1:]
                s = set(l)
                if a[i] in s:
                    return False
                
            return True
    4. The big O of this function is O(N) since it loops 
        through the length of a once.
    
3. 
    Original:
    def slow3(a, b):
        # assume a and b are the same length n
        n = len(a) # O(1)
        assert(n == len(b)) # O(1)
        result = 0 
        for c in b: # O(N**2)
            if c not in a: # O(N)
                result += 1
        return result 
        
    1. This code checks for the number of uncommon digits a and b contain.
    
    2. O(N**2) because it has to loop through the length of b for
        the length of a
    
    3. def fast3(a, b):
            n = len(a)
            assert(n == len(b))
            count = 0
            
            s = set(b)
            
            for i in range(n):
                if not a[i] in b:
                    count += 1
            
            return count
            
    4. The big O of this function is O(N) because it loops through
        the length of a once. 
            
            
    
4. 
    Original:
    def slow4(a, b):
        # assume a and b are the same length n
        n = len(a) # O(1)
        assert(n == len(b)) # O(1)
        result = abs(a[0] - b[0]) # O(1)
        
        for c in a: # O(N) times O(N) = O(N**2)
            for d in b: # O(N)
                delta = abs(c - d) # O(1)
                if (delta > result): # O(1)
                    result = delta
        return result
        
    1. This function finds the largest possible difference 
        that can be calculated using one digits from the list a 
        and one digit from b.
    
    2. O(N**2) because it has to loop through the each digit in b 
        for each digit in a
    
    3. def fast4(a,b):
        assert(n == len(b)) # O(1)
        mergeSort(a) # NlogN
        mergeSort(b) # NlogN
        
        if a[len(a) - 1] > b[len(b) - 1]: # 1
            return abs(a[len(a) - 1] - b[0])
            
        elif a[len(a) - 1] < b[len(b) - 1] # 1
            return abs(b[len(b) - 1] - a[0])
        
        # big O of NlogN
    4. The big O of this function is O(NlogN) because mergeSort takes nlogn 
        to complete and the rest of the tasks take only O(1) and thus, do not 
        significantly affect the efficiency of the function.
    
5. 
    Original:
    def slow5(a, b):
        n = len(a)
        assert(n == len(b))
        result = abs(a[0] - b[0])
        
        for c in a:
            for d in b:
                delta = abs(c - d)
                
                if (delta < result):
                    result = delta
                    
        return result
        
    1. This function finds the smallest possible difference 
        that can be calculated using one digits from the list a 
        and one digit from b.
    
    2. O(N**2) because it has to loop through the each digit in b 
        for each digit in a
    
    3. def fast5(a,b):
            mergeSort(a) # NlogN
            smallestDiff = 100
            diff = 0
            
            for num in a: # N
                bIndex = bisect.bisect(b, a)
                diff = abs(num - b[bIndex])
                
                if diff < smallestDiff:
                    smallestDiff = diff
            
            return smallestDiff
            
    4. The big O of this function is O(N) because N > NlogN, and it is
        looping through the length of N once. 
                
    
'''

#################################################

import cs112_f17_week7_linter
import math
import bisect

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

# mergeSort from notes
# sorts list a in ascending order
def merge(a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
    for i in range(length):
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
        a[i] = aux[i - start1]

def mergeSort(a):
    n = len(a)
    step = 1
    while (step < n):
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            merge(a, start1, start2, end)
        step *= 2
        
######################################################################
# Functions
######################################################################

# input: list of integers
# output: largest sum of any two elements in that list 
# returns non if length of list is smaller than 1

def largestSumOfPairs(a):
    #print("a: ", a)
    #print(len(a))
    if len(a) > 1:

        mergeSort(a)
        #print("a: ",a)
        return a[len(a)-1] + a[len(a) - 2]
        
    return None

# input: list of positive integers
# output: True if any three values form a Pythagorean Triple
# # a**2 + b**2 == c**2
def containsPythagoreanTriple(a):
    mergeSort(a) # NlogN
    # sorted list a = [2, 6, 7, 8, 14, 15, 17]
    
    
    #print(a)
    squaresList = []
    
    for i in range(len(a)): # N
        squaresList += [int(a[i]**2)]
    #print(squaresList)
    
    # check if sum of any two nums in squaresList is in squaresList
    i = 0
    s = set(squaresList)
    for b in squaresList:
        j = len(squaresList) - 1
        
        while i < j:
            
            if squaresList[i] + squaresList[j] in s:
                return True

            j -= 1
        i += 1
        
    return False
    

        

#################################################
# Test Functions
#################################################

def testLargestSumOfPairs():
    print("testing largestSumOfPairs()...", end="")
    assert(largestSumOfPairs([9,2,4,6]) == 15)
    assert(largestSumOfPairs([0,62,10,1]) == 72)
    assert(largestSumOfPairs([1,2]) == 3)
    assert(largestSumOfPairs([]) == None)
    print("Passed")
    
def testContainsPythagoreanTriple():
    print("testing containsPythagoreanTriple()...", end="")
    assert(containsPythagoreanTriple([1,3,6,2,5,1,4]) == True)
    assert(containsPythagoreanTriple([1,7,1,2,25,1,24]) == True)
    assert(containsPythagoreanTriple([1,3,3]) == False)
    print("Passed")
    pass

#################################################
# testAll and main
#################################################

def testAll():
    testLargestSumOfPairs()
    testContainsPythagoreanTriple()

def main():
    cs112_f17_week7_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
