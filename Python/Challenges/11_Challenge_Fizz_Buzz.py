"""Write a program that iterates over the integers 1 through 50 using a loop.

However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output.  For example, 15 is divisible by both 3 and 5, so instead of printing 15, print "FizzBuzz".  For numbers which are multiples of 3 but not 5 (such as 42) print “Fizz” instead of the number.  For the numbers that are multiples of 5 but not 3 (such as 20) print “Buzz” instead of the number.

All the integers which are not multiples of 3 or 5 should just be printed as themselves."""

for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuss")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)