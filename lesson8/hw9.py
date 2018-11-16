#################################################
# Hw9
#
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

# input: pos/neg int n, k
# output: 1**k + 2**k + ... + n**k
# output: 0 if n,k is neg
def powerSum(n, k):
    
    if n <= 0 or k < 0:
        return 0
    else:
        return n**k + powerSum(n-1, k)
        
# input: int n
# output: sum of the squares of digits in n
def sumOfSquaresOfDigits(n):
    
    if n <= 0:
        return 0
    else:
        return ((n%10)**2) + sumOfSquaresOfDigits(n//10)

# input: int n
# output: True or False, if is/ is not happy
def isHappyNumber(n):
    
    #print(n)
    if n < 0:
        return False
    elif n == 4:
        return False
    elif n == 1:
        return True
    else:
        return isHappyNumber(sumOfSquaresOfDigits(n))

# gets the index of the last operator
def getOpIndex(L):
    
    if isinstance(L[0], int):
        L.pop(0)
    
    else:
        return [len(L) - 1] + getOpIndex(L)
 
def findIntIndex(L, i = 0):
    
    #print(i)
    if i >= len(L):
        return None
    elif isinstance(L[i], int):
        return i
    else:
        findIntIndex(L[i + 1:], i = i + 1)
    
def evalPrefixNotation(L):
    #i = getOpIndex(reversed(L))
    if len(L) == 1:
        return L[0]
    
    else:
        operator = L.pop(0)
       
        if isinstance(L[0], int):
            num1 = L.pop(0)
        else:
            num1 = evalPrefixNotation(L)
        if isinstance(L[0], int):
            num2 = L.pop(0)
        else: 
            num2 = evalPrefixNotation(L)
            
        if operator == "+":
            return num1 + num2
        if operator == "*":
            return num1 * num2
        if operator == "-":
            return num1 - num2


##############################################
# OOP questions
##############################################

class VendingMachine(object):
    def __init__(self, bottles, price, money = 0):
        self.bottles = bottles
        
        self.price = price
        #decimal version of price
        self.dec = (self.price//100) + ((self.price%100)/100)
        
        self.money = money
        # initial money owed
        self.owe = (self.price - self.money)//100 +\
         ((self.price - self.money)%100)/100
    
    def __eq__(self, other):
        if not isinstance(other, VendingMachine):
            return False
        elif self.bottles != other.bottles:
            return False
        elif self.price != other.price:
            return False
        elif self.money != other.money:
            return False
        else:
            return True
        
    def __repr__(self):
        # initial status
        
        # account for grammar
        if self.bottles == 1:
            bottleStr = "bottle"
        else:
            bottleStr = "bottles"
        
        string1 = "Vending Machine:"
        string2 = "<%d %s; "%(self.bottles, bottleStr)
        if int(self.dec) == self.dec:
            string3 = "$%d each; "%(self.dec)
        else:
            string3 = "$%0.2f each; "%(self.dec)
        
        string4 = "$%d paid>"%(self.money)
        string = string1 + string2 + string3 + string4
        print(string)
        return string
    
    def __hash__(self):
        return hash((self.bottles, self.price))
    
    def isEmpty(self):
        if self.bottles <= 0:
            return True
        else:
            return False
    
    def stillOwe(self):
        # returns non decimal version of money owed
        print("owe: ",self.owe)
        return self.owe*100
    
    # adjusts money that has been paid
    def paidMoney(self, num):
        
        if num > self.price:
            paid = self.price
        else:
            paid = (num//100) + ((num%100)/100)
        
        # account for $1.00 --> $1
        if int(paid) == paid:
            paid = int(paid)
            
        if self.bottles <= 0 or self.owe == 0:
            paid = 0
        
        return paid
        
    def insertMoney(self, num):
        
        
        # adjusts status based on money inserted
        if num > self.price:
            change = num - (self.price)
            self.owe = 0
            self.money = self.price
        else:
            self.owe -= (num/100)
            change = 0
            self.money = self.paidMoney(num)
            #self.money = 5
        
        # if $1.00, returns $1            
        if int(self.owe) == self.owe:
            self.owe = int(self.owe)
            oweString = "Still owe $%d"%(self.owe)
        else:
            oweString = "Still owe $%0.2f"%(self.owe)
        
        # machine has no more bottles
        if self.bottles <= 0:
            oweString = "Machine is empty"
            change = num
            self.owe = self.dec
            self.money = 0
        
        # full price for bottle is paid, machine resets
        if self.owe == 0:
            oweString = "Got a bottle!"
            self.bottles -= 1
            self.owe = (self.price)//100 +\
                ((self.price)%100)/100
            self.money = 0
        
        print((oweString, change))
        return (oweString, change)
  
    def getBottleCount(self):
        return self.bottles
    
    def stockMachine(self, num):
        self.bottles += num 
        return self.bottles
    
        
#################################################
# Test Functions
#################################################

def testPowerSum():
    print('Testing powerSum()...', end='')
    assert(powerSum(4, 6) == 1**6 + 2**6 + 3**6 + 4**6)
    assert(powerSum(0, 6) == 0)
    assert(powerSum(4, 0) == 1**0 + 2**0 + 3**0 + 4**0)
    assert(powerSum(4, -1) == 0)
    print('Done!')

def testIsHappyNumber():
    print('Testing isHappyNumber()...', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Done!')

def testEvalPrefixNotation():
    print('Testing evalPrefixNotation()...', end='')
    assert(evalPrefixNotation([42]) == 42)
    assert(evalPrefixNotation(['+', 3, 4]) == 7)
    assert(evalPrefixNotation(['-', 3, 4]) == -1)
    assert(evalPrefixNotation(['-', 4, 3]) == 1)
    assert(evalPrefixNotation(['+', 3, '*', 4, 5]) == 23)
    assert(evalPrefixNotation(['+', '*', 2, 3, '*', 4, 5]) == 26)
    assert(evalPrefixNotation(['*', '+', 2, 3, '+', 4, 5]) == 45)
    assert(evalPrefixNotation(['*', '+', 2, '*', 3, '-', 8, 7,
                               '+', '*', 2, 2, 5]) == 45)
    print('Done!')

def testVendingMachineClass():
    print("Testing Vending Machine class...", end="")
    # Vending machines have three main properties: 
    # how many bottles they contain, the price of a bottle, and
    # how much money has been paid. A new vending machine starts with no
    # money paid.
    vm1 = VendingMachine(100, 125)
    assert(str(vm1) == "Vending Machine:<100 bottles; $1.25 each; $0 paid>")
    assert(vm1.isEmpty() == False)
    assert(vm1.getBottleCount() == 100)
    assert(vm1.stillOwe() == 125)
    
    # When the user inserts money, the machine returns a message about their
    # status and any change they need as a tuple.
    assert(vm1.insertMoney(20) == ("Still owe $1.05", 0))
    assert(vm1.stillOwe() == 105)
    assert(vm1.getBottleCount() == 100)
    assert(vm1.insertMoney(5) == ("Still owe $1", 0))
    
    # When the user has paid enough money, they get a bottle and 
    # the money owed resets.
    assert(vm1.insertMoney(100) == ("Got a bottle!", 0))
    assert(vm1.getBottleCount() == 99)
    assert(vm1.stillOwe() == 125)
    assert(str(vm1) == "Vending Machine:<99 bottles; $1.25 each; $0 paid>")
    
    # If the user pays too much money, they get their change back with the
    # bottle.
    assert(vm1.insertMoney(500) == ("Got a bottle!", 375))
    assert(vm1.getBottleCount() == 98)
    assert(vm1.stillOwe() == 125)
    
    # Machines can become empty
    vm2 = VendingMachine(1, 120)
    assert(str(vm2) == "Vending Machine:<1 bottle; $1.20 each; $0 paid>")
    assert(vm2.isEmpty() == False)
    assert(vm2.insertMoney(120) == ("Got a bottle!", 0))
    assert(vm2.getBottleCount() == 0)
    assert(vm2.isEmpty() == True)
    
    # Once a machine is empty, it should not accept money until it is restocked.
    assert(str(vm2) == "Vending Machine:<0 bottles; $1.20 each; $0 paid>")
    assert(vm2.insertMoney(25) == ("Machine is empty", 25))
    assert(vm2.insertMoney(120) == ("Machine is empty", 120))
    assert(vm2.stillOwe() == 120)
    vm2.stockMachine(20) # Does not return anything
    assert(vm2.getBottleCount() == 20)
    assert(vm2.isEmpty() == False)
    assert(str(vm2) == "Vending Machine:<20 bottles; $1.20 each; $0 paid>")
    assert(vm2.insertMoney(25) == ("Still owe $0.95", 0))
    assert(vm2.stillOwe() == 95)
    vm2.stockMachine(20)
    assert(vm2.getBottleCount() == 40)
    
    # We should be able to test machines for basic functionality
    vm3 = VendingMachine(50, 100)
    vm4 = VendingMachine(50, 100)
    vm5 = VendingMachine(20, 100)
    vm6 = VendingMachine(50, 200)
    vm7 = "Vending Machine"
    assert(vm3 == vm4)
    assert(vm3 != vm5)
    assert(vm3 != vm6)
    assert(vm3 != vm7) # should not crash!
    s = set()
    assert(vm3 not in s)
    s.add(vm4)
    assert(vm3 in s)
    s.remove(vm4)
    assert(vm3 not in s)
    assert(vm4.insertMoney(50) == ("Still owe $0.50", 0))
    print("vm3: ", vm3, vm3.owe)
    print("vm4: ", vm4, vm4.owe)
    assert(vm3 != vm4)
    print("Done!")
    vm5 = VendingMachine(100, 125)
    vm5.insertMoney(20)
    print("vm5: ", vm5)
    assert(str(vm5) == "Vending Machine:<100 bottles; $1.25 each; $0.20 paid>")
    
##############################################
# testAll and main
##############################################

def testAll():
    testPowerSum()
    testIsHappyNumber()
    testEvalPrefixNotation()
    testVendingMachineClass()

def main():
    cs112_f17_week9_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
