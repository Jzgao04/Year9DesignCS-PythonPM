#Python C11


def intNSum(intN):
    intTotal = 0
    for i in range(1, intN+1):
        intTotal += 1
    return intTotal

def intNSum1(intN):
    #The base case
    if intN == 1:
        return 1
    else:
        return intNSum1(intN-1) + intN
    
def intNProduct(intN):
    if intN == 1:
        return 1
    
    return intN * intNProduct(intN-1)
'''
Taking an Integer parameter intN > 0 reutrn the Binary equivalent of intN
'''

def DeciToBin(intN):

    if(intN > 1):
        DeciToBin(intN // 2)
        print(intN % 2)
    else:
        print(1)
    
'''
Tests whether a given text conatins a string. For example, find ("Mississippi", "sip") returns true
'''

def findStr(strText, strTarget):
    if(len(strText) == 0):
        return False
    elif(not strText.startswith(strTarget)):
       return findStr(strText[1:len(strText)], strTarget)
                      
    return True
'''
Taking a String parameter strWord return true if strWord is  a Palindrome
else return false
'''

def isPalindrome(strWord):
    #Base Case
    if len(strWord) == 1:
        return True
    elif len(strWord) == 2 and (strWord[0] == strWord[1]):
        return True
    elif strWord[0] == strWord[len(strWord)-1]:
        return isPalindrome(strWord[1:len(strWord)-1])
    return False

'''
Taking an Integer parameter intN >= 1, reutrn the intNth Fibonacci Number
1 1 2 3 5 8...
'''

def nthFibonacci(intN):
    if intN == 1 or intN == 2:
        return 1
    return nthFibonacci(intN-1) + nthFibonacci(intN-2)

if nthFibonacci(2) == 1:
    print("Fibonacci Test 1 Pass")
if nthFibonacci(12) == 144:
    print("Fibonacci Test 2 Pass")
        
print(isPalindrome("radar"))
print(isPalindrome("noon"))
print(isPalindrome("elephant"))

print(findStr("Mississippi", "sip"))
print(DeciToBin(24))
print(intNSum(10))

print(intNSum1(10))

if(intNProduct(5) == 120):
    print("IntNProduct Test 1 passed")
    
if(intNProduct(4) == 24):
    print("IntNProduct Test 1 passed")
    
