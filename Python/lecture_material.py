# --------------- Exponentiation, Floor Division and Modulo
exponentiation = 4 ** 4  # 256
floor_division = 16 // 5  # 3
modulo = 7 % 3  # 1
print(exponentiation)
print(floor_division)
print(modulo)
print("\n")

# ---------------- Assignment Operators
# in this case, the assignment operator is thr addition assignment operator, which is represented by the plus equals symbol.

add_assign = 5
add_assign += 7
print(add_assign)
print("\n")

'''Using the addition assignment operator the expression on line two reassigned the variable, add assign, the equivalent of thr sum
of its original stored value, five and the integer seven. That means that add assign was reassigned the value 12 '''

# ------------------ Order of Operations
'''     ()   
        **
        %, / // and * 
        + and  - '''
#B – Brackets, O – Order of powers or roots, D – Division, M – Multiplication A – Addition, and S – Subtraction
''' Example :   (9-7)*2**3+10%6//-1*2-1
                2*2**3+10%6//-1*2-1
                2*8+10%6//-1*2-1
                2*8-4*2-1  
                16-8-1
                7   '''

#Why do expressions that involve floats produce inaccurate result?
print(1.23 + 2.80)  # output : 4.029999999999999 (Actual Output : 4.03)

''' the sum resulted in a very long decimal number instead. When working with floats in python, you will often get approximation errors like this "4.029999999999999" '''

''' when used in expressions?
Well, the reason is that python is built on top of the C language. The problem with this is that the C language approximates floats using a fixed number of binary digits, and some
 numbers such as the sum of 1.23 and 2.80 cannot be represented with exactness by the limited numbers of binary digits used to represented a float'''
# How to get around the approximation error
# there are two ways to get expressions containing floats to evaluate to the correct values.
# The First is to avoid using floats altogether and to use integers instead.

ex2 = (123 + 280) / 100
print(ex2)

# when using floats is by using the round function "round()"
ex3 = 1.23 + 2.80
print(round(ex3, 2))  # 2 is the number of decimal place that you want to round to
print("\n")

# --------- String -------------
#What is a string
'''A string is just a sequence of characters. Those characters can be any combination of numbers, spaces, uppercase letters, lowercase letters, underscores or symbols, such as a period or exclamation point'''

ex_4 = "Orange"
print(ex_4[2])
print("apple"[4])
print("\n")

#________________ String slicing
''' String slicing allows you to get slices of a string and assign them to variables or print them, Where a slice of a string is just a string that was originally part of another string'''
ex_5 = "apricots"

print(ex_5[:3])
print(ex_5[2:5])
print(ex_5[4:])
print("\n")

# _______________ Concatenation
''' String can also be added together using the addition operator in a process known as concatenation'''
print("pecan" + " " + "pie")

concatenated = "R2" + "_" + "D2"
print(concatenated)
print(concatenated[3])
print(concatenated[1:4])
print("\n")

# effects of accessing by index and string slicing on variables
''' If we had a variable holding a string and we sliced it and then assigned the slice to a variable we could print both the slice and the string'''
unchanged: str = "forrest gump"
sliced = unchanged[6:]
print(sliced)
print(unchanged)
print("\n")

#___________type() and str() _______________
#type()
''' The type function allows you to find out the data type of a piece of data. To use it, you type whatever you want to know the data type of within its parentheses. 
Then it will return back what the data type is '''

ex_1 = False
ex_2 = 29
ex_3 = 4.1352
print(type(ex_1))
print(type(ex_2))
print(type(ex_3))
print("\n")

# str()
''' The string function converts whatever is put between its parentheses into a string.'''
ex_4 = str(True)
ex_5 = str(5)
ex_6 = str(3.21)
print(type(ex_4))
print(type(ex_5))
print(type(ex_6))
print("\n")

# ___________ escape sequences ________
# What is an escape sequence?
''' Escape sequences are special characters you can use and strings which enable you to do things such as insert quotes within them and to make different parts of string appear on different lines in the output
 '''
