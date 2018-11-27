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