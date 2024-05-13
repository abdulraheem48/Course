#create a variable and assign it the following dictionary:
#{"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
dic_0 = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like A Rolling Stone"}
#make the dictionary span multiple lines so that the line the dictionary starts on is not too long.
dic = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like A Rolling Stone"}

#print the length of the dictionary.
print("\n ----- using len() ""\n",len(dic))

#use the .keys() method and a for loop to get and print all the keys from the dictionary on separate lines.

print("\n ---- using .keys()",dic.keys())
for key in dic.keys():
    print(key)

#print all the values from the dictionary using the .values() method
print("\n ---- using .values() ""\n",dic.values())

#use .items() with a for loop to iterate through and print all the key value pairs from the dictionary.
print("\n ---using .items() ""\n",dic.items())
for key, value in dic.items():
    print(key, value)

#use the .get() method to check the dictionary for the key
print("\n ---using .items() ""\n", dic.get("Promise of the Real", "\"Promise of the Real\" is not a key in dic"))