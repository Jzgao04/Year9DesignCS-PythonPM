# Python Fall 18 Class 12 Demo
# Read 10 names along with thier phone number and store them in such a way if the user entered the phone number
# we should be able to retrieve the Name of the person

NameList = []
phoneList = []
for i in range(0, 10):
    name = input("Enter the name ")
    phone = input("Enter the phone number")
    NameList.append(name)
    phonelist.append(phone)
    
phoneN = input("Enter the phone number to search for")
for i in range(0, 10):
    if phoneList[i] == phoneN:
        print(NameList[i])

