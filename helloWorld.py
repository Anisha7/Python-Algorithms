def helloWorld():
    print("Hello World!") # This is a comment
    print("What will this line do?")
    print("Cool Cool!")

helloWorld()

#How to get an input from the user? Use input()
name= input("Enter your name: ")
print("Your name is:", name)

#How to allow input of integers and run a function with it? Use int()
x = int(input("Enter a number: "))
print("One half of", x, "=", x/2)

#Must import modules to use functions in that module!
import math
print(math.factorial(20))

#What does a module export?
# list all the functions in the math module
# (ignore items in __double_underscores__)
import math
print(dir(math))

# even better, read the online docs!
#This gives more info on the functions in the math module.
import webbrowser
input("Hit enter to see the online docs for the math module.")
webbrowser.open("https://docs.python.org/3/library/math.html")
