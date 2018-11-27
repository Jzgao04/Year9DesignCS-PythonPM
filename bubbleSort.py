# Python F18 Class 11 HW - Train Swap
def bubbleSort(list1):
    intCount = 0 #Count the Number swap needed to sort the entire array
    for i in range(0, len(list1)):
        for j in range(0, len(list1)-1):
            if list1[j] > list1[j+1]:
                intTemp = list1[j+1]
                list1[j+1] = list1[j]
                list1[j] = intTemp
                intCount += 1
    return intCount

intNTest = int(input()) # Number of test cases
intSwaps = 0
for i in range(0, intNTest):
    intCars = int(input())
    carList = []
    for j in range(0, intCars):
        intX = int(input())
        carList.append(intX)
    intSwap = bubbleSort(carList)
    print("Optimal swap takes", (intSwaps), "swap(s).")
    
    
#Time on Task

def bubbleSort(list1):
    for i in range(0, len(list1)):
        for j in range(0, len(list1)-1):
            if list1[j] > list1[j+1]:
                intTemp = list1[j+1]
                list1[j+1] = list1[j]
                list1[j] = intTemp
                intCount += 1
                
intMaxTime = int(input()) # The max time to complete all of the tasks
intNTask = int(input()) # The number of tasks
intTimeList = []
for i in range(0, intNTask):
    intTime = int(input())
    intTimeList.append(intTime)
    
bubbleSort(intTimeList)

intCount = 0 #Count the maximum possible task
intTimeUsed = 0 #Keep and accumulate the time for each task that can be completed
intIndex = 0 # The index to access the element in the intTimeList

while intTimeUsed + intTimeList[intIndex] <= intMaxTime:
    intTimeUsed = intTimeUsed + intTimeList[intIndex]
    intIndex += 1
    intCount += 1
    
print(intCount)
    