# \t TAB character
print("This\tis\ta\tlot\tof\tspace.")

# \n New line character
print("Line one\nline two")

# \' & \" to show single or double quotes in output. For instance, 'Hello' and "World" are valid string literals containing single and double quotes, respectively.
print('"When I said \'immediately\' I meant today!" said King Saul.')
print("\"Do or do not. There is no try.\"")

# \\  Backslash escape sequence is used whenever you want to put a backslash in string.
print("All escape sequence contain a \\.")
print('\n')

# -------------------- input() ---------------
''' Which will allow you to make your programs get and use input from a user'''
'''

name = input("Please enter your name.")
print("Your name is " + name + ".")
print(type(name))

fav_num = input("What is your favorite number?.")
print("Your Favorite number is " + fav_num + ".")
print(type(fav_num))

'''
#_______ int() and float() _________
''' int()  --->  The integer function lets you convert a string into an integer '''

''' -------------------------------------------------------------

user_int = input("Please enter an integer")
print(user_int)
print(type(user_int))


user_int = int(input("Please enter an integer"))
print(user_int)
print(type(user_int))

---------------------------------------------------------------'''
# float()

''' -------------------------------------------------------------

user_float = input("Please enter an float.")
print(user_float)
print(type(user_float))


user_float = float(input("Please enter an float."))
print(user_float)
print(type(user_float))

---------------------------------------------------------------'''

# ---------------- Functions -----------------------------------
''' When being able to reuse code on different variables and values without having to rewrite it!'''


def print_four():
    print("this")
    print("is")
    print("an")
    print("example")


print_four()
print_four()
print_four()
print_four()
print("\n")

# __________ defining a function
#Creating a function is also known as defining a function
''' There are at least five parts to every function, the keyword "def", a "function_name", "parentheses", a "colon", then code that the function is meant to run.  '''


def function_name():
    print(2 + 2)


# __________ Calling a function :
#function do not automatically run their code after there created.
# To use a function, you must call it. To call a function, you type its name followed by parentheses.


function_name()


def function_name(parameter):
    print(parameter + 2)


function_name(8)

#____________ Multiple parameters
#when you define a function, you can create as many parameters as you want
first_str = "The number "


def function_name(p1, p2, p3):
    print(p1 + str(p2) + p3)


function_name(first_str, 5, " is an integer")


#___________default parameters
#when you create a function, you can give its parameters value to default to in the event that function is called without arguments for those parameters


def default_example(num1=7, num2=8):
    print(num1 * num2)


default_example()


#__________return
#The return keyword is what will allow you to do that.


def default_example(num1=7, num2=8):
    return num1 * num2


product = default_example(2)  # not get any output


#using return with expressions


def default_example(num1=7, num2=8):
    return num1 * num2


print(default_example() + 44)
print('\n')

# ------- Introduction to modules
''' Modules contain sets of functions that can be useful for many different things. To use the functions within them, you must import them. There are three different ways to do this, generic imports, function imports and universal imports.'''

#________________Generic import
import random

print(random.randint(1, 10))

#_______________ Function import
'''A function import is when a specific function is imported from a module. To import a function form a module, you must type from, the name of the module, tht=at the function is being imported from, import, then the name of the function being imported. '''
from random import randint

print(randint(10, 20))

#_______________ Universal import
'''A universal import is when you import every function from a module so that whenever you call any function form that module, you do not need to type the module's name and period.'''
from random import *

print(random())
print('\n')

#------------ Variable Scope
''' Variables created within functions have a local scope. While variable that are created outside of functions have a global scope.  Every line of code in a program is also either in the global scope or local scope, and each function also has its own local scope'''

example = "Hello world"  # global


def loc_ex():
    example = "this is a string"  # local
    return example


print(example)
print(loc_ex())

#why is understanding variable scope important?
''' ---> Local variable cannot be used by code in the global scope.
    ---> Global variable can be accessed by code in a local scope.
    ---> The local scope of one function can't use variable from another function's local scope.
    ---> You can use the same name for different variables as long as they are in different scopes'''


