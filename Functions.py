# EXAMPLE 1 
# This function return value
# Minimun difference betwen three values. 
print("-----------------------------------------------")
print("EXAMPLE 1 First Function")
def least_difference(a, b, c):
    
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)

# EXAMPLE 2
# This function do not return a value 
print("-----------------------------------------------")
print("EXAMPLE 2 This function do not return a value")
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)
    
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)

#Python allows us to define such functions. 
#The result of calling them is the special value None. 
# (This is similar to the concept of "null" in other languages.)

# EXAMPLE 3
# Adding optional arguments with default values 
# to the functions we define turns out to be pretty easy
print("-----------------------------------------------")
print("EXAMPLE 3 Adding optional arguments")
def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")

# EXAMPLE 4
#Functions Applied to Functions
#Here's something that's powerful,
#though it can feel very abstract at first. 
# You can supply functions as arguments to other functions. 
# Some example may make this clearer:
print("-----------------------------------------------")
print("EXAMPLE 4 Functions Applied to Functions")
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)
# EXAMPLE 5
# Functions that operate on other functions are called "higher-order functions." 
# Here's an interesting example using the max function.

#By default, max returns the largest of its arguments.
#But if we pass in a function using the optional key argument,
# it returns the argument x that maximizes key(x) (aka the 'argmax').
print("-----------------------------------------------")
print("EXAMPLE 5 Fhigher-order functions")

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)