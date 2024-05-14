#Create a function called name_printer which takes 1 parameter and prints it

def name_printer(p1):
    print(p1)


name_printer(5)

#Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.

name = input("Enter the name")

#Call name_printer() with the variable "name" as its argument.
name_printer(name)