#Example for each of the four points

# ---> Local variable cannot be used by code in the global scope.


def loc_ex():
    breakfast = "waffles"
    return breakfast


loc_ex()
#print(breakfast)

''' The print statement above the call of the function loc_ex() cannot print the string assigned to breakfast since it is outside the function, meaning that the print 
statement is in the global scope rather than in the local scope of loc_ex() because variable in a local scope are forgotten after a function returns somethings...
The print statement can't find a breakfast variable to print.'''


# ---> Global variable can be accessed by code in a local scope.


def print_glob():
    print(glob_var)


glob_var = "This is a string..!"
print_glob()
''' Here in the output, the function print glob is able to print the string assigned to the variable glob_var When it is called because glob_var is outside of all functions, meaning that it is in the global scope'''


# or

def print_glob():
    loc_var = " that is very long."
    print(glob_var + loc_var)


# noinspection PyRedeclaration
glob_var = "This is a string..!"
print_glob()

# ---> The local scope of one function can't use variable from another function's local scope.


def first():
    loc = 2
    return loc


def second():
    """return loc"""


first()
second()

''' In this example program, the local scope of the called first d=function was destroyed after it returned.
 Thus, when the second function was called and tried to return LOC, it could not find a LOC variable to return and the name error message was displayed as a result.'''

# ---> You can use the same name for different variables as long as they are in different scopes


def loc_ex1():
    fruit = "pear"
    print(fruit)


def loc_ex2():
    fruit = "banana"
    print(fruit)


fruit = "apple"
loc_ex1()
loc_ex2()
print(fruit)
print("\n")
# ------- Global statements
#if you wanted to assign a global variable a new value from within a function, you could do that using global statements.


def loc_ex():
    fruit = 'pear'
    print(fruit)


fruit = "apple"
loc_ex()
print(fruit)
''' For example, suppose that we had a global variable called fruit, which held the string apple and we wanted to change that global variable assigned string to pear.
To do that, using a global statement within the function loc_ex, we would have to type global and the name of the global variable whose value we want to change at the top of the function.'''


def loc_ex():
    global fruit
    fruit = 'pear'
    print(fruit)


fruit = "apple"
loc_ex()
print(fruit)
print("\n")


# Intro to Flow Control
''' Comparison operators
    --->  >  (Greater than)
    --->  <  (Less than)
    --->  >= (greater than equal to)
    --->  <= (less than equal to)
    --->  != (is not equal to)
    --->  == ( equal to)
Comparisons made using these operators evaluate to boolean value, meaning that comparisons result in either a true or false.'''

print(4 > 2)
print(1 > 3)
print(5.79 < 6)
print(3 < 3)
print(9 >= 9)
print(1 <= 2)
print(10 != 100)
print(10 != 10)
print(10 == 100)
print(10 == 10)
print("hello" == "hello")
print("Hello" == "hello")
print("hello" != "world")
print(4.0 >= 4)
print(4.0 <= 4)
print(4.0 == 4)
print('\n')

#_______ boolean operators
''' There are three of them,
    ---> and
    ---> or
    ---> not
             ---- AND Operator -----
         ------------------------------
        | statement        |   Result  |
         ------------------------------
        | True and True    |    True   |
         ------------------------------
        | True and False   |    False  |
         ------------------------------
        | False and False  |    False  |
         ------------------------------
        | False and True   |    False  |
         ------------------------------'''
# example for AND operator
print("AND Operator..!")
print(4 > 1 and "word" == "word")       # True and True
print(8.76 == 8.7600 and 2 != 2)        # True and False
print("earth" == "Earth" and 6 <= 3)    # False and False
print(10 == 5 and 10 != 5)              # False and True

print("\n")
''' --------------- OR Operator ---------
         ------------------------------
        | statement        |   Result  |
         ------------------------------
        | True and True    |    True   |
         ------------------------------
        | True and False   |    True  |
         ------------------------------
        | False and False  |    False  |
         ------------------------------
        | False and True   |    True  |
         ------------------------------'''

