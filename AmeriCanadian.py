#1. Obtain last two characters of string
#2. Find out if the last two characters are "or"
#3. Create a new string by adding "u" in between the o and r.
#4. Return the new string

word = input("Write the word here: ")

part1 = word[:-1]
if word[-2:] == 'or':
    print(part1 + "ur")
else: 
	print(word)
