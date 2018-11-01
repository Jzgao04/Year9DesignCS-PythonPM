#Python Strings Demo
#Declaring a String Variable in PYthon
str1 = "Stephen"
str2 = "1234"
str3 = "Stephen@#$%^"
str4 = "a"
#printing the string variable
print(str1)
#string method
#length of the string --> The number characters in a string
str5 = "Stephen Harper"
print(len(str5))
#Accessing each character in the string
print(str5[0])
#Write a print statement that will access the last character in the following string
str6 = "Srimawo Ratwatee Banadaranayake"
print(str6[len(str6)-1])
str7 = "Donald Trump"
#print the reverse version of str7
#You cannot use any build in reverse method
#output should be pmurT dlanoD


for i in range(len(str7)-1, -1,-1):
    print(str7[i])
print("\n")
    

str8 = "the red cat sat on the mat"
print(str8[0:3])
print(str8[:-1])
print(str8[-1:])

str9 = "apple"
print(str9.find("a"))

strFirst = "Stephen"
strLast = "Harper"
strFull = strFirst + strLast
print(strFull)

#Accessing the ASCII characters 