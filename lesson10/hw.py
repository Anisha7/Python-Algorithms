#################################################
# HW 11
# Anisha Jain - anishaj

#################################################

import cs112_f17_week11_linter
import math
import types

######################################################################
# Functions
######################################################################

# Gate Classes
        
class Gate(object):
    inputList = [True, True]
    def __init__(self, input1 = 2, input2 = True):
        self.input1 = input1
        self.input2 = input2
        
    def __str__(self):
        if type(self) == AndGate:
            x = "And"
        if type(self) == OrGate:
            x = "Or"
        if type(self) == NotGate:
            return "Not(" + str(NotGate.inputList[0]) + ")"
        
        return x + "(" + str(Gate.inputList[0]) + "," +\
         str(Gate.inputList[1]) + ")"
         
        return x + "(" + str(Gate.inputList[0]) + "," +\
         str(Gate.inputList[1]) + ")"
    
    def numberOfInputs(self):
        return len(Gate.inputList)
        
    def setInput(self, x, y):
        #Gate.inputList[x] = y
        type(self).inputList[x] = y

class AndGate(Gate):
    def getOutput(self):
        for val in Gate.inputList:
            if val == False:
                return False
        return True
          
class OrGate(AndGate):
        
    def getOutput(self):
        for val in Gate.inputList:
            if val == True:
                return True
        return False
        
class NotGate(Gate):

    #inputList = [Gate.inputList[0]]
    inputList = [True]
    
    def getOutput(self):
        
        return not (NotGate.inputList[0])
    
    def numberOfInputs(self):
        return len(NotGate.inputList)
        
# Complex Number

class ComplexNumber(object):
    x = None
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        #print(self.x, isinstance(self.x, int))
        
        # allow input of complex numbers
        if not isinstance(self.x, int):
            s = str(self.x)
            #print("s: ",s)
            x = ""
            for i in range(len(s)):
                if s[i] == "+":
                    s = s[i+1:]
                    break
                if s[i].isdigit():
                    x += s[i]
            
            #print("s: ",s)
            self.x = int(x)
            y = ""
            for i in range(len(s)):
                #print("...",s[i], s[i].isdigit())
                if s[i].isdigit():
                    y += s[i]
                #print("y: ", y)
            self.y = int(y)
            
    def __str__(self):
        #if not isinstance(self.x, int):
            #return str(self.x)
        return str(self.x) + "+" + str(self.y) + "i"
        
    def realPart(self):
        return self.x
        
    def imaginaryPart(self):
        return self.y
    
    def __eq__(self, other):
        if isinstance(other, int):
            return self.x == other
        if not isinstance(other, ComplexNumber):
            return False
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    @staticmethod
    def getZero():
        if ComplexNumber.x == None:
            ComplexNumber.x = ComplexNumber()
        return ComplexNumber.x
        
#################################################
# Test Functions
#################################################

def getLocalMethods(clss):
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class.
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

def testGateClasses():
    print("Testing Gate Classes... ", end="")

    # require methods be written in appropriate classes
    assert(getLocalMethods(Gate) == ['__init__', '__str__',
                                     'numberOfInputs', 'setInput'])
    assert(getLocalMethods(AndGate) == ['getOutput'])
    assert(getLocalMethods(OrGate) == ['getOutput'])
    assert(getLocalMethods(NotGate) == ['getOutput', 'numberOfInputs'])

    # make a simple And gate
    and1 = AndGate()
    assert(type(and1) == AndGate)
    assert(isinstance(and1, Gate) == True)
    assert(and1.numberOfInputs() == 2)
    and1.setInput(0, True)
    and1.setInput(1, False)
    # Hint: to get the name of the class given an object obj,
    # you can do this:  type(obj).__name__
    # You might do this in the Gate.__str__ method...
    assert(str(and1) == "And(True,False)")
    assert(and1.getOutput() == False)
    and1.setInput(1, True) # now both inputs are True
    assert(and1.getOutput() == True)
    assert(str(and1) == "And(True,True)")

    # make a simple Or gate
    or1 = OrGate()
    assert(type(or1) == OrGate)
    assert(isinstance(or1, Gate) == True)
    assert(or1.numberOfInputs() == 2)
    or1.setInput(0, False)
    or1.setInput(1, False) 
    assert(or1.getOutput() == False)
    assert(str(or1) == "Or(False,False)")
    or1.setInput(1, True)
    assert(or1.getOutput() == True)
    assert(str(or1) == "Or(False,True)")

    # make a simple Not gate
    not1 = NotGate()
    assert(type(not1) == NotGate)
    assert(isinstance(not1, Gate) == True)
    assert(not1.numberOfInputs() == 1)
    not1.setInput(0, False)
    
    print('iL', NotGate.inputList)
    print("not1",not1.getOutput())
    
    assert(not1.getOutput() == True)
    assert(str(not1) == "Not(False)")
    not1.setInput(0, True)
    
    print('iL', NotGate.inputList)
    print("not1",not1.getOutput())
    
    assert(not1.getOutput() == False)
    assert(str(not1) == "Not(True)")

    print("Passed!")

def testComplexNumberClass():
    print("Testing ComplexNumber class... ", end="")
    # Do not use the builtin complex numbers in Python!
    # Only use integers!

    c1 = ComplexNumber(1, 2)
    assert(str(c1) == "1+2i")
    assert(c1.realPart() == 1)
    assert(c1.imaginaryPart() == 2)

    c2 = ComplexNumber(3)
    assert(str(c2) == "3+0i") # default imaginary part is 0
    assert(c2.realPart() == 3)
    assert(c2.imaginaryPart() == 0)

    c3 = ComplexNumber()
    assert(str(c3) == "0+0i") # default real part is also 0
    assert(c3.realPart() == 0)
    assert(c3.imaginaryPart() == 0)

    # Here we see that the constructor for a ComplexNumber
    # can take another ComplexNumber, which it duplicates
    c4 = ComplexNumber(c1)
    
    print(ComplexNumber(c1))
    print("c4: ", c4)
    print("str(c4): ", str(c4))
    
    assert(str(c4) == "1+2i")
    assert(c4.realPart() == 1)
    assert(c4.imaginaryPart() == 2)

    print("c1: ", c1, "c4: ", c4)
    assert((c1 == c4) == True)
    assert((c1 == c2) == False)
    assert((c1 == "Yikes!") == False) # don't crash here
    assert((c2 == 3) == True)

    s = set()
    assert(c1 not in s)
    s.add(c1)
    assert(c1 in s)
    assert(c4 in s)
    assert(c2 not in s)

    assert(ComplexNumber.getZero() == 0)
    assert(isinstance(ComplexNumber.getZero(), ComplexNumber))
    assert(ComplexNumber.getZero() == ComplexNumber())
    # This next one is the tricky part -- there should be one and
    # only one instance of ComplexNumber that is ever returned
    # every time you call ComplexNumber.getZero():
    assert(ComplexNumber.getZero() is ComplexNumber.getZero())
    # Hint: you might want to store the singleton instance
    # of the zero in a class attribute (which you should
    # initialize to None in the class definition, and then
    # update the first time you call getZero()).

    print("Passed!")

    
#################################################
# testAll and main
#################################################

def testAll():
    testGateClasses()
    testComplexNumberClass()

def main():
    cs112_f17_week11_linter.lint() # check style rules
    testAll()
    
    
    

if __name__ == '__main__':
    main()

