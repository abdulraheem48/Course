# Create a variable and assign it the string "Just do it!"
str_1 = "Just do it!"
print(str_1)

#Access the "!" from the variable by index and print() it
str_1 = "Just do it!"
print(str_1[10])

#Print the slice "do" from the variable
str_1 = "Just do it!"
print(str_1[5:7])

#Get and print the slice "it!" from the variable
str_1 = "Just do it!"
print(str_1[8:])

# Print the slice "Just" from the variable
str_1 = "Just do it!"
print(str_1[:4])

#Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.

str_1 = "Just do it!"
print("Don't " + str_1[5:])