# example for AND operator
print("OR Operator..!")
print(4 > 1 or "word" == "word")        # True and True
print(8.76 == 8.7600 or 2 != 2)         # True and False
print("earth" == "Earth" or 6 <= 3)     # False and False
print(10 == 5 or 10 != 5)               # False and True
print('\n')

''' --------------- NOT Operator ---------
         ------------------------------
        | statement        |   Result  |
         ------------------------------
        |     not True     |    False   |
         ------------------------------
        |     not False    |    True   |
         ----------------------------- '''
# example for AND operator
print("NOT Operator..!")
print(not 6482 > 0)                 # not True
print(not "Python" != "Python")     # not False
print('\n')

# ------------- if statements -------
''' We'll go over the syntax of an IF statement
# if True:
    "Do the stuff here"
There are four things every if statement must have. The word "if", a condition, which if it evaluates to true will make thee if statement run its code, a colon, then code for the if statement to execute
 if its condition evaluates too true.'''

""" --------- example for if statement ------------
veg = input("Type the name of vegetable.")
if veg == "corn":
    print("The vegetable is corn.") """

# -------- flow chat diagram
'''         program is run
                    |
                   \|/
                veg == "corn"      true
                     |       ----------------> print("The vegetable is corn.") 
                     |                                      |
                     | False                                |
                     |                                      |
                    \|/                                     |
                program ends <------------------------------|
                    '''

# --------- Else Statements ---------
""" else statement syntax
    if False:
        "Do the stuff here"
    else:
        "Do this instead"
There are three parts that every else statement must have the word else, a colon and code to execute. """

#__________ Flow chat diagram ______

"""               program is run
                        |
                        |
                       \|/
                    veg == "corn"     True
                                --------------->  print("The vegetable is corn.")
                        |                                       |
                        |                                       |
                        | False                                 |
                        |                                       |
                       \|/                                      |
          print("The vegetable is not corn.")                   |
                        |                                       |
                        |                                       |
                       \|/                                      |
                    program ends <-------------------------------"""


#--------- example for else statement ------------
"""veg = input("Type the name of vegetable.")
if veg == "corn":
    print("The vegetable is corn.")
else:
    print("the vegetable is not corn..")"""

# --------- nested if and else statements -------
"""                     person applies for loan
                                  |
                False            \|/                Ture
             <----------  high school GPA >= 3.7 ---------->
             |                                              |
             |                                              |
            \|/                          False             \|/                     True
need higher GPA to qualify            <-------- Accepted by approved Institution  -------->
            |                         |                                                    |
            |                   does not qualify                               qualifies for low APR loan
            |                         |                                                    |
            |                         |____________________________________________________|
            |                                                   |     
            |___________________________________________________|
                                     |
                                    \|/
                                 Programs ends"""

# example foe nested if and else statements
"""gpa = float(input("What was the applicant's grade point average?"))
inst_app = input("Is the student going to be educated at an approved institution?")

# ----------- example for nested if and else statements

if gpa >= 3.7:
    if inst_app == "yes":
        print("The application qualifies for a low APR student loan.")
    else:
        print("The application does not qualify since they have not been accepted into an approved institution.")
else:
    print("The application did not have enough grades to qualify.")"""

#---------- elif statements --------------
''' The elif statements is also know as the else/if statements, is a statements which allows you to provide as many additional conditions to check as you need without the messiness that comes
 with having to use multiple nested if statements and if/else statements block.'''


# example for elif statements
"""
user_num = int(input("Please enter an integer."))

if user_num < 0:
    print("The number you entered is less then 0.")
elif user_num == 0:
    print("The number you entered is 0.")
elif user_num <= 100:
    print("The number you entered can be 1, 100, or anything in between.")
else:
    print("The number yoy entered is greater than 100.") """


# ---------- truthy and falsey values  ------------

''' Foe string anything other than an empty string is truthy. An empty string is falsey, meaning that it is seen as being equivalent to the false boolean value '''

