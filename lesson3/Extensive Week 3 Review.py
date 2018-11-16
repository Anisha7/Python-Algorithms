#Extensive Previous Week Review
#Week 3

#split vs splitlines
splitlines = split("\n") #returns a list

for word in words.split(","):
    #do stuff

# strip() ==> whitespace (leading and trailing)
strip("\n")

# %d ==> ints

age = 3
birthyear = 1996

string = "Abhi is" + str(age) + "years old" #ugly
string = "Abhi is %d years old and was born in %d" % (age, birthyear)

# %s ==> string

# %f ==> float

# look at how to write functions under Basic File IO 
# ==> String Methods

# "foo.txt"
# count all instancces of word "cow"
# each word is separated by commas
# readFile takes in the full path
# no full path ==> assumes same folder
# if file in directory, writeFile overwrites

text = readFile("foo.txt")
count = 0
for word in text.split(","):
    if(word == "cow"):
        count += 1
return count

content = "Rishabh is the best"
writeFile("lalala.txt", content)

# Top Down Design Functions: 
# ==> Assume helpers are written for you
# ==> write bigger function first

def nthPrime(n):
    return None
    # write nthPrime first
    # helpers second
    
# ******************************************** #

def ct1(s, n):
    result = ""
    d = 0
    
    while n > 0 and len(s) > 0:
        
        if s[-1].isdigit() :
            
            result += str( (n%10) % int(s[-1]) )
            
        else:
            result += chr(ord('0') + d)
            
        n //= 10
        s = s[1: -1]
        d += 1
        
    return result

print(ct1("abc3c3", 2468))

s                 n                 result                d 
abc3c3           2468                 ""                  0
                                      "2"
bc3c             246                  "2E"                1
c3                24                  "2E1"               2
""                2                                       3

# Convert file from hacked file to normal file
# ==> for specific format

def find(orig, new):
    
    for line in orig.splitlines():
        [name, score] = line.split(",")
        score1 = int(score)
        
        for line2 in new.splitlines():
            [name2, score2] = line2.split(",")
            scoreToCompare = int(score2)
            
            if name == name2:
                if scoreToCompare > score1:
                    res += name + " "
                    
    return res.strip()

#Why will this code crash?

def f(s):
    t = s
    for i in range(len(t)):
        if (t[i] == 'Q'):
            t[i] = 'R' # strings are immutable
            
    return t

# ==> Better version

def f_fixed(s):
    result = ""
    
    for i in range(len(s)):
        
        if s[i] == "Q" :
            result = result + "R"
            
        else:
            result = result + s[i]
    
    return result
    
# code tracing

def f(s):
    for x in range(1,4):
        spec = "%%0.%df" % x
        print(spec % float(s))
        
    # "%0.1f"
    #if f = 12.586, using above thing rounds it to 12.6

    #when using variable, use single percent. else, use double percent.
f("12.45645")

#console:
    #


#hw 3 last problem
#if length of col is less than length of row
    #fill it with a dash
def calculateNumDashes(s, key):
    cols = len(key)
    nDashes = cols - len(s) % cols
    
    newS = s + (nDashes * "-")


