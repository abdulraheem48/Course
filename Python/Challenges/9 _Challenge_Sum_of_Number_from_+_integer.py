"""Write a program which gets a positive integer from a user using input() and assigns it to a variable.

The program should then use a while loop to get the sum of all of the integers from the integer that was entered by the user down to 1.  For example, if the integer entered by the user was 6, the while loop would find the sum of 6, 5, 4, 3, 2, and 1, which is 21.

At the bottom of your program create two print statements.  One will display the user entered integer and the other will display the sum found by the while loop."""

pos_int = int(input("Please enter positive integer"))

int_init = pos_int
sum = 0
while pos_int > 0:
    sum += pos_int
    pos_int -= 1

print(int_init)
print(sum)