# example for truthy and falsey values
"""string_ex = input("Enter any string other than an empty one.")

if string_ex != "":
    print("Thank you for entering something")
else:
    print("you did not enter a string.!") """

# ------- bool() ---------
print(bool(0))              # false
print(bool(100))            # True
print(bool(0.0))            # False
print(bool(3.142))          # True
print(bool(""))             # False
print(bool("Hello World"))  # True
print("\n")


#-------------- Loops ------------------------

# ________________ While loop ______________
''' A while loop has Four parts, the word while a condition which evaluates to a boolean value a colon and code that the while loop will run.
'''

# A loop which is controlled by what its condition evaluates to when using while loop, you won't always know. How may time the loop will execute its code before it ends.

counter = 0

while counter < 3:
    print("Something")
    counter += 1

print('\n')

# ________________ For loop _____________
#for performing A fixed number of iterations the loop is particularly useful because it is type of loop that is controlled by the length of the iterable piece of data that it is being on rather than a condition.
"""To make a for loop, you need six things the word "for", a variable name to hold an item form the being iterate through, the word "in", 
the item being iterated through colon. then code that the for loop will run on each item for the thing it is iterating through.  
"""
word = "house"

for letter in word:
    print(letter)

print('\n')

#  ___________ range()
#range is function that returns a sequence of numbers and is usually used for iterating over with a for loop. It can take three arguments, start, stop and step, and can be used with one, two or all three of them at the same time.

# __________ using ranger() with 1 argument 1
one_input = range(5)

for num in one_input:
    print(num, end=" ")

print('\n')

# __________ using range() with i argument 2

two_input = range(5, 10)

for num in two_input:
    print(num, end=" ")

print('\n')

# # __________ using range() with i argument 3

three_input = range(2, 20, 2)

for num in three_input:
    print(num, end=" ")

print('\n')

# -------------- String Methods 1 ------------
'''String methods are function that are built into Python, which allow you to perform useful operations with string such as splitting
them or changing their case so that they can be used as aprt of non case sensitive comparisons with other strings.'''


# ________ .upper() & .lower() _________

''' The upper string method allows you to make everything in string uppercase.'''

all_low = "there are no capital here..!"
print(all_low.upper())
print(all_low)


all_up = "THIS IS NOTHING TEXT!"
print(all_up.lower())
print(all_up)
print('\n')

# ______ .isupper() & .islower() _______
''' This upper method returns a boolean value. It only return true if the letters in the string it is being used on are all uppercase'''
print("Mixed case".isupper())
print("ALL CAPS!".isupper())

print("ALL CAPS!".islower())
print("mixed case $100".islower())
print("".isupper())
print("37&8.,\"".islower())
print("\n")

# ________ Multiple String Methods ___________
'''String method like upper and lower return string, you can them in combination with other string methods'''

'''          -----------------------------------------------
            |   .isalpha()      |       Only letters        |
             -----------------------------------------------
            |   .isalnum()      |   Only numbers & letters  |
             -----------------------------------------------
            |   .isdecimal()    |       Only numbers        |
             -----------------------------------------------
            |   .isspace()      |       Only spaces         |
             -----------------------------------------------
            |   .istitle()      |       Only titlecase      |
             -----------------------------------------------    '''


print("Batman".isalpha())       # True
print("Batman12".isalpha())     # False
print("Batman123".isalnum())    # True
print("123".isdecimal())        # True
print("3.14".isdecimal())       # False
print(" ".isspace())            # or print("not just space"[3].isspace()) #True
print(" not just space".isspace())   # False
print("The Empire Strikes Back".istitle())  # True

print("the greate gatsby".title())   # output: The Greate Gatsby
print("\n")


# _______ .startswith() & .endswith() ________
"""Start with and ends with both take a string as an argument starts with return True if the string it is used on begins with its 
arguments ends with return true if the string it is being used on ends with its arguments."""

print("this is a string".startswith("t"))   # True
print("this is a string".startswith("T"))   # False

print("To infinity and beyond!".endswith("beyond!"))       # True
print("To infinity and beyond!".endswith("beyond"))         # False

print("\n")


