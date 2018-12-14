#Python F18 Class 12 Dictionary Demo
myDictionary = {}

#ASsigning the key value pair to the dictionary

myDictionary[4169199999] = "Stephen"
myDictionary[4169119111] = "Emergency"
myDictionary["Leaf"] = "Green"

print(myDictionary[4169199999])
print(myDictionary["Leaf"])

#if the key doesn't exist in the dictionary Python will
#Throw an exception

#Printing the key, value pair in the dictionary
for key in myDictionary:
    print(key, myDictionary[key])
    
#Methods associated with dictionary 
#Checking whether a key exists in the dictionary
if 4169199999 in myDictionary:
    print(myDictionary[4169199999])
    
strSentence = input("Enter a sentence")
letterD = [] # The dictionary to store the letters along with thier frequency
for i in range(0, len(strSentence)):
    if strSentence[i] in letterD.keys():
        letterD[i] = letterD[i] + 1 # Update the count for that key
    else:
        letterD[i] = D = 1
        
for key in letterD:
    print(key, letterD[key])
    
    
    
#Read 10 integer values form the user and calculate it's mode
#1 1 1 1 2 2 4 4 1 5
#The output should be 1

num1 = int(input())
num2 = int(