#Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]
ind = [[0, 2], [4,6], [8,10], [12,14]]
print(ind)

#Access the first list from the list of lists in step 1 by index then print it.
print(ind[0])

#Access the 14 from the list in step 1 then print it.
print(ind[3] [1])

#Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]
ass = ["chair", "table", "desk", "lamp", "bed"]
print(ass)

#Use a negative integer to access "chair" from the variable in step 4 by index then print it.
print(ass[-5])

#Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and the "chair" from the list in step 4 with "Most people own at least ", a space, and a period.

print("\"Most people own at least " + str(ind[0][1]) + "s.\"")

#Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]

cre_list = [0.98, 8.78, 6.54, 4.32]

#Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7
print(cre_list[1:])

#Print the slice [8.76, 6.54] from the variable you created in step 7
print(cre_list[1:3])

#Print the slice [0.98, 8.76] from the variable you created in step 7.
print(cre_list[:2])