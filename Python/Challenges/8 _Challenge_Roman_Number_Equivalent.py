"""
For this exercise, start by creating a variable and assigning it a randomly generated integer between and inclusive of both 1 and 10.

Then, using your knowledge of if, elif, and else statements, create a program which prints the roman numeral equivalent of the randomly generated number.

For example, if the randomly generated integer was 9, then the program would say that the roman numeral equivalent of 9 is IX in the output."""

from random import randint
one_to_ten = randint(1,10)

if one_to_ten == 1:
    print("The roman number equivalent of " + str(one_to_ten) + " is I.")
elif one_to_ten == 2:
    print("The roman number equivalent of " + str(one_to_ten) + " is II.")
elif one_to_ten == 3:
    print("The roman number equivalent of " + str(one_to_ten) + " is III.")
elif one_to_ten == 4:
    print("The roman number equivalent of " + str(one_to_ten) + " is IV.")
elif one_to_ten == 5:
    print("The roman number equivalent of " + str(one_to_ten) + " is V.")
elif one_to_ten == 6:
    print("The roman number equivalent of " + str(one_to_ten) + " is VI.")
elif one_to_ten == 7:
    print("The roman number equivalent of " + str(one_to_ten) + " is VII.")
elif one_to_ten == 8:
    print("The roman number equivalent of " + str(one_to_ten) + " is VIII.")
elif one_to_ten == 9:
    print("The roman number equivalent of " + str(one_to_ten) + " is IX.")
else:
    print("The roman number equivalent of " + str(one_to_ten) + " is X.") #