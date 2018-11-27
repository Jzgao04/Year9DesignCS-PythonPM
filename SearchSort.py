# Python F18 Class 11 Demos

intList3 = [-100,9,6,12,34,167,89,45,1000]

maximum = max(intList3)
minimum = min(intList3)

range = (maximum - minimum)
print(range)

'''
Taking an Integer list and target value as a parameter, return the index of the 
target value in the list if found else return -1
'''

def LinearSearch(intList1, intTarget):
    for i in range(0, len(intList1)):
        if intList1[i] == intTarget:
            return i
    return -i

'''
Taking a sorted integer list and a target value as a parameter return the index of the target value if found in
list else return -1
'''

def BinarySearch(intList1, intTarget):
    intMax = len(intList1)-1
    intMin = 0
    intMid = (intMax + intMin)//2
    
    while(intMin <= intMax):
        if intList1[intMid] == intTarget:
            return intMid
        elif intTarget > intList1[intMid]:
            intMind = intMid + 1
            intMid = (intMax + intMin)//2
        else:
            intMax = intMax -1
            intMid = (intMax + intMin)//2
    return -1

def bubbleSort(intList1):
    for i in range(0, len(intList1)):
        for j in range(0, len(intList1)-1):
             if intList1[j] > intList1[j+1]:
                 intTemp = intList1[j]
                 intList1[j] = intList1[j+1]
                 intList1[j+1] = intTemp
                 
def printList(intList1):
    for i in range(0, len(intList1)):
        print(intList1[i])
    print("\n")
            
    
intMyList1 = [10,12,-4,5,67,89,100]
print(LinearSearch(intMyList1, 1000))
intMyList2 = [1,2,3,4,5,6,7,8,9,10]
print(BinarySearch(intMyList2,9))

bubbleSort(intMyList12)
printList(intMyList2)

#Find the range of the values in intList3

intList3 = [-100,9,6,12,34,167,89,45,1000]

maximum = max(intList3)
minimum = min(intList3)

range = (maximum - minimum)
print(range)

