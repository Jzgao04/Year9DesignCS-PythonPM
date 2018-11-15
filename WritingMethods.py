#python Writing Methods
'''
Print the Prime Minister's address
'''
def print_address():
    print("Justin Trudeau")
    print("20 Sussex Drive")
    print("Ottawa, Ontario")
    
'''
Taking three string arguments/parameters print the address of a person
'''
def print_address1(strFullName, strAdd1, strAdd2):
    print(strFullName)
    print(strAdd1)
    print(strAdd2)
'''
Taking two Integer parameters and return the sum of intA and intB
'''
def sum(intA, intB):
    return intA + intB

'''
Taking an Integer parameter return true if intA is even, else return False
'''

def isEven(intA):
    return intA % 2 == 0

'''
Taking an Integer parameter intN >= 1, return the sum of the first intN numbers. i.e. if intN = 10 should return 55
'''

def nSum(intN):
    
    return (intN + 1)*(intN//2)

'''
Return the reverse version of str1 without using the build in 
reverse method. Do not use the slicing either
'''

def reverseString(str1):
    strTemp = ""
    for i in range(len(str1)-1, -1, -1):
        strTemp = strTemp + str1[i]
    return strTemp

'''
return true if str1 is a palindrome, else return false
'''

def isPalindrome(str1):
    return reverseString(str1) == str1

#Calling the method in program
print_address()
print_address1("Donald Trump", "White House", "Washington")

#Read the input from the user and passing into a method
#str1 = input("Enter your full name")
#str2 = input("Enter your street address")
#str3 = input("Enter your city")

#print_address1(str1,str2,str3)

#To call a method that retuns some value you 
#need to call with a print statement
print(sum(10,15))
#We can assign the return value into a variable
intD = sum(10,20)
print(intD)
print(isEven(15))