# ________________ .join() _____________
#When you use join on a string, you pass it a list of string that you want to join together. Then join combines them and returns back a single string.
print("".join(["one", "two", "three"]))
print(" ".join(["one", "two", "three"]))
print(",".join(["one", "two", "three"]))
print(", ".join(["one", "two", "three"]))
print("...".join(["one", "two", "three"]))

print("\n")

# ________________ .split() ____________
# The split method does the opposite of the join method, meaning that when it is used on a string, it splits that string and returns a list.

print("Eggs, Milk, waffles, Bacon".split())
print("Eggs, Milk, waffles, Bacon".split(","))
print("Eggs, Milk, waffles, Bacon".split(", "))

print('\n')


# --------------- String methods 2 -----------------

#___________ .rjust() & .ljust() __________ one argument
#The rjust and ljust methods can both take one argument and return right justified or left justified versions of the string they are called on.
#What that means is that when called with one argument, they will return strings that have had spaces added to the left of them or to the right of them.

print("hello world".rjust(15))  # also count the string value of "hello world" there are 11 words
print("hello world".ljust(15) + "four space later.")

print("\n")
#___________ .rjust() & .ljust() __________ second argument
# Can also change the fill character of rjust or ljust to something other than spaces by calling either of them with a second argument.

#####Note: That this second argument can only be one character long and must be a string

print("hello world".rjust(15, "_"))
print("hello world".ljust(15, "*"))

# ______________ .center() ________________
'''The center method works in a similar manner to the rjust and ljust methods, except that it adds fill characters on either side of the string it is being used on,
rather than just then left or right. like rjust and ljust, it can also take up to two arguments one for a total length and the other for the fill character. '''
print("hello world".center(15, ":"))

print("\n")


# ____________ .strip(), .rstrip() & lstrip() ____________________
''' Strip, rstrip and lstrip are useful fro when you want to remove characters such as white spaces from a string.
 By default, strip removes all of the spaces form both sides of a string, rstrip removes all of the spaces from the right side of a string, and lstrip removes all of the spaces form the left side of a string '''

print("I had an exciting trip!!!11111")
print("I had an exciting trip!!!11111".strip("1"))
print("I had an exciting trip!!!11111".rstrip("1"))
print("I had an exciting trip!!!11111".lstrip("1"))
print("juice, bread, cheese, beef, bread".rstrip(", bread"))
print("juice, bread, cheese, beef".rstrip("beef"))
print("blueblueyelloweblue".strip("eubl"))
print("blueblueyelloweblue".rstrip("eubl"))

print("\n")


#____________ .replace() ___________

"""Replace is string method which is used to search for and replace a string. It takes two t=strings as arguments. The first argument is the string it will search for when it is called."
 that the string being searched for will be replaced with if it is found. """

print("Good morning" .replace("morning", "afternoon"))

print("\n")


# _____________ len() _____________
''' The len() function lets you get the length of an iterable data type, such as a string.In the case of string, its length is the number of characters it contains. 
The length of a string includes all characters, which means spaces, punctuation and even special characters like asterisk and percentage symbols are included in a string length. '''

print(len("Tree"))
print("This" + " " + "is a " + "string.")
print(len("This" + " " + "is a " + "string."))
print("antidisestablishmentarianism" [7:20])
print(len("antidisestablishmentarianism" [7:20]))

print("\n")

# ___________ .format() _____________
''' Normally, if you wanted to combine string together, you would use the addition operator to concatenate them.'''

""" ------ Example for .format() ______________
name = input("What is the job applicant's name?")
degree = input("What did they major in at college?")
job = input("What is their current occupation?")
experience = input("How many years have they been working in their field?")

# using concatenated
print(name + " majored in " + degree + ", works as a " + job + ", and has " + experience + " years of experience.")
# using formate
print("{} majored in {}, works as a {}, and has {} years of experience" .format(name, degree, job, experience))

"""

# ------------------- Introduction to lists -------------------

