#################################################
# Lab9
# Anisha Jain, anisha j
# Team: zhenyan, zhenyanw

# No iteration! no 'for' or 'while'.  Also, no 'zip' or 'join'.
# You may add optional parameters
# You may use wrapper functions
#
#################################################

import cs112_f17_week9_linter

def almostEqual(x, y, epsilon = 10**-8):
    return abs(x-y) < epsilon

##############################################
# Recursive questions
##############################################

# input: List (empty or with numbers)
# output: alternating sum, every other value subtracted
def alternatingSum(L):
    #print(L)
    if L == []:
        return 0
    elif len(L) == 1:
        return L[0]
    else:
        return L[0] - L[1] + alternatingSum(L[2:])

# input: pos or neg float or int n
# output: list of positive powers of 3 up to/including n
# output: None if no values exist
# powersOf3ToN(10.5) returns [1, 3, 9]
def powersOf3ToN(n, m = 0):
    n = int(n)
    L = []
    if n <= 0:
        L = None
        
    else:
        if 3**m <= n:
            #print("m: ", m)
            #print(3**m)
            if L != None:
                L = list([3**m]) + powersOf3ToN(n, m = m + 1)
    return L
        

# input: sorted list L, value v
# output: a list of tuples, (index, value), 
# of the values that binary search must check 
# to verify whether or not v is in L  
def binarySearchValues(L, v, i = 0):
    
    prevMid = len(L) - 1
    mid = (len(L) - 1) // 2

    print("mid: ",mid)
    
    if mid < 0:
        return []
        
    if L[mid] == v:
        return [(mid + i, L[mid])]
    
    else:

        if L[mid] > v:
            #print(L[:mid])
            return [(mid+i, L[mid])] + binarySearchValues(L[:mid],v, i)
            
        elif L[mid] < v:
            #print(L[mid + 1:])
            return ([(mid+i, L[mid])] + 
                binarySearchValues(L[mid + 1:],v, i + len(L[:mid + 1])))
            
            
            
            

##############################################
# OOP questions
##############################################

class Book(object):
    def __init__(self, name, author, totPage, currPage = 1):
        self.name = name
        self.author = author
        self.totPage = totPage
        self.currPage = currPage
        self.bookmark = None
    def __repr__(self):
        
        if self.totPage > 1 or self.totPage == 0:
            S = "pages"
        else:
            S = "page"

        string1 = "Book<%s by %s: "%(self.name, self.author)
        string2 = "%d %s, "% (self.totPage, S)
        string3 = "currently on page %s"% (self.currPage)
        string4 = ">"
        print(string1 + string2 + string3)
        
        
        if self.bookmark != None:
            string4 = ", page %d bookmarked>"%(self.bookmark)
        
        fullString = string1 + string2 + string3 + string4
        return fullString
        
    def turnPage(self, page):
        self.currPage += page
        if self.currPage > self.totPage:
            self.currPage = self.totPage
        elif self.currPage < 1:
            self.currPage = 1
        print("currPage: ", self.currPage)
    
    def getCurrentPage(self):
        return self.currPage
    
    def placeBookmark(self):
        
        self.bookmark = self.currPage
        print(self.bookmark)
        
    def getBookmarkedPage(self):
        return self.bookmark
        
    def turnToBookmark(self):
        if self.bookmark != None:
            self.currPage = self.bookmark
    
    def removeBookmark(self):
        self.bookmark = None
        
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        elif not (self.name == other.name):
            return False
        elif not (self.author == other.author):
            return False
        elif not (self.totPage == other.totPage):
            return False
        elif not (self.currPage == other.currPage):
            return False
        elif not (self.bookmark == other.bookmark):
            return False
        else:
            return True
        # finish this

#################################################
# Test Functions
#################################################

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Done!')

def testPowersOf3ToN():
    print('Testing powersOf3ToN()...', end='')
    assert(powersOf3ToN(-42) == None)
    assert(powersOf3ToN(0.99) == None)
    assert(powersOf3ToN(1) == [1])
    assert(powersOf3ToN(3) == [1, 3])
    assert(powersOf3ToN(8.9999) == [1, 3])
    assert(powersOf3ToN(9) == [1, 3, 9])
    assert(powersOf3ToN(9.1111) == [1, 3, 9])
    assert(powersOf3ToN(100) == [1, 3, 9, 27, 81])
    print('Done!')

