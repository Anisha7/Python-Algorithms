#################################################
# Hw2
#################################################

import cs112_f17_week7_linter
import math
import time

#################################################
# Helper functions
#################################################

def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])
    
#################################################

# input: dictionary d that maps keys to values
# output: inverted d, that maps the values to keys
def invertDictionary(d):
    #print(d)
    
    invertedD = {}
    tupleList = []
    prevkey = ''
    
    for key in d:
        tupleList += [(d[key], key)]
       
    tupleList.sort()
    
    print("tL: ", tupleList)
    
    for tuple in tupleList:
        
        (key, value) = tuple
        #print(tuple)
        
        if key == prevkey:
            #print("key: ", key)
            #print(invertedD)
            if isinstance(invertedD[key], list):
                invertedD.update({key: invertedD[key] + [value]})
            else:  
                invertedD.update({key: [invertedD[key], value]})
            
        else:
            invertedD.update({key: value})
            #print("currInvertedD", invertedD)
            prevkey = key
            
    for key in invertedD:
        #print(key)
        if not isinstance(invertedD[key], list):
            invertedD.update({key: set({invertedD[key]})})
        elif isinstance(invertedD[key], list):
            s = set()
            for num in invertedD[key]:
                s.update({num})
            #print("s", s)
            invertedD.update({key: s})
            
    
    print("inD", invertedD)
    
    return invertedD
    
# input: d, a dictionary that maps people to their friends
# output: map people to their friends of friends
def friendsOfFriends(d):
    
    #fof = set()
    newD = {}
    
    for person in d:
        
        fofList = []
        f = d[person]
        print("f: ", f)
        
        for friend in f:
            fof = d[friend]
            print("fof: ", fof)
            
            for name in fof:
                if name != person:
                    if not (name in f):
                        fofList += [name]
            print("fofList: ", fofList)
        
        
        newD.update({person: set(fofList)})    
    print(newD)
    return newD
    
def instrumentedSelectionSort(a):
    n = len(a)
    comp = 0 # num of comparisons
    swaps = 0 #num of swaps
    time0 = time.time() # getting time
    
    for startIndex in range(n):
        minIndex = startIndex
        
        for i in range(startIndex+1, n):
            comp += 1
            if (a[i] < a[minIndex]):
                minIndex = i
                
        swap(a, startIndex, minIndex)
        swaps += 1
    time1 = time.time()
    timeT = time1 - time0
    print((comp, swaps, timeT))
    return (comp, swaps, timeT)

def  instrumentedBubbleSort(a):
    n = len(a)
    end = n
    swapped = True
    comp = 0 # num of comparisons
    swaps = 0 #num of swaps
    startTime = time.time() 
    # getting time
    
    while (swapped):
        swapped = False
        
        for i in range(1, end):
            comp += 1
            
            if (a[i-1] > a[i]):
                swap(a, i-1, i)
                swapped = True
                swaps += 1
                
        end -= 1
    
    time1 = time.time()
    timeT = time1 - startTime
    print((comp, swaps, timeT))
    return (comp, swaps, timeT)

def selectionSortVersusBubbleSortHelper():
    counta = 0
    countb = 0
    
    compCountA = 0
    compCountB = 0
    
    swapCountA = 0
    swapCountB = 0
    
    testList = [[4,2,10,9,5], [42,1,3,5], 
                [1,1,2,9,53], [15,2,10,91,15]]
    quadTest = False
    
    for a in testList:
        N = len(a)
        (compA, swapsA, timeA) = instrumentedSelectionSort(a)
        (compB, swapsB, timeB) = instrumentedBubbleSort(a)
        
        if timeA > timeB:
            countb += 1
        elif timeA < timeB:
            counta += 1
        if compA > compB:
            compCountB += 1
        elif compB > compA:
            compCountA += 1
        if swapsA > swapsB:
            swapCountB += 1
        elif swapsB > swapsA:
            swapCountA += 1
            
        # check logic. Are the functions O(N**2)?
        # says false. how to properly check?
        if timeA == N**2 and timeB == N**2:
            quadTest = True
            
    tuple = (counta, countb, compCountA, compCountB, swapCountA, \
    swapCountB, quadTest)
    return tuple
    
def selectionSortVersusBubbleSort():
    (counta, countb, compCountA, compCountB, swapCountA,\
     swapCountB, quadTest) = selectionSortVersusBubbleSortHelper()
    if quadTest == True:
        print("""InstrumentedBubbleSort() and instrumentedSelectionSort()
        are quadratic (O(n**2).""", end="")
    elif quadTest == False:
        print("""InstrumentedBubbleSort() and instrumentedSelectionSort()
        are not quadratic (O(n**2).""", end="")
        
    if counta > countb:
        print("""InstrumentedBubbleSort() runs faster than 
                instrumentedSelectionSort().""", end="")
    elif countb < counta:
        print("""InstrumentedSelectionSort() runs faster than 
                instrumentedBubbleSort().""", end="")
    
    if compCountA > compCountB:
        print("""InstrumentedBubbleSort() has lesser computations than 
                instrumentedSelectionSort().""", end="")
    elif compCountB > compCountA:
        print("""InstrumentedSelectionSort() has lesser computations than 
                instrumentedBubbleSort().""", end="")
    
    if swapCountA > swapCountB:
        print("""InstrumentedBubbleSort() has lesser swaps than 
                instrumentedSelectionSort().""", end="")
    elif swapCountB > swapCountA:
        print("""InstrumentedSelectionSort() has lesser swaps than 
                instrumentedBubbleSort().""", end="")
    


##### Bonus #####

def threeWayMergesort(L):
    pass
    
def keplerPolygons():
    pass


#################################################
# Test Functions
#################################################

def testInvertDictionary():
    print("Testing invertDictionary()...", end="")
    
    assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) == 
       {2:set([1]), 3:set([2,5]), 4:set([3])})
       
    assert(invertDictionary({1:2, 4:3, 2:3, 3:4, 5:3}) == 
       {2:set([1]), 3:set([2,5,4]), 4:set([3])})
       
    assert(invertDictionary({3:4, 8:2, 9:1, 52:1}) == 
       {4:set([3]), 2:set([8]), 1:set([9, 52])})
    
    print("Passed")
    
def testFriendsOfFriends():
    print("testing friendsOfFriends()...", end="")
    
    # test 1
    d = {}
    d["jon"] = set(["arya", "tyrion"])
    d["tyrion"] = set(["jon", "jaime", "pod"])
    d["arya"] = set(["jon"])
    d["jaime"] = set(["tyrion", "brienne"])
    d["brienne"] = set(["jaime", "pod"])
    d["pod"] = set(["tyrion", "brienne", "jaime"])
    d["ramsay"] = set()
    print(d)
    
    a = {
        'tyrion': {'arya', 'brienne'}, 
        'pod': {'jon'}, 
        'brienne': {'tyrion'}, 
        'arya': {'tyrion'}, 
        'jon': {'pod', 'jaime'}, 
        'jaime': {'pod', 'jon'}, 
        'ramsay': set()
        }
    assert(friendsOfFriends(d) == a)
    
    print("Passed")


#################################################
# testAll and main
#################################################

def testAll():
    testInvertDictionary()
    testFriendsOfFriends()

def main():
    cs112_f17_week7_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