# A list is a data type which contains multiple values in an ordered sequence. Values within a list are also known as items.
#Here we have a variable called example_list one. To create a list, you type square brackets, then whatever items you want to be in the list separated by commas that have spaces after them.

example_list_1 = [5,4,3,2,1]
example_list_2 = [2.718, 9.31]
example_list_3 = ["blue", "green", "red", "yellow"]
example_list_4 = [True, False, False, True, False]
example_list_5 = [[1,2,3], [4,5], [6,7,8]]
example_list_6 = [10,3.14159, "tree",False, [1,2,3]]

print(example_list_1)
print(example_list_2)
print(example_list_3)
print(example_list_4)
print(example_list_5)
print(example_list_6)

print("\n")
#______________ list() _______________

# The list function takes an iterable data type, such as string, as an argument, converts it to a list that it then returns

print(list("blah"))


# _____________ in & not in ________________

# The "in" and "not in" operators can be used to check whether a value is or isn't in a list. Like other operators such as math operators, they are used in expressions.

checked_list = [1,2,3,4]
not_in_example = 8 not in checked_list  # if it's there then printing "False" if not there then printing "True"
print(1 in checked_list)
print(not_in_example)

print("\n")


#--------------- indexes & list slicing -----------

#___________ accessing by index _____________
# Index just like for strings, index numbers in a list also start at zero.

indexes_example = ["carpet", "hardwood", 'linoleum']
print(indexes_example[1])
print(indexes_example[2][1])

indexes_example_1 = [[1,2,3], [4,5,6], [7,8,9]]
print(indexes_example_1[2][1])

# _______- negative indexes ______
# Accessing by index using a negative integer start from the end of a list and goes backwards.

negative = [1,2,3,4,5]
print(negative[-2], " --> accessing from backwards")

# _____ using items accessed by index in expressions ______

mixed = [False, 365, 4.24, "this is a string"]
print(mixed[2] + 1.76)
print("I have used \"" + mixed[-1] + "\" as an example too may times.")

print("\nlist slicing")
# _______ list slicing _______

sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sliced[:5])   # 1 2 3 4 5
print(sliced[2:7])  # 3 4 5 6 7
print(sliced[4:])   # 5 6 7 8 9

print("\nreassigning a list's items")
# _______ reassigning a list's items _________
example = [2, 4, 6, 8, 0]
print(example)
example[3] = 10
print(example)

print("reassigning a list using slicing")
example_1 = [2, 4, 6, 8, 0]
print(example_1)
example_1[1:4] = [3, 2, 1]
print(example_1)

example_1[4:7] = [7,6,5]
print(example_1)


print("\n")



# ---------- del & list methods ------------

# ___________ del __________________
#del statements allow you to delete values from a list.

planets = ["pluto", "mars", "earth", "venus"]
del planets[0]
print(planets)

# ________ .remove() ___________
#The remove method allows yoy to remove what yoy pass it as an argument from a list.

planets_1 = ["pluto", "mars", "earth", "venus"]
planets_1.remove("pluto")
print(planets_1)

colors = ["blue", "red", "white", "blue", "orange", "blue"]
colors.remove("blue")
print(colors)

'''may be wondering why you would want to use remove instead of del remove items form a list. Well, the difference 
between del and remove is that del removes an item based on the index number of the item being removed. While the remove 
method searches a list for whatever item you passed it as an argument and removed it from the list when it finds that item'''

# ____________ .append() ______________
#The append list method takes an argument and adds that to the end of the list it is being used on

print("\n_______ .append() _______")
pets = ["cat", "dog", "parrot"]
print(pets)
pets.append("fish")
print(pets)

# ___________ .insert() _________________
'''insert is similar to append in that it is used to add an item to a list. However, unlike append, insert allows you to 
add an item anywhere in the list rather than just at its end. To do this insert takes two arguments where the first argument 
is the index at which a new item will br added to a list, and the second argument is the item that will be added to the list at that index'''

print("\n_______ .insert() _______")
pets_1 = ["cat", "dog", "parrot"]
pets_1.insert(2, "turtle")
print(pets_1)
