def testBinarySearchValues():
    print('Testing binarySearchValues()...', end='')
    L = ['a', 'c', 'f', 'g', 'm', 'q']
    assert(binarySearchValues(L, 'a') == [(2,'f'), (0,'a')])
    #print("Pass 1")
    assert(binarySearchValues(L, 'c') == [(2,'f'), (0,'a'), (1,'c')])
    #print("Pass 2")
    assert(binarySearchValues(L, 'f') == [(2,'f')])
   # print("Pass 3")
    assert(binarySearchValues(L, 'g') == [(2,'f'), (4, 'm'), (3, 'g')])
    #print("Pass 4")
    assert(binarySearchValues(L, 'm') == [(2,'f'), (4, 'm')])
    #print("Pass 5")
    assert(binarySearchValues(L, 'q') == [(2,'f'), (4, 'm'), (5, 'q')])
    #print("Pass 6")
    assert(binarySearchValues(L, 'z') == [(2,'f'), (4, 'm'), (5, 'q')])
    #print("Pass 7")
    assert(binarySearchValues(L, 'b') == [(2,'f'), (0,'a'), (1,'c')])
    #print("Pass 8")
    print('Done!')

def testBookClass():
    print("Testing Book class...", end="")
    # A Book has a title, and author, and a number of pages.
    # It also has a current page, which always starts at 1. There is no page 0!
    
    book1 = Book("Harry Potter and the Sorcerer's Stone", 
                 "J. K. Rowling", 309)
    #print(book1)
    assert(str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " + 
                         "J. K. Rowling: 309 pages, currently on page 1>")
    book2 = Book("Carnegie Mellon Motto", "Andrew Carnegie", 1)
    assert(str(book2) == "Book<Carnegie Mellon Motto by Andrew Carnegie: " +
                         "1 page, currently on page 1>")
                         
    # You can turn pages in a book. Turning a positive number of pages moves
    # forward; turning a negative number moves backwards. You can't move past
    # the first page going backwards or the last page going forwards
    book1.turnPage(4) 
    #print(book1.turnPage(4)) # turning pages does not return
    #print(book1.getCurrentPage())
    assert(book1.getCurrentPage() == 5)
    book1.turnPage(-1)
    assert(book1.getCurrentPage() == 4)
    book1.turnPage(400)
    assert(book1.getCurrentPage() == 309)
    assert(str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " + 
                         "J. K. Rowling: 309 pages, currently on page 309>")
    book2.turnPage(-1)
    assert(book2.getCurrentPage() == 1)
    book2.turnPage(1)
    assert(book2.getCurrentPage() == 1)
    
    # You can also put a bookmark on the current page. This lets you turn
    # back to it easily. The book starts out without a bookmark.
    book3 = Book("The Name of the Wind", "Patrick Rothfuss", 662)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 1>")
    assert(book3.getBookmarkedPage() == None)
    book3.turnPage(9)
    book3.placeBookmark() # does not return
    assert(book3.getBookmarkedPage() == 10)
    book3.turnPage(7)
    assert(book3.getBookmarkedPage() == 10)
    assert(book3.getCurrentPage() == 17)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 17, page 10 bookmarked>")
    book3.turnToBookmark()
    assert(book3.getCurrentPage() == 10)
    book3.removeBookmark()
    assert(book3.getBookmarkedPage() == None)
    book3.turnPage(25)
    assert(book3.getCurrentPage() == 35)
    book3.turnToBookmark() # if there's no bookmark, don't turn to a page
    assert(book3.getCurrentPage() == 35)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 35>")
    
    # Finally, you should be able to compare two books directly
    book5 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book6 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book7 = Book("A Natural History of Dragons", "Marie Brennan", 334)
    book8 = Book("A Game of Spoofs", "George R.R. Martin", 807)
    
    assert(book5 == book6)
    assert(book5 != book7)
    assert(book5 != book8)
    book5.turnPage(1)
    print("book5 currPage: ", book5.currPage)
    print("book6 currPage: ", book6.currPage)
    print(book5 != book6)
    assert(book5 != book6)
    book5.turnPage(-1)
    assert(book5 == book6)
    book6.placeBookmark()
    assert(book5 != book6)
    print("Done!")

##############################################
# testAll and main
##############################################

def testAll():
    testAlternatingSum()
    testPowersOf3ToN()
    testBinarySearchValues()
    testBookClass()

def main():
    cs112_f17_week